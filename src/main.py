# main.py

"""
Archivo principal de la aplicación.

Este archivo se encarga de iniciar la calculadora.
La interfaz y la lógica están separadas en otros archivos
para mantener el proyecto más limpio y profesional.
"""

# Importamos tkinter para crear la ventana principal
import tkinter as tk

# Importamos la clase que contiene toda la interfaz gráfica
from calculator_ui import CalculatorApp


def main():
    """
    Función principal del programa.

    Buena práctica:
    Usar una función main() ayuda a que el código sea más organizado
    y evita que todo se ejecute directamente al importar el archivo.
    """

    # Creamos la ventana principal de la aplicación
    root = tk.Tk()

    # Creamos la aplicación de calculadora y le pasamos la ventana principal
    CalculatorApp(root)

    # Iniciamos el ciclo principal de Tkinter
    # Esto mantiene la ventana abierta esperando acciones del usuario
    root.mainloop()


# Buena práctica:
# Esta condición permite que el programa solo se ejecute
# cuando corremos directamente este archivo.
if __name__ == "__main__":
    main()