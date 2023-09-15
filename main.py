from needed_modules import *
from functions import *

bot = telebot.TeleBot(bot_api)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, bot_introduction_msg)

@bot.message_handler(func=lambda message: True)
def send_qr(message):
    generate_qr(message.chat.id, message.text)
    output_file_path = f"{output_folder}/{message.chat.id}.png"
    with open(output_file_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    # delete photo after sending
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
    
bot.infinity_polling()
