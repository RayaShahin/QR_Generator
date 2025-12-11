import qrcode
from qrcode.constants import ERROR_CORRECT_H

def generate_qr_code():
    
    # add QR code instance
    qr = qrcode.QRCode(
        version = 4, # size of the QR code
        box_size = 12,
        border = 4, 
        error_correction=ERROR_CORRECT_H # controls the error correction used in the QR code
    )