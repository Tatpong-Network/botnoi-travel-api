BOTNOI-TRAVEL-API/
│
├── static/                   # 📁 โฟลเดอร์สำหรับเก็บรูปภาพทั้งหมด (เรียกใช้ผ่าน URL ได้)
│   ├── beach.jpg
│   ├── great_wall.jpg        # รูปกำแพงเมืองจีน
│   ├── kunming.jpg           # รูปอุทยานป่าหิน
│   └── luang_prabang.jpg     # รูปหลวงพระบาง
│
├── templates/                # 📁 โฟลเดอร์เก็บเทมเพลตข้อความ / Flex Message
│   ├── __init__.py
│   ├── travel_flex.py        # โค้ด Flex Carousel 10 สถานที่ท่องเที่ยว
│   └── tour_package_flex.py # โค้ด Flex Carousel แพ็กเกจทัวร์
│
├── .env                      # 🔐 ไฟล์เก็บ Token ในคอมส่วนตัว (ไม่ดันขึ้น GitHub)
├── app.py                    # 🚀 ไฟล์หลักรับ Webhook และส่งข้อความตอบกลับ
├── google_sheets.py          # 📊 ไฟล์จัดการเชื่อมต่อ Google Sheets API
├── Dockerfile
└── requirements.txt