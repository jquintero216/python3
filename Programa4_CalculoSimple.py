# Lenguaje: Python3
# Compilador: Python 3.6.9
# Empresa: N/A
# Ubicación: Lima - Perú

# Aplicación: Operaciones entre variables ingresadas
# Versión: 1.0
# Fecha: abril/27/2020

# Programa 4 Cálculo simple
# SO: Linux Ubuntu 18.04

# Importar archivos de cabeceras
import math

# Declaracion de variables 
Varx = int(input("Introduzca valor variable x: "))
Vary = int(input("Introduzca valor variable y: "))
Varz = int(input("Introduzca valor variable z: "))

# Operacion entre variable
suma = Varx + Vary
resta = Varx - Vary
producto = Varx * Vary
division = Varx / Vary
mod = Varx % Vary
raiz2 = math.sqrt (Varz)
cosen = math.cos (Varz)

# Mostrar resultados
print (" ")
print ("Resultados: ")
print ("Suma: ",suma)
print ("Resta: ",resta)
print ("Producto: ",producto)
print ("Division: ",division)
print ("Resto: ", mod)
print ("Raiz cuadrada: ",raiz2)
print ("Coseno de Z: ", cosen)