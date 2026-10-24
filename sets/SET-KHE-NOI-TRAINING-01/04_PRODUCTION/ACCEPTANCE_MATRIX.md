# ACCEPTANCE_MATRIX — เข้น้อย อยู่ระหว่างฝึก

## Document checks
GEM Aตรวจ31ไฟล์+assetexact SHA256; IDs/captions/matrix/mapping40/40; ไม่ย้ายownerapprovalข้ามscope; manifestทุกpayloadและcountตรง รันvalidatorหลังเขียนและก่อนรายงานcomplete

## Visual checks
GEM B/ownerตรวจทุกframeหัวเหมือนCHAR04 อารมณ์ตรงintent มือชัด cropครึ่งบน captionไทยใหญ่ไม่ทับตาปาก/มือ ตัวละครกึ่งสมจริงและชุดเดิม ต้องดูภาพจริงไม่อ้างจากprompt

## Pixel checks
GEM B/compositorตรวจgeometryตามspec ratio592:512 กรอบ3 gutter15 safe20±5% RGBA alphaและdiecut3–5px ไม่มีcaptionสระหลุดmask crop/cutterexportทดสอบจริง ทำobservedstats/pathsไม่สร้างPASSล่วงหน้า

## Return conditions
caption/intent/mappingผิดคืนAรายF; ภาพหัวหรือalphaผิดBแก้ภายใต้locks; sourceimage/hashผิดหยุดก่อนrender; ownerแก้identityให้กลับCharacterapproval ไม่ข้ามgateเพราะอยากประหยัดโควต้า
