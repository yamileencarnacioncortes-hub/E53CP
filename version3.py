import tkinter as tk
from tkinter import ttk

#configuracion de todos los frames
COLOR_FONDO = "#d3CECE"
COLOR_MENU= "#2951d3"
COLOR_TEXTO= "#FFFFFF" 
FUENTE_TITULO =("Arial",16,"bold") 
FUENTE_TEXTO= ("Arial",12)

#ventana principal
root=tk.Tk()
root.title("Software de deteccion de addiciones")
root.geometry("900x500")
root.config(bg=COLOR_FONDO)

#configuramos el frame del menu lateral
menu_frame=tk.Frame(root,bg=COLOR_MENU,width=200)
menu_frame.pack(side="left", fill="y")

#contenido del frame de la izquierda
contenido_frame=tk.Frame(root,bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

# funcion para cambiar a las siguientes ventanas

def mostrar_pagina(nombre):
    for witget in contenido_frame.winfo_children():
        witget.detroy()
        paginas[nombres]()

#pagina de bienvenida
def pagina_bienvenida():
 tk.Label(contenido_frame, text="aqui va el contenido de mi pagina",font=FUENTE_TITULO, bg=COLOR_FONFO).pack(pady=30)
tk.Label(contenido_frame, text="aqui va el contenido de la pagina", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=10)
#pagina de registro

#pagina del test

#adicciones de las paginas

paginas={
"Bienvenida": pagina_bienvenida,
"Registro": pagina_registro,
"Test": pagina_test,
}

#mandamos a llamar a la aventanas 
root.mainloop()
