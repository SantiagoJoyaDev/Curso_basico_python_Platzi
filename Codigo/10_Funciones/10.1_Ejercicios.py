print("----------EJERCICIOS DE FUNCIONES----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Función que saluda a un usuario.Escribe una función que reciba un nombre como parámetro e imprima un saludo.")
def saludo_usuario (saludo):
    return saludo
print(saludo_usuario("Hola, como estas?"))
print("----------FIN----------")

print("Ejercicio 2: Suma de dos números.Define una función que reciba dos números y devuelva su suma.")
def my_operacion (num1,num2):
    my_suma = num1 + num2
    return my_suma
print("El resultado de la suma es: ", my_operacion(5,10))
print("----------FIN----------")

print("Ejercicio 3: Cuadrado de un número.Crea una función que reciba un número y devuelva su cuadrado.")
def my_operacion(num1):
    my_cuadrado = num1 ** 2
    return my_cuadrado
print("El cuadrado del número es: ", my_operacion(5))
print("----------FIN----------\n")

print("----------EJERCICIOS INTERMEDIO----------")

print("Ejercicio 4: Función con valores por defecto.Crea una función que calcule el área de un rectángulo. Si no se proporciona la altura, debe asumir que es un cuadrado.")
def my_operacion (base,altura = None):#si se quiere probar el else simplemente se le borra el valor de none a la altura
    if altura == None:
        altura_none = base ** 2
        return altura_none
    else:
        return base * altura
print("El área del cuadrado es: ", my_operacion(5))#y aqui en esta parte se agrega el valor de la altura
print("----------FIN----------")

print("Ejercicio 5: Define una función que reciba una lista de números y devuelva una nueva lista solo con los números pares.")
def numeros_pares(lista):
    return [num for num in lista if num % 2 == 0]

print("La lista de números pares es: ", numeros_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


print("----------FIN----------")

print("Ejercicio 6: Escribe una función que reciba un texto y devuelva el número de palabras que contiene.")
def my_contador_de_palabras (texto):
    words = texto.split()#El slplit se utiliza para separa cada palabra
    return len(words)#y aqui con el len contamos las palabras separadas

print("El numeo de palabras que hay en el texto es: ",my_contador_de_palabras("Hola como estas cuenta las palabras de este texto."))

print("----------FIN----------\n")

print("----------EJERCICIOS DIFICL----------")
print("Ejercicio 7: Crea una función que reciba dos números y una operación (+, -, *, /) y devuelva el resultado de la operación.")
def my_operacion (num1,num2,operacion):
    if operacion == '+':
        return num1 + num2
    elif operacion == '-':
        return num1 - num2
    elif operacion == '*':
        return num1 * num2
    elif operacion == '/':
        return num1 / num2
    else:
        print("Ingresa el valor correcto")
print("El resultado de la operacion es: ",my_operacion(3,23,"+"))        
print("----------FIN----------")

print("Ejercicio 8: Define una función que genere la serie de Fibonacci hasta un número dado.")
def fibonacci(n):## La serie de Fibonacci es una secuencia de números donde cada número es la suma de los dos anteriores,
    # generalmente comenzando con 0 y 1. Es decir, la secuencia comienza 0, 1, 1, 2, 3, 5, 8, 13, ...
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])  # Lo que hace con el append 
        #es agregar el siguiente número en la serie sumando los dos últimos números de la lista
    return fib_series[:n]

print("La serie de Fibonacci es: ", fibonacci(10))
print("----------FIN----------")

print("Ejercicio 9: Escribe una función que determine si un número es primo.")
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("El número es primo: ", es_primo(29))
print("----------FIN----------")
 
print("Ejercicio 10: Crea una función que reciba un número arbitrario de valores y devuelva su promedio.")
def promedio(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

print("El promedio de los valores es: ", promedio(1, 2, 3, 4, 5))
print("----------FIN----------")