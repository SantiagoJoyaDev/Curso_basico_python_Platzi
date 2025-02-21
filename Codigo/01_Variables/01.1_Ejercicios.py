print("----------EJERCICIOS DE VARIABLES----------")
print("----------NIVEL FACIL----------")
print("Ejercicio 1: Declara tres variables: una de tipo str, otra de tipo int, y otra de tipo float." 
      "Imprime el contenido de cada variable en una línea diferente.")
ciudad = "Bucaramanga"
edad = 25
salario = 500000.0
print(ciudad)
print(edad)
print(salario)
print("-----FIN-----\n")
print("Ejercicio 2: Declara dos variables, a y b, con valores iniciales. Cambia sus valores entre sí e imprime ambos antes y después del intercambio." 
      "(Sin usar funciones ni estructuras adicionales).")
a = 10
b = 20
print("Antes del intercambio: a =", a, "b =", b)
a = 86
b = 32
print("Despues del intercambio: a =", a, "b =", b)
print("-----FIN-----\n")

print("Ejercicio 3: Declara tres variables de tipo str con diferentes textos. Concátelas en una sola variable y muestra el resultado.")
nombre , apellido , ciudad = "Santiago" , "Joya" , "Bucaramanga"
print("Hola", nombre , apellido , " tu lugar de residencia es ", ciudad)
print("-----FIN-----\n")

print("----------NIVEL INTERMEDIO----------")
print("Ejercicio 4: Declara tres variables en una sola línea. Por ejemplo: a, b, c = 5, 10, 15. Luego, imprime cada una en una línea diferente.")
procesador , ram , tarjeta_grafica = "amd ryzen 7700x" , 32 , "amd 7800xt"
print("Hola santiago tu procesador es ", procesador , " con una memoria RAM de ", ram ," GB y por ultimo una tarjeta grafica de ", tarjeta_grafica)
print("-----FIN-----\n")

print("Ejercicio 5: Declara una variable de tipo float, por ejemplo 3.14. Convierte este valor a int y luego a str. Imprime los tres resultados," 
      "mostrando qué tipo tiene cada uno.")
variable_1 = 3.1416
variable_2 = 4.1416
variable_3 = 5.1416
print("Antes de la impresion")
print(type(variable_1))
print(type(variable_2))
print(type(variable_3))
print("Impresion con INT")
print(type(int(variable_1)))
print(type(int(variable_2)))
print(type(int(variable_3)))
print("Impresion con STRING")
print(type(str(variable_1)))
print(type(str(variable_2)))
print(type(str(variable_3)))
print("-----FIN-----\n")

print("Ejercicio 6: Declara una variable nombre con tu nombre y una variable edad con tu edad." 
      "Usa un solo print para mostrar un mensaje como: Hola, mi nombre es [nombre] y tengo [edad] años a demas que tengas que ingresar por consola los datos")
nombre = "Santiago"
edad = 23
print("Hola ", nombre , " tu edad es ", edad , " anios y es un gusto conocerte")
print("-----FIN-----\n")

print("----------NIVEL DIFICIL----------")
print("Ejercicio 7: Declara tres variables, x, y y z. Asigna un valor inicial a x, y luego haz que tanto y como z tomen el valor de x." 
      "Cambia el valor de x y verifica que los valores de y y z no se vean afectados.")
x = 23
y = x
z = x
print("Antes de la modificacion de x")
print("este es el valor de X", x , " este es el valor de Y ", y , " y por ultimo este es el valor de Z ", z)
print("Modificando el valor de X")
x = 45
print("Despues de la modificacion de x")
print("este es el valor de X", x , " este es el valor de Y ", y , " y por ultimo este es el valor de Z ", z)
print("-----FIN-----\n")

print("Ejercicio 8: Declara una variable de tipo str con el texto 'MI_CONSTANTE'." 
      "Cambia su contenido intencionadamente durante el programa y muestra un mensaje indicando que es mala práctica modificar 'constantes'.")
variable = "MI_COSNTANTE"
print("Es mala practica modificar variables que se supone que son constantes, ya que por su nombre constante no pueden ser cambiadas")
print("Cambiamos la constante de ", variable)
variable = "aksjdflk;asd"
print("La constante ahora es ", variable , " lo cual es una mala practica al ser una CONSTANTE.")
print("-----FIN-----\n")

print("Ejercicio 9: Declara una variable original con cualquier valor. Crea una segunda variable referencia que apunte al valor de original." 
      "Modifica el valor de original y demuestra que referencia no cambia. Explica el resultado con comentarios.")
original = 23
referencia = original
print("Este es el valor de original ", original , " y este es el valor de referencia ", referencia)
print("Modificando el valor de original")
original = 45
print("Despues de la modificacion de original")
print("Este es el valor de original ", original , " y este es el valor de referencia ", referencia)
print("El motivo por el cual no cambia el valor de referencia es porque no se igualo nuevamente el valor de referencia")
print("-----FIN-----\n")

print("Ejercicio 10: Declara una variable con un texto muy largo (de al menos 500 caracteres) y otra con el valor None." 
      "Imprime ambas con un mensaje que indique el tipo de cada una. (Por ejemplo, usa type(variable) dentro del print).")
larga = ("Hola mucho gusto mi nombre es Santiago y tengo 23 anios actualmente vivo en la ciudad de Bucaramanga en donde hay un clima espectacular...")
a = None
print("Este es el tipo de la variable larga ", type(larga))
print("Este es el tipo de la variable None ", type(None))