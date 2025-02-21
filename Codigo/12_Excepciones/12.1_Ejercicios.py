print("----------EJERCICIOS DE EXCEPCIONES----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Escribe un programa que solicite dos números al usuario e intente dividirlos."
"Usa try-except para manejar la división por cero.")
    
numero_1 = 234
numero_2 = "sdfg"


try:
    division = numero_1 / numero_2
    print("La division de los numero es: ", division)
except:
    print("Se ha producido un error")#En este caso entra aqui!!!!1
else:
    print("La ejecucion se ha ejecutado correctamente")

print("----------FIN----------")

print("Ejercicio 2: Pide un número al usuario e intenta convertirlo a entero."
"Usa try-except para manejar errores si el usuario ingresa texto en lugar de un número.")

try:
    numero = int(input("Ingresa un numero"))
    print("El numero ingresado es: ", numero)
except:
    print("Se ha producido un error")
print("----------FIN----------")

print("Ejercicio 3: Crea una lista con 5 elementos y solicita al usuario un índice para acceder a un elemento."
"Usa try-except para manejar el caso en que el índice esté fuera del rango.")

try:
    my_lista = [23,123,1,1,5]
    indice = int(input("Ingresa a cual indice quiere acceder del 0 al 4"))
    print("El indice al cual se ingreso es:", my_lista[indice])
except:
    print("Se produjo un error")
print("----------FIN----------\n")

print("----------EJERCICIOS INTERMEDIO----------")

print("Ejercicio 4: Pide al usuario dos números y una operación (+, -, *, /)."
"Usa try-except para manejar errores como división por cero o caracteres no válidos.")

try:
      numero_1 = int(input("Ingresa el primer numero:"))
      numero_2 = int(input("Ingresa el segundo numero:"))
      my_operation = input("Ingresa la operación (+, -, *, /): ")
      
      if my_operation == "+":
          print("El resultado de la suma es:", numero_1 + numero_2)
      elif my_operation == "-":
          print("El resultado de la resta es:", numero_1 - numero_2)
      elif my_operation == "*":
          print("El resultado de la multiplicación es:", numero_1 * numero_2)
      elif my_operation == "/":
          print("El resultado de la división es:", numero_1 / numero_2)
except:
    print("Se produjo un error")


print("----------FIN----------")

print("Ejercicio 5: Solicita al usuario el nombre de un archivo y trata de abrirlo."
"Usa try-except para manejar el error si el archivo no existe.")
try:
      nombre_del_archivo = input("Ingresa el nombre del archivo: ")
      if not isinstance(nombre_del_archivo, str):
            raise ValueError("El nombre del archivo debe ser una cadena de texto.")
      print("El nombre del archivo es:", nombre_del_archivo)
except ValueError as ve:
      print("Se produjo un error:", ve)
except Exception as e:
      print("Se produjo un error:", e)

print("----------FIN----------")

print("Ejercicio 6: Crea un diccionario con nombres y edades."
"Pide al usuario un nombre y usa try-except para manejar el caso en que la clave no exista en el diccionario.")

try:
    my_nombres_dict = {"Nombre_1":"Santiago Joya",
                 "Nombre_2":"Jonaha garcia",
                  "Nombre_3":"Juan luis perez",
                  "Nombre_4":"Armando mendoza",
                  "Nombre_5":"Sofia vergara"}
    nombre = input("Ingresa un nombre para buscar en el diccionario: ")
    print("El nombre es: ", my_nombres_dict[nombre])
except:
      print("El nombre elegido no existe")

print("----------FIN----------\n")

print("----------EJERCICIOS DIFICL----------")
print("Ejercicio 7: Escribe un programa que combine varias excepciones: división por cero, acceso a un índice fuera de" 
    "rango y errores en conversión de tipos."
    "Usa try-except para manejarlas de manera adecuada.")

try:
    numero_1 = int(input("Ingresa el primer numero: "))
    numero_2 = int(input("Ingresa el segundo numero: "))
    resultado_division = numero_1 / numero_2
    print("El resultado de la división es:", resultado_division)

    lista = [1, 2, 3, 4, 5]
    indice = int(input("Ingresa un índice para acceder a la lista: "))
    print("El valor en el índice es:", lista[indice])

except ZeroDivisionError:
    print("Error: División por cero.")
except IndexError:
    print("Error: Índice fuera de rango.")
except ValueError:
    print("Error: Conversión de tipo inválida.")
except Exception as e:
    print("Se produjo un error:", e)

print("----------FIN----------")

print("Ejercicio 8: Simula un sistema de inicio de sesión donde el usuario tiene tres intentos para ingresar la contraseña correcta."
"Usa try-except para manejar el error si el usuario introduce un tipo de dato incorrecto o si se queda sin intentos.")

try:
    nombre = input("Ingresa tu nombre: ")
    print("Hola!!! Bienvenido de nuevo,", nombre)
    intentos = 3
    while intentos > 0:
        contrasena = input("Ingresa tu contraseña: ")
        if contrasena == "Santyjoya02":
            print("Inicio de sesión exitoso!")
            break
        else:
            intentos -= 1
            print("Contraseña incorrecta. Te quedan", intentos, "intentos.")
    if intentos == 0:
        print("Ups!!! lo siento", nombre, "te quedaste sin intentos")
except:
    print("Dato incorrecto.....")

print("----------FIN----------")

print("Ejercicio 9: Escribe un programa que intente leer un archivo y, sin importar si el archivo existe o no," 
      "garantice que se ejecuta un bloque finally.")

try:
    nombre_archivo = str(input("Ingrese el nombre del archivo"))
    print("Perfecto seleccionaste un archivo")
except:
    print("Uyyy no se selecciono un archivo :(")
finally:
    print("El nombre del archivo que elgiste es: ", nombre_archivo)

print("----------FIN----------")
 
print("Ejercicio 10: Pide dos números al usuario y una operación."
"Si la operación es inválida, lanza una excepción personalizada con raise.")

try:
    numero_1 = int(input("Ingrese el primer numero"))
    numero_2 = int(input("Ingrese el segundo numero"))
    operacion = input("Ingrese algunas de las siguientes operaciones (+ - * /)")
    if operacion == "+":
        op = numero_1 + numero_2
    print("El resultado de la operacion es: ", op)
except:
    print("La operacion no es valida....")        

print("----------FIN----------")