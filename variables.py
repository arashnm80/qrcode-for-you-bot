import os

# settings
output_folder = "./output"
bot_api = os.environ["QRCODE_FOR_YOU_BOT_API"]
send_logs = True # if is set to True 'LOG_CHANNEL_ID' should be defined env

# names
bot_name = "QR-Code For You Bot"
bot_username = "@qrcode_for_you_bot"

# messages
start_cmd_msg = '''Hi, send me a text and I'll generate its qrcode for you 😉'''
help_cmd_msg = '''\
You can send me a text and I'll generate its qrcode for you 😉

This bot is open source. you can support the project by contributing or giving a star⭐️:
https://github.com/arashnm80/qrcode-for-you-bot

developer:
https://t.me/Arashnm80_Channel'''
error_message = '''Oops :(

Sorry, I couldn't make it but you can try again with another text.'''