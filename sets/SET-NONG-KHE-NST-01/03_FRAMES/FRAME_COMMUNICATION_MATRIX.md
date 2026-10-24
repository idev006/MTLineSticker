# FRAME COMMUNICATION MATRIX — น้องเข้ นสต. v0.3.0

## Shared locks
ใช้ L01–L07 ทุก frame สีหน้าและ props เปลี่ยนได้ตามรายการเท่านั้น แต่หัวและชุดต้องตรง Character ที่ผ่าน owner approval แผนนี้ยังเป็นข้อความผลิต ไม่มีภาพ pixels ที่ผ่าน visual QA

## Frame records
แต่ละรายการเป็น brief ส่งผลิตที่แยก intent กับท่าทางและ expectation อย่างชัดเจน

### F01
Caption: หวัดดีค้าบ | lock: PROPOSED
Sender intent: ทักทาย
Chat situation: เริ่มแชททักเพื่อนหรือคนคุย
Tone: เป็นกันเอง
Expression: ยิ้มอ่อน ตาปรือ คิ้วยกข้างเดียว
Pose/action: ยกมือทัก ยิ้มเอียงคอ
Minimum props: ไม่มี
Composition: มือที่ทักอยู่ข้างแก้ม ไม่บังปาก
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ทักแบบกวนอย่างสุภาพ
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F02
Caption: รับทราบครับ! | lock: PROPOSED
Sender intent: รับคำสั่ง
Chat situation: ตอบรับข้อความแจ้งงานหรือเพื่อนนัด
Tone: กระตือรือร้นปนลน
Expression: ตาเบิก ปากปิดตรง เหงื่อหนึ่งหยด
Pose/action: ยืนตรงทันที เหงื่อแตก
Minimum props: เหงื่อหยดเล็ก
Composition: ยืนตรงเต็มตัว แขนแนบลำตัว
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: รับเรื่องแล้ว
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F03
Caption: ขอบคุณค้าบ | lock: PROPOSED
Sender intent: ขอบคุณ
Chat situation: ได้รับความช่วยเหลือหรือคำชม
Tone: อบอุ่น
Expression: ยิ้มตาหยี ก้มคอเล็กน้อย
Pose/action: ไหว้ ยิ้มตาหยี
Minimum props: ไม่มี
Composition: ครึ่งตัว ไหว้ระดับอก มือไม่ทับปาก
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ขอบคุณอย่างจริงใจ
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F04
Caption: ขอโทษค้าบ | lock: PROPOSED
Sender intent: ขอโทษ
Chat situation: มาสายหรือตอบช้าจนเพื่อนรอ
Tone: สำนึกผิดแบบน่าเอ็นดู
Expression: หลบตา ปากหุบ คางลด
Pose/action: หัวหด กุมมือ
Minimum props: ไม่มี
Composition: กุมมือหน้าท้อง ไหล่ห่อ
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ขอโทษด้วยความเกรงใจ
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F05
Caption: ได้เลยเพื่อน | lock: PROPOSED
Sender intent: ตกลง
Chat situation: รับปากช่วยเพื่อนเรื่องเล็กๆ
Tone: มั่นใจ
Expression: ยิ้มเปิดมุมปาก มองตรง
Pose/action: ชูนิ้วโป้ง ยิ้ม
Minimum props: ไม่มี
Composition: ชูโป้งระดับอก นิ้วครบ
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ตกลงช่วยได้
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F06
Caption: จัดไป! | lock: PROPOSED
Sender intent: พร้อมลงมือ
Chat situation: เพื่อนชวนลงมือหรือออกเดินทาง
Tone: ฮึกเหิม
Expression: คิ้วแน่ว ยิ้มมุมปาก
Pose/action: กำหมัด ยืนก้าวหน้า ทำหน้ามั่นใจ
Minimum props: ไม่มี
Composition: กำหมัดหนึ่งข้าง ยืนก้าวหน้า แทนพับแขนเสื้อสั้น
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: พร้อมลงมือเดี๋ยวนี้
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F07
Caption: รอแป๊บ | lock: PROPOSED
Sender intent: ขอเวลา
Chat situation: กำลังแต่งตัวก่อนออกไปพบเพื่อน
Tone: เร่งรีบ
Expression: ตาลน ปากแง้ม
Pose/action: มือห้าม อีกมือใส่รองเท้า
Minimum props: รองเท้าดำ
Composition: นั่งใส่รองเท้า อีกมือห้าม นิ้วไม่พันกัน
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: รออีกนิด
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F08
Caption: ไปก่อนนะ | lock: PROPOSED
Sender intent: ลา
Chat situation: ขอตัวออกจากแชทหรือจากกลุ่ม
Tone: สบายๆ
Expression: ยิ้มกว้างแบบเป็นมิตร
Pose/action: สะพายกระเป๋า โบกมือ
Minimum props: กระเป๋าผ้าสีเข้ม
Composition: โบกมือเหนือไหล่ กระเป๋าอยู่ข้างสะโพก
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ขอตัวก่อน
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F09
Caption: วันนี้ขอหล่อ | lock: PROPOSED
Sender intent: อวดหล่อ
Chat situation: ก่อนออกไปพบสาวหรือถ่ายรูป
Tone: เก๊กมั่นใจ
Expression: เชิดคาง ตาปรือ ยิ้มเจ้าเล่ห์
Pose/action: จัดปกเสื้อ เชิดคาง
Minimum props: ไม่มี
Composition: จัดปกเสื้อ อกผาย ร่างคนเห็นครึ่งตัวขึ้นไป
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ขออวดหล่อหนึ่งวัน
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F10
Caption: ทรงได้อยู่ | lock: PROPOSED
Sender intent: มั่นใจตัวเอง
Chat situation: ส่งเซลฟีแล้วชื่นชมตัวเอง
Tone: หลงตัวเองขำๆ
Expression: หรี่ตาประเมินตน ยิ้มพอใจ
Pose/action: ส่องกระจก ยิ้มพอใจ
Minimum props: กระจกมือถือ
Composition: ถือกระจกเล็กต่ำกว่าระดับตา
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ดูดีอยู่นะ
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F11
Caption: เผลอ ๆ ก็เท่ | lock: PROPOSED
Sender intent: เก๊กเผลอ
Chat situation: แกล้งโพสเผลอให้คนสนใจ
Tone: เก๊กเนียน
Expression: สายตาเหล่มาที่คนดู ปากยิ้มข้างเดียว
Pose/action: แกล้งมองไกล เหล่มองกล้อง
Minimum props: ไม่มี
Composition: ตัวหันสามส่วน แขนกอดอกหลวม
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: แอบโพสเท่
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F12
Caption: มองเราเหรอ | lock: PROPOSED
Sender intent: ชวนคุย
Chat situation: มีคนส่งสัญญาณสนใจในแชท
Tone: หยอกล้อ
Expression: ตาเบิกนิดหนึ่ง คิ้วยก หน้าแดงบาง
Pose/action: ชี้ตัวเอง คิ้วยก
Minimum props: ไม่มี
Composition: ชี้นิ้วเข้าหน้าอก ไม่ชี้ปืนใส่ผู้รับ
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ชวนให้สนใจเรา
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F13
Caption: คนนี้มีใจ | lock: PROPOSED
Sender intent: บอกชอบ
Chat situation: ต้องการบอกชอบโดยไม่รุกมาก
Tone: อ่อนโยนแต่เก๊ก
Expression: ปากยิ้มสงบ แก้มแดงเล็กน้อย
Pose/action: ยื่นหัวใจเล็ก ทำหน้าขรึม
Minimum props: หัวใจหนึ่งดวง
Composition: ยื่นหัวใจเล็กหนึ่งดวงใกล้อก
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ส่งใจให้
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F14
Caption: จีบได้ ยังโสด | lock: PROPOSED
Sender intent: อ่อยขำๆ
Chat situation: แนะนำสถานะโสดแบบขำๆ
Tone: ขี้เล่น
Expression: ตาปรือ ยิ้มมุมปาก
Pose/action: พิงเสาเล็ก ยิ้มมุมปาก
Minimum props: เสาเรียบส่วนสั้น
Composition: พิงเสาเรียบเล็ก ตัวเอนเล็กน้อย ไม่มีท่าชี้คุกคาม
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: เปิดให้เข้ามาคุย
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F15
Caption: คิดถึงค้าบ | lock: PROPOSED
Sender intent: คิดถึง
Chat situation: บอกคนคุยว่าอยากเจอ
Tone: คิดถึง
Expression: ตาอ่อน ปากยิ้มเศร้านิดๆ
Pose/action: กอดหมอน หน้าแดง
Minimum props: หมอนเรียบ
Composition: กอดหมอนแน่น หัวเอียงหาคนดู
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: คิดถึงแบบอ้อน
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F16
Caption: ฝันดีนะ | lock: PROPOSED
Sender intent: บอกฝันดี
Chat situation: ปิดบทสนทนาก่อนนอน
Tone: อ่อนโยน
Expression: ตาปรือสงบ ยิ้มบาง
Pose/action: ห่มผ้า กอดหัวใจ
Minimum props: ผ้าห่มและหัวใจ
Composition: ห่มผ้าบนไหล่ กอดหัวใจเล็ก เสื้อชุดนักเรียนเห็นช่วงปกเป็นสัญลักษณ์
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: บอกฝันดี
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F17
Caption: สาวมา! | lock: PROPOSED
Sender intent: เตือนเพื่อน
Chat situation: เตือนเพื่อนว่าเจอคนที่ชอบ
Tone: ตื่นเต้น
Expression: ตาโต ปากแง้มเบา
Pose/action: สะกิดเพื่อน ตาโต
Minimum props: แขนเพื่อนประกอบ
Composition: สะกิดเพียงไหล่หรือแขนเพื่อนที่เข้ามาริมภาพ
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: สะกิดให้รู้ตัว
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F18
Caption: เก๊กก่อน | lock: PROPOSED
Sender intent: สร้างภาพเท่แต่กลัวเสียทรง
Chat situation: ตั้งตัวให้เท่ก่อนพบคนคุย
Tone: เก๊กปนลน
Expression: ตาปรือยิ้ม แต่เหงื่อเม็ดหนึ่งและมือสั่น
Pose/action: จัดปกเสื้อ อกผาย มือสั่นเมื่อเห็นเงาครูฝึก
Minimum props: เงาครูฝึกหนึ่งรูปขนาดรอง
Composition: ครึ่งถึงเต็มตัวจัดปกเสื้อ มีเงาครูฝึกเล็กข้างหลัง
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ทำเท่แต่กลัวเสียทรง
Hero: YES
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F19
Caption: หล่อยังเพื่อน | lock: PROPOSED
Sender intent: ขอความเห็น
Chat situation: ขอให้เพื่อนดูความเรียบร้อย
Tone: ขอความมั่นใจ
Expression: คิ้วยก สายตาถาม
Pose/action: หันข้าง ชี้เสื้อให้เพื่อนตรวจ
Minimum props: ไม่มี
Composition: หันข้างเล็กน้อย มือชี้ปกเสื้อตัวเอง
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ช่วยดูให้หน่อย
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F20
Caption: อย่าเพิ่งแฉ | lock: PROPOSED
Sender intent: ห้ามแซว
Chat situation: เพื่อนกำลังเล่าเรื่องหน้าแตก
Tone: ลนแบบตลก
Expression: ตาเหลือก ยิ้มแห้ง
Pose/action: ยกฝ่ามือห้ามเพื่อนอย่างขำๆ ตาลน
Minimum props: ไหล่เพื่อนประกอบ
Composition: ฝ่ามือห้ามตรงหน้าอกเพื่อน ไม่จับปิดปากจริง
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: อย่าเพิ่งแฉเรา
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F21
Caption: เขายิ้มให้! | lock: PROPOSED
Sender intent: ดีใจ
Chat situation: ดีใจที่คิดว่าคนที่ชอบยิ้มให้
Tone: ปลื้มใจ
Expression: ตาเป็นประกาย ปากยิ้มกว้าง
Pose/action: ตัวลอย ตาเป็นประกาย หัวใจสองดวง
Minimum props: หัวใจสองดวง
Composition: ยกส้นเท้าดีใจ หัวใจสองดวงอยู่ใกล้หัว
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: เขาสนใจเราหรือเปล่า
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F22
Caption: อ้าว…ยิ้มให้เพื่อน | lock: PROPOSED
Sender intent: หน้าแตก
Chat situation: เพิ่งรู้ว่าคนที่ชอบมองคนอื่น
Tone: หน้าแตก
Expression: ตาค้าง ปากตรง แก้มซีดลง
Pose/action: ยืนค้าง หัวใจแฟบ
Minimum props: หัวใจแฟบหนึ่งดวง
Composition: ยืนชะงัก หัวใจแฟบข้างอก
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: เข้าใจผิดเอง
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F23
Caption: ใจเย็นไอ้เข้ | lock: PROPOSED
Sender intent: ระงับความเขิน
Chat situation: พยายามตั้งสติหลังโดนชม
Tone: เขินมาก
Expression: แก้มแดง คิ้วโค้ง ตาหลบ
Pose/action: จับอกตัวเอง หน้าแดงจัด
Minimum props: ไม่มี
Composition: มือทาบอก หายใจเข้า ไม่ตีกระแทกตัวเอง
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: เตือนตัวเองให้ใจเย็น
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F24
Caption: เสียทรงเลย | lock: PROPOSED
Sender intent: กลบเกลื่อน
Chat situation: โดนแซวจนความเท่หาย
Tone: ขำเขิน
Expression: ยิ้มแห้ง ตาหลุบ
Pose/action: ยิ้มแห้ง ปกเสื้อยับ
Minimum props: ไม่มี
Composition: ไหล่ห่อ ปกเสื้อยับเล็กน้อย มือเกาท้ายหัว
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: หลุดเก๊กแล้ว
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F25
Caption: ครูฝึกมา! | lock: PROPOSED
Sender intent: ตกใจ
Chat situation: เตือนเพื่อนให้กลับมามีระเบียบ
Tone: ตกใจ
Expression: ตาเบิก คิ้วสูง ปากเม้ม
Pose/action: ยืนตรง ตาเหลือก
Minimum props: เส้นตกใจสองเส้น
Composition: ยืนตรงฉับพลัน มือแนบตัว
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ครูฝึกใกล้เข้ามา
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F26
Caption: ผมพร้อมครับ! | lock: PROPOSED
Sender intent: รวบรวมความกล้า
Chat situation: ตอบรับภารกิจแม้แอบกลัว
Tone: ฮึดสู้
Expression: ตาแน่ว ปากยิ้มฝืน
Pose/action: ยืนฮึด ขาสั่น
Minimum props: เส้นสั่นสองเส้น
Composition: อกตั้ง ยืนตรง เข่าสั่นเล็กน้อย
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ใจพร้อมรับหน้าที่
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F27
Caption: พร้อมแต่ใจ | lock: PROPOSED
Sender intent: เหนื่อยแต่ใจสู้
Chat situation: เพื่อนชวนทำสิ่งที่เหนื่อยมาก
Tone: เหนื่อยแต่ใจสู้
Expression: ตาปรือ ยิ้มมุมปากแห้ง
Pose/action: นั่งหมดแรง ยกมือสู้
Minimum props: ไม่มี
Composition: นั่งกอง ยกหมัดเล็กที่ระดับไหล่
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: อยากสู้แต่แรงหมด
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F28
Caption: อีกกี่รอบครับ | lock: PROPOSED
Sender intent: ถามอย่างเหนื่อย
Chat situation: ถามว่างานหรือการฝึกเหลือเท่าไร
Tone: เหนื่อยขำๆ
Expression: ตาเหลือบหลัง ลิ้นออกเล็กน้อย
Pose/action: วิ่งลิ้นห้อย เหลียวหลัง
Minimum props: เหงื่อสองหยด
Composition: วิ่งช้า แขนแกว่ง มีเหงื่อสองหยด
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: เหลืออีกมากไหม
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F29
Caption: ขอพักหายใจ | lock: PROPOSED
Sender intent: ขอพัก
Chat situation: ขอหยุดพักจากกิจกรรมหนัก
Tone: อ่อนแรง
Expression: ตาปิดครึ่ง ปากแง้ม
Pose/action: ก้มจับเข่า เหงื่อท่วม
Minimum props: เหงื่อสามหยด
Composition: ก้มจับเข่า ลำตัวเอนอยู่ในเฟรม
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ขอหายใจสักครู่
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F30
Caption: ยังไหว…มั้ง | lock: PROPOSED
Sender intent: ฝืนสู้
Chat situation: บอกว่ายังสู้แม้เกือบหมดแรง
Tone: ฝืนแบบตลก
Expression: ตาปรือเกือบปิด ยิ้มแห้ง
Pose/action: นอนแผ่ ชูนิ้วโป้ง
Minimum props: ไม่มี
Composition: นอนหงายสั้นๆ ชูโป้งให้เห็นชัด ไม่เป็นท่าบาดเจ็บ
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ยังพอไหว
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F31
Caption: ตั้งใจเรียนอยู่ | lock: PROPOSED
Sender intent: แก้ง่วง
Chat situation: เพื่อนถามว่าอ่านหนังสืออยู่ไหม
Tone: แกล้งขยัน
Expression: ตาปรือหรี่ลง คิ้วฝืนตั้ง
Pose/action: ถือหนังสือกลับหัว ตาปรือ
Minimum props: หนังสือปกเรียบ
Composition: ถือหนังสือกลับหัว ข้อความบนสติกเกอร์ยังอ่านตรง
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: กำลังพยายามเรียน
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F32
Caption: ตาจะปิดแล้ว | lock: PROPOSED
Sender intent: ง่วงมาก
Chat situation: เรียนหรืออ่านจนง่วงมาก
Tone: ง่วง
Expression: เปลือกตาหนัก ปากหาว
Pose/action: พยายามเบิกตาหนังสือเปิด
Minimum props: หนังสือเปิด
Composition: หนังสือเปิดต่ำกว่าอก มือพยุงคาง
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ใกล้หลับแล้ว
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F33
Caption: หิวแล้วค้าบ | lock: PROPOSED
Sender intent: หิว
Chat situation: ถึงเวลาอาหารหรือชวนไปกิน
Tone: กระตือรือร้น
Expression: ตาเป็นประกาย ยิ้มกว้าง
Pose/action: ถือถาดอาหาร ตาเป็นประกาย
Minimum props: ถาดข้าว
Composition: ถือถาดใกล้เอว ถาดไม่บังชุดทั้งหมด
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: หิวแล้ว
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F34
Caption: เติมพลังแป๊บ | lock: PROPOSED
Sender intent: พักกินข้าว
Chat situation: พักบทสนทนาเพื่อกินข้าว
Tone: อิ่มเอม
Expression: แก้มตุ่ย ตายิ้ม
Pose/action: กินข้าวแก้มตุ่ย
Minimum props: ช้อนและจานข้าว
Composition: ยกช้อนใกล้ปาก ถาดอยู่ด้านล่าง
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ขอกินก่อน
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F35
Caption: วันปล่อยแล้ว! | lock: PROPOSED
Sender intent: ดีใจได้ออกนอกโรงเรียน
Chat situation: ได้หยุดหรือได้ออกนอกโรงเรียน
Tone: ดีใจสุดๆ
Expression: ตาโต ยิ้มกว้าง
Pose/action: กระโดดดีใจ ถือกระเป๋า
Minimum props: กระเป๋าผ้าสีเข้ม
Composition: กระโดดหนึ่งขา อีกมือยกกระเป๋า รองเท้าไม่หลุดเฟรม
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ดีใจที่ได้ออกไปพัก
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F36
Caption: กลับเข้าโรงเรียน | lock: PROPOSED
Sender intent: อาลัยวันหยุด
Chat situation: หมดวันหยุดต้องกลับไปเรียน
Tone: อาลัยแบบขำๆ
Expression: ตาตก ยิ้มเศร้า ปากห้อยนิด
Pose/action: ลากกระเป๋า ไหล่ตก
Minimum props: กระเป๋าลากเล็ก
Composition: ลากกระเป๋า ไหล่ตก หลังห่อเล็กน้อย
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ต้องกลับไปแล้ว
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F37
Caption: เพื่อนรัก | lock: PROPOSED
Sender intent: มิตรภาพ
Chat situation: ส่งขอบคุณเพื่อนสนิท
Tone: อบอุ่น
Expression: ยิ้มจริงใจ ตาอ่อน
Pose/action: กอดคอเพื่อน ยิ้ม
Minimum props: เพื่อนประกอบหนึ่งคน
Composition: กอดไหล่เพื่อนข้างเดียว เพื่อนเห็นเพียงหัวด้านข้างและไหล่
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: รักเพื่อนนะ
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F38
Caption: อย่าทิ้งกัน | lock: PROPOSED
Sender intent: ขออยู่ด้วย
Chat situation: อยากให้เพื่อนรอหรืออยู่ด้วย
Tone: อ้อน
Expression: ตาอ้อน คิ้วโค้ง
Pose/action: เกาะแขนเพื่อน ตาอ้อน
Minimum props: แขนเพื่อนประกอบ
Composition: เกาะแขนเพื่อนเบาๆ ไม่ดึงล้ม
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: อย่าปล่อยเราไว้คนเดียว
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F39
Caption: สู้ไปด้วยกัน | lock: PROPOSED
Sender intent: ให้กำลังใจ
Chat situation: ส่งแรงใจให้คนที่กำลังฝึกหรือเรียน
Tone: มุ่งมั่น
Expression: ยิ้มหนักแน่น สบตา
Pose/action: ชนหมัดเพื่อน มองอย่างมุ่งมั่น
Minimum props: หมัดเพื่อนประกอบ
Composition: ชนหมัดเพื่อนบริเวณกลางภาพ มือไม่ซ้อนผิดนิ้ว
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: เราสู้ไปด้วยกัน
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

