import pyTelegramBotAPI as telebot
from pyTelegramBotAPI import types
from random import randrange

bot = telebot.TeleBot('1523718358:AAEkc6Kbq2cUz_JO3xMj5cMFUEYQd3CNv8Y')
to_chat_id = 391113744
from_chat_id = -1001417851600


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        key_get = types.KeyboardButton('Generate')
        keyboard.add(key_get)
        bot.send_message(message.from_user.id, text='Press button to get a random idiom', reply_markup=keyboard)
    else:
        message_id = randrange(150)
        print(message_id)
        bot.forward_message(message.from_user.id, from_chat_id, message_id)


bot.polling(none_stop=True, interval=0)
