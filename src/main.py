# main.py

"""
Archivo principal de la aplicación.

Este archivo se encarga de iniciar la calculadora.
La interfaz y la lógica están separadas en otros archivos
para mantener el proyecto más limpio y profesional.
"""

import os
import tkinter as tk

def main():
    # Si estamos en Docker (o en un entorno sin pantalla), no inicies la GUI
    if os.environ.get('DISPLAY') is None:
        print("Modo Servidor detectado: Ejecutando en modo texto...")
        # Aquí llamarías a una función de consola en lugar de la GUI
        calculadora_consola()
    else:
        print("Modo Escritorio detectado: Abriendo GUI...")
        root = tk.Tk()
        # ... resto de tu código GUI
        root.mainloop()

# Debes crear esta función que solo usa print e input
def calculadora_consola():
    num1 = float(input("Número 1: "))
    # ... lógica de suma
    print(f"Resultado: {resultado}")