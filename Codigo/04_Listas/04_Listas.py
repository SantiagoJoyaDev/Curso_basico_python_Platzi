print("----------LISTAS----------")

#La diferencia entres las tlistas y las tuplas es que las tuplas no se pueden modificar y las listas si. Ademas de que las tuplas se declaran con parentesis y las listas con corchetes
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
print(len(my_lista))

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