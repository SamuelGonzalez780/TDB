from customtkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk


def loadImages(filePath, size):
    imgTemp = Image.open(filePath)
    imgTemp = imgTemp.resize((size, size), Image.LANCZOS)
    phiTem = ImageTk.PhotoImage(imgTemp)
    return phiTem


'''
root=CTk()

lbl=CTkButton(root, text="",image=loadImages("../Media/show.png",20)).pack()

root.mainloop()

'''
