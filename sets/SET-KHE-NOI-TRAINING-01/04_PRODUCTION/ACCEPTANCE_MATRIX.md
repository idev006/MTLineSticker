# ACCEPTANCE_MATRIX — เข้น้อย อยู่ระหว่างฝึก v0.2.0

## Document checks
GEM Aรับผิดชอบregistry31ไฟล์, frame/caption/matrix/mapping40ตรงกันและspecJSONล่าสุด ส่งconsumerอ่านSHEET_FRAME_SPEC.jsonคู่กับhandoff ตรวจmanifesthashactualก่อนเริ่ม ตำแหน่งที่ส่งเป็นhalf-openพิกัด[x0,y0,x1,y1)ไม่ใช่inclusive ห้ามพิมพ์พิกัดทับart

## Visual checks
GEM Bและownerดูactualproofทุกframe: identityตรงCharacter04 หน้าใหญ่ครึ่งบน ตา/ปาก/มือแยกintentได้ captionไทยใหญ่ไม่เกิน2บรรทัดไม่กลบอวัยวะสำคัญ ไม่เต็มตัวหรือฉากกว้าง ค่าfontเป็นจุดเริ่มไม่รับประกันอ่านง่าย ต้องดูย่อในบริบทแชท

## Pixel checks
ตรวจไฟล์PNGจริงด้วยโค้ด: modeRGBA actualsheet/framegeometry8ตำแหน่ง ratio592:512 กรอบดำopaque3pxครบ4ด้านมุมฉากของแต่ละเฟรม gutter15pxalpha0ตลอดทุกช่องไม่ใช่sampleจุดเดียว safezoneband20±5%ไม่ให้art/ไดคัทล้ำขั้นต่ำ19px ไดคัทwhiteopaque3–5pxตามcontour ไม่มีrectangularwhitecanvasและไม่cropped ตรวจcoordinatesจริงก่อนตัด ชีทnominal2413x1039ไม่มีoutermargin ถ้าscaledต้องระบุactualspecและcutterผลจริง

## Return conditions
BORDER_MISSING_OR_INVALID:กรอบดำขาด/บาง/ไม่ทึบ/ใช้เส้นร่วม; GUTTER_ALPHA_FAIL:ช่องว่างมีpixelsไม่โปร่งใส; SAFE_ZONE_INTRUSION:เนื้อหาใกล้ขอบเกินขั้นต่ำ; FALSE_TRANSPARENCY:RGB/พื้นขาว/checkerboard; DIECUT_MISSING:ขอบขาวหายหรือไม่ครอบcaption/FX; FRAME_MAP_MISMATCH:IDหรือcaptionสลับ; CHARACTER_DRIFT:หัว/ชุดเปลี่ยน ข้อมูลต้นทางผิดคืนA ภาพหรือpixelsผิดBแก้ภายใต้spec ห้ามลดมาตรฐานเพื่อให้ผ่าน

## Evidence ownership
GEM Aยืนยันเอกสารและmapping; GEM Bรับart/compositor/pixelreports; cutterรับremovedborder+preserveddiecut+8outputtest; ownerอนุมัติHero/batch/releaseตามขั้น ถ้ายังไม่มีไฟล์ผลิตจริงทุกpixel/cuttertestเป็นNOT_RUN ไม่ใช่PASSจากpromptหรือคำอธิบาย

