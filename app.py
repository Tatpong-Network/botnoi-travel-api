from flask import Flask, request, jsonify, send_from_directory
import requests
import os
from deep_translator import GoogleTranslator

# ดึงโมดูล flex_templates และ google_sheets ที่สร้างไว้
from flex_templates import get_travel_flex_carousel, get_tour_package_flex
from google_sheets import save_to_google_sheets

app = Flask(__name__)

# ดึง LINE Access Token จาก Environment Variable (หากไม่มีให้ใช้ค่าสำรอง)
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN", "uDBGnZLLvai5KHJ6gRASyJJEdSYWxO7AIQM+3YnN6MDWXT7kti2eEeUZjrIknzdE/f7N4E6FNnK5Ml00xif6RwrWiPOvGgy5gldzxqAPOhFxPLbfXqeNtpB8ni8SpDsOYqvVcTYYk9W8ggdD/n/kUAdB04t89/1O/w1cDnyilFU=")

user_states = {}

def get_line_profile(user_id):
    """
    ดึงชื่อ Display Name ของผู้ใช้งานจาก LINE API
    """
    headers = {'Authorization': f'Bearer {LINE_ACCESS_TOKEN}'}
    try:
        res = requests.get(f'https://api.line.me/v2/bot/profile/{user_id}', headers=headers, timeout=5)
        if res.status_code == 200:
            return res.json().get('displayName', 'คุณลูกค้า')
    except Exception as e:
        print(f"Error fetching profile: {e}")
    return 'คุณลูกค้า'

@app.route('/static/<filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(force=True, silent=True) or {}
    print("Received data:", data)

    events = data.get('events', [])
    if not events:
        return jsonify({"status": "ok"}), 200

    event = events[0]
    reply_token = event.get('replyToken')
    user_id = event.get('source', {}).get('userId', 'ไม่ระบุ ID')
    if not reply_token:
        return jsonify({"status": "ok"}), 200

    user_text = event.get('message', {}).get('text', '').strip()
    domain_url = request.host_url.rstrip('/')
    messages = []

    # ดึงชื่อ Display Name ของผู้ใช้
    user_name = get_line_profile(user_id) if user_id != 'ไม่ระบุ ID' else "คุณลูกค้า"

    # บันทึกประวัติการพิมพ์ทุกข้อความลง Google Sheets (LINE ID | Name | Message)
    save_to_google_sheets(user_id, user_name, user_text)

    # แปลงเป็นตัวพิมพ์เล็กสำหรับคำสั่งภาษาอังกฤษ (เช่น hi, hello)
    user_text_lower = user_text.lower()

    # --- โลจิกประมวลผลคำสั่งตาม Intent ---

    # 1. Intent: ทักทาย (Greeting)
    if user_text_lower in ["สวัสดี", "สวัสดีครับ", "สวัสดีค่ะ", "hi", "hello"]:
        user_states[user_id] = None  # ยกเลิกโหมดแปลภาษาถ้ามีอยู่
        messages.append({
            "type": "text", 
            "text": f"สวัสดีค่ะคุณ {user_name}! 👋\nยินดีต้อนรับสู่ Travel Guide Bot ค่ะ มีอะไรให้แนะนำเกี่ยวกับสถานที่ท่องเที่ยวหรือแพ็กเกจทัวร์ไหมคะ?"
        })

    # 2. Intent: แปลภาษา (แปลไทย-จีน / แปลจีน-ไทย)
    elif user_text == "แปลไทย-จีน":
        user_states[user_id] = "TH_TO_CN"
        messages.append({"type": "text", "text": "เปิดโหมดแปลภาษา [ไทย -> จีน] แล้วค่ะ! พิมพ์ข้อความภาษาไทยส่งมาได้เลย"})

    elif user_text in ["แปลจีน-ไทย", "พิมพ์จีน"]:
        user_states[user_id] = "CN_TO_TH"
        messages.append({"type": "text", "text": "已开启 [中文 -> 泰语] 翻译模式！请发送中文 short text。"})

    # 3. Intent: ดูแพ็กเกจทัวร์
    elif user_text in ["ดูแพ็กเกจทัวร์", "Package tour", "ทัวร์"]:
        messages.append(get_tour_package_flex())

    # 4. Intent: ดูสถานที่ท่องเที่ยว
    elif user_text in ["ที่เที่ยว", "แนะนำที่เที่ยว"]:
        user_states[user_id] = None
        messages.append(get_travel_flex_carousel(domain_url))

    # 5. Intent: ซื้อ / สั่งซื้อ / จองทัวร์
    elif "จองทัวร์" in user_text or "ซื้อ" in user_text or "สั่งซื้อ" in user_text:
        messages.append({
            "type": "text", 
            "text": f"ขอบคุณค่ะ คุณ {user_name}\nระบบได้บันทึกความสนใจ '{user_text}' เรียบร้อยแล้ว เจ้าหนาที่จะติดต่อกลับเพื่อยืนยันข้อมูลโดยเร็วที่สุดค่ะ"
        })

    # 6. ประมวลผลแปลภาษาเมื่ออยู่ในโหมดแปล
    elif user_id in user_states and user_states[user_id] == "TH_TO_CN":
        translated = GoogleTranslator(source='th', target='zh-CN').translate(user_text)
        messages.append({"type": "text", "text": f"🇨🇳 คำแปลภาษาจีน:\n{translated}"})

    elif user_id in user_states and user_states[user_id] == "CN_TO_TH":
        translated = GoogleTranslator(source='zh-CN', target='th').translate(user_text)
        messages.append({"type": "text", "text": f"🇹🇭 คำแปลภาษาไทย:\n{translated}"})

    # ข้อความเริ่มต้นกรณีทั่วไป (Default Fallback)
    else:
        messages.append({
            "type": "text", 
            "text": f"สวัสดีค่ะ คุณ {user_name}!\nคุณสามารถเลือกกดปุ่มเมนูด้านล่าง หรือพิมพ์ 'ที่เที่ยว', 'ดูแพ็กเกจทัวร์' ได้เลยค่ะ"
        })

    # ส่งข้อความกลับหา LINE API
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LINE_ACCESS_TOKEN}'
    }
    payload = {
        'replyToken': reply_token,
        'messages': messages
    }

    requests.post('https://api.line.me/v2/bot/message/reply', headers=headers, json=payload)

    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(port=5000, debug=True)