def get_travel_flex_carousel(domain_url=""):
    """
    Flex Carousel แนะนำสถานที่ท่องเที่ยว 10 แห่ง (ไทย-จีน และ จีน-ลาว)
    พร้อมรูปภาพตรงสถานที่จริง และปุ่มกดส่งข้อความดูรายละเอียดทัวร์
    """
    places = [
        # --- เส้นทาง ไทย - จีน ---
        {
            "name": "กำแพงเมืองจีน (ปักกิ่ง)",
            "desc": "1 ใน 7 สิ่งมหัศจรรย์ของโลก สิ่งก่อสร้างยิ่งใหญ่ระดับตำนาน",
            "img": "https://images.unsplash.com/photo-1508804185872-d7badad00f7d?w=500",
            "action_text": "รายละเอียดทัวร์ปักกิ่ง"
        },
        {
            "name": "พระราชวังต้องห้าม (ปักกิ่ง)",
            "desc": "พระราชวังโบราณใจกลางกรุงปักกิ่ง สถาปัตยกรรมสุดอลังการ",
            "img": "https://images.unsplash.com/photo-1543731068-7e0f5beff43a?w=500",
            "action_text": "รายละเอียดทัวร์ปักกิ่ง"
        },
        {
            "name": "อุทยานป่าหิน (คุนหมิง)",
            "desc": "มหัศจรรย์ปฏิมากรรมหินธรรมชาติอายุกว่าร้อยล้านปี",
            "img": "https://images.unsplash.com/photo-1599571234909-29ed5d1321d6?w=500",
            "action_text": "รายละเอียดทัวร์ไทย-จีน"
        },
        {
            "name": "หุบเขาพระจันทร์สีน้ำเงิน (ลี่เจียง)",
            "desc": "น้ำตกแม่น้ำสีฟ้ามรกต วิวทิวทัศน์หิมะด้านหลังสุดตระการตา",
            "img": "https://images.unsplash.com/photo-1528164344705-47542687990d?w=500",
            "action_text": "รายละเอียดทัวร์ไทย-จีน"
        },
        {
            "name": "หาดพัทยา (ชลบุรี ไทย)",
            "desc": "เมืองท่องเที่ยวชายทะเลใกล้นครหลวง ยอดฮิตของชาวต่างชาติ",
            "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=500",
            "action_text": "รายละเอียดทัวร์ไทย-จีน"
        },

        # --- เส้นทาง จีน - ลาว ---
        {
            "name": "สิบสองปันนา (ยูนนาน)",
            "desc": "สัมผัสวัฒนธรรมไทลื้อและบรรยากาศตลาดยามค่ำคืนริมแม่น้ำโขง",
            "img": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?w=500",
            "action_text": "รายละเอียดทัวร์จีน-ลาว"
        },
        {
            "name": "หลวงพระบาง (ลาว)",
            "desc": "เมืองมรดกโลก สัมผัสวิถีชีวิตตักบาตรข้าวเหนียวและวัดโบราณ",
            "img": "https://images.unsplash.com/photo-1583417319070-4a69db38a482?w=500",
            "action_text": "รายละเอียดทัวร์จีน-ลาว"
        },
        {
            "name": "วังเวียง (ลาว)",
            "desc": "กุ้ยหลินเมืองลาว สายชิลธรรมชาติต้องไม่พลาด ล่องห่วงยางลำธาร",
            "img": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=500",
            "action_text": "รายละเอียดทัวร์จีน-ลาว"
        },
        {
            "name": "พระธาตุหลวง (เวียงจันทน์)",
            "desc": "ชมพระธาตุหลวงสีทองอร่าม แลนด์มาร์กศูนย์รวมจิตใจของชาวลาว",
            "img": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=500",
            "action_text": "รายละเอียดทัวร์จีน-ลาว"
        },
        {
            "name": "น้ำตกตาดกวางสี (หลวงพระบาง)",
            "desc": "น้ำตกหินปูนชั้นสวยงาม น้ำสีฟ้าเทอร์ควอยซ์ธรรมชาติ",
            "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=500",
            "action_text": "รายละเอียดทัวร์จีน-ลาว"
        }
    ]

    bubbles = []
    for p in places:
        bubbles.append({
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": p["img"],
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {"type": "text", "text": p["name"], "weight": "bold", "size": "lg"},
                    {"type": "text", "text": p["desc"], "size": "sm", "color": "#888888", "wrap": True, "margin": "md"}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#02B150",
                        "action": {
                            "type": "message",
                            "label": "ดูรายละเอียดแพ็กเกจ",
                            "text": p["action_text"]
                        }
                    }
                ]
            }
        })

    return {
        "type": "flex",
        "altText": "แนะนำ 10 สถานที่ท่องเที่ยว (ไทย-จีน / จีน-ลาว)",
        "contents": {
            "type": "carousel",
            "contents": bubbles
        }
    }


def get_tour_package_flex():
    """
    Flex Carousel แพ็กเกจทัวร์ 2 วัน 3 คืน (ไทย-จีน และ จีน-ลาว)
    """
    packages = [
        {
            "title": "แพ็กเกจ ไทย-จีน 2 วัน 3 คืน",
            "desc": "เที่ยวคุนหมิง-ป่าหิน-หุบเขาพระจันทร์ พักโรงแรม 4 ดาว ฟรีวีซ่า",
            "price": "ราคา 11,900 บาท / ท่าน",
            "img": "https://images.unsplash.com/photo-1508804185872-d7badad00f7d?w=500",
            "detail_text": "รายละเอียดทัวร์ไทย-จีน",
            "booking_text": "จองทัวร์ไทย-จีน 2วัน3คืน"
        },
        {
            "title": "แพ็กเกจ จีน-ลาว 2 วัน 3 คืน",
            "desc": "นั่งรถไฟความเร็วสูง สิบสองปันนา-หลวงพระบาง-วังเวียง-เวียงจันทน์",
            "price": "ราคา 9,900 บาท / ท่าน",
            "img": "https://images.unsplash.com/photo-1583417319070-4a69db38a482?w=500",
            "detail_text": "รายละเอียดทัวร์จีน-ลาว",
            "booking_text": "จองทัวร์จีน-ลาว 2วัน3คืน"
        }
    ]

    bubbles = []
    for pkg in packages:
        bubbles.append({
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": pkg["img"],
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {"type": "text", "text": pkg["title"], "weight": "bold", "size": "xl"},
                    {"type": "text", "text": pkg["desc"], "size": "sm", "color": "#666666", "margin": "md", "wrap": True},
                    {"type": "text", "text": pkg["price"], "weight": "bold", "size": "md", "color": "#E53935", "margin": "sm"}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "secondary",
                        "action": {
                            "type": "message",
                            "label": "ดูโปรแกรมการเดินทาง",
                            "text": pkg["detail_text"]
                        }
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#0056B3",
                        "action": {
                            "type": "message",
                            "label": "สนใจจองแพ็กเกจนี้",
                            "text": pkg["booking_text"]
                        }
                    }
                ]
            }
        })

    return {
        "type": "flex",
        "altText": "แพ็กเกจทัวร์ 2 วัน 3 คืน (ไทย-จีน / จีน-ลาว)",
        "contents": {
            "type": "carousel",
            "contents": bubbles
        }
    }