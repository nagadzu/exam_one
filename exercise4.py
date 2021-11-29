import telebot

TOKEN = "2110248904:AAGduom6637ev0sDGGDOMyae0Gk94eifL0I"

bot = telebot.TeleBot(TOKEN)
count = "A, E, I, O, U, a, e, i, o, u"
count = 0

@bot.message_handler(commands=['start'])
def send_hello(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     "Are u Ikhtiyar?",)


@bot.message_handler(content_types=['text', 'document', 'audio'])
def counter():
    chat_id = message.chat.id
    if message.text == "A, E, I, O, U, a, e, i, o, u"
    count + 1
    bot.send_message(chat_id, "в этом предложении {count} гласных")