### F40
Caption: จบไปด้วยกัน | lock: PROPOSED
Sender intent: ตั้งเป้าเรียนจบด้วยกัน
Chat situation: ให้กำลังใจกันจนเรียนสำเร็จ
Tone: ภูมิใจ
Expression: ยิ้มกว้าง ตาอ่อน
Pose/action: กอดคอเพื่อน ยิ้มภูมิใจ ยังอยู่ชุดนักเรียน
Minimum props: เพื่อนประกอบหนึ่งคน
Composition: กอดคอเพื่อนชี้มองข้างหน้า ยังสวมชุดนักเรียนไม่มีปริญญาหรือยศ
Character constraints: L01, L02, L03, L04, L05, L06, L07; ชุดนักเรียนร่างคนหัว REF01
Forbidden distractions: ห้ามหางหรือมือสัตว์; ห้ามเพิ่มยศ/ตราที่ไม่มีหลักฐาน; ห้ามฉากร้านและโลโก้; ไม่เพิ่มตัวละครเต็มตัวแย่งตัวหลัก
One-second expectation: ตั้งใจเรียนให้จบด้วยกัน
Hero: NO
Segmentation: รวมตัวละคร ข้อความ อุปกรณ์และเอฟเฟกต์ใน mask ไดคัท แต่ละองค์ประกอบลอยต้องมีไดคัทครบและไม่ชน safe zone

