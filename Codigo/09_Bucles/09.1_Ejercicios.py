print("----------EJERCICIOS DE BUCLES----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Contar del 1 al 10 usando while.Escribe un bucle while que imprima los números del 1 al 10.")
i = 0
while i <= 10:
    i += 1# si no quiero imprimir el 0 lo tengo que poner antes de imprimir el valor de i
    print(i)
    #i += 1 imprimir esta linea si quiero que se imprima el 0
print("----------FIN----------")
print("Ejercicio 2: Imprimir elementos de una lista con for.Dada una lista, imprime cada elemento usando un bucle for.")
my_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in my_lista:
    print(number)
print("----------FIN----------")

print("Ejercicio 3: Suma de los primeros 5 números naturales con while.Usa un bucle while para sumar los números del 1 al 5 e imprime el resultado.")
my_numbers = 0
my_suma = 0
while my_numbers < 5:
    my_numbers += 1
    my_suma = my_numbers + my_suma
    print(my_suma)

print("----------FIN----------\n")

print("----------EJERCICIOS INTERMEDIO----------")
print("Ejercicio 4: Imprimir números pares entre 1 y 20 usando while.Crea un bucle que imprima solo los números pares entre 1 y 20.")
my_number = 0
while my_number < 20:
    my_number += 2
    print(my_number)
print("----------FIN----------")

print("Ejercicio 5: Tablas de multiplicar con for.Solicita al usuario un número y muestra su tabla de multiplicar del 1 al 10.")
my_number = int(input("Introduce un número: "))
for i in range(1, 11):
    print(my_number, "x", i, "=", my_number * i)
print("----------FIN----------")

print("Ejercicio 6: Suma de números en una lista con for.Dada una lista de números, calcula la suma de todos los elementos usando un bucle for.")
my_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in my_lista:
    suma = sum(my_lista)
print("La suma de los elementos de la lista es:", suma)
print("----------FIN----------\n")

print("----------EJERCICIOS DIFICL----------")
print("Ejercicio 7: Cálculo de factorial con while.Solicita al usuario un número e imprime su factorial.")
my_number = int(input("Introduce un número: "))
factorial = 1
while my_number > 0:
    print("Numeros:", my_number)
    factorial = factorial * my_number
    my_number -= 1
print("Factorial:", factorial)

print("----------FIN----------")
print("Ejercicio 8: Filtrar y sumar números positivos de una lista.Dada una lista de números, suma solo los positivos usando un bucle for.")
my_list = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
suma = 0
for number in my_list:
    if number > 0:
        suma = suma + number
print("La suma de los números positivos de la lista es:", suma)
print("----------FIN----------")

print("Ejercicio 9: Números primos en un rango.Escribe un programa que encuentre e imprima todos los números primos entre 1 y 50.")
my_list = list(range(1, 51))
for number in my_list:
    if number > 1:#si el numero es mayor a 1 entonces se empieza a dividir
        for i in range(2, number):#aqui se empieza a dividir el numero entre los numeros que estan en el rango el cual empieza en 2 
            if number % i == 0:#si el residuo de la division es 0 entonces no es primo
                break
        else:
            print(number)
print("----------FIN----------")
 
print("Ejercicio 10: Triángulo de asteriscos invertido.Solicita al usuario un número y genera un triángulo de asteriscos invertido.")
my_number = int(input("Introduce un número: "))
for i in range(my_number, 0, -1):#el rango empieza en el numero que introduzca el usuario y va disminuyendo en 1 el funcionamient es el siguiente
    #el primer valor es el numero que introduce el usuario el segundo valor es el numero que va a llegar y el tercer valor es el decremento en este caso es -1
    my_operation = "*" * i
    print(my_operation)#se imprime el asterisco multiplicado por el numero que introduzca el usuario
    
#de igual manera se puede hacer de la siguiente manera pero no esta invertido
my_number = int(input("Introduce un número: "))
for i in range(1, my_number + 1):
    my_operation = "*" * i
    print(my_operation)
    
print("----------FIN----------")