import os

# messages
bot_introduction_msg = '''Hello
Send a text for me and I will make a QR-Code out of it for you'''

output_folder = "./output"
bot_api = os.environ["QRCODE_FOR_YOU_BOT"]

# log
send_logs = True # if is set to True 'LOG_CHANNEL_ID' should be defined env
