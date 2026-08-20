import qrcode

def main():
 song ="https://youtu.be/dhsy6epaJGs?si=4EZ0zUvCkxWJYMYU"
 qr= qrcode.QRCode(version=1, box_size=5, border=5)
 qr.add_data (song)
 qr.make(fit=True)

 img=qr.make_image(fill_color="pink",back_color="white")
 img.save("youtube-qr.png")

if __name__== "__main__":
    main()


