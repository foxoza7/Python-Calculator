import os
import tkinter as tk
from calculator_ui import CalculatorApp

def main():
    # VERIFICACIÓN INTELIGENTE:
    # Si la variable de entorno 'DISPLAY' está vacía, estamos en Docker/Servidor
    if os.environ.get('DISPLAY') is None:
        print("--- MODO SERVIDOR/DOCKER DETECTADO ---")
        print("La interfaz gráfica no puede abrirse.")
        print("Ejecutando lógica de calculadora en modo texto...")
        
        # AQUÍ DEBES LLAMAR A TU LÓGICA DE CÁLCULO
        # Ejemplo: calculadora_consola() 
        # (Si no tienes una, solo imprime un mensaje por ahora)
        print("Resultado: El contenedor está vivo pero la GUI está desactivada.")
        
    else:
        # MODO ESCRITORIO NORMAL
        print("--- MODO ESCRITORIO DETECTADO ---")
        root = tk.Tk()
        CalculatorApp(root)
        root.mainloop()

if __name__ == "__main__":
    main()