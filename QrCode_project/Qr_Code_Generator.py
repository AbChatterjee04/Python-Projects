import qrcode


def genearate_qrcode(text):
    
    qr = qrcode.QRCode(
        version = 1, # higher version number leads bigger code image with complicated picture
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10, # size of the box where Qr Code will be displayed
        border = 4, #it is white part of the image || border in all 4 sides with white color
    )

    qr.add_data(data)
    qr.make(fit= True)
    img = qr.make_image(fill='black',back_color = 'white')
    img.save("Rickinsta.png")

data = input("Enter Your url:  ") # give any path inside the code to generate the Qr code :)
genearate_qrcode(data)