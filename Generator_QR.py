from tkinter import *
from tkinter import messagebox
import pyqrcode

tk=Tk()
tk.title("QR code generator")
tk.config(bg="#1a2a40")

def generate_QR_Code():
    if len(userInput.get())!=0:
        global qr,img
        qr=pyqrcode.create(userInput.get())
        img=BitmapImage(data=qr.xbm(scale=10))
    else:
        messagebox.showwarning('warning',"text in the field are required")

    try:
        display()

    except:
        pass


def display():
    img_label.config(image=img)

label=Label(tk,text="Type text or URL",bg="#1a2a40",fg="white",padx=30,pady=2,font=("Arial",30))
label.pack()

userInput=StringVar()
entry=Entry(tk,textvariable=userInput,width=50,font=("arial",15))
entry.pack(padx=50,pady=30)

button = Button(tk, text="generate QR here",bg="aliceblue",relief="flat",width=20,command=generate_QR_Code,font=("arial",15))

button.pack(padx=10,pady=10)
img_label=Label(tk,bg="#f2f2f2")
img_label.pack()

output=Label(tk,text="",bg="#1a2a40",fg="white")
output.pack()

tk.mainloop()


