print("----------EXCEPCIONES----------")
"""
Las excepciones en Python son eventos que ocurren durante la ejecución de un programa y que pueden interrumpir el flujo normal 
de las instrucciones. Cuando ocurre una excepción, Python genera un objeto de excepción que contiene información sobre el error. 
Las excepciones pueden ser manejadas utilizando bloques try-except, lo que permite al programador controlar el comportamiento 
del programa en caso de errores.
"""
numero_1 = 23
numero_2 = 2
numero_3 = "asdf"
numero_4 = 0


try:
    suma = numero_1 + numero_3
    print("La suma de los numeros es: ", suma)
except:
    print("Se ha producido un error")#En este caso entra aqui!!!! 
else:
    print("La ejecucion se ha ejecutado correctamente")
    
try:
    suma = numero_1 + numero_2
    print("La suma de los numeros es: ", suma)#Entra aqui!!!
except:
    print("Se ha producido un error")
else:
    print("La ejecucion se ha ejecutado correctamente")#Pero tambien entra aqui!!!!!
    
try:
    suma = numero_1 + numero_2
    print("La suma de los numeros es: ", suma)#Entra aqui!!!
except:
    print("Se ha producido un error")
else:
    print("La ejecucion se ha ejecutado correctamente")#Pero tambien entra aqui!!!!!
finally:
    print("La ejecucion continua...")#Este finally se ejecuta sea cual sea el caso si hay un error o no

try:
    suma = numero_1 + numero_3
    print("La suma de los numeros es: ", suma)
except:
    print("Se ha producido un error :(")#En este caso entra aqui!!!! 
else:
    print("La ejecucion se ha ejecutado correctamente")
    

try:
    division = numero_1 / numero_4
    print("La suma de los numeros es: ", suma)
except ZeroDivisionError as e:#Aqui simplemente le defino un alias y imprimo el error pero de parte de python
    print("Error: pero aqui python muestra el error -->", e)
else:
    print("La ejecucion se ha ejecutado correctamente")

numero_5 = int(input("Ingresa el valor: "))
try:
    division = numero_1 / numero_5
    print("La division de los numeros es: ", division)
except ValueError as e:#Aqui simplemente le defino un alias y imprimo el error pero de parte de python
    print("Error: pero aqui python muestra el error -->", e)
else:
    print("La ejecucion se ha ejecutado correctamente")
    
def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

print_exception_hierarchy(Exception)