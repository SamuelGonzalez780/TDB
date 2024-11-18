import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


class AnimatedGIFBackground(ctk.CTk):
    def __init__(self, gif_path, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Lista para almacenar los fotogramas del GIF
        self.frames = []

        # Abre el GIF y extrae cada fotograma
        gif = Image.open(gif_path)
        try:
            while True:
                frame = ImageTk.PhotoImage(gif.copy().convert("RGBA"))
                self.frames.append(frame)
                gif.seek(len(self.frames))  # Mueve al siguiente fotograma
        except EOFError:
            pass  # Cuando se llega al último fotograma

        # Etiqueta para mostrar el GIF como fondo
        self.background_label = ctk.CTkLabel(self, image=self.frames[0])
        self.background_label.place(relwidth=1, relheight=1)

        # Variables para la animación
        self.frame_index = 0
        self.animate_gif()

    def animate_gif(self):
        # Actualiza la imagen cada 100 ms (puedes ajustar la velocidad)
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.background_label.configure(image=self.frames[self.frame_index])
        # Programa la siguiente actualización
        self.after(100, self.animate_gif)
