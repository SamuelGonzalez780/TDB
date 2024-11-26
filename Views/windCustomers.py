from Tools.ctrl import *
from customtkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from tpModClient import ModClient
from tpNewClient import NewClient


#TODO HACER QUE AL BUSCAR  SEA POR NUMERO, NOMBRE , APELLIDOS,
#TODO AL HACER ENTER SE HABRA LA VENTANA DE MODIFICAR AL HACER ENTER O   DOBLE CLICK
#TODO ACTULIZAR EL TREEV AL AGREGAR O ELMINAR CLIENTE


class Customers(CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.registros = [['1234567890', 'Juan Pérez', 28, '2023-01-15', 'Masculino'],
                          ['0987654321', 'María López', 34, '2022-11-22', 'Femenino'],
                          ['1122334455', 'Carlos García', 45, '2023-03-10', 'Masculino'],
                          ['2233445566', 'Ana Martínez', 29, '2023-02-05', 'Femenino'],
                          ['3344556677', 'Luis Rodríguez', 38, '2022-12-18', 'Masculino'],
                          ['4455667788', 'Elena Sánchez', 31, '2023-04-01', 'Femenino'],
                          ['5566778899', 'Pedro Gómez', 22, '2023-05-20', 'Masculino']]

        self.root = parent

        self.frameTitle = CTkFrame(self.root, fg_color='#F9FAFB')
        self.frameTitle.pack(fill=X, expand=True, padx=20, pady=10)

        self.lblTitle = CTkLabel(self.frameTitle, text='Gestion de clientes', font=('Verdana', 30, 'bold'),
                                 fg_color='#F9FAFB', anchor=W).pack(side=LEFT)
        self.btnAddClient = CTkButton(self.frameTitle, text='Nuevo cliente', font=('Verdana', 15, 'bold'),
                                      image=loadIcon('../Media/addClient.png', 30), text_color='#F9FAFB',
                                      fg_color='#0652DD', command=self._newClient)
        self.btnAddClient.pack(padx=20, side=RIGHT, expand=True, anchor=E)

        self.entrySearch = (
            CTkEntry(self.root, width=400, height=50, justify=CENTER, font=('Verdana', 15), placeholder_text='🔍 Buscar',
                     text_color='#1e272e', border_color='#dcdde1'))
        self.entrySearch.pack(side=TOP, expand=1, fill=BOTH, padx=20, pady=(20, 10))

        self.entrySearch.bind("<FocusIn>", lambda event: inFocus(self.entrySearch))
        self.entrySearch.bind("<FocusOut>", lambda event: outFocus(self.entrySearch))

        self._loadCustomers()

    def _loadCustomers(self):

        style = ttk.Style()
        style.theme_use('clam')

        style.configure("Custom.Treeview", background="#ffffff", foreground="black", rowheight=25)
        style.configure("Custom.Treeview.Heading", background="#dcdde1", foreground="#000000",
                        font=('Verdana', 18, 'bold'))
        style.map("Custom.Treeview", background=[('selected', '#0652DD')])

        self.treevCustomers = Treeview(self.root, style="Custom.Treeview", show='headings',
                                       columns=('phone', 'fullName', "age", "enryDate", "sex"))

        self.treevCustomers.pack(fill=BOTH, expand=1, padx=20, pady=(20, 10))

        self.treevCustomers.bind('<Return>', self._update)

        headings = [("phone", "Telefono"), ("fullName", "Nombre"), ("age", "Edad"), ("enryDate", "Ingreso"),
                    ("sex", "Sexo")]

        for heading in headings:
            self.treevCustomers.heading(heading[0], text=[heading[1]])

        for data in self.registros:
            self.treevCustomers.insert("", END, values=data)

        for column in headings:
            self.treevCustomers.column(column[0], width=100, anchor=CENTER)

    def _newClient(self):
        self.newClient = NewClient(self)
        self.wait_window(self.newClient)
        print(self.newClient.answer)

    def _update(self, event):
        if self.treevCustomers.selection():
            item = self.treevCustomers.selection()[0]
            itemValues = self.treevCustomers.item(item, 'values')
            self.newClient = ModClient(self, itemValues)
            self.wait_window(self.newClient)

            if len(self.newClient.answer) == 2:
                pass
            else:
                print(self.newClient.answer)

    def _rechargeTreev(self):
        pass
