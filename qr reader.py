"""
Modules - pyzbar, Pillow(PIL)
"""

from pyzbar.pyzbar import decode
from PIL import Image

print("Welcome to QR Code Reader")

#Opening the image
image = Image.open("QR_CODE.png")

#Decoding the image
dec = decode(image)

print(dec[0].data.decode())






