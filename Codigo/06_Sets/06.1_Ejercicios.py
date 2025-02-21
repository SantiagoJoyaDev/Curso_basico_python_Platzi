print("----------EJERCICIOS DE SETS----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Crea un set con valores repetidos. Imprime el set y verifica que los elementos duplicados se eliminan automáticamente.")
my_repeated_numbers_set = {1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10}
print("Tupla con valores repetidos: ", my_repeated_numbers_set)
print("-----FIN-----\n")
print("Ejercicio 2: Crea un set vacío y agrega tres elementos uno por uno usando el método add. Imprime el set después de cada adición.")
my_empty_set = set()
print("Set vacío: ", my_empty_set)
my_empty_set.add("Rojo")
print("Set con un elemento: ", my_empty_set)
my_empty_set.add("Verde")
print("Set con dos elementos: ", my_empty_set)
my_empty_set.add("Azul")
print("Set con tres elementos: ", my_empty_set)
print("-----FIN-----\n")
print("Ejercicio 3: Crea un set con colores. Verifica si 'Rojo' está en el set y si 'Azul' no está en el set.")
my_colors_set = {"Rojo", "Verde", "Amarillo", "Blanco","Negro"}
print("Rojo" in my_colors_set, "es verdadero(True) porque si se encuenta el color Rojo en el el set")
print("Azul" in my_colors_set, "es falso(false) porque no se encuenta el color Azul en el el set")
print("-----FIN-----\n")
print("----------EJERCICIOS INTERMEDIO----------")
print("Ejercicio 4: Crea dos sets con números y concaténalos utilizando update. Imprime el set resultante.")
my_numbers1_set = {1,2,3,4,5,6}
my_numbers2_set = {7,8,9,10}
my_numbers1_set.update(my_numbers2_set)
print("Los sets concatenados con el metodo Update son: ",my_numbers1_set)
print("-----FIN-----\n")
print("Ejercicio 5: Crea dos sets con letras. Combínalos usando el método union e imprime el resultado.")
my_letters1_set = {"a","b","c"}
my_letters2_set = {"d","e","f"}
my_both_letter_sets = my_letters1_set.union(my_letters2_set)
print("Los dos set concatenado con el metodo Union son: ",my_both_letter_sets)
print("-----FIN-----\n")
print("Ejercicio 6: Crea un set con tres palabras. Usa el método discard para eliminar una palabra que no existe y observa que no genera error.")
my_words_set = {"Hola","Mundo","Python"}
my_words_set.discard("Java")
print("El set de palabras es: ",my_words_set)
print("-----FIN-----\n")
print("----------EJERCICIOS DIFICIL----------")
print("Ejercicio 7: Crea un set con números y usa el método clear para vaciarlo. Imprime el set antes y después de la limpieza.")
my_numbers_set = {1,2,3,4,5,6,7,8,9,10}
print("El set de numeros es: ",my_numbers_set)
my_numbers_set.clear()
print("El set de numeros despues de limpiarlo es: ",my_numbers_set)
print("-----FIN-----\n")
print("Ejercicio 8: Crea dos sets con números. Calcula la diferencia entre ambos sets usando difference y muestra el resultado.")
my_numbers1_set = {1,2,3,4,5,6,7,8,9,10}
my_numbers2_set = {5,6,7,8,9,10,11,12,13,14}
my_difference_numbers = my_numbers1_set.difference(my_numbers2_set)
print("La diferencia entre los dos sets es: ",my_difference_numbers)
print("-----FIN-----\n")
print("Ejercicio 9: Crea un set y elimina un elemento que no está en él usando remove para observar el error generado. Luego usa discard para evitar el error.")
my_numbers_set = {1,2,3,4,5,6,7,8,9,10}
print("El set de numeros es: ",my_numbers_set)
#my_numbers_set.remove(11)#Genera un error porque el elemento no se encuentra en el set
my_numbers_set.discard(11)#No genera error porque el elemento no se encuentra en el set
print("El set de numeros despues de limpiarlo es: ",my_numbers_set)
print("-----FIN-----\n")
print("Ejercicio 10: Crea dos sets con colores. Calcula los elementos únicos que están en uno u otro set pero no en ambos usando symmetric_difference.")
my_colors1_set = {"Rojo", "Verde", "Amarillo", "Blanco"}
my_colors2_set = {"Azul", "Verde", "Amarillo", "Blanco"}
my_symmetric_difference_colors = my_colors1_set.symmetric_difference(my_colors2_set)
print("Los elementos únicos que están en uno u otro set pero no en ambos son: ",my_symmetric_difference_colors)
print("-----FIN-----\n")