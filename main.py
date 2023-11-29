import telebot
bot = telebot.TeleBot('6778122356:AAE1EG7WGr3VhT2lpawCRUgo00ENl703J0I') 

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'здравствуйте! мы приветствуем Вас, можно узнать ваш запрос?')

bot.infinity_polling()
