import tkinter as tk
# aqui defiinimos las funciones
def mostrar_ventana2():
    ventana1.withdraw() # oculte pantalla 1
    ventana2.deiconify() #mueatre pantalla 2

def regresar():
    ventana2.withdraw() # oculta ventana2
    ventana1.deiconify() #muestra ventana1
