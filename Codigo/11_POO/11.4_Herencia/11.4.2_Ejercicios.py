print("----------EJERCICIOS DE HERENCIA----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Escribe un programa que solicite al usuario dos números y muestre la suma en pantalla.")
class Operacion():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
class Suma(Operacion):
    def suma(self):
        suma = self.num1 + self.num2
        return suma
    
suma = Suma(3,5)
rta_suma = suma.suma() #Tengo que llamar a la funcion que me realiza la operacion...
print("El resultado de la suma es: ", rta_suma)
print("----------FIN----------")

print("Ejercicio 2: Escribe un programa que pida un número y determine si es par o impar.")
class Number():
    def __init__(self,num):
        self.num = num

class ParImpar(Number):
    def operacion(self):
        if self.num % 2 == 0:
            return print(f"El numero {self.num} es un numero PAR")
        else:
           return print(f"El numero {self.num} es un numero IMPAR")

numero = int(input("Ingresa el numero:"))
resultado = ParImpar(numero).operacion()
print(resultado)
print("----------FIN----------")

print("Ejercicio 3: Escribe un programa que convierta una temperatura de grados Celsius a Fahrenheit.")
class General:
    def __init__(self, valor):
        self.valor = valor

class Fahrenheit(General):
    def convertir(self):
        return (self.valor - 32) * 5/9  # Convierte Fahrenheit a Celsius

class Celsius(General):
    def convertir(self):
        return (self.valor * 9/5) + 32  # Convierte Celsius a Fahrenheit

# Mostramos las instrucciones al usuario
print("Instrucciones:\n"
      "Ingrese 1 para convertir de Fahrenheit a Celsius\n"
      "Ingrese 2 para convertir de Celsius a Fahrenheit")

# Pedimos la opción al usuario
opcion = int(input("Ingrese la opción: "))

if opcion == 1:
    fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
    resultado = Fahrenheit(fahrenheit).convertir()
    print(f"{fahrenheit}°F equivale a {resultado:.2f}°C")
    
elif opcion == 2:
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    resultado = Celsius(celsius).convertir()
    print(f"{celsius}°C equivale a {resultado:.2f}°F")
    
else:
    print("Opción inválida, por favor ingrese 1 o 2.")
print("----------FIN----------\n")

print("----------EJERCICIOS INTERMEDIO----------")

print("Ejercicio 4: Escribe un programa que cuente cuántas vocales hay en una palabra ingresada por el usuario.")
class Vocales():
    def __init__(self,palabra):
        self.palabra = palabra

class ContarVocales(Vocales):
    def contar_vocales(self):
        vocales = "a e i o u"
        cont = sum(1 for letra in self.palabra if letra in vocales)# el 1 no quiere decir que empiece con 1 sino que por cada valor
        #que sea una vocal va a devolver un 1 y luego suma los 1 los cuales son los valores de las vocales para saber el total de vocales
        return cont
        
palabra = input("Ingrese una palabra: ")
contador = ContarVocales(palabra)
cantidad_vocales = contador.contar_vocales()

print(f"La palabra '{palabra}' tiene {cantidad_vocales} vocales.")
print("----------FIN----------")

print("Ejercicio 5: Escribe un programa que muestre la tabla de multiplicar de un número ingresado por el usuario.")
class Numeros():
    def __init__(self,numero1):
        self.numero1 = numero1
\

class TablasDeMultiplicar(Numeros):
    def tablas(self):
        for i in range(1, 11):
            print(my_number, "x", i, "=", my_number * i)


my_number = int(input("Ingrese el número: "))
print("La tabla de multiplicar del numero", my_number ,"es")
tabla = TablasDeMultiplicar(my_number)
tabla.tablas()
print("----------FIN----------")

print("Ejercicio 6: Escribe un programa que genere una lista de números primos hasta un valor ingresado por el usuario.")
class Numero():
    def __init__(self, num):
        self.num = num
        
    def numeros_primos(self):
        print(f"Números primos hasta {self.num}:")
        for n in range(2, self.num + 1):
            es_primo = True
            for i in range(2, int(n ** 0.5) + 1):# saber el rango de numero los cuales se va a dividir el numero ingresado por el usuario
                if n % i == 0:
                    es_primo = False
                    break
            if es_primo:
                print(n)
            
numero = int(input("Ingrese un número: "))
numero_primos = Numero(numero)
print("Los numeros primos son:")
numero_primos.numeros_primos()

print("----------FIN----------\n")

print("----------EJERCICIOS DIFICIL----------")
print("Ejercicio 7: Escribe un programa que invierta una cadena de texto sin usar funciones predefinidas como reverse().")
class Texto():
    def __init__(self, cadena):
        self.cadena = cadena

class InversorTexto(Texto):
    def invertir(self):
        invertida = ""
        for i in range(len(self.cadena) - 1, -1, -1):  # Itera de atrás hacia adelante
            invertida += self.cadena[i]
        return invertida

cadena = input("Ingrese una cadena de texto: ")
inversor = InversorTexto(cadena)
print("Cadena invertida:", inversor.invertir())
      
print("----------FIN----------")

print("Ejercicio 8: Escribe un programa que ordene una lista de números ingresados por el usuario usando el" 
      "algoritmo de ordenamiento burbuja.")
class ListaDesordenada():
    def __init__(self):
        self.list = [64, 34, 25, 12, 22, 11, 90]

class BubbleSort(ListaDesordenada):
    def lista_ordenada(self):
        arr = self.list  # Usamos la lista de la clase padre
        n = len(arr)
        
        for i in range(n):
            swapped = False
            print(f"Iteración {i+1}: {arr}")  # Muestra la lista en cada iteración
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            
            if not swapped:
                break  # Si no hubo intercambios, la lista ya está ordenada
        
        return arr  # Retorna la lista ordenada

# Crear objeto y ejecutar el algoritmo
ordenador = BubbleSort()
print("Lista inicial(desordenada):",ordenador.list)
print("Lista ordenada:", ordenador.lista_ordenada())
print("----------FIN----------")

print("Ejercicio 9: Escribe un programa que determine si un número ingresado por el usuario es un número perfecto" 
      "(un número es perfecto si la suma de sus divisores propios es igual a sí mismo).")
class Num():
    def __init__(self, num):
        self.num = num

    def es_perfecto(self):
        suma_divisores = sum(i for i in range(1, self.num) if self.num % i == 0)
        return suma_divisores == self.num

# Solicitar un número al usuario
numero = int(input("Ingrese un número: "))
numerito = Num(numero)

# Verificar si es un número perfecto
tipo = "es un número perfecto" if numerito.es_perfecto() else "no es un número perfecto"
print(f"El número {numero} {tipo}.")

print("----------FIN----------")
 
print("Ejercicio 10: Escribe un programa que permita agregar, eliminar y mostrar las tareas")
class GestorTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
    
    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)
    
    def mostrar_tareas(self):
        for i, tarea in enumerate(self.tareas):#La función enumerate() en Python se usa para recorrer iterables 
            #(como listas, tuplas o cadenas) y obtener tanto el índice como el valor de cada elemento en un bucle.
            print(f"El indice de la tarea agregada es {i} y la tarea es -->{tarea}")
        if not self.tareas:
            print("No hay tareas.")

# Ejemplo de uso
gestor = GestorTareas()
gestor.agregar_tarea("Hacer ejericio")
gestor.agregar_tarea("Estudiar python")
gestor.agregar_tarea("Proyecto cepci")
gestor.agregar_tarea("Trabajar")
print("Se muestran las tareas sin eliminar ninguna tarea")
gestor.mostrar_tareas()
gestor.eliminar_tarea(1)
print("\nSe muestran las tareas eliminando la tarea de Estudiar python")
gestor.mostrar_tareas()
print("----------FIN----------")
