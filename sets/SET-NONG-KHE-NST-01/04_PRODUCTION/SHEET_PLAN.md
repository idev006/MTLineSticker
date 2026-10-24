# SHEET PLAN — น้องเข้ นสต. v0.6.0

## Layout
5 ชีท S01–S05 ชีทละ 8 ภาพ 4 คอลัมน์ 2 แถว ตาม mapping ราย frame ไม่มีช่องสำรอง ทุกเฟรมมีกรอบแยกไม่ใช้เส้นขอบร่วม จัด master ด้วย compositor หลังสร้างภาพ ไม่ฝากความแม่น pixel ให้ image model

## Geometry
Frame nominal 592x512 px; rescale ได้แต่อัตราส่วนต้องตรง w*512 == h*592 กรอบดำ #000000 alpha255 ประมาณ 3px เข้าในเฟรม Gutter nominal15px±5% ที่ integer จึงใช้15px Safe clearance เลือก20px±5% วัดจากขอบด้านในถึงไดคัทนอกสุด ไม่สับสนกับ gutter Nominal sheet2413x1039px ไม่มี margin ภายนอก; ขนาดจริงคำนวณจากกรอบและ gutter

## Alpha and diecut
PNG RGBA พื้น/ช่องว่าง alpha0 ไดคัทขาว #FFFFFF alpha255 3–5px รอบ silhouette รวม caption/prop/FX และแต่ละชิ้นลอย ไม่ใช่พื้นขาวสี่เหลี่ยม วัด safe zone รวมไดคัท ภาพนอน F30 และหัวจระเข้ยาวเป็นจุดเสี่ยง crop ต้องจัดให้พอดีก่อน compose

## Cutter interface
ส่งพิกัดกรอบจริงของทุกภาพและผล QA ให้ cutter เอากรอบดำออกแต่เก็บไดคัท ต้องตรวจไฟล์ตัดจริง 40 ภาพและขอบบนพื้นขาว/เขียว/เข้มก่อน READY_FOR_ENGINE engine ส่วนกลางเดิมยังต้องทดสอบ alpha preservation และ diecut ไม่ถือเอกสารเป็นหลักฐานรันผ่าน
