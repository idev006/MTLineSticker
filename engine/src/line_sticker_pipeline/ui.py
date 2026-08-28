from __future__ import annotations
import os, sys, threading
from pathlib import Path

try:
    from PySide6.QtCore import QObject, Signal, Slot, QThread, Qt, QSize, QSettings, QUrl
    from PySide6.QtGui import QIcon, QPixmap, QDesktopServices
    from PySide6.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
        QLabel, QLineEdit, QPushButton, QFileDialog, QSpinBox, QProgressBar,
        QPlainTextEdit, QGroupBox, QFormLayout, QMessageBox, QCheckBox, QTabWidget,
        QTableWidget, QTableWidgetItem, QHeaderView, QListWidget, QListWidgetItem,
        QSplitter, QFrame, QAbstractItemView
    )
except ImportError as e:
    raise RuntimeError('PySide6 is required. Install with: pip install "line-sticker-pipeline[desktop]"') from e

from .pipeline import ProductionPipeline, PipelineOptions
from .scanner import scan_folder
from .parallel import ProcessingCancelled

APP_NAME='MT LINE Sticker Studio'
ORG_NAME='MTDEV'

class PipelineWorker(QObject):
    progress=Signal(str,float,str); finished=Signal(dict); failed=Signal(str); cancelled=Signal()
    def __init__(self,input_dir:str,output_dir:str,workers:int,recursive:bool,auto_package:bool):
        super().__init__(); self.input_dir=input_dir; self.output_dir=output_dir; self.workers=workers
        self.recursive=recursive; self.auto_package=auto_package; self._cancel=threading.Event()
    def request_cancel(self): self._cancel.set()
    @Slot()
    def run(self):
        try:
            options=PipelineOptions(workers=self.workers,recursive=self.recursive,package_when_valid_count=self.auto_package)
            result=ProductionPipeline(options=options).run_folder(
                self.input_dir,self.output_dir,
                progress=lambda s,p,m:self.progress.emit(s,float(p),m),
                should_cancel=self._cancel.is_set)
            self.finished.emit(result)
        except ProcessingCancelled:
            self.cancelled.emit()
        except Exception as e:
            self.failed.emit(f'{type(e).__name__}: {e}')

