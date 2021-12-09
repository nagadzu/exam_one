import telebot

TOKEN = ''

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(content_types=['text'])
def auto_hendler(message):
    text = message.text.lower()
    print(text)
    glasnie = 0
    for i in text:
        letter = i.lower()
        if letter == "a" or letter == "e" or \
                letter == "i" or letter == "o" or \
                letter == "u" or letter == "y":
            glasnie += 1

    bot.send_message(message.from_user.id, f'Гласных слов в слове: {glasnie}')

bot.infinity_polling()