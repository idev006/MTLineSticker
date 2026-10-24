# ACCEPTANCE MATRIX — น้องเข้ นสต. v0.5.0

## Document checks
GEM A: registry31ครบ; exact caption40; matrix40; mapping40; unique IDs/slots; references/path/hash; owner decisions; manifest payloadและarchive count ทดสอบด้วย bundled validator พร้อม manual content review ผลจริงเก็บนอกแพ็ก ไม่ให้ checker ทำหน้าที่รับรองความสวย

## Visual checks
GEM B: ภาพจริงตรง L01–L07 สีหน้าทุกภาพตรงเจตนา ไม่มีคนอื่นเด่นกว่า ไม่มี caption ผิด/ย้าย ID; owner: อนุมัติ Character, Hero และ release แยกกัน ต้องแสดงภาพทุกภาพก่อนกล่าวว่าครบ visual QA

## Pixel checks
GEM B/compositor/cutter: aspect592:512, กรอบ3px, gutter15px, clearance20±5%, RGBA alpha0, ไดคัท3–5pxครบ ไม่มี crop, export/cutter ไม่ลบชิ้นลอย ทุกข้อเป็น NOT_RUN จนมีไฟล์จริงและรายงาน pixels

## Return conditions
ข้อมูล/intent/caption/mappingผิด→RETURN_TO_GEM_A พร้อม IDและrevision; artworkผิดหรือalphaเสีย→GEM Bแก้; เครื่องหมาย/identityกำกวม→เจ้าของตัดสินก่อนภาพต่อ; contract mismatch→integration ownerแก้ ไม่ downgrade ตัวเลขให้ผ่านเงียบๆ