class MetricCard(QFrame):
    def __init__(self,name:str,value:str='—'):
        super().__init__(); self.setFrameShape(QFrame.StyledPanel)
        l=QVBoxLayout(self); l.setContentsMargins(16,12,16,12); l.setSpacing(4)
        self.value=QLabel(value); self.value.setObjectName('MetricValue'); name_label=QLabel(name); name_label.setObjectName('MetricName')
        l.addWidget(self.value); l.addWidget(name_label)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(); self.settings=QSettings(ORG_NAME,APP_NAME); self.thread=None; self.worker=None; self.last_report=None
        self.setWindowTitle(APP_NAME); self.resize(1180,780); self.setMinimumSize(980,680)
        self._build(); self._restore_settings(); self.setAcceptDrops(True)

    def _build(self):
        root=QWidget(); self.setCentralWidget(root); outer=QVBoxLayout(root); outer.setContentsMargins(18,16,18,14); outer.setSpacing(12)
        header=QFrame(); header.setFrameShape(QFrame.StyledPanel); hl=QHBoxLayout(header); hl.setContentsMargins(20,15,20,15); hl.setSpacing(14)
        txt=QVBoxLayout(); title=QLabel('MT LINE Sticker Studio'); title.setObjectName('Title'); sub=QLabel('Contact sheet → frame crops. LINE cleanup/package is a later step.'); sub.setObjectName('Subtitle')
        txt.setSpacing(3); txt.addWidget(title); txt.addWidget(sub); hl.addLayout(txt); hl.addStretch(); self.header_status=QLabel('READY'); hl.addWidget(self.header_status); outer.addWidget(header)

        setup=QGroupBox('งานและการประมวลผล'); sg=QGridLayout(setup); sg.setContentsMargins(18,20,18,16); sg.setHorizontalSpacing(10); sg.setVerticalSpacing(10)
        self.inp=QLineEdit(); self.inp.setPlaceholderText('เลือกโฟลเดอร์ที่มี contact-sheet images')
        self.out=QLineEdit(); self.out.setPlaceholderText('เลือกโฟลเดอร์ผลลัพธ์')
        in_label=QLabel('Input folder'); in_label.setObjectName('FieldLabel'); out_label=QLabel('Output folder'); out_label.setObjectName('FieldLabel')
        sg.addWidget(in_label,0,0); sg.addWidget(self.inp,0,1); binp=QPushButton('เลือก...'); binp.setFixedWidth(86); binp.clicked.connect(lambda:self._browse(self.inp)); sg.addWidget(binp,0,2)
        sg.addWidget(out_label,1,0); sg.addWidget(self.out,1,1); bout=QPushButton('เลือก...'); bout.setFixedWidth(86); bout.clicked.connect(lambda:self._browse(self.out)); sg.addWidget(bout,1,2)
        opt=QHBoxLayout(); self.workers=QSpinBox(); self.workers.setRange(1,32); self.workers.setValue(max(1,min(4,(os.cpu_count() or 2)-1)))
        self.recursive=QCheckBox('ค้นหาในโฟลเดอร์ย่อย'); self.package=QCheckBox('สร้าง LINE package อัตโนมัติในโหมด LINE'); self.package.setChecked(False)
        workers_label=QLabel('Workers'); workers_label.setObjectName('FieldLabel'); self.workers.setFixedWidth(88)
        opt.setSpacing(12); opt.addWidget(workers_label); opt.addWidget(self.workers); opt.addSpacing(8); opt.addWidget(self.recursive); opt.addWidget(self.package); opt.addStretch(); sg.addLayout(opt,2,1,1,2)
        buttons=QHBoxLayout(); self.scan_btn=QPushButton('สแกน'); self.start_btn=QPushButton('เริ่มประมวลผล'); self.start_btn.setObjectName('Primary'); self.cancel_btn=QPushButton('ยกเลิก'); self.cancel_btn.setObjectName('Danger'); self.cancel_btn.setEnabled(False)
        self.open_btn=QPushButton('เปิดโฟลเดอร์ผลลัพธ์'); self.open_btn.setEnabled(False)
        self.scan_btn.clicked.connect(self.scan); self.start_btn.clicked.connect(self.start_processing); self.cancel_btn.clicked.connect(self.cancel_processing); self.open_btn.clicked.connect(self.open_output)
        buttons.setSpacing(8)
        for b in (self.scan_btn,self.start_btn,self.cancel_btn,self.open_btn): buttons.addWidget(b)
        buttons.addStretch(); sg.addLayout(buttons,3,1,1,2); outer.addWidget(setup)

        metrics=QHBoxLayout(); metrics.setSpacing(12); self.m_files=MetricCard('Input files','0'); self.m_stickers=MetricCard('Stickers','0'); self.m_fail=MetricCard('Technical failures','0'); self.m_workers=MetricCard('Effective workers','—')
        for m in (self.m_files,self.m_stickers,self.m_fail,self.m_workers): metrics.addWidget(m)
        outer.addLayout(metrics)
        self.status=QLabel('พร้อมใช้งาน'); self.status.setObjectName('SectionStatus'); self.progress=QProgressBar(); self.progress.setRange(0,1000); outer.addWidget(self.status); outer.addWidget(self.progress)

        self.tabs=QTabWidget(); outer.addWidget(self.tabs,1)
        jobs=QWidget(); jl=QVBoxLayout(jobs); jl.setContentsMargins(10,10,10,10); self.table=QTableWidget(0,5); self.table.setHorizontalHeaderLabels(['ไฟล์','สถานะ','ขั้นตอน','Progress','หมายเหตุ']); self.table.setSelectionBehavior(QAbstractItemView.SelectRows); self.table.setEditTriggers(QAbstractItemView.NoEditTriggers); self.table.setAlternatingRowColors(True); self.table.verticalHeader().setVisible(False); self.table.setShowGrid(False)
        self.table.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch); self.table.horizontalHeader().setSectionResizeMode(4,QHeaderView.Stretch)
        self.table.verticalHeader().setDefaultSectionSize(34); jl.addWidget(self.table); self.tabs.addTab(jobs,'งาน')
        previews=QWidget(); pl=QVBoxLayout(previews); pl.setContentsMargins(10,10,10,10); pl.setSpacing(10); note=QLabel('Visual QA: ตรวจบนพื้นโปร่งใส/สว่าง/เข้มก่อนอนุมัติส่ง LINE'); note.setFrameShape(QFrame.StyledPanel); pl.addWidget(note)
        self.preview=QListWidget(); self.preview.setViewMode(QListWidget.IconMode); self.preview.setResizeMode(QListWidget.Adjust); self.preview.setIconSize(QSize(185,160)); self.preview.setSpacing(8); self.preview.setMovement(QListWidget.Static); pl.addWidget(self.preview,1); self.tabs.addTab(previews,'Preview / Visual QA')
        logs=QWidget(); ll=QVBoxLayout(logs); ll.setContentsMargins(10,10,10,10); self.log=QPlainTextEdit(); self.log.setReadOnly(True); ll.addWidget(self.log); self.tabs.addTab(logs,'Log')

    def _browse(self,edit:QLineEdit):
        d=QFileDialog.getExistingDirectory(self,'เลือกโฟลเดอร์',edit.text() or str(Path.home()))
        if d: edit.setText(d); self._save_settings()

    def _restore_settings(self):
        self.inp.setText(self.settings.value('input','')); self.out.setText(self.settings.value('output',''))
        self.workers.setValue(int(self.settings.value('workers',self.workers.value()))); self.recursive.setChecked(str(self.settings.value('recursive','false')).lower()=='true'); self.package.setChecked(str(self.settings.value('package','true')).lower()=='true')

    def _save_settings(self):
        self.settings.setValue('input',self.inp.text()); self.settings.setValue('output',self.out.text()); self.settings.setValue('workers',self.workers.value()); self.settings.setValue('recursive',self.recursive.isChecked()); self.settings.setValue('package',self.package.isChecked())

    def scan(self):
        p=Path(self.inp.text())
        if not p.is_dir(): QMessageBox.warning(self,'Input','กรุณาเลือก Input folder ที่ถูกต้อง'); return
        try:
            rows=scan_folder(p,recursive=self.recursive.isChecked()); self.table.setRowCount(0); unique=0
            for item in rows:
                r=self.table.rowCount(); self.table.insertRow(r); dup=bool(item['duplicate']); unique += 0 if dup else 1
                values=[item['path'].name,'DUPLICATE' if dup else 'READY','SCAN','0%','SHA-256 duplicate' if dup else 'พร้อมประมวลผล']
                for c,v in enumerate(values): self.table.setItem(r,c,QTableWidgetItem(str(v)))
            self.m_files.value.setText(str(unique)); self.status.setText(f'พบ {unique} ไฟล์ที่พร้อมตัดเฟรม'); self._log('SCAN',f'{unique} unique file(s), {len(rows)-unique} duplicate(s)')
        except Exception as e: QMessageBox.critical(self,'Scan failed',str(e))

    def start_processing(self):
        inp=Path(self.inp.text()); out=Path(self.out.text()) if self.out.text() else None
        if not inp.is_dir(): QMessageBox.warning(self,'Input','กรุณาเลือก Input folder ที่ถูกต้อง'); return
        if out is None: QMessageBox.warning(self,'Output','กรุณาเลือก Output folder'); return
        try:
            if inp.resolve()==out.resolve() or inp.resolve() in out.resolve().parents: QMessageBox.warning(self,'Folder safety','Output folder ต้องไม่ใช่ Input folder หรือ parent ของ Input'); return
        except Exception: pass
        self._save_settings(); self.scan(); self._set_running(True); self.progress.setValue(0); self.preview.clear(); self.last_report=None
        self.thread=QThread(self); self.worker=PipelineWorker(str(inp),str(out),self.workers.value(),self.recursive.isChecked(),self.package.isChecked()); self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run); self.worker.progress.connect(self.on_progress); self.worker.finished.connect(self.on_finished); self.worker.failed.connect(self.on_failed); self.worker.cancelled.connect(self.on_cancelled)
        for sig in (self.worker.finished,self.worker.failed,self.worker.cancelled): sig.connect(self.thread.quit)
        self.thread.finished.connect(lambda:self._set_running(False)); self.thread.start()

    def cancel_processing(self):
        if self.worker: self.cancel_btn.setEnabled(False); self.status.setText('กำลังยกเลิก…'); self.worker.request_cancel(); self._log('CANCEL','Cancellation requested')

    @Slot(str,float,str)
    def on_progress(self,stage,pct,msg):
        self.header_status.setText(stage); self.status.setText(msg); self.progress.setValue(max(0,min(1000,int(pct*10)))); self._log(stage,f'{pct:5.1f}%  {msg}'); self._refresh_rows(stage,pct)

    @Slot(dict)
    def on_finished(self,r):
        self.last_report=r; blockers=r.get('package_blockers') or []; visual=(r.get('visual_qa') or {}).get('status','SKIPPED')
        output_mode=r.get('output_mode','frame_crop'); output_label='frames' if output_mode=='frame_crop' else 'stickers'
        self.header_status.setText('DONE' if output_mode=='frame_crop' else ('PASS' if not blockers else 'REVIEW'))
        self.status.setText(f"เสร็จสมบูรณ์ — {r.get('outputs',r['stickers'])} {output_label}")
        self.progress.setValue(1000); self.m_files.value.setText(str(r['input_images'])); self.m_stickers.value.setText(str(r['stickers'])); self.m_fail.value.setText(str(r['technical_failures'])); self.m_workers.value.setText(str(r['workers_effective'])); self.open_btn.setEnabled(True); self._load_preview(); self._load_job_rows(r.get('jobs',[])); self.tabs.setCurrentIndex(1)
        msg=f"สร้าง {r.get('outputs',r['stickers'])} {output_label} แล้ว"
        if output_mode=='line_sticker':
            msg += f"\nTechnical preflight: PASS\nVisual QA: {visual}"
        else:
            msg += "\nโหมดนี้ตัดเฟรมเท่านั้น: ไม่ remove background, ไม่ resize, ไม่สร้าง LINE package"
        if blockers:
            msg += "\nPackage blocked:\n- " + "\n- ".join(blockers)
        else:
            msg += "\nPackage: READY"
        msg += "\n\nกรุณาตรวจผลลัพธ์ก่อนนำไปขั้นตอน LINE cleanup/package"
        QMessageBox.information(self,'เสร็จสมบูรณ์',msg)

    @Slot(str)
    def on_failed(self,msg): self.header_status.setText('FAIL'); self.status.setText('ประมวลผลไม่สำเร็จ'); self._log('ERROR',msg); QMessageBox.critical(self,'Processing failed',msg)
    @Slot()
    def on_cancelled(self): self.header_status.setText('CANCELLED'); self.status.setText('ยกเลิกแล้ว'); self._log('CANCELLED','Processing stopped safely')

    def _set_running(self,running:bool):
        self.start_btn.setEnabled(not running); self.scan_btn.setEnabled(not running); self.cancel_btn.setEnabled(running); self.inp.setEnabled(not running); self.out.setEnabled(not running); self.workers.setEnabled(not running); self.recursive.setEnabled(not running); self.package.setEnabled(not running)
        if not running and self.header_status.text() not in ('PASS','FAIL','CANCELLED'): self.header_status.setText('READY')

    def _load_preview(self):
        self.preview.clear(); folder=Path(self.out.text())/'frames'
        if not folder.exists(): folder=Path(self.out.text())/'stickers'
        for p in sorted(folder.glob('*.png')):
            pix=QPixmap(str(p)); item=QListWidgetItem(QIcon(pix),p.stem); item.setData(Qt.UserRole,str(p)); item.setToolTip(str(p)); self.preview.addItem(item)

    def _load_job_rows(self,jobs:list[dict]):
        self.table.setRowCount(0)
        for j in jobs:
            r=self.table.rowCount(); self.table.insertRow(r); vals=[Path(j['source_path']).name,j['status'],j['stage'],f"{float(j['progress']):.0f}%",j.get('error') or '']
            for c,v in enumerate(vals): self.table.setItem(r,c,QTableWidgetItem(str(v)))

    def _refresh_rows(self,stage:str,pct:float):
        for r in range(self.table.rowCount()):
            if self.table.item(r,1) and self.table.item(r,1).text()!='DUPLICATE': self.table.setItem(r,1,QTableWidgetItem('PROCESSING' if pct<100 else 'COMPLETED')); self.table.setItem(r,2,QTableWidgetItem(stage)); self.table.setItem(r,3,QTableWidgetItem(f'{pct:.0f}%'))

    def _log(self,stage,msg): self.log.appendPlainText(f'[{stage:<10}] {msg}')
    def open_output(self):
        p=Path(self.out.text());
        if p.exists(): QDesktopServices.openUrl(QUrl.fromLocalFile(str(p.resolve())))

    def dragEnterEvent(self,event):
        if event.mimeData().hasUrls() and any(Path(u.toLocalFile()).is_dir() for u in event.mimeData().urls()): event.acceptProposedAction()
    def dropEvent(self,event):
        dirs=[Path(u.toLocalFile()) for u in event.mimeData().urls() if Path(u.toLocalFile()).is_dir()]
        if dirs: self.inp.setText(str(dirs[0])); self.scan(); event.acceptProposedAction()
    def closeEvent(self,event):
        if self.thread and self.thread.isRunning(): QMessageBox.warning(self,'กำลังประมวลผล','กรุณายกเลิกหรือรอให้งานเสร็จก่อนปิดโปรแกรม'); event.ignore(); return
        self._save_settings(); super().closeEvent(event)


def main():
    app=QApplication(sys.argv); app.setApplicationName(APP_NAME); app.setOrganizationName(ORG_NAME)
    win=MainWindow(); win.show(); return app.exec()

if __name__=='__main__': raise SystemExit(main())
