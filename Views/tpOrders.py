from Tools.ctrl import *


class Order(CTkToplevel):
    def __init__(self, parent, name, price):
        super().__init__(parent)
        self.title(name)
        self.geometry(f'300x150+{((self.winfo_screenwidth()) // 2)}+{((self.winfo_screenheight()) // 2)}')
        self.resizable(False, False)
        self.configure(fg_color='#F9FAFB')

        self.total = StringVar()
        self.price = price

        #Make the dialog modal
        self.grab_set()

        self.lblTotal = CTkLabel(self, text=f'$ {self.total.get()}', font=('Verdana', 16, 'bold'))
        self.lblTotal.pack(pady=(20, 5))

        self.entryOrder = CTkEntry(self, justify=CENTER, font=('Verdana', 15,), corner_radius=20, placeholder_text='Escriba la cantidad')
        self.entryOrder.pack(fill=X, padx=20, pady=10)

        self.entryOrder.bind("<FocusIn>", lambda event: inFocus(self.entryOrder))
        self.entryOrder.bind("<Return>", lambda event: self._onOk())
        self.entryOrder.bind("<KeyRelease>", lambda event: self._total())

        self.buttonFrame = CTkFrame(self)
        self.buttonFrame.pack(pady=10)

        self.btnCancel = CTkButton(self.buttonFrame, text="Cancelar", fg_color='#0652DD', hover_color='#eb2f06',
                                   command=self._onCancel)
        self.btnCancel.pack(side=LEFT, padx=5)

        self.btnBuy = CTkButton(self.buttonFrame, text="Comprar", fg_color='#0652DD', hover_color='#4cd137',
                                state=DISABLED, command=self._onOk)
        self.btnBuy.pack(side=RIGHT, padx=5)


        self.amount = None
        self.charge = None

    def _onOk(self):
        if self.entryOrder.get() is None or self.entryOrder.get() == '' or self.entryOrder.get() == '0':
            messagebox.showerror("Error", "Por favor, ingresa un número válido.", icon='error')
            self.entryOrder.configure(border_color='#eb2f06')
        else:
            self.amount = int(self.entryOrder.get())
            self.charge = float(self.total.get())
            self.destroy()

    def _onCancel(self):
        messagebox.showinfo(title='Cancelado', message='Cancelado correctamente')
        self.destroy()

    def _total(self):
        try:
            value = int(self.entryOrder.get())
            new_total = value * self.price
            self.total.set(f"{new_total:.2f}")
            self.lblTotal.configure(text=f'$ {self.total.get()}')
            self.btnBuy.configure(state=NORMAL)
            self.entryOrder.configure(border_color='#0652DD')
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")
            self.btnBuy.configure(state=DISABLED)
            self.lblTotal.configure(text='$ 0.0')
            self.entryOrder.delete(0, 'end')
            self.entryOrder.configure(border_color='#eb2f06')
            return
