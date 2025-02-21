print("----------BUCLES----------")
print("----------WHILE----------")
#En Python existen dos tipos de bucles: while y for los cuales se utilizan para repetir un bloque de código varias veces.
#estos sirven para ejecutar un bloque de código varias veces.

#Bucle while
#El bucle while se ejecuta mientras una condición sea verdadera.

my_condition = 0

while my_condition < 11:
    print("El valor de la condición es:", my_condition)
    my_condition += 1#Incrementa en 1 el valor de la variable my_condition esto se llama contador

print("Mensaje fuera del bucle while")

my_condition = 0 #lo tengo que volver a inicializar para que no me tome el valor anterior
while my_condition < 20:
    print(my_condition)
    my_condition += 1
    if my_condition == 15:
        print("El valor de la condición es:", my_condition)
        
my_condition = 0 #lo tengo que volver a inicializar para que no me tome el valor anterior
while my_condition < 20:
    print(my_condition)
    my_condition += 1
    if my_condition == 15:
        print("El valor de la condición es:", my_condition)
        break

my_condition = 0 #lo tengo que volver a inicializar para que no me tome el valor anterior
while my_condition < 20:
    print(my_condition)
    my_condition += 1
    if my_condition == 15:
        print("El valor de la condición es:", my_condition)
        continue
    
print("----------FOR----------")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in my_list: #Recorre la lista y asigna el valor a la variable number el number es una variable temporal que se crea en el bucle para 
    #almacenar el valor de la lista en cada iteración pero puede tener cualquier nombre como x, y, z, i, etc.
    print(number)