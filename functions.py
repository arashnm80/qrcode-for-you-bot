from needed_modules import *

def generate_qr(user_id, text):
    qr = qrcode.QRCode(version=1, box_size=100, border=3)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#000000", back_color="#ffffff")
    output_file_path = f"{output_folder}/{user_id}.png"
    img.save(output_file_path, overwrite=True)

# if __name__ == '__main__':
#     generate_qr(123,"hello")