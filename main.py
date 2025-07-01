# Dein echter Telegram Bot Token
TOKEN = '7404537703:AAEtSSQBE6Cuf3TpLEa0bJScUtol4TB66o0'
bot = telebot.TeleBot(TOKEN)

# Begrüßung bei /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Willkommen bei CoinStarrr! ✨")

# Echo: antwortet auf alles
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Bot starten
bot.infinity_polling()