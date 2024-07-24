import  qrcode


qr_img = qrcode.make("")

qr_img.save("qr-img.jpg")