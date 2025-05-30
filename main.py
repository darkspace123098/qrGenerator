from tkinter import *
import qrcode


root = Tk()
root.title("Qr code Generator")
root.geometry("1000x550")
root.config(bg="green")
root.resizable(False,False)

#icon image
# image_icon=PhotoImage(file="icon.png")
# root.iconphoto

def generate():
    name = title.get()
    text =entry.get()
    qr = qrcode.make(text)
    qr.save("Qrcode/"+str(name)+".png")
    
    global Image
    Image=PhotoImage(file="Qrcode/"+str(name)+".png")
    Image_view.config(image=Image)
    
Image_view=Label(root,bg="#AE2321")
Image_view.pack(padx=50,pady=10,side=RIGHT)



Label(root,text="Title",fg="white",bg="#AE2321",font=15).place(x=50,y=170)
Label(root,text="Description",fg="white",bg="#AE2321",font=10).place(x=50,y=230)

title = Entry(root,width=13,font="arial 15")
title.place(x=50,y=200)

entry = Entry(root,width=28,font="arial 15")
entry.place(x=50,y=260)

Button(root,text="Generate",width=20,height=2,bg="black",fg="white",command=generate).place(x=50,y=300)

root.mainloop()
