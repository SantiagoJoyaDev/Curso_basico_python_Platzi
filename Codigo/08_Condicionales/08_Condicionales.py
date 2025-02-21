print("----------CONDICIONALES----------")

#Los condicionales son estructuras de control que nos permiten tomar decisiones en nuestro código.

#Estructura de un condicional
my_condition = True
#si le cambio el valor a False, el else se ejecutará

if my_condition:
    print("La condición se cumple")
else:
    print("La condición no se cumple")

my_operation = 5 * 5
if my_operation == 10:
    print("El resultado es 25")
else:
    print("El resultado no es 25")
    
print("----------ELIF----------")

my_operation = 5 * 10
my_edad = 18

if my_operation == 10:
    print("El resultado es 25")
elif my_edad == 18:
    print("Tienes 18 años")
elif my_operation and my_edad == 18:
    print("No se cumplió ninguna condición")
elif my_operation == 50 or my_edad == 33:
    print("Se cumplió alguna de las condiciones")
else:
    print("El resultado no es 25")
    
my_operation = 5 * 100
my_edad = 18

if my_operation == 10:
    print("El resultado es 25")
elif my_edad == 1:
    print("Tienes 18 años")
elif my_operation and my_edad == 34:
    print("No se cumplió la condicion")
elif my_operation == 500 or my_edad == 33:
    print("Se cumplió alguna de las condiciones")
else:
    print("El resultado no es 25")
    
print("----------ESTRUCTURA SWITCH----------")

#En Python no existe la estructura switch, pero podemos simularla con un diccionario

print("----------SWITCH----------")

print("Por favor, ingrese un número del 1 al 7")
print("1. Lunes", "2. Martes", "3. Miércoles", "4. Jueves", "5. Viernes", "6. Sábado", "7. Domingo")
my_day = int(input("Ingrese el dia de la semana:"))

if my_day == 1:
    print("Bievenido al dia Lunes")
elif my_day == 2:
    print("Martes")
elif my_day == 3:
    print("Miércoles")
elif my_day == 4:
    print("Jueves")
elif my_day == 5:
    print("Viernes")
elif my_day == 6:
    print("Sábado")
elif my_day == 7:
    print("Domingo")
else:
    print("El número ingresado no corresponde a un día de la semana")
