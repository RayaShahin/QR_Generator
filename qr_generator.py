import argparse
import sys

import qrcode
from qrcode.constants import ERROR_CORRECT_H

def generate_qr_code(data, file_name, box_size=12, border=4):
    
    # error handling for empty data or file name
    if not data or not data.strip():
        raise ValueError("Data for QR code cannot be empty.")
    if not file_name or not file_name.strip():
        raise ValueError("File name cannot be empty.")
    
    # add QR code instance 
    qr = qrcode.QRCode(
        box_size=box_size,
        border=border,
        error_correction=ERROR_CORRECT_H # controls the error correction used for the QR code
    ) 

    # add QR code data
    qr.add_data(data)
    qr.make(fit=True) # find the best size for the data

    # create image from the QR code instance
    qr_image = qr.make_image(
        fill_color = "black",
        back_color = "white"
    )

    # save QR code image
    qr_image.save(f"{file_name}.png")

data = input("Enter URL for the QR code: ")
file_name = input("Enter file name to save: ")

generate_qr_code(data, file_name)
print(f"QR code generated and saved as {file_name}")