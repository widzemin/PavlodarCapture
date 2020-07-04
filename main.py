import telebot
bot = telebot.TeleBot('1066033330:AAGRLKs4XXRxpY-_GTcls0kYnutiLuEQtrw')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Иди нахуй Максим')

bot.polling()

