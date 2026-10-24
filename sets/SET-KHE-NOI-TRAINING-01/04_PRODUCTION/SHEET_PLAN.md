# SHEET_PLAN — เข้น้อย อยู่ระหว่างฝึก v0.2.0

## Layout
ส่งmaster5ไฟล์S01–S05 ไฟล์ละ8เฟรม4คอลัมน์2แถว รวม40ตามFRAME_TO_SHEET_MAPPING โดยแต่ละเฟรมมีกรอบดำสี่เหลี่ยมของตนเองครบ4ด้าน ห้ามใช้เส้นร่วม และห้ามส่งเพียงภาพตัวละคร8ชิ้นลอยที่ไม่มีกรอบดำเป็นmaster ใช้sheet-generation8ภาพต่อรอบได้เพื่อประหยัดโควต้า แต่ต้องจัดกรอบ/gutter/alphaด้วยcompositorหลังgeneration ไม่เชื่อmodelว่าจัดpixelsถูกเอง

## Geometry
ค่าเริ่มต้นที่ใช้ส่งมอบคือframe592x512px, borderดำทึบ3pxวาดเข้าในมุมฉาก, gutterโปร่งใส15px, ไม่มีmarginนอกชีท จึงได้master2413x1039px x-origin0,607,1214,1821; y-origin0,527 อ่านซ้ายขวาบนแล้วล่าง รายละเอียดพิกัด40ช่องและJSONที่consumerอ่านได้อยู่SHEET_FRAME_SPEC.json อัตราส่วนทุกเฟรมต้องตรวจw*512==h*592
เลือกsafe-zoneband20pxจากขอบด้านในกรอบถึงpixelนอกสุดของart+caption+FX+ไดคัท ความคลาดเคลื่อนความกว้างband±5%=19–21px ต้องไม่มีเนื้อหารุกbandขั้นต่ำ19px เป้าหมาย20px พื้นที่ว่างจากcompositionที่มากกว่า20pxไม่ใช่เหตุให้ยืดรูปหรือขยายหัวผิดสัดส่วน nominalcontentbounds local[23,23,569,489)รวมไดคัทแล้ว ค่าscaledที่ยังคงratioเที่ยงตรงอนุญาตตามglobalpolicyแต่ต้องแจ้งขนาด/พิกัด/toleranceและทดสอบcutterจริง ห้ามอ้างnominalgeometryกับไฟล์scaled

## Alpha and diecut
PNGmodeRGBAจริง พื้นและทุกgutteralpha0 กรอบดำ#000000alpha255 ไดคัทขาว#FFFFFFalpha255ขยาย3–5pxเป้าหมาย4pxรอบunionตัวละครข้อความอุปกรณ์เอฟเฟกต์ แต่ละชิ้นลอยต้องมีunderlayครบ ไดคัทขาวไม่ใช่กรอบดำ ไม่ใช่พื้นขาวสี่เหลี่ยม ห้ามcheckerboardวาดหรือRGBไม่มีalpha ขอบanti-aliasของartได้แต่ห้ามสีพื้นตกค้างและต้องรวมในsafezone

## Cutter interface
ส่งspecJSON+actualcoordinateJSON+QAรายชีทให้cutter ตัดกรอบออกแล้วเก็บwhite-diecutไว้ ทดสอบ8ภาพต่อชีทและรวม40ภาพจริงก่อนCUTTER_COMPATIBLE ห้ามอ้างภาพpreviewแทนpixelQA ขอบดำเป็นmarkerในmasterไม่ควรติดไปในสติ๊กเกอร์ที่ตัดแล้ว ชื่อmaster KHE_NOI_TRAINING_S01_MASTER_RGBA.png ถึงS05 ไม่ใช้ไฟล์previewRGBแทนmaster

## Upper-body and caption acceptance
ทุกเฟรมเน้นเอว/อกขึ้นไป หน้าและตาชัด หัวครบไม่cropped มือสำคัญต้องอยู่ในพื้นที่ปลอดภัย คงidentityและwhiteclosedcollar/navytie/SNW.01ตามCharacter04 ข้อความไทยตรงCAPTION_MASTERใหญ่หนาไม่เกิน2บรรทัด font60–84pxเป็นจุดเริ่มจัดวางที่nominalframe ไม่ใช่หลักฐานautomaticPASS วางcaptionล่างประมาณ30–35% ปรับตามรูปแต่ไม่บังตาปากหรือgesture สระวรรณยุกต์ครบ ต้องดูproofย่อบนพื้นขาว/เขียว/เข้ม

## Required proof before delivery
ส่งmasterbinaryจริง, SHA256, observedsize/mode, detected8rects, border/gutter/safezone/diecutผลตรวจ และproof3พื้นให้ownerตรวจ ผลvisualกับผลtechnicalแยกกัน FAILหรือNOT_RUNต้องรายงานตรงๆ หากไม่เห็นกรอบดำครบทุกเฟรม masterถือไม่ผ่าน BORDER_MISSING_OR_INVALID แม้ภาพสวยและพื้นโปร่งใส ห้ามเรียกREADY_FOR_ENGINEจนcutterผ่าน และห้ามเรียกLINE_READYก่อนexport/platformchecks

