from needed_modules import *

def log(log_message):
    # exit funciton if it should not send logs
    if not send_logs:
        return
    
    log_bot_url = "https://api.telegram.org/bot" + bot_api + "/"
    log_channel_id = os.environ['LOG_CHANNEL_ID'] # 'LOG_CHANNEL_ID' should be present in env
    log = requests.post(log_bot_url + "sendMessage", data={
        "chat_id": log_channel_id,
        "text": log_message
    })