from Tools.ctrl import  loadImages
from customtkinter import  *

root= CTk()

lbl=CTkButton(root, text="",image=loadImages("../Media/show.png",20)).pack()

root.mainloop()