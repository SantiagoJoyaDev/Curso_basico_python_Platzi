print("----------EJERCICIOS DE CONDICIONALES----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Pide al usuario un número y verifica si es positivo, negativo o igual a cero.")
my_number = int(input("Ingresa un número: "))
if my_number > 0:
      print("El número es numero positivo")
elif my_number < 0:
      print("El número es numero negativo")
else:
      print("El número es igual a cero")
print("----------FIN----------")
print("Ejercicio 2: Comprobar si un número es par o impar")
my_number = int(input("Ingresa un número: "))
if my_number % 2 == 0:
      print("El número es par")
else:
      print("El número es impar")
print("----------FIN----------")

print("Ejercicio 3: Verificar si una palabra comienza con vocal,Solicita una palabra e indica si comienza con una vocal (a, e, i, o, u).")
my_word = input("Ingresa una palabra: ")
if my_word[0] in "aeiou" or my_word[0] in "AEIOU":
      print("La palabra comienza con una vocal")
else:
      print("La palabra no comienza con una vocal")
print("----------FIN----------")

print("----------EJERCICIOS INTERMEDIO----------")
print("Ejercicio 4: Determinar la calificación cualitativa,Pide al usuario una calificación del 0 al 100 e indica su rango:," 
      "Excelente (90+), Bueno (70-89), Regular (50-69), Reprobado (<50) y imprime el resultado.")
my_qualification = int(input("Ingresa tu calificación: "))
if my_qualification >= 90 and my_qualification <= 100:
      print("Felicitaciones tu calificacion es Excelente")
elif my_qualification >= 70 and my_qualification <= 89:
      print("Tu calificacion es Buena")
elif my_qualification >= 50 and my_qualification <= 69:
      print("Tu calificacion es Regular")
elif my_qualification < 50:
      print("Tu calificacion es Reprobado")
else:
      print("Calificación inválida")
print("----------FIN----------")

print("Ejercicio 5: Día de la semana con la estructura switch.Solicita al usuario un número del 1 al 7 e imprime el día," 
      "correspondiente (lunes a domingo). Si no está en el rango, indica que es inválido.")
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
print("----------FIN----------")

print("Ejercicio 6: Solicita el nombre y la edad de la persona. Indica si es menor, mayor de edad o tiene exactamente 18 años.")
my_name = input("Ingresa tu nombre: ")
my_age = int(input("Ingresa tu edad: "))
if my_age >= 18:
      print("Felicidades", my_name ,"eres mayor de edad y tienes", my_age ,"años")
else:
      print("Lo siento", my_name ,"eres menor de edad tienes", my_age ,"años")
print("----------FIN----------")

print("----------EJERCICIOS DIFICL----------")
print("Ejercicio 7: Solicita tres números y determina cuál es el mayor.")
my_first_number = int(input("Ingresa el primer número: "))
my_second_number = int(input("Ingresa el segundo número: "))
my_third_number = int(input("Ingresa el tercer número: "))
if my_first_number > my_second_number and my_first_number > my_third_number:
      print("El número", my_qualification ,"es mayor que", my_second_number ,"y", my_third_number)
elif my_second_number > my_first_number and my_second_number > my_third_number:
      print("El número", my_second_number ,"es mayor que", my_first_number ,"y", my_third_number)
else:
      print("El número mayor es:", my_third_number)
print("----------FIN----------")

print("Ejercicio 8: Pide los coeficientes a,b,y c de una ecuación cuadrática. Verifica si tiene soluciones reales, imaginarias o únicas."
      "si la solucion da > 0 solucion(Real), si la solucion da = 0 solucion(Imaginaria), si la solucion da < 0 solucion(Unica) "
      "la ecuacion cuadratica es ax^2 + bx + c = 0")
my_first_number = float(input("Ingresa el primer número: "))
my_second_number = float(input("Ingresa el segundo número: "))
my_third_number = float(input("Ingresa el tercer número: "))
ecuacion_cuadratica = my_first_number**2 - 4 * my_second_number * my_third_number

if ecuacion_cuadratica > 0:
      print("La solución es real")
elif ecuacion_cuadratica == 0:
      print("La solución es imaginaria")
elif ecuacion_cuadratica < 0: 
      print("La solución es única")
else:
      print("La ecuación no tiene solución")

# Pruebas
# Prueba 1: Solución real
# Ingresa el primer número: 5
# Ingresa el segundo número: 1
# Ingresa el tercer número: 1
# La solución es real

# Prueba 2: Solución imaginaria
# Ingresa el primer número: 2
# Ingresa el segundo número: 1
# Ingresa el tercer número: 1
# La solución es imaginaria

# Prueba 3: Solución única
# Ingresa el primer número: 1
# Ingresa el segundo número: 2
# Ingresa el tercer número: 3
# La solución es única
print("----------FIN----------")

print("Ejercicio 9: Solicita dos números y una operación (+, -, *, /). Realiza la operación indicada.")
my_first_number = float(input("Ingresa el primer número: "))
my_second_number = float(input("Ingresa el segundo número: "))
my_operation = input("Ingresa la operación (+, -, *, /): ")
if my_operation == "+":
      print("El resultado de la suma es:", my_first_number + my_second_number)
elif my_operation == "-":
      print("El resultado de la resta es:", my_first_number - my_second_number)
elif my_operation == "*":
      print("El resultado de la multiplicación es:", my_first_number * my_second_number)
elif my_operation == "/":
      print("El resultado de la división es:", my_first_number / my_second_number)
else:
      print("Operación inválida")
print("----------FIN----------")
 
print("Ejercicio 10: Categoría según IMC,Solicita el peso y la altura de una persona. Calcula el índice de masa corporal (IMC) y clasifícalo"
      "como bajo peso (<18.5), peso normal (18.5-24.9), sobrepeso (25-29.9) u obesidad (>30).El indice de masa corporal se calcula con la formula IMC = peso / altura^2")
my_weight = float(input("Ingresa tu peso en kg: "))
my_height = float(input("Ingresa tu altura en m: "))
my_imc = my_weight / my_height**2
if my_imc < 18.5:
      print("Tu IMC es:", my_imc ,"y tienes bajo peso")
elif my_imc >= 18.5 and my_imc <= 24.9:
      print("Tu IMC es:", my_imc ,"y tienes peso normal")
elif my_imc >= 25 and my_imc <= 29.9:
      print("Tu IMC es:", my_imc ,"y tienes sobrepeso")
elif my_imc > 30:
      print("Tu IMC es:", my_imc ,"y tienes obesidad")
else:
      print("IMC inválido")
print("----------FIN----------")