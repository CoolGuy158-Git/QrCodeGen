####################################################################################
# QR Code Generator - A Python project that generates QRCODES for you              #
# Under MIT license                                                                #
# Copyright (c) 2025 CoolGuy158-Git <https://coolguy158-git.github.io/My_Web_Page/>#
####################################################################################
import qrcode
import customtkinter as ctk
from PIL import Image

root = ctk.CTk()
root.geometry("600x600")
root.title("QRCodeGen")
root.resizable(False, False)
root.attributes("-alpha", 0.9)
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
label = ctk.CTkLabel(root, text="Type your url here:")
label.pack()
textbox = ctk.CTkTextbox(root, width=500, height=1, font=ctk.CTkFont(size=14, family="Courier"),)
textbox.pack(pady=10)
label = ctk.CTkLabel(root, text="Type what you want your file name to be:")
label.pack(pady=10)
textbox2 = ctk.CTkTextbox(root, width=500, height=1, font=ctk.CTkFont(size=14, family="Courier"),)
textbox2.pack(pady=15)
# Create the QrCode
def gencode():
    filename = textbox2.get("1.0", "end").strip()
    url = textbox.get("1.0", "end").strip()
    if not url:
        print("Please enter a url")
        return
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    qr_img = Image.open(filename)
    photo = ctk.CTkImage(light_image=qr_img, size=(200, 200))

    txtlabel = ctk.CTkLabel(root, text="Your QR Code:")
    txtlabel.pack(pady=15)
    imglabel = ctk.CTkLabel(root, image=photo, text="")
    imglabel.pack(pady=10)

btn = ctk.CTkButton(root, text="Generate QR Code", command=gencode)
btn.pack(pady=20)


root.mainloop()