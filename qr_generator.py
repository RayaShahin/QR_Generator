import argparse
import sys
import os

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
    os.makedirs("qr_codes", exist_ok=True)
    output_path = os.path.join("qr_codes", f"{file_name}.png")
    qr_image.save(output_path)

    return output_path

def main():
    # set up argument parser for command line usage
    parser = argparse.ArgumentParser(description="Generate a QR code from text or a URL.")
    parser.add_argument("-d", "--data", help="Text or URL to encode.")
    parser.add_argument("-o", "--output", help="Output file name (without .png extension).")
    parser.add_argument("--box-size", type=int, default=12, help="Pixel size of each QR box (default: 12).")
    parser.add_argument("--border", type=int, default=4, help="Border thickness in boxes (default: 4).")

    args = parser.parse_args()

    data = args.data or input("Enter URL for the QR code: ")
    file_name = args.output or input("Enter file name to save: ")

    try:
        output_path = generate_qr_code(data, file_name, box_size=args.box_size, border=args.border)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Failed to generate QR code: {e}")
        sys.exit(1)

    print(f"QR code generated and saved as {output_path}")


if __name__ == "__main__":
    main()