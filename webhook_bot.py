from flask import Flask, request
import requests

app = Flask(__name__)

# بيانات البوت
TELEGRAM_TOKEN = "8029179226:AAGxqCJT4KOcd7wKIC5iHe4xPYUgQebWgfs"
CHAT_ID = "7081261649"

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    message = f"""🚨 تنبيه جديد ({data.get('trend', 'N/A')})

📌 الزوج: {data.get('pair', 'N/A')}
📥 الدخول: {data.get('entry', 'N/A')}
🎯 الهدف 1: {data.get('target1', 'N/A')}
🎯 الهدف 2: {data.get('target2', 'N/A')}
🎯 الهدف 3: {data.get('target3', 'N/A')}
🛑 وقف الخسارة: {data.get('stop_loss', 'N/A')}
🕒 الوقت: {data.get('time', 'N/A')}
"""
    send_to_telegram(message)
    return "تم الاستلام والإرسال ✅", 200

@app.route("/", methods=["GET"])
def home():
    return "📡 Webhook is running!", 200

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    response = requests.post(url, json=payload)
    print("📬 Telegram:", response.status_code, response.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
