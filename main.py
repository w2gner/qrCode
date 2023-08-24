import qrcode

# Generate QR code
url = "https://www.linkedin.com/in/w4gner/"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an Image object from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img_path = "./linkedin_qr.png"
img.save(img_path)

print(img_path)
