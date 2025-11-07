import qrcode


product_name = "Organic Groundnut Oil"
manufacturing_date = "2025-07-15"
expiry_date = "2026-01-15"
batch_id = "OIL0725B15"
origin = "Chennekothapalli, Andhra Pradesh"




product_info = f"""
Product: {product_name}
Manufacturing Date: {manufacturing_date}
Expiry Date: {expiry_date}
Batch ID: {batch_id}
Origin: {origin}
"""

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(product_info)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")
img.save("newqr.png")

print("✅ QR Code generated and saved as 'newqr.png'")
