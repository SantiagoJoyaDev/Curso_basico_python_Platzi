import numpy as np # pylint: disable=import-error
print("----------LISTAS----------")


#La diferencia entres las listas y las tuplas es que las tuplas no se pueden modificar y las listas si. 
# Ademas de que las tuplas se declaran con parentesis y las listas con corchetes
my_lista = list()
my_other_lista = []#Se declaran con corchetes

print(len(my_lista))

my_lista = [123,545,32,12,12,346,8]
print(my_lista[0])#Puedo imprimir o acceder cada valor solo de la lista segun lo necesite
print(my_lista[1])
print(my_lista[2])
print(my_lista[3])
print(my_lista[4])
print(my_lista[5])
print(my_lista[6])
print(my_lista)
print(type(my_lista))#Para saber que tipo de dato es (Lista)
print(len(my_lista))#Para saber cuantos elementos tiene mi lista
print(my_lista[0:5])#Nos devuelve exactamente estos dos valores que queremos

my_other_lista = [22,1.82,"Santiago","Joya","joya",22]
print(my_other_lista[0])
print(my_other_lista[+2])
print(my_other_lista[1])
print(my_other_lista[-1])
print(my_other_lista[-2])
print(my_other_lista)
print(my_other_lista.count(22))
print(my_other_lista.count("joya"))

edad1, estatura, nombre, apellido1, apellido2, edad2 = my_other_lista#como se igualo el numero de caracteres a la de la lista funciona
#pero pues si hay al menos un dato menos no funciona porque tiene que tener el mismo tamano de la lista para poder hacer el print
print(edad2)

print("----------CONCATENADO DE LISTAS----------")

lista_1 = ["santiago","joya"]
lista_2 = ["blanco"]

suma_de_listas = lista_1 + lista_2
print(suma_de_listas)

lista_1 = ["Andres","joya"]
lista_2 = ["Anaya"]

#Importante se concatena dependiento del orden en el que esten
print(lista_1 + lista_2)
print(lista_2 + lista_1)

print("----------FUNCIONES DE LISTAS----------")
lista_1 = [1,2,3,4,5,5,5,5,5]
print("-----COUNT-----")#Sirve para contar cuantos elementos repetidos del mismo caracter hay
print("Cuantos numero 5 hay repetidos:",lista_1.count(5) , "funcion de COUNT implementado\n")

print("-----MAYO O MENOR-----")#Sirve para limpiar la lista completa
print("EL numero mayor de toda la lista es: ",max(lista_1))
print("EL numero menor  de toda la lista es: ",min(lista_1))

print("-----APPEND-----")#Sirve para agregar un caracter nuevo a la lista al final de la lista
print("Aqui esta la respuesta con la funcion de APPEND imiplementado...",lista_1)
lista_1.append(6)
print(lista_1,"\n")

print("-----INSERT-----")#Sirve para agregar un caracter pero en la posicion que yo quiera
lista_1.insert(3,4)
print("Aqui esta la respueta con la fucion de INSERT implementada",lista_1,"\n")

print("-----REMOVE-----")#Sirve para remover cualquier caracter de la lista
lista_1.remove(5)
print("Aqui esta la respueta con la fucion de REMOVE implementada",lista_1,"\n")

print("-----POP-----")#Sirve para quitar solo un valor el ultimo que se ingreso o si lo defino borrar el que yo quiera
lista_1.pop()
print("Aqui esta la respueta con la fucion de POP implementada",lista_1)
lista_1.pop(0)#aqui le digo al pop espeficamente cual elemento borrar especificamente
print("Aqui esta la respueta con la fucion de POP implementada con unvalor especifico borrado",lista_1,"\n")

print("-----REVERSE-----")#Sirve para darle la vuelta a la lista original
lista_1.reverse()
print("Aqui esta la respueta con la fucion de REVERSE implementada",lista_1,"\n")

print("-----SORT-----")#Sirve par ordenar la lista de menor a mayor
lista_1.sort()
print("Aqui esta la respueta con la fucion de SORT implementada",lista_1,"\n")

print("-----COPY-----")#Sirve para realizar una copia independiente de la lista original
my_nueva_lista_1 = lista_1.copy()  # Crear una copia independiente
lista_1.clear()  # Limpiar la lista original
print("Aqui esta la respuesta con la funcion de COPY implementada", my_nueva_lista_1, "\n")

print("-----CLEAR-----")#Sirve para limpiar la lista completa
lista_1.clear()
print("Aqui esta la respueta con la fucion de CLEAR implementada",lista_1,"\n")

print("----------LISTAS DE LISTAS (MATRICES)----------")
#Basicamente seria una matriz pero en realidad tiene las mismas propiedades que una lista puedo añadir o modificar elemento
#lo que quiere decir que son datos mutables
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix)
print(len(matrix))
print(type(matrix))
#Ahora vamos a acceder a todos los elementos de la matriz
print(matrix[0][0])
print(matrix[0][1])
print(matrix[0][2])
#------------------
print(matrix[1][0])
print(matrix[1][1])
print(matrix[1][2])
#------------------
print(matrix[2][0])
print(matrix[2][1])
print(matrix[2][2])

print("----------COMPRENHESION LIST----------")
#Las list comprehensions (comprensiones de listas) son una forma concisa y eficiente de crear listas en Python, 
# utilizando una sola línea de código en lugar de un bucle for tradicional.

squares = [x**2 for x in range(1,11)]
print("Cuadrados: ", squares)

cubes = [x**3 for x in range(1,11)]
print("Cubos: ", cubes)

celsius = [0, 10, 20, 30, 40]
fareheit = [(temp * 9/5)*32 for temp in celsius]
print("Temperatura en grados F°", fareheit)

numeros_pares = [x for x in range(1,21) if x%2 == 0]
print("Los numeros pares del 1 al 20 son:", numeros_pares)

numeros_impares = [x for x in range(1,21) if x%2 != 0]
print("Los numeros impares del 1 al 20 son:", numeros_impares)

#La transpuesta de una matiz
#esta es la forma larga para entender la logica de lo que se realizo
# transposed = []
# for i in range(len(matrix[0])):
#     print(i)
#     transposed_row = []
#     for row in matrix:
#         print(transposed_row)
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
#     print(transposed_row)

# print(transposed)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transposed)

#Utilizando la libreria de NUMPY
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

transposed = matrix.T  # Transponer la matriz
print("\nUtilizando la libreria NUMPY")
print("Matriz original:")  
print(matrix)

print("\nMatriz transpuesta:")
print(transposed)
