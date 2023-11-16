import tkinter as tk
from PIL import ImageGrab
import keyboard

def capturar_pantalla():
    rect = None  # Se define rect aquí, en el mismo ámbito que las funciones anidadas.
    x0, y0, x1, y1 = 0, 0, 0, 0

    def on_drag(event):
        nonlocal rect  # Ahora rect se refiere a la variable definida arriba.
        canvas.delete(rect)
        rect = canvas.create_rectangle(x0, y0, event.x, event.y, outline='red', fill='black', tag='rect')

    def on_click(event):
        nonlocal x0, y0  # Define x0 y y0 con nonlocal para que puedan ser modificados dentro de esta función.
        canvas.delete('rect')  # Borra cualquier rectángulo existente.
        x0, y0 = event.x, event.y
        canvas.bind('<B1-Motion>', on_drag)

    def on_release(event):
        nonlocal x1, y1
        x1, y1 = event.x, event.y
        canvas.unbind('<B1-Motion>')  # Desvincula el evento de movimiento una vez que se suelta el botón.
        root.quit()

    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('print_screen'):
        root = tk.Tk()
        root.attributes("-fullscreen", True)
        root.attributes('-alpha', 0.3)  # Ventana transparente

        canvas = tk.Canvas(root, cursor="cross")
        canvas.pack(fill=tk.BOTH, expand=True)

        canvas.bind('<ButtonPress-1>', on_click)
        canvas.bind('<ButtonRelease-1>', on_release)

        root.mainloop()
        root.destroy()

        return ImageGrab.grab(bbox=(x0, y0, x1, y1))

    return None
