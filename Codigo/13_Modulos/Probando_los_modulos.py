def my_function():
    print("Hola soy una función")
my_function()

def suma(num1,num2):
    suma = num1 + num2
    print("La suma de los dos numero es: ",suma)
    
def multiplicacion(num1,num2):
    multiplicacion = num1 * num2
    print("El resultado de la multiplicacion es: ",multiplicacion)
    
def mayusculas():
    texto = "Hola como estas ?"
    print("Texto solo con la primera en mayusculas -->",texto)
    texto = "hola como estas ?"
    print("Texto con todo en mayusculas -->",texto.upper())
    
def conversiones_de_grados(fahrenheit,celsius):
    opcion = int(input("Ingresa cual es la conversion que quieres realizar\n"
          "1. Convertir de grados Fahrenheit a Celsius \n"
          "2. Convertir de Celsius a fahrenheit "))
    
    if opcion == 1:
        farenheit = int(input("Ingrese los grados Farenheit "))
        conversion = ((farenheit - 32) * 5/9)
        return("La conversion de los grados farenheit", farenheit ,"°C a grados celsius es: ", conversion,"°C")
    
    elif opcion == 2:
        celsius = int(input("Ingrese los grados Celcius "))
        conversion = (celsius * (9/5) + 32)
        return("La conversion de los grados Celsius", celsius ," °F a grados Farenheit es: ", conversion,"°F")
        
    else:
        print("La opcion seleccionada es incorrecta.")