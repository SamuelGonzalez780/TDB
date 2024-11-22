
from Tools.ctrl import *
from windSell import Sell


class Index(CTkFrame):
    def __init__(self, root):
        super().__init__(root)

        set_appearance_mode('light')

        self.root = root

        self.frameTop = CTkFrame(self.root, fg_color='#0652DD', corner_radius=10, )
        self.frameTop.pack(fill=BOTH, padx=10, pady=10)

        self.frameHalf = CTkScrollableFrame(self.root, corner_radius=10, fg_color='#F9FAFB')
        self.frameHalf.pack(fill=BOTH, expand=True, padx=10, pady=10, )

        self.btnHome = CTkButton(self.frameTop, text='', fg_color='transparent',
                                 image=loadIcon('../Media/home.png', 40), command=self._home)
        self.btnHome.grid(column=0, row=0, padx=(20, 10), ipady=10)

        self.btnBack = CTkButton(self.frameTop, text='', fg_color='transparent',
                                 image=loadIcon('../Media/back.png', 50))
        self.btnBack.grid(column=1, row=0, padx=10, ipady=10)

        self.lblTitle = CTkLabel(self.frameTop, text='nombre sucursal: ...', font=('Verdana', 20, 'bold'), text_color='#f5f6fa',
                                 justify=RIGHT, )
        self.lblTitle.grid(column=2, row=0, padx=200, pady=30, ipady=10, sticky=NSEW)

        # create elements in the half frame
        self._elementsIndex()

    #Todo hacer que que regrese al frame anterior, en caso de estar en el index regresar al login

    def _back(self):
        pass

    def _home(self):
        deleteContent(self.frameHalf)
        self._elementsIndex()

    #Todo Cargar cada frame
    def _loadWind(self, window):
        deleteContent(self.frameHalf)

        if window == 1:
            Sell(self.frameHalf)
        elif window == 2:
            pass
        elif window == 3:
            pass
        elif window == 4:
            pass

        #TODO cambiar los frames de abajo con información respectiva de cada boton

    def _frames(self, window):
        if window == 1:
            pass
        elif window == 2:
            pass
        elif window == 3:
            pass
        elif window == 4:
            pass
        pass

    def _elementsIndex(self):

        self.btnSell = CTkButton(self.frameHalf, text='Vender', font=('Verdana', 16), text_color='#1e272e',
                                 fg_color='#ffffff', border_color='#dcdde1', corner_radius=10,
                                 image=loadIcon('../Media/dollarBlack.png', 40), command=lambda: self._frames(1))
        self.btnSell.grid(column=0, row=0, padx=(300, 20), pady=30, ipadx=100, ipady=30)

        self.btnPurchases = CTkButton(self.frameHalf, text='Comprar', font=('Verdana', 16), text_color='#1e272e',
                                      fg_color='#ffffff', border_color='#dcdde1', corner_radius=10,
                                      image=loadIcon('../Media/shpCartBlack.png', 40),
                                      command=lambda: self._frames(2))
        self.btnPurchases.grid(column=1, row=0, ipadx=100, ipady=30)

        self.btnCustomers = CTkButton(self.frameHalf, text='Clientes', font=('Verdana', 16), text_color='#1e272e',
                                      fg_color='#ffffff', border_color='#dcdde1', corner_radius=10,
                                      image=loadIcon('../Media/customersBlack.png', 40),
                                      command=lambda: self._frames(3))
        self.btnCustomers.grid(column=0, row=1, padx=(300, 20), pady=10, ipadx=100, ipady=30)

        self.btnBranch = CTkButton(self.frameHalf, text='Sucursal', font=('Verdana', 16), text_color='#1e272e',
                                   fg_color='#ffffff', border_color='#dcdde1', corner_radius=10,
                                   image=loadIcon('../Media/branchBlack.png', 40), command=lambda: self._frames(4))
        self.btnBranch.grid(column=1, row=1, ipadx=100, ipady=30)

        buttons = [(self.btnSell, '#0652DD', '../Media/dollarWhite.png', '../Media/dollarBlack.png', 1),
                   (self.btnPurchases, '#4cd137', '../Media/shpCartWhite.png', '../Media/shpCartBlack.png', 2),
                   (self.btnCustomers, '#c56cf0', '../Media/customersWhite.png', '../Media/customersBlack.png', 3),
                   (self.btnBranch, '#fa8231', '../Media/branchWhite.png', '../Media/branchBlack.png', 4)]

        # Events
        for button, hover_color, hover_icon, leave_icon, case in buttons:
            button.bind("<Enter>", lambda event, b=button, c=hover_color, i=hover_icon: increase(b, c, i))
            button.bind("<Leave>", lambda event, b=button, i=leave_icon: decrease(b, 'transparent', i))
            button.bind("<Double-Button-1>", lambda event, d=case: self._loadWind(d))
