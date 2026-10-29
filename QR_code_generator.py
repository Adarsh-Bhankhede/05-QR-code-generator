
#! Project Name: QR Code generator

import qrcode  # python -m pip install qrcode[pil] pillow
import os

def generate_qr_code():

    print("\n====== QR Code Generator ======\n")
    # 1. get URL 
    data = input(
        "Enter the URL to convert into QR code: "
    ).strip()
    
    if not data:
        print("Error: data cannot be empty.")
        return
    
    # 2. get output QR code filename
    filename = input(
        "Enter the output filename(e.g., my_qrcode.png ): "
    ).strip()
    
    if not filename:
        filename = "qrcode.png"

    if not filename.lower().endswith(('.png','.jpg', '.jpeg')):
        filename += '.png'
    try:
        # 3. configure the QR code parameters
        qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 2
        )

        # 4. Add data to QR code
        qr.add_data(data)
        qr.make(fit=True)

        # 5. save the QR code in filename
        image = qr.make_image(fill_color = "black", back_color = "white")
        image.save(filename)

        # 6. Success message
        print("\nSuccess! Your QR code has been saved as: "+filename)
        print("Location of file: ",os.path.abspath(filename))

        # 7. display QR directly on terminal screen
        print("\n---Terminal scan preview of QR code---\n")
        # qr.print_tty()
        qr.print_ascii(invert=True)
        print("\n--------------------------------------\n")
        
    except Exception as e:
        print("An error occurred while generating the QR code as:",e)

if __name__ == "__main__":
    generate_qr_code()