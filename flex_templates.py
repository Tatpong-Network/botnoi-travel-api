def get_travel_flex_carousel(domain_url=""):
    """
    Flex Carousel แนะนำสถานที่ท่องเที่ยว
    """
    image_url = f"{domain_url}/static/beach.jpg" if domain_url else "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=500"

    return {
        "type": "flex",
        "altText": "แนะนำสถานที่ท่องเที่ยว",
        "contents": {
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": image_url,
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {"type": "text", "text": "ทะเลสวยงาม", "weight": "bold", "size": "xl"},
                            {"type": "text", "text": "จุดเช็คอินแนะนำประจำสัปดาห์", "size": "sm", "color": "#888888"}
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
                                    "type": "uri",
                                    "label": "ดูรายละเอียด",
                                    "uri": "https://line.me"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }


def get_tour_package_flex():
    """
    Flex Carousel แพ็กเกจทัวร์ (ปักกิ่ง / คุนหมิง)
    """
    return {
        "type": "flex",
        "altText": "แพ็กเกจทัวร์ท่องเที่ยวแนะนำ",
        "contents": {
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://images.unsplash.com/photo-1508804185872-d7badad00f7d?w=500",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {"type": "text", "text": "ทัวร์ปักกิ่ง 5 วัน 4 คืน", "weight": "bold", "size": "xl"},
                            {"type": "text", "text": "ชมกำแพงเมืองจีน พระราชวังต้องห้าม", "size": "sm", "color": "#666666", "margin": "md"},
                            {"type": "text", "text": "ราคาเริ่มต้น 18,900 บาท", "weight": "bold", "size": "md", "color": "#E53935", "margin": "sm"}
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "button",
                                "style": "primary",
                                "color": "#0056B3",
                                "action": {
                                    "type": "message",
                                    "label": "สนใจจองทัวร์ปักกิ่ง",
                                    "text": "จองทัวร์ปักกิ่ง"
                                }
                            }
                        ]
                    }
                },
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://images.unsplash.com/photo-1543731068-7e0f5beff43a?w=500",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {"type": "text", "text": "ทัวร์คุนหมิง 4 วัน 3 คืน", "weight": "bold", "size": "xl"},
                            {"type": "text", "text": "ตื่นตาตื่นใจกับป่าหิน หุบเขาพระจันทร์藍月谷", "size": "sm", "color": "#666666", "margin": "md"},
                            {"type": "text", "text": "ราคาเริ่มต้น 14,900 บาท", "weight": "bold", "size": "md", "color": "#E53935", "margin": "sm"}
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "button",
                                "style": "primary",
                                "color": "#0056B3",
                                "action": {
                                    "type": "message",
                                    "label": "สนใจจองทัวร์คุนหมิง",
                                    "text": "จองทัวร์คุนหมิง"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }