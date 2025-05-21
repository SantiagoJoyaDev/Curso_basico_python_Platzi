print("----------EJERCICIOS DE MODULOS----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Usa el módulo math para calcular la raíz cuadrada de un número ingresado por el usuario.")
import math
from platform import node
numero = int(input("Ingrese un numero "))
operacion = math.sqrt(numero)
print("La raiz cuadrada del numero ingresado es:",operacion)
    
print("----------FIN----------")

print("Ejercicio 2: Crea un módulo llamado operaciones.py con una función multiplicar(num1, num2). Luego," 
      "importa este módulo y usa la función en otro archivo.")
from Probando_los_modulos import conversiones_de_grados, multiplicacion
multiplicacion(2,4)

print("----------FIN----------")

print("Ejercicio 3: Crea un módulo llamado conversiones.py con una función convertir_a_mayusculas(texto) que" 
      "devuelva el texto en mayúsculas. Luego, importa este módulo en otro archivo y utiliza la función para" 
      "convertir un mensaje ingresado por el usuario a mayúsculas.")
import Probando_los_modulos

Probando_los_modulos.mayusculas()

print("----------FIN----------\n")

print("----------EJERCICIOS INTERMEDIO----------")

print("Ejercicio 4: Crea un módulo conversiones.py con funciones para convertir de Celsius a Fahrenheit y viceversa. Luego," 
      "importa solo la" 
      "función que convierte a Fahrenheit y úsala.")
import Probando_los_modulos
resultado = Probando_los_modulos.conversiones_de_grados(fahrenheit=node,celsius=node)
print(resultado)


print("----------FIN----------")

print("Ejercicio 5: Usa el módulo datetime para imprimir la fecha y hora actuales en el formato 'Día-Mes-Año Hora:Minuto:Segundo'.")
import datetime
fecha_actual = datetime.datetime.now()#Aqui primero importamos la funcionalidad de datetime luego llamamos el metodo
#datetime para utilizar las fechas y horas(el formato) luego llamamos el metodo now para de igual forma trabajar
#con fecha y hora actual
formato = fecha_actual.strftime("%H:%M:%S %d-%m-%y")#aqui despues de que ya llamamos el formato de fecha y hora luego 
#utilizamos el metodo strftime el cual me permite definir que quiero mostrar en fecha y hora
print("La hora y feca actual es: ", formato)

print("----------FIN----------")

print("Ejercicio 6: Importa el módulo math con un alias (m) y usa m.sqrt() para calcular la raíz cuadrada de 144.")
import math as m  # Importamos el módulo math con el alias 'm'

raiz = m.sqrt(144)  # Calculamos la raíz cuadrada de 144
print("La raíz cuadrada de 144 es:", raiz)

print("----------FIN----------\n")

print("----------EJERCICIOS DIFICL----------")
print("Ejercicio 7: Crea una carpeta llamada utilidades/ con dos módulos:"
"texto.py: contiene una función contar_palabras(texto) que devuelve la cantidad de palabras en una cadena."
"numeros.py: contiene una función es_primo(n) que verifica si un número es primo."
"Luego, importa estos módulos y úsales en un script principal.")
import Probando_los_modulos

Probando_los_modulos.contar_palabras()

print("----------FIN----------")

print("Ejercicio 8: Usa el módulo datetime para obtener la fecha y hora actual e imprímela en pantalla.")
import datetime
fecha_actual = datetime.datetime.now()#Aqui primero importamos la funcionalidad de datetime luego llamamos el metodo
#datetime para utilizar las fechas y horas(el formato) luego llamamos el metodo now para de igual forma trabajar
#con fecha y hora actual
formato = fecha_actual.strftime("%H:%M:%S %d-%m-%y")#aqui despues de que ya llamamos el formato de fecha y hora luego 
#utilizamos el metodo strftime el cual me permite definir que quiero mostrar en fecha y hora
print("La hora y feca actual es: ", formato)
print("----------FIN----------")

print("Ejercicio 9: Usa el módulo random para mezclar una lista de nombres y luego imprimir el resultado.")
import random as r

# Lista de nombres
nombres = ["Ana", "Carlos", "Luis", "María", "Sofía", "Juan"]

# Mezclar la lista de nombres de forma aleatoria
r.shuffle(nombres)

# Imprimir la lista mezclada
print("Lista mezclada:", nombres)

print("----------FIN----------")
 
print("Ejercicio 10: Usa el módulo os para listar todos los archivos y carpetas en el directorio actual.")
import os

# Listar todos los archivos y carpetas en el directorio actual
contenido = os.listdir('.')#Llama a la función listdir del módulo os, la cual devuelve una lista con los nombres 
#(como cadenas de texto) de todos los archivos y carpetas que se encuentran en el directorio que se le indique.

#Especifica el directorio actual. En sistemas operativos, el punto (.) se utiliza para referirse al directorio en el que se está ejecutando el script.
print("Archivos y carpetas en el directorio actual:")
print(contenido)

print("----------FIN----------")