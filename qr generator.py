"""
Module - pyqrcode
install pypng using "pip install pypng"
"""

import pyqrcode

print("Welcome to QR Code Generator")

content = input("Add details you want to include your QR code : ")

qr_code = pyqrcode.create(content)

#Convert the code into PNG & save

qr_code.png("QR_CODE.png", scale=5)

print("QR code Generated Successfully !!!")