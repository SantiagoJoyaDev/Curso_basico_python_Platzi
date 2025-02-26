print("----------EJERCICIOS DE LISTAS----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Crea una lista con los nombres de tus amigos. Imprime el primer y el último nombre de la lista.")
nombres = ["luis","kathe","jonathan","angel","nicol","arian"]
print("El primer nombre de la lista es:",nombres[0])
print("El ultimo nombre de la lista es:",(nombres[5]))
print("-----FIN-----\n")

print("Ejercicio 2: Crea dos listas: una con frutas y otra con verduras. Concátenalas en una sola lista e imprime el resultado.")
frutas = ["Manzana","Banano","Fresa","Frambuesa","Coco"]
verduras = ["Berenjena","Pimenton","Zanahoria","Espinaca","Apio"]
print("Las Frutas y Verduras son:", frutas + verduras)
print("-----FIN-----\n")

print("Ejercicio 3: Crea una lista que contenga números repetidos. Usa count para determinar cuántas veces aparece un número específico.")
numeros = [1,2,345,67,89,3,2]
print("El numero", numeros[1] ,"esta repetido", numeros.count(2) , "veces")
print("-----FIN-----\n")

print("----------EJERCICIOS INTERMEDIO----------")
print("Ejercicio 4: Crea una lista con los números del 1 al 5.Usa append para agregar el número 6."
      "Luego usa remove para eliminar el número 3."
      "Finalmente, imprime la lista.")
numeros = [1,2,3,4,5]
print("Impresion sin el Append", numeros)
numeros.append(6)
print("Impresion con el Append",numeros)
numeros.remove(6)
print("Impresion sin el 6",numeros)
print("-----FIN-----\n")

print("Ejercicio 5: Crea una lista de números desordenados.Usa sort para ordenarlos de menor a mayor."
      "Luego, usa reverse para invertir el orden.")
numeros = [12,2,45,23,24,1,34]
numeros.sort()#El sort ordena los numero de manera automatica de menor a mayor
print("Impresion con el sort",numeros)
print("-----FIN-----\n")

print("Ejercicio 6: Crea una lista con cinco elementos.Haz una copia independiente de la lista usando copy."
      "Limpia la lista original usando clear y muestra ambas listas.")
elementos = ["Rodio","Plata","Oro","Estaño","Cobre"]
copia_elementos = elementos.copy()
elementos.clear()
print("Impresion de la lista original",copia_elementos)
print("-----FIN-----\n")

print("----------EJERCICIOS DIFICIL----------")
print("Ejercicio 7: Crea una lista con al menos 5 elementos." 
      "Escribe un programa que intercambie el primer elemento con el último y el segundo con el penúltimo.")
numeros = [1,2,3,4,5]
print("Impresion sin el intercambio", numeros)
intercambio = numeros[0],numeros[4] = numeros[4],numeros[0]
print("Impresion con el intercambio",intercambio)
print("-----FIN-----\n")

print("Ejercicio 8: Crea una lista de números entre 1 y 20." 
      "Escribe un programa que elimine todos los números pares de la lista sin usar un bucle explícito (for o while).")
numeros = list(range(1,21))#de esta manera utilizo una forma diferente de crear una lista
#y aparte utilizo una funcion range la cual me crea un listado de numero del 1 al 20
print("Impresion sin el remove", numeros)
#La siguiente linea elimina todos los numeros pares de la lista
numeros = list(filter(lambda x: x % 2 != 0, numeros))#de igual manera utilizo la forma especifica de crear la lista
#La función filter() en Python se utiliza para filtrar elementos de un iterable (como una lista o una tupla) 
#según una condición especificada en una función.
#La función lambda es una forma de definir funciones anónimas en una sola línea, lo que es útil cuando se usa con filter().
print("Lista sin números pares:", numeros)
print("-----FIN-----\n")

print("Ejercicio 9: Crea una lista de números del 1 al 10." 
      "Escribe un programa que divida esta lista en dos sublistas: una con los números pares y otra con los números impares.")

numeros = list(range(1, 11))
pares = list(filter(lambda x: x % 2 == 0, numeros))
impares = list(filter(lambda x: x % 2 != 0, numeros))

# Mostrar resultados
print("Números pares:", pares)
print("Números impares:", impares)
print("-----FIN-----\n")

print("Ejercicio 10: Dada una lista con las edades de un grupo de personas, escribe un programa que:"
      "Encuentre la edad máxima y mínima usando las funciones max y min.Calcule el promedio de las edades."
      "Ordene la lista en orden ascendente.")
edades = [12,34,65,76,53,49,23]
promedio = sum(edades) / len(edades)

print("la edad maxina es:",max(edades))
print("la edad minima es:",min(edades))
print("El promedio de las edades es",promedio)
edades.sort()
print("El orden de la lista de forma ascendente es",edades)

print("-----FIN-----\n")