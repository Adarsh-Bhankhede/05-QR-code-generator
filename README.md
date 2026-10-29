# 📱 QR Code Generator

**Week 4 - Project 4**

## Description

Build a Python program to generate a **QR Code** from user-provided text or a URL.

The program asks the user to enter the data they want to convert into a QR code and specify an output filename. It generates the QR code, saves it as an image file, displays the file location, and prints an ASCII preview directly in the terminal.

## Features

- Convert a URL or text into a QR code.
- Allow the user to choose the output filename.
- Use a default filename if no filename is provided.
- Save the QR code as a PNG, JPG, or JPEG image.
- Display the absolute path of the generated file.
- Print an ASCII preview of the QR code in the terminal.
- Handle empty input and errors during generation.

## Program Flow

1. Display the welcome message.
2. Ask the user to enter a URL or text.
3. Validate the input to ensure it is not empty.
4. Ask the user to enter an output filename.
5. Use `qrcode.QRCode()` to configure the QR code.
6. Add the input data and generate the QR code.
7. Save the QR code as an image file.
8. Display a success message and the file location.
9. Print an ASCII preview in the terminal.
10. Handle any errors that occur during generation.

## Technologies Used

- Python
- `qrcode` library
- Pillow (`PIL`) library
- `os` module

## Installation

Install the required libraries using the following command:

```bash
python -m pip install qrcode[pil] pillow
```

## ▶️ How to Run

1. Save the program as `qr_code_generator.py`.
2. Open a terminal in the project folder.
3. Run the following command:

```bash
python qr_code_generator.py
```

4. Enter the URL or text and the desired output filename.
5. Find the generated QR code image at the displayed file location.

## 🧠 Concepts Used

- Functions
- User input and string methods
- Conditional statements
- Exception handling (`try-except`)
- File extensions and image saving
- `os.path.abspath()`
- Python modules and third-party libraries
- Main guard (`if __name__ == "__main__":`)

---

**Part of my 12 Weeks → 12+ Projects challenge.** 🚀