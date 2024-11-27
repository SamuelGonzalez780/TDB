from Tools.ctrl import *


#TODO LOS DATOS LOS CAPTURA POR MEDIO DEL ID
#TODO ACTULIZAR LOS PRODUCTOS NO LOS REGISTROS 

class ModProduct(CTkToplevel):
    def __init__(self, parent, id):
        super().__init__(parent)
        self.title('id')
        self.configure(fg_color='#F9FAFB', padx=10, pady=5)
        self.geometry(f'600x300+{((self.winfo_screenwidth()) // 2)}+{((self.winfo_screenheight()) - 900 // 2)}')
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.data = ['addName', 'addPrice', 'addProv', 'addPriceProv']

        self.id = id
        self.img = f'{self.id}.jpg'

        self._Product()

    def _Product(self):
        self.lblTitle = CTkLabel(self, text='Eliminar producto', font=('Verdana', 20, 'bold'),
                                 text_color='#1e272e').grid(column=0, row=0, padx=10, columnspan=2, sticky=NSEW)
        self.lblName = CTkLabel(self, text='Nombre', font=('Verdana', 15))
        self.lblName.grid(column=0, row=1, padx=10, pady=10, sticky=W)
        self.entryName = CTkEntry(self, width=100, justify=CENTER, font=('Verdana', 15), text_color='#1e272e',
                                  border_color='#dcdde1')
        self.entryName.grid(column=0, row=2, padx=10, sticky=NSEW)

        self.lblPrice = CTkLabel(self, text='Precio', font=('Verdana', 15)).grid(column=1, row=1, padx=10, sticky=W)
        self.entryPrice = CTkEntry(self, width=100, justify=CENTER, font=('Verdana', 15), text_color='#1e272e',
                                   border_color='#dcdde1')
        self.entryPrice.grid(column=1, row=2, padx=10, sticky=NSEW)

        self.lblSupplier = CTkLabel(self, text='Proveedor', font=('Verdana', 15,))
        self.lblSupplier.grid(column=0, row=3, padx=10, sticky=W)
        self.entrySupplier = CTkEntry(self, width=100, justify=CENTER, font=('Verdana', 15), text_color='#1e272e',
                                      border_color='#dcdde1')
        self.entrySupplier.grid(column=0, row=4, padx=10, sticky=NSEW)

        self.lblPriceSupplier = CTkLabel(self, text='Precio Provedor', font=('Verdana', 15))
        self.lblPriceSupplier.grid(column=1, row=3, padx=10, pady=10, sticky=W)
        self.entryPriceSupplier = CTkEntry(self, width=100, justify=CENTER, font=('Verdana', 15), text_color='#1e272e',
                                           border_color='#dcdde1')
        self.entryPriceSupplier.grid(column=1, row=4, padx=10, sticky=NSEW)

        self.btnAddImage = CTkButton(self, text='Imagen', font=('Verdana', 15), fg_color='#0652DD',
                                     command=self._chargeImage)
        self.btnAddImage.grid(column=0, row=5, padx=10, pady=10)

        self.btnClear = CTkButton(self, text='Cancelar', font=('Verdana', 15), fg_color='#0652DD',
                                  hover_color='#eb2f06', command=self._cancel).grid(column=0, row=5, padx=10,
                                                                                    columnspan=2)

        self.btnAccept = CTkButton(self, text='Aceptar', font=('Verdana', 15), fg_color='#0652DD', command=self._update)
        self.btnAccept.grid(column=1, row=5, padx=10, pady=10)

        self.entries = [self.entryName, self.entryPrice, self.entrySupplier, self.entryPriceSupplier, ]

        for entry in self.entries:
            entry.insert(0, self.data[0])
            entry.bind("<FocusIn>", lambda event, e=entry: inFocus(e))
            entry.bind("<FocusOut>", lambda event, e=entry: outFocus(e))

    def _update(self):
        self.data.clear()
        for entry in self.entries:
            if entry.get() == '':
                entry.configure(border_color='#eb2f06')
                messagebox.showwarning('Advertencia', 'Llenar todos los campos')
                self.data.clear()
                break
            else:
                self.data.append(entry.get())

        if self.img is None:
            self.img = f'{self.id}.jpg'

        if not self.img == f'{self.id}.jpg':
            moveImage(self.img)
            renameImage(self.img, 'add id')

        if len(self.data) == 0:
            pass
        else:
            print(self.data, self.img)
            self.withdraw()

    def _chargeImage(self):
        self.img = searchImage()

    def _cancel(self):
        messagebox.showinfo('Canmcelado', 'Cancelado con exito')
        self.withdraw()
