import telebot

# التوكن الخاص بك
TOKEN = '7784931197:AAFE0CtIslDZ05FmyUEU2Zidm7gwpNSsVtI'
# الـ Chat ID الذي حصلنا عليه
CHAT_ID = '7081261649'

bot = telebot.TeleBot(TOKEN)

def send_signal(message):
    bot.send_message(CHAT_ID, message)

# 📈 صفقة تجريبية
signal = "🚨 صفقة جديدة:\nزوج: BTCUSDT\nشراء من: 65500\nالهدف: 67000\nالستوب: 64800"
send_signal(signal)
