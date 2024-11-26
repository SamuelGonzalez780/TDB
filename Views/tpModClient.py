from Tools.ctrl import *
from tkcalendar import Calendar


#TODO LLENAR CON LA INFORMATION PREVIA
#TODO HACER QUE EL CALENDAR SELECCIONE LA FECHA DADA

class ModClient(CTkToplevel):
    def __init__(self, parent, list):
        super().__init__(parent)
        self.dateVar = StringVar()

        self.title('Modificar Cliente')
        self.configure(fg_color='#F9FAFB', padx=10, pady=5)
        self.geometry(f'500x450+{((self.winfo_screenwidth()) // 2)}+{((self.winfo_screenheight()) // 2)}')
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grab_set()

        self.entries = []
        self.answer = []

        self.tags = ['Nombre(s)', 'Apellido Paterno', 'Apellido Materno', 'Numero de telefono', 'Fecha de nacimiento',
                     'sexo']

        self.lblTitle = CTkLabel(self, text='Modificar Cliente', font=('Verdana', 15, 'bold'), justify=CENTER).grid(
            column=0, row=0, padx=20, columnspan=2)

        self.lblCellular = CTkLabel(self, text='Numero de telefono', font=('Verdana', 15, 'bold'), justify=LEFT).grid(
            column=0, row=1, padx=20, sticky=W)
        self.entryCellular = CTkEntry(self, justify=CENTER, font=('Verdana', 15,), corner_radius=20,
                                      border_color='#dcdde1')
        self.entryCellular.grid(column=0, row=2, padx=20, pady=10, sticky=NSEW)

        self.lblName = CTkLabel(self, text='Nombre', font=('Verdana', 15, 'bold'), justify=LEFT).grid(column=1, row=1,
                                                                                                      padx=20, sticky=W)
        self.entryName = CTkEntry(self, justify=CENTER, font=('Verdana', 15,), corner_radius=20, border_color='#dcdde1')
        self.entryName.grid(column=1, row=2, padx=20, pady=10, sticky=NSEW)

        self.lblLastNameF = CTkLabel(self, text='Apellido paterno', font=('Verdana', 15, 'bold'), justify=LEFT).grid(
            column=0, row=3, padx=20, sticky=W)
        self.entryLastNameF = CTkEntry(self, justify=CENTER, font=('Verdana', 15,), corner_radius=20,
                                       border_color='#dcdde1')
        self.entryLastNameF.grid(column=0, row=4, padx=20, pady=10, sticky=NSEW)

        self.lblLastNameM = CTkLabel(self, text='Apellido materno', font=('Verdana', 15, 'bold'), justify=LEFT).grid(
            column=1, row=3, padx=20, sticky=W)
        self.entryLastNameM = CTkEntry(self, justify=CENTER, font=('Verdana', 15,), corner_radius=20,
                                       border_color='#dcdde1')
        self.entryLastNameM.grid(column=1, row=4, padx=20, pady=10, sticky=NSEW)

        self.lblBirthdate = CTkLabel(self, text='Fecha de nacimiento', font=('Verdana', 15, 'bold'), justify=LEFT).grid(
            column=0, row=5, padx=20, sticky=W)
        self.calendarBirthdate = Calendar(self, selectmode='day', date_pattern='dd-mm-yyyy')
        self.calendarBirthdate.grid(column=0, row=6, padx=20, pady=10)

        self.lblSex = CTkLabel(self, text='Sexo', font=('Verdana', 15, 'bold'), justify=LEFT).grid(column=1, row=5,
                                                                                                   padx=20, sticky=W)
        self.cmbxSex = CTkComboBox(self, values=['Masculino', 'Femenino'], font=('Verdana', 15, 'italic'),
                                   bg_color='#dcdde1')
        self.cmbxSex.grid(column=1, row=6, padx=20, pady=10)

        self.btnCancel = CTkButton(self, text="Cancelar", fg_color='#0652DD', font=('Verdana', 15),
                                   hover_color='#eb2f06', text_color='#dcdde1', command=self._onCancel)
        self.btnCancel.grid(column=0, row=7, padx=20, pady=10, columnspan=2, sticky=W)

        self.btnSave = CTkButton(self, text='Guardar', font=('Verdana', 15), fg_color='#0652DD', text_color='#dcdde1',
                                 command=self._save)
        self.btnSave.grid(column=0, row=7, padx=20, pady=10, columnspan=2, sticky=E)

        self.entries = [self.entryCellular, self.entryName, self.entryLastNameF, self.entryLastNameM]

        for entry in self.entries:
            entry.insert(0, list[0])
            entry.bind("<FocusIn>", lambda event, e=entry: inFocus(e))
            entry.bind("<FocusOut>", lambda event, e=entry: outFocus(e))

    def _onCancel(self):
        messagebox.showinfo(title='Cancelado', message='Cancelado correctamente')
        self.destroy()

    def _save(self):
        self.answer.clear()
        for entry in self.entries:
            if entry.get() != '':
                self.answer.append(entry.get())
            else:
                messagebox.showwarning('Error', 'Llenar todos los campos')
                self.answer = []
                entry.configure(border_color='#eb2f06')
                break

        self.answer.append(self.calendarBirthdate.get_date())
        self.answer.append(self.cmbxSex.get())
        if len(self.answer) > 2:
            self.destroy()
