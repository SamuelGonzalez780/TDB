from customtkinter import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import shutil


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


def deleteElement(element):
    element.destroy()


def inFocus(entry):
    entry.configure(border_color='#0652DD')


def outFocus(entry):
    entry.configure(border_color='#dcdde1')


def increase(btn, color, image):
    btn.configure(width=150, height=60, fg_color=color, text_color='#f5f6fa', image=loadIcon(image, 40))


def decrease(btn, color, image):
    btn.configure(width=120, height=50, fg_color=color, text_color='#1e272e', image=loadIcon(image, 40))


def searchImage():
    tempPath = filedialog.askopenfile()
    if tempPath is None:
        messagebox.showwarning('Cancelado', message='Cancelado')
    else:
        return tempPath.name


def moveImage(path):
    shutil.move(path, '../Media')


def renameImage(path, id):
    a, b = os.path.splitext(os.path.basename(path))
    oldName = a + b
    newName = f'{id}{b}'
    os.rename(f'../Media/{oldName}', f'../Media/{newName}')


def upper(entry):
    current_text = entry.get()

    if current_text != current_text.upper():
        entry.delete(0, END)
        entry.insert(0, current_text.upper())
