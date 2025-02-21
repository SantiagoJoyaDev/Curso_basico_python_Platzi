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

try:
    suma = numero_1 + numero_3
    print("La suma de los numero es: ", suma)
except:
    print("Se ha producido un error")#En este caso entra aqui!!!!1
else:
    print("La ejecucion se ha ejecutado correctamente")
    
try:
    suma = numero_1 + numero_2
    print("La suma de los numero es: ", suma)#Entra aqui!!!
except:
    print("Se ha producido un error")
else:
    print("La ejecucion se ha ejecutado correctamente")#Pero tambien entra aqui!!!!!
    
try:
    suma = numero_1 + numero_2
    print("La suma de los numero es: ", suma)#Entra aqui!!!
except:
    print("Se ha producido un error")
else:
    print("La ejecucion se ha ejecutado correctamente")#Pero tambien entra aqui!!!!!
finally:
    print("La ejecucion continua...")#Este finally se ejecuta sea cual sea el caso si hay un error o no


