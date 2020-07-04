import telebot;
bot = telebot.TeleBot('1066033330:AAGRLKs4XXRxpY-_GTcls0kYnutiLuEQtrw')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'привет')

@bot.message_handler(commands=['end'])
def start_message(message):
    bot.send_message(message.chat.id, 'пошел нахуй')

@bot.message_handler(content_types=['text'])
def get(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()