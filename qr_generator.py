import qrcode
from qrcode.constants import ERROR_CORRECT_H

def generate_qr_code(data, file_name):
    
    # add QR code instance
    qr = qrcode.QRCode(
        version = 4, # size of the QR code
        box_size = 12,
        border = 4, 
        error_correction=ERROR_CORRECT_H # controls the error correction used in the QR code
    )

    # add QR code data
    qr.add_data(data)
    qr.make(fit=True) # find the best size for the data

    # create image from the QR code instance
    qr_image = qr.make_image(
        fill_color = "black",
        back_color = "white"
    )

