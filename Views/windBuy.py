from Tools.ctrl import *
from tpOrders import Order
from tpModProduct import ModProduct


#TODO HACER QUE EL PRODUCTO SE ACTULIZE  CUANDO SE AGREGA O ELIMINA PRODUCTO
#TODO GURADAR LA COMPRA Y QUE ACTULIZE EL TOTAL EN FUNCION DEL PRECION PROVEEDOR
#TODO AL HACER  QUE EL PEDIO ACTUALIZE LA EXISTECIA
#TODO AL DISMINUIR O AUMENTAR EN 1 , SE ACTULIZE LA EXISTENCIA Y HAGA LA COMPRA O VENTA
#TODO EL ID DEL PRODUCTO SE GENERA AL AGREGARLO , EN CASO DE YA ESTAR SE ACTULIZA POR MEDIO DEL MISMO
#TODO LA EDITAR EL PRODUCTO LA IMAGEN ES LA MISMA HASTA QUE SE REMMPLAZA
#TODO LA CADUCIDAD SE GENERA SOLA DESPUES DE LA COMPRA DADO CADA TIEMPO DE STOCK 7, 14 O 20 DIAS
#TODO SI EL ID SE ENCUENTRA SE MODIFICA, SI NO SE AGREGA


class Buy(CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.root = parent

        self.products = [['p1', 50], ['p2', 20], ['p3', 60], ['p4', 70]]
        self.reply = []
        self.img = None

        self.lblTitle = CTkLabel(self.root, text='Gestion de producto', font=('Verdana', 30, 'bold'),
                                 text_color='#1e272e').pack(side=TOP, fill=BOTH)

        self.entrySearch = (
            CTkEntry(self.root, width=400, height=50, justify=CENTER, font=('Verdana', 15), placeholder_text='🔍 Buscar',
                     text_color='#1e272e', border_color='#dcdde1'))
        self.entrySearch.pack(side=TOP, expand=1, fill=BOTH, padx=10, pady=(20, 10))

        self.entrySearch.bind("<FocusIn>", lambda event: inFocus(self.entrySearch))
        self.entrySearch.bind("<FocusOut>", lambda event: outFocus(self.entrySearch))

        self.frameNewProduct = CTkFrame(self.root, fg_color='#ffffff', corner_radius=20)
        self.frameNewProduct.pack(side=TOP, fill=X, padx=10, pady=(20, 10))

        self.frameNewProduct.grid_columnconfigure(0, weight=1)
        self.frameNewProduct.grid_columnconfigure(1, weight=1)

        self.frameProducts = CTkFrame(self.root, fg_color='#F9FAFB', corner_radius=20)
        self.frameProducts.pack(side=TOP, fill=BOTH, padx=10, pady=(20, 10))

        self.frameProducts.grid_columnconfigure(0, weight=1)
        self.frameProducts.grid_columnconfigure(1, weight=1)

        self._newProduct()
        self._loadProducts()

    def _newProduct(self):
        self.lblTitle = CTkLabel(self.frameNewProduct, text='Agregar producto', font=('Verdana', 20, 'bold'),
                                 text_color='#1e272e').grid(column=0, row=0, padx=10, columnspan=2, sticky=NSEW)
        self.lblName = CTkLabel(self.frameNewProduct, text='Nombre', font=('Verdana', 15))
        self.lblName.grid(column=0, row=1, padx=10, pady=10, sticky=W)
        self.entryName = CTkEntry(self.frameNewProduct, width=100, justify=CENTER, font=('Verdana', 15),
                                  text_color='#1e272e', border_color='#dcdde1')
        self.entryName.grid(column=0, row=2, padx=10, sticky=NSEW)

        self.lblPrice = CTkLabel(self.frameNewProduct, text='Precio', font=('Verdana', 15)).grid(column=1, row=1,
                                                                                                 padx=10, sticky=W)
        self.entryPrice = CTkEntry(self.frameNewProduct, width=100, justify=CENTER, font=('Verdana', 15),
                                   text_color='#1e272e', border_color='#dcdde1')
        self.entryPrice.grid(column=1, row=2, padx=10, sticky=NSEW)

        self.lblSupplier = CTkLabel(self.frameNewProduct, text='Proveedor', font=('Verdana', 15,))
        self.lblSupplier.grid(column=0, row=3, padx=10, sticky=W)
        self.entrySupplier = CTkEntry(self.frameNewProduct, width=100, justify=CENTER, font=('Verdana', 15),
                                      text_color='#1e272e', border_color='#dcdde1')
        self.entrySupplier.grid(column=0, row=4, padx=10, sticky=NSEW)

        self.lblPriceSupplier = CTkLabel(self.frameNewProduct, text='Precio Provedor', font=('Verdana', 15))
        self.lblPriceSupplier.grid(column=1, row=3, padx=10, pady=10, sticky=W)
        self.entryPriceSupplier = CTkEntry(self.frameNewProduct, width=100, justify=CENTER, font=('Verdana', 15),
                                           text_color='#1e272e', border_color='#dcdde1')
        self.entryPriceSupplier.grid(column=1, row=4, padx=10, sticky=NSEW)

        self.btnAddImage = CTkButton(self.frameNewProduct, text='Imagen', font=('Verdana', 15), fg_color='#0652DD',
                                     command=self._chargeImage)
        self.btnAddImage.grid(column=0, row=5, padx=10, pady=10)

        self.btnClear = CTkButton(self.frameNewProduct, text='Limpiar', font=('Verdana', 15), fg_color='#0652DD',
                                  hover_color='#eb2f06', command=self._clear).grid(column=0, row=5, padx=10,
                                                                                   columnspan=2)

        self.btnAccept = CTkButton(self.frameNewProduct, text='Aceptar', font=('Verdana', 15), fg_color='#0652DD',
                                   command=self._addProduct)
        self.btnAccept.grid(column=1, row=5, padx=10, pady=10)

        self.entries = [self.entryName, self.entryPrice, self.entrySupplier, self.entryPriceSupplier, ]

        for entry in self.entries:
            entry.bind("<FocusIn>", lambda event, e=entry: inFocus(e))
            entry.bind("<FocusOut>", lambda event, e=entry: outFocus(e))

    def _loadProducts(self):
        row = 0
        column = 0
        max_columns = 2

        for product in self.products:
            self.tempFrame = CTkFrame(self.frameProducts, width=600, height=700, fg_color='#ffffff')
            self.tempFrame.grid(row=row, column=column, sticky=NSEW, padx=10, pady=10)

            self.lblImage = CTkLabel(self.tempFrame, text='', corner_radius=100,
                                     image=loadImagesCustom('../Media/bolillo.jpg', 600, 300))
            self.lblImage.pack(side=TOP, padx=10, pady=10)

            self.lblName = CTkLabel(self.tempFrame, text='nombre', font=('Verdana', 20, 'bold'))
            self.lblName.pack(padx=20, anchor=W)

            self.lblId = CTkLabel(self.tempFrame, text='id:   fecha cad:', font=('Verdana', 15, 'italic'))
            self.lblId.pack(padx=20, anchor=W)

            self.lblPrice = CTkLabel(self.tempFrame, text='Precio:   Precio Provedor:', font=('Verdana', 13, 'italic'),
                                     text_color='#0652DD')
            self.lblPrice.pack(padx=20, anchor=W)

            self.tempFrameUnder = CTkFrame(self.tempFrame, fg_color='#ffffff')
            self.tempFrameUnder.pack(padx=10, pady=10, side=TOP, fill=BOTH)

            self.lblLessTemp = (
                CTkLabel(self.tempFrameUnder, text='', image=loadIcon('../Media/less.png', 20), anchor=E))
            self.lblLessTemp.grid(column=1, row=0, padx=(20, 5), sticky=W)

            self.lblStockTemp = (
                CTkLabel(self.tempFrameUnder, text='1', font=('Verdana', 15, 'bold'), text_color='#1e272e', anchor=E))
            self.lblStockTemp.grid(column=2, row=0, sticky=NSEW)

            self.lblPlusTemp = (
                CTkLabel(self.tempFrameUnder, text='', image=loadIcon('../Media/plus.png', 15), anchor=W))
            self.lblPlusTemp.grid(column=3, row=0, padx=5, sticky=E)

            self.btnBuy = CTkButton(self.tempFrameUnder, width=20, text='', fg_color='#F9FAFB', hover_color='#F9FAFB',
                                    image=loadIcon('../Media/shpCartBlack.png', 20),
                                    command=lambda: self._loadOrder('add name', 12))
            self.btnBuy.grid(column=4, row=0, padx=(30, 5), sticky=E)

            self.btnEdit = CTkButton(self.tempFrameUnder, width=20, text='', fg_color='#F9FAFB', hover_color='#F9FAFB',
                                     image=loadIcon('../Media/pen.png', 20),
                                     command=lambda: self._editProduct('id'))
            self.btnEdit.grid(column=5, row=0, sticky=W)

            column += 1
            if column >= max_columns:
                column = 0
                row += 1

    def _chargeImage(self):
        self.img = searchImage()


    def _addProduct(self):
        self.reply.clear()
        for entry in self.entries:
            if entry.get() == '':
                entry.configure(border_color='#eb2f06')
                messagebox.showwarning('Advertencia', 'Llenar todos los campos')
                self.reply.clear()
                break
            else:
                self.reply.append(entry.get())

        if self.img is None:
            messagebox.showwarning('Advertencia', 'No hay imagen')
            self.reply.clear()

        if len(self.reply) == 0:
            pass
        else:
            print(self.reply)
            moveImage(self.img)
            renameImage(self.img, 'add id')
            self._reloadProducts()

    def _reloadProducts(self):
        deleteContent(self.frameProducts)
        self._loadProducts()

    def _clear(self):
        for entry in self.entries:
            entry.delete(0, 'end')
        self.img = None

    def _editProduct(self, id):
        self.new = ModProduct(self, id)

    def _loadOrder(self, name, price):
        self.order = Order(self, name, price)
        self.wait_window(self.order)

        if (self.order.amount or self.order.charge) is None:
            pass
        else:
            print(self.order.amount)
            print(self.order.charge)

