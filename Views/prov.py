from tkinter import *
from tkcalendar import Calendar

def get_date():
    selected_date = cal.get_date()
    print(f"Fecha seleccionada: {selected_date}")

root = Tk()
cal = Calendar(root, selectmode='day', date_pattern='dd-mm-yyyy')
cal.pack(pady=20)

button = Button(root, text="Mostrar Fecha", command=get_date)
button.pack(pady=10)

root.mainloop()