import io
import qrcode

def create_qr(url: str):
    # generate QR code using specified brand colors
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # fill color = Navy, Back color = Cream
    img = qr.make_image(fill_color="#0F2439", back_color="#FFFEF4")

    # save to memory buffer as PNG
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer.getvalue()