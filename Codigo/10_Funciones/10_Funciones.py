print("----------FUNCIONES----------")

#Las funciones son bloques de código que se pueden ejecutar varias veces, las funciones pueden recibir parámetros y devolver un valor.
#Las funciones se definen con la palabra reservada def seguida del nombre de la función y los parámetros que recibe la función.

def my_function():
    print("Hola soy una función")

my_function()

#la diferencia de una funcion con return y una sin el return es que la que tiene return nos devuelve un valor 
# y la que no tiene return no nos devuelve nada.

def sum_two_values (numero1,numero2): #Función que suma dos valores
    return numero1 + numero2

#Llamamos a la función sum_two_values y le pasamos dos valores 5 y 10 y nos devuelve la suma de estos dos valores
print("La suma de los dos valores es:", sum_two_values(5,10))
sum_two_values(5,10)#de esta manera no nos devuelve nada porque no estamos imprimiendo el valor que nos devuelve la función

def my_multiplicacion (numero1,numero2):
    my_multi = numero1 * numero2
    return my_multi

print("La multiplicación de los dos valores es:", my_multiplicacion(5,10))

def print_name (name,surname):
    print(f"{name} {surname}")#con este tipo de print podemos imprimir variables dentro de un string
    
print_name("Perez","Juan")
print_name(surname = "Perez",name = "Juan")
#de esta manera podemos pasar los valores de los parámetros de la función en cualquier orden

def print_name_with_default (name,surname,alias = "Desconocido"):#si le defino aqui el valor del alias, no es necesario pasarlo como parámetro
    print(f"{name} {surname} {alias}")
    
print_name_with_default("Sophia","Anaya")#entonces aqui no es necesario pasar el valor del alias
print_name_with_default("Sophia","Anaya","Sophi")#pero si lo pasamos, se imprimirá el valor que le pasamos

def print_texts (*text):
    print(text)

print_texts("Hola", "Python", "Curso")#de esta manera podemos pasar varios valores a la función los que queramos

print("\n----------FUNCIONES LAMBDA----------")
#Las funciones lambda son funciones anónimas, es decir, no tienen nombre, se definen de la siguiente manera

suma = lambda a,b: a + b 
print("La suma de los dos valores es:", suma(5,10))

multiplicacion = lambda a,b: a * b 
print("La multiplicacion de los dos valores es:", multiplicacion(5,10))

numeros = list(range(1,11))
cuadrado = list(map(lambda x : x**2,numeros))#El map sirve especificamente para realizar la operacion en cada elemento de un iterable
print("Cuadrados", cuadrado)

#Esta es otra manera de realizarlo pero sin el map utilizando una list comprehesion!!!
# numeros = list(range(1, 11))
# cuadrado = [x**2 for x in numeros]  # List comprehension
# print("Cuadrados", cuadrado)

#Obtener los numeros pares
numeros = list(range(1,21))
NumerosPares = list(filter(lambda x: x % 2 == 0,numeros))#se usa para filtrar elementos de un iterable basándose en una condición.
#Solo los elementos que cumplan la condición (es decir, para los que la función devuelve True) se incluyen en el resultado.
print("Numeros pares", NumerosPares)



