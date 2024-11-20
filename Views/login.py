from customtkinter import *
from tkinter import messagebox
from Tools.ctrl import loadImages
from index import Index


#TODO QUE EL USUARIO CON PUESTO B NO DEJE ENTRAR AL SISTEMA
#TODO QUE LA CONTRASEÑA O EL USUARIO ESTEN INCORRECTOS MARCAR ERRROR

class Login(CTk):
    def __init__(self):
        super().__init__()

        self.title('Login')
        self.configure(fg_color='#f5f6fa')
        self.geometry(f'455x325+{((self.winfo_screenwidth() - 400) // 2)}+{((self.winfo_screenheight() - 600) // 2)}')

        self.resizable(False, False)

        self.columnconfigure(0, weight=1)

        self.contLogin = CTkFrame(self, fg_color='#f5f6fa')
        self.contLogin.grid(row=0, column=0, sticky=NSEW, pady=10)

        self.stateUnShow = True

        self._elementsLogin()  # * Create all elements

    def _show(self, event):
        if self.stateUnShow:
            self.entryPwd.configure(show='')
            self.lblShow.configure(image=loadImages('../Media/unShow.png', 20))
            self.stateUnShow = False
        else:
            self.entryPwd.configure(show='•')
            self.lblShow.configure(image=loadImages("../Media/show.png", 20))
            self.stateUnShow = True

    def _enter(self, event):
        self._logIn()

    def _close(self):
        self.destroy()

    def _inFocus(self, entry):
        entry.configure(border_color='#0652DD')

    def _outFocus(self, entry):
        entry.configure(border_color='#dcdde1')

    def _logIn(self):
        if (len(self.entryUser.get()) or len(self.entryPwd.get())) == 0:
            self.entryUser.configure(border_color='#eb2f06')
            self.entryPwd.configure(border_color='#eb2f06')
            messagebox.showerror('Error', 'Por favor llenar todos los campos')
        else:
            self.withdraw()
            self.windIndex = CTkToplevel()
            self.windIndex.protocol('WM_DELETE_WINDOW', self._close)
            self.windIndex.title('Corazón de canela ')
            self.windIndex.geometry(f'{self.winfo_screenwidth()}x{self.winfo_screenheight()}')
            self.frameIndex = CTkFrame(self.windIndex)
            self.frameIndex.pack(fill=BOTH, expand=True)
            Index(self.frameIndex)

    def _elementsLogin(self):

        self.lblWelcome = CTkLabel(self.contLogin, text='Bienvenido!', font=('Verdana', 30, 'bold'),
                                   text_color='#1e272e', justify=CENTER).pack()

        self.lblUser = CTkLabel(self.contLogin, text='Usuario', justify=LEFT, font=('Verdana', 15),
                                text_color='#1e272e').pack(ipadx=20, pady=5, anchor='w')
        self.entryUser = CTkEntry(self.contLogin, width=400, height=50, font=('Verdana', 15),
                                  placeholder_text='Escribe tu RFC', text_color='#1e272e', fg_color='#f5f6fa',
                                  border_color='#dcdde1')
        self.entryUser.pack()

        self.lblPwd = CTkLabel(self.contLogin, text='Contraseña', justify=LEFT, font=('Verdana', 15),
                               text_color='#1e272e').pack(ipadx=20, pady=5, anchor=W, )
        self.entryPwd = CTkEntry(self.contLogin, width=400, height=50, font=('Verdana', 15), show='•',
                                 placeholder_text='Escribe tu contraseña', text_color='#1e272e', fg_color='#f5f6fa',
                                 border_color='#dcdde1')
        self.entryPwd.pack()

        self.lblShow = CTkLabel(self.contLogin, text='', image=loadImages('../Media/show.png', 20))
        self.lblShow.pack()

        self.btnLogin = CTkButton(self.contLogin, text='Login', font=('Verdana', 15, 'bold'), width=400, height=50,
                                  text_color='#f5f6fa', fg_color='#0652DD', command=self._logIn).pack()

        self.lblShow.bind("<Button-1>", self._show)

        # list of entries
        entries = [self.entryUser, self.entryPwd]

        # configure events from focus for entries de
        for entry in entries:
            entry.bind("<FocusIn>", lambda event, e=entry: self._inFocus(e))
            entry.bind("<FocusOut>", lambda event, e=entry: self._outFocus(e))
            entry.bind("<Return>", self._enter)


Login().mainloop()
