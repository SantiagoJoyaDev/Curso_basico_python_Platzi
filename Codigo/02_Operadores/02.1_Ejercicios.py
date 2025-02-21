print("----------EJERCICIOS DE OPERADORES----------")
print("----------NIVEL FACIL----------")
print("Ejercicio 1: Declara dos variables a y b, asígnales valores e imprime la suma de ambas.")
a = 23
b = 245
suma = a + b
print("La suma entre ", a , " + " , b , " es: ", suma)
print("-----FIN-----\n") 

print("Ejercicio 2: Declara dos variables x y y, imprímelas y luego imprime la resta y el producto de x y y")
x = 189
y = 23
resta = x - y
print("La resta entre ", x , " + " , y , " es: ", resta)
print("-----FIN-----\n")

print("Ejercicio 3: Declara dos variables num1 y num2, e imprime un mensaje que diga si num1 es mayor que num2.")
num_1 = 6900
num_2 = 2000
print("El número ", num_1 , " es mayor que el número ", num_2 ,)
print("-----FIN-----\n")

print("----------NIVEL INTERMEDIO----------")
print("Ejercicio 4: Declara dos variables num1 y num2. Imprime la división de num1 entre num2 y el residuo (módulo) de la división.")
num_1 = 26
num_2 = 3
division = float(num_1 / num_2)
modulo = num_1 % num_2
print("La división entre ", num_1 , " y ", num_2 , " es: ", division , " y el modulo de esa division es: ", modulo)

print("-----FIN-----\n")

print("Ejercicio 5: Declara tres variables con valores diferentes." 
      "Usa operadores de comparación para imprimir si las variables son iguales o distintas entre sí.")
c = 123
d = 123
e = 111
print("La variable c --> ", c , " es igual que la varible d --> ", d)
print("La variable c --> ", c , " es diferente que la varible e --> ", e) 
print("-----FIN-----\n")

print("Ejercicio 6: Declara tres variables a, b y c con valores numéricos." 
      "Imprime el resultado de (a + b) * c y luego de a + (b * c). Explica cómo cambian los resultados dependiendo del uso de paréntesis.")
a = 567
b = 3
c = 90
operacion_1 = (a + b) * c
operacion_2 = a + (b * c)
print("La operación (a + b) * c es: ", operacion_1)
print("La operación a + (b * c) es: ", operacion_2)
print("Lo que sucede en la primer operacion es que se genera un orden y una organizacion de la operaciones en donde primero se ejecuta lo que esta en el parentesis")
print("Lo que sucede en la primer operacion es que se genera un orden y una organizacion de la operaciones en donde primero se ejecuta lo que esta en el parentesis")
print("-----FIN-----\n")

print("----------NIVEL DIFICIL----------")
print("Ejercicio 7: Declara tres variables x, y, y z con valores numéricos. Calcula e imprime el promedio de esos tres números.")
x = 12
y = 89
z = 145
promedio = int((x + y + z) / 3)#La conversion o la funcion que quiera utilizar se realiza en la operacion
print("El promedio de X, Y y Z es: ", promedio)
print("-----FIN-----\n")

print("Ejercicio 8: Declara cuatro variables a, b, c, y d. Imprime el resultado de la comparación (a > b) and (c < d) y otra con (a == c) or (b != d).")
a = 12
b = 56
c = 89
d = 765
print("La comparación entre (a > b) ", a , " mayor (>) ", b ," es FALSO y la comparacion entre (c < d) ", c , " menor(<) ", b , " es VERDADERO")
print("-----FIN-----\n")

print("Ejercicio 9: Declara dos variables n1 y n2. Imprime True si n1 es múltiplo de n2 y False en caso contrario.")
n_1 = 9
n_2 = 3
operacion = num_1 % num_2 == 0
print("El resultado de la operacion es: ", operacion , " por lo tanto...")
print("La variable n_1 --> ", n_2 , " no es un multiplo de la variable n_1 --> ", num_2)
print("-----FIN-----\n")

print("Ejercicio 10: Declara dos variables num1 y num2." 
      "Calcula la diferencia absoluta entre ellas e imprime si la diferencia es mayor que 10. Utiliza la función abs() para la diferencia.")
num_1 = 9
num_2 = 3
operacion = num_1 - num_2
operacion_2 = abs(operacion >= 10)
#la explicacion seria que como tal deberia el problema un valor True o False pero en realidad si lo esta arrojando solo que en valor bool 1 o 0
#entonces 1 es True y 0 es False
print("El resultado de la operacion entre ", num_1 , " y " , num_2 , " es: ", operacion ," pero con el valor absoluto es: ",operacion_2)
print("Por lo tanto el valor de ", operacion_2 , "es decir que es FALSE no es mayor a 10.")
print("-----FIN-----\n")