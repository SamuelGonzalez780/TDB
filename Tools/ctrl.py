from customtkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk


def loadIcon(filePath, size):
    imgTemp = Image.open(filePath)
    imgTemp = imgTemp.resize((size, size), Image.LANCZOS)
    phiTem = ImageTk.PhotoImage(imgTemp)
    return phiTem


def loadImagesCustom(filePath, width, height):
    imgTemp = Image.open(filePath)
    imgTemp = imgTemp.resize((width, height), Image.LANCZOS)
    phiTem = ImageTk.PhotoImage(imgTemp)
    return phiTem


def deleteContent(frame):
    for widget in frame.winfo_children():
        widget.destroy()



def deleteElement(self):
    self.destroy()


def increase(btn, color, image):
    btn.configure(width=150, height=60, fg_color=color, text_color='#f5f6fa', image=loadIcon(image, 40))


def decrease(btn, color, image):
    btn.configure(width=120, height=50, fg_color=color, text_color='#1e272e', image=loadIcon(image, 40))
