from customtkinter import *
from Tools.ctrl import loadImages


#  color del btnVenta #0652DD
#  color del btnCompra ##4cd137
#  color del btnClients #c56cf0
#  color del btnSuccours #fa8231


class Index(CTkFrame):
    def __init__(self, root):
        super().__init__(root)

        set_appearance_mode('light')

        self.root = root

        self.frameTop = CTkFrame(self.root, fg_color='#0652DD', corner_radius=10, )
        self.frameTop.pack(fill=BOTH, padx=10, pady=10)

        self.frameHalf = CTkScrollableFrame(self.root, corner_radius=10, fg_color='#f5f6fa')
        self.frameHalf.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.lblHome = CTkLabel(self.frameTop, text='', image=loadImages('../Media/home.png', 40))
        self.lblHome.grid(column=0, row=0, padx=20, ipady=10)

        self.lblBack = CTkLabel(self.frameTop, text='', image=loadImages('../Media/back.png', 50))
        self.lblBack.grid(column=1, row=0, padx=20, ipady=10)

        self.lblTitle = CTkLabel(self.frameTop, text='CORAZON: ...', font=('Verdana', 20, 'bold'), text_color='#f5f6fa',
                                 justify=RIGHT, )
        self.lblTitle.grid(column=2, row=0, padx=200, pady=30, ipady=10, sticky=NSEW)

        self._elementsIndex()

    def _elementsIndex(self):
        self.btnSell = CTkButton(self.frameHalf, text='Vender', font=('Verdana', 16), text_color='#f5f6fa',
                                 fg_color='#0652DD')
        self.btnSell.grid(column=0, row=0, pady=30, padx=200, ipadx=100, ipady=20)
