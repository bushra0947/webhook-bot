from flask import Flask, request
import telebot

app = Flask(__name__)

# التوكن الخاص بك
TOKEN = '7784931197:AAFE0CtIslDZ05FmyUEU2Zidm7gwpNSsVtI'
# الـ Chat ID الذي حصلنا عليه
CHAT_ID = '7081261649'
bot = telebot.TeleBot(TOKEN)

@app.route('/send', methods=['POST'])
def send_signal():
    data = request.json

    message = (
        f"📢 إشارة جديدة:\n"
        f"📊 النوع: {data.get('type')}\n"
        f"💱 الزوج: {data.get('pair')}\n"
        f"💰 السعر الحالي: {data.get('price')}\n"
        f"🎯 TP1: {data.get('tp1')}\n"
        f"🎯 TP2: {data.get('tp2')}\n"
        f"🎯 TP3: {data.get('tp3')}\n"
        f"🛑 ستوب: {data.get('sl')}"
    )

    bot.send_message(CHAT_ID, message)
    return 'OK', 200

# لا تقم بتشغيل السيرفر هنا لأن Vercel يتكفل بذلك
