import os
import requests

# ดึง GAS_URL จาก Environment Variable (หากไม่มีให้ใช้ค่าสำรอง)
GAS_URL = os.getenv("GAS_URL", "https://script.google.com/macros/s/AKfycbz19bP8c9tSb-6YPVKRYLgQoyYlbY5i3u2xlDW-gujbCI3HON8aEaISVm8UNCR_GNFBVA/exec")

def save_to_google_sheets(user_id, user_name, user_message):
    """
    ฟังก์ชันยิงข้อมูล LINE ID, ชื่อผู้ใช้ และข้อความไปบันทึกบน Google Sheets
    """
    if "YOUR_DEPLOYMENT_ID" in GAS_URL:
        print("⚠️ ยังไม่ได้ใส่ GAS_URL ที่ถูกต้อง")
        return False

    payload = {
        "userId": user_id,
        "name": user_name,
        "message": user_message
    }
    
    try:
        response = requests.post(GAS_URL, json=payload, timeout=5)
        return response.status_code == 200
    except Exception as e:
        print(f"Error saving to Google Sheets: {e}")
        return False