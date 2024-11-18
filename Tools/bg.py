import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk


class AnimatedGIFBackground:
    def __init__(self, frame, gif_path):
        # Lista para almacenar los fotogramas del GIF
        self.frames = []

        # Abre el GIF y extrae cada fotograma
        gif = Image.open(gif_path)

        # Obtiene el tamaño del GIF
        self.width, self.height = gif.size

        # Redimensiona el frame al tamaño del GIF
        frame.configure(width=self.width, height=self.height)

        try:
            while True:
                frame_img = gif.copy().convert("RGBA")
                # Redimensiona el fotograma
                frame_img = frame_img.resize(
                    (self.width, self.height), Image.LANCZOS)
                self.frames.append(ImageTk.PhotoImage(frame_img))
                gif.seek(len(self.frames))  # Mueve al siguiente fotograma
        except EOFError:
            pass  # Cuando se llega al último fotograma

        # Etiqueta para mostrar el GIF como fondo
        self.background_label = CTkLabel(frame, image=self.frames[0])
        self.background_label.place(
            relwidth=1, relheight=1)  # Ocupa todo el Frame

        # Variables para la animación
        self.frame_index = 0
        self.animate_gif()

    def animate_gif(self):
        # Actualiza la imagen cada 100 ms (puedes ajustar la velocidad)
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.background_label.configure(image=self.frames[self.frame_index])
        # Programa la siguiente actualización
        self.background_label.after(100, self.animate_gif)

'''
# Inicializa CustomTkinter y crea la ventana
set_appearance_mode("dark")  # Modo claro o oscuro
set_default_color_theme("blue")  # Tema de colores

# Crear ventana principal
root = CTk()  # Crea la ventana principal
root.geometry("600x400")  # Establece un tamaño inicial para la ventana

# Crear un Frame
fram = CTkFrame(root, )
# Expande el Frame para ocupar todo el espacio
fram.pack(fill=tk.BOTH, expand=True)

# Crear el fondo animado
AnimatedGIFBackground(fram, "TBD/media/YQgT.gif")

# Añade widgets encima del GIF animado
boton = CTkButton(root, text="Haz clic aquí",
                  fg_color="transparent", corner_radius=20)
boton.place(relx=0.5, rely=0.5, anchor=CENTER)

# Ejecuta la ventana
root.mainloop()
'''