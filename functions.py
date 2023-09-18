from needed_modules import *

def generate_qr(user_id, text):
    output_file_path = f"{output_folder}/{user_id}.png"
    # Check if the file already exists and remove it
    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    # # version 1 of qrcode creation
    # qr = qrcode.QRCode(version=10, box_size=100, border=3)
    # qr.add_data(text)
    # qr.make(fit=True)
    # img = qr.make_image(fill_color="#000000", back_color="#ffffff")
    # img.save(output_file_path)

    # version 2 of qrcode creation
    img = qrcode.make(text)
    img.save(output_file_path)
    