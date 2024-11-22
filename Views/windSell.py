from customtkinter import *
from Tools.ctrl import *


#TODO que la base de datos recupere de la mayor existencia de producto al menor
#TODO que al buscar por nombre salgan los resultados; que al buscar por id salgan los resultados
#TODO HACER QUE ENCUENTRE LA INFORMACION DE CADA PRODUCTO COMO UN METODO, LAS IMAGENES LLEVAN POR NOMBRE EL ID DEL PROUCTO
#TODO HACER QUE SUME  LOS PRECIOS Y  HACER TICKET DE VENTA , GUARDAR LA VENTA EN LA DB  AL TOCAR EL BOTON PAGAR
#TODO HACER QUE LAS ETIQUETAS LESS Y PLUS AUNMENTEN LA CANTIDAD DEL PRODUCTO
#TODO HACER QUE AL ELMINAR UN PRODUCTO EL FRAME SE AJUSTE AL TAMAÑO ANTERIOR
class Sell(CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.root = parent

        self.products = [['p1', 50], ['p2', 20], ['p3', 60], ['p4', 70]]
        self.price = StringVar()

        self.price.set('0.0')

        self.entryLookFor = (
            CTkEntry(self.root, width=400, height=50, justify=CENTER, font=('Verdana', 15), placeholder_text='🔍 Buscar',
                     text_color='#1e272e', border_color='#dcdde1'))
        self.entryLookFor.pack(side=TOP, expand=1, fill=BOTH, padx=10, pady=(20, 10))

        self.frameProducts = CTkFrame(self.root, width=900, height=self.root.winfo_height(), fg_color='#dcdde1',
                                      corner_radius=20)
        self.frameProducts.pack(fill=BOTH, side=LEFT, padx=10, pady=10, anchor=CENTER)

        self.frameCart = CTkFrame(self.root, height=self.root.winfo_height(), fg_color='#ffffff', corner_radius=20)
        self.frameCart.pack(fill=BOTH, side=RIGHT, expand=True, padx=10, pady=10, anchor=CENTER)

        self._loadProducts()
        self._loadCart()

    def _loadCart(self):
        self.frameTitleCart = CTkFrame(self.frameCart, fg_color='#ffffff', corner_radius=20, )
        self.frameTitleCart.pack(fill=X)

        self.lblCart = CTkLabel(self.frameTitleCart, text='Carrito', font=('Verdana', 20, 'bold'), )
        self.lblCart.pack(side=LEFT, fill=BOTH, expand=True, padx=(20, 5), pady=10, anchor=W)

        self.lblTrash = CTkButton(self.frameTitleCart, text='', fg_color='#ffffff', hover_color='#ffffff',
                                  image=loadIcon('../Media/trash.png', 30), command=self._clearCart)
        self.lblTrash.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, anchor=CENTER)

        self.frameCartMiddle = CTkFrame(self.frameCart, height=100, fg_color='#ffffff', corner_radius=10, )
        self.frameCartMiddle.pack(fill=X)

        self.frameCartUnder = CTkFrame(self.frameCart, fg_color='#ffffff', corner_radius=10, )
        self.frameCartUnder.pack(fill=X)

        self.lblTotal = CTkLabel(self.frameCartUnder, text='Total', font=('Verdana', 15, 'bold'), fg_color='#ffffff')
        self.lblTotal.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10, anchor=W)

        self.lblTotal = CTkLabel(self.frameCartUnder, text=f'$ {self.price.get()}', font=('Verdana', 20, 'bold'),
                                 fg_color='#ffffff')
        self.lblTotal.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10, anchor=E)

        self.btnPay = CTkButton(self.frameCart, text='Pagar', font=('Verdana', 15, 'bold'), text_color='#F9FAFB',
                                fg_color='#4cd137', image=loadIcon('../Media/shpCartWhite.png', 30), command=self._pay)
        self.btnPay.pack(side=TOP, fill=X, padx=10, pady=10)

    def _loadProducts(self):
        row = 0
        column = 0
        max_columns = 3

        for product in self.products:

            self.tempFrame = CTkFrame(self.frameProducts, width=400, height=700, fg_color='#F9FAFB')
            self.tempFrame.grid(row=row, column=column, sticky=NSEW, padx=10, pady=10)

            self.lblImage = CTkLabel(self.tempFrame, text='', image=loadImagesCustom('../Media/bolillo.jpg', 300, 200))
            self.lblImage.pack(side=TOP, padx=10, pady=10)

            self.lblName = CTkLabel(self.tempFrame, text='nombre', font=('Verdana', 15, 'bold'))
            self.lblName.pack(padx=10, anchor=W)

            self.lblId = CTkLabel(self.tempFrame, text='id', font=('Verdana', 15, 'italic'))
            self.lblId.pack(padx=10, anchor=W)

            self.lblPrice = CTkLabel(self.tempFrame, text='Precio:   Existencia:', font=('Verdana', 13, 'bold'),
                                     text_color='#0652DD')
            self.lblPrice.pack(padx=10, anchor=W)

            self.btnAdd = CTkButton(self.tempFrame, text='Agregar', font=('Verdana', 15), fg_color='#0652DD',
                                    command=lambda: self._addProduct('agregar nombre', 'agregar precio', '423432'))
            self.btnAdd.pack(padx=10, pady=10, anchor=CENTER)

            column += 1
            if column >= max_columns:
                column = 0
                row += 1

    def _addProduct(self, name, price, amount):
        self.tempFrame = CTkFrame(self.frameCartMiddle, height=100, fg_color='#F9FAFB')
        self.tempFrame.pack(fill=X)

        self.lblNameTemp = (
            CTkLabel(self.tempFrame, text=name, font=('Verdana', 15, 'bold'), text_color='#1e272e', anchor=W)).grid(
            column=0, row=0, padx=15, pady=10)

        self.lblPriceTemp = (
            CTkLabel(self.tempFrame, text=price, font=('Verdana', 14, 'italic'), text_color='#718093', anchor=W)).grid(
            column=0, row=1, padx=10, pady=10)

        self.lblLessTemp = (CTkLabel(self.tempFrame, text='', image=loadIcon('../Media/less.png', 20), anchor=E))
        self.lblLessTemp.grid(column=1, row=0, rowspan=2, sticky=W)

        self.lblAmountTemp = (
            CTkLabel(self.tempFrame, text=amount, font=('Verdana', 15, 'bold'), text_color='#1e272e', anchor=E))
        self.lblAmountTemp.grid(column=2, row=0, rowspan=2, sticky=NSEW, padx=10)

        self.lblPlusTemp = (CTkLabel(self.tempFrame, text='', image=loadIcon('../Media/plus.png', 18), anchor=W))
        self.lblPlusTemp.grid(column=3, row=0, rowspan=2, sticky=E)

    def _clearCart(self):
        deleteContent(self.frameCartMiddle)
        self.frameCartMiddle.configure(height=100)

    def _pay(self):
        print('AGREGAR FUNCION')
