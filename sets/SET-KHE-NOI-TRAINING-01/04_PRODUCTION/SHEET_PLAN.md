# SHEET_PLAN — เข้น้อย อยู่ระหว่างฝึก

## Layout
S01–S05แปดภาพต่อชีท4x2 ทุกframeupperbodyตามmappingรายID ไม่มีpartial อ่านซ้ายขวาแล้วแถวล่าง ไม่ต้องเรียกimagegenทีละชิ้น40ครั้ง: ตั้งแผนสร้างvisualเป็นชีทละ8เพื่อลดgenerationcallsตามแนวทางownerในงานต่อเนื่อง แล้วcompose/rebuildgeometryอย่างdeterministic ห้ามอ้างmodelให้pixelตรงเอง

## Geometry
เฟรมnominal592x512; กรอบดำ#000000 alpha255เข้าใน3pxแยกแต่ละเฟรม; gutterโปร่งใส15px; safe clearanceเลือก20px±5%จากinnerborderถึงouterdiecut; ratioต้อง w*512 == h*592; sheet4x2แปดภาพ nominal2413x1039 หรือคำนวณตามgeometryจริง; 5ชีทครบ40 ไม่มีpartial วัดค่าจริงทุกframeและส่งพิกัดให้cutter ระยะว่างตามรูปร่างบางด้านอาจมากกว่าเป้า ต้องแยกnominalselectedclearanceจากพื้นที่composition ไม่ตัดหัวหรือcaptionเพื่อบังคับเต็มกรอบ

## Alpha and diecut
RGBA PNGพื้นและgutteralpha0 ไดคัทขาวalpha255ขยายประมาณ3–5pxรอบunionของตัวละครcaptionpropsเหงื่อFX แต่ละชิ้นลอยต้องมีunderlayครบ ห้ามพื้นขาวrectangularและcheckerboardเทียม ต้องตรวจalphaจริงจากไฟล์บันทึก

## Cutter interface
cutterลบกรอบดำเก็บdiecutและพิกัดcropครบ40 รายงานไฟล์จริงขอบบนพื้นแชทขาว/เขียว/มืด captionใหญ่ต้องไม่ถูกตัดสระ/วรรณยุกต์ ภาพsheetเป็นmasterไม่ใช่LINEsubmissionพร้อมส่ง ห้ามผ่านengineถ้าalphaหาย
