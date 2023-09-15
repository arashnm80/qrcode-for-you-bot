from needed_modules import *
from functions import *
from log import *

bot = telebot.TeleBot(bot_api)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    log(f"{bot_name} log:\n\nCommand received from user {message.chat.id}")
    bot.reply_to(message, bot_introduction_msg)

@bot.message_handler(func=lambda message: True)
def send_qr(message):
    generate_qr(message.chat.id, message.text)
    output_file_path = f"{output_folder}/{message.chat.id}.png"
    with open(output_file_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    
bot.infinity_polling()
