# -*- coding: utf-8 -*-
from captura import capturar_pantalla
from ocr import extraer_texto
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

def mostrar_gui(imagen_path, texto):
    ventana = tk.Tk()
    ventana.title("Captura y OCR")
    ventana.configure(bg='black')  # Fondo negro para la ventana

    # Estilo de fuente moderno
    fuente_moderna = font.Font(family='Helvetica', size=12, weight='bold')

    # Configurar el panel de imagen
    img = Image.open(imagen_path)
    img = ImageTk.PhotoImage(img)
    panel_imagen = tk.Label(ventana, image=img, bg='black')
    panel_imagen.image = img
    panel_imagen.pack(side="left")

    # Configurar el widget de texto
    texto_transcripcion = tk.Text(ventana, wrap="word", height=25, width=50, bg='grey20', fg='white', font=fuente_moderna, padx=10)
    texto_transcripcion.insert("1.0", texto)
    texto_transcripcion.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    ventana.mainloop()
def main():
    while True:
        screenshot = capturar_pantalla()
        if screenshot:
            screenshot.save('captura.png')
            texto = extraer_texto('captura.png')
            mostrar_gui('captura.png', texto)
            print(texto)

if __name__ == "__main__":
    main()
