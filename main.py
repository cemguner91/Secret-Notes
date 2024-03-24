import tkinter
from PIL import ImageTk,Image
import cryptocode

FONT = ("Arial", 15, "normal")
title_sets = []

#window
window = tkinter.Tk()
window.minsize(width=400,height=700)
window.config(pady=20,padx=20)
window.title("Secret Notes / made by Cem")

#image
app_im = Image.open("chatting.png")
app_im_photo = ImageTk.PhotoImage(app_im.resize((60,60)))
image_label = tkinter.Label(image=app_im_photo, width=250,height=150)
image_label.pack()

#title label
title_label = tkinter.Label(text="Lütfen Başlığı Giriniz", font=FONT)
title_label.pack()

#title Entry
title_entry = tkinter.Entry()
title_entry.pack()

#secret label
secret_label = tkinter.Label(text="Sırları Giriniz", font=FONT)
secret_label.pack()

#secret_text
secret_text = tkinter.Text()
secret_text.config(width=40)
secret_text.pack()

#master_key_label
key_label = tkinter.Label(text="Şifre Giriniz")
key_label.pack()

#key entry
key_entry = tkinter.Entry()
key_entry.pack()

message_box = tkinter.Message()

def save_to_file(text,filename):
    with open(filename, "w") as file:
        file.write(text)

def save():
    if not title_entry.get() == "" or secret_text.get("1.0") == "" or key_entry == "":
        encode_text = cryptocode.encrypt(secret_text.get("1.0", tkinter.END), key_entry.get())
        save_to_file(encode_text, filename=f"{title_entry.get()}.txt")
        title_sets.append(title_entry.get())
        return encode_text
    else:
        print("Boş kaldı")

def comeback():
    encode_text = ""
    with open(f"{title_entry.get()}.txt", "r") as file:
        encode_text = file.read()
        decode_text = cryptocode.decrypt(encode_text, key_entry.get())

    if not decode_text == 0:
        secret_text.delete("1.0", tkinter.END)
        secret_text.insert("1.0", decode_text)
    else: print("Şifre Hatalı")

#Sakla buton
save_button = tkinter.Button(text="Kaydet ve Şifrele", command=save)
save_button.pack()

#çözümle buton
decrypto_button = tkinter.Button(text="Çözümle", command=comeback)
decrypto_button.pack()

window.mainloop()