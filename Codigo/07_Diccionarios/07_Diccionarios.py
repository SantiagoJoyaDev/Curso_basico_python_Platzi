print("----------DICCIONARIOS----------")

# Los diccionarios son una estructura de datos que nos permite almacenar valores de cualquier tipo, como enteros, cadenas, listas, tuplas, etc. y a diferencia de las tuplas y las listas   
# que se acceden a través de un índice, los diccionarios se acceden a través de una clave y se definen mediante llaves {}.

my_dict = ()
my_other_dict = {}#los diccionarios se definen con llaves

print(type(my_dict))
print(type(my_other_dict))

my_personal_data_dict = {"Nombre":"Santiago",
                         "Edad":22,
                         "Pais":"Colombia",
                         "Ciudad":"Bucaramanga"}

print(type(my_personal_data_dict))
print(len(my_personal_data_dict))

my_favorites_cars = {"Mazda":"Mazda 3",
                     "Ferrari":"Ferrari 488",
                     "Mustang":"Ford Mustang",
                     1:"Maserati Ghibli",# Las claves pueden ser de cualquier tipo
                     "Maserati":{1:"Maserati Ghibli", 2:"Maserati Quattroporte"}}

print(type(my_favorites_cars))
print(len(my_favorites_cars))
print(my_favorites_cars["Mazda"])
print(my_favorites_cars["Ferrari"])
print(my_favorites_cars["Mustang"])
print(my_favorites_cars[1])
print(my_favorites_cars["Maserati"])


print("----------OPERACIONES CON DICCIONARIOS----------")

my_favorite_programming_languages_dict = {1:"Python",
                     2:"Java",
                     3:"JavaScript",
                     4:"C++",# Las claves pueden ser de cualquier tipo
                     5:"C#",
                     6:"Ruby"}

print(my_favorite_programming_languages_dict)
my_favorite_programming_languages_dict[7] = "PHP"# Agregar un nuevo elemento al diccionario
print(my_favorite_programming_languages_dict)
my_favorite_programming_languages_dict[8] = "Go"
print(my_favorite_programming_languages_dict)
my_favorite_programming_languages_dict[8] = "PHP"# Modificar un elemento del diccionario
print(my_favorite_programming_languages_dict)
my_favorite_programming_languages_dict.pop(8)# Eliminar un elemento del diccionario
print(my_favorite_programming_languages_dict)
my_favorite_programming_languages_dict.update({8:"Go"})# Agregar un nuevo elemento al diccionario
print(my_favorite_programming_languages_dict)
print(1 in my_favorite_programming_languages_dict)# Verificar si una clave existe en el diccionario se busca por la clave que es el indice
print("Python" is not my_favorite_programming_languages_dict)# Verificar si un valor existe en el diccionario se busca por el valor
print(my_favorite_programming_languages_dict.get(1))# Obtener un valor del diccionario en especifico
print(my_favorite_programming_languages_dict.keys())# Obtener todas las claves del diccionario
print(my_favorite_programming_languages_dict.values())# Obtener todos los valores del diccionario
print(my_favorite_programming_languages_dict.items())# Obtener todos los items del diccionario
my_favorite_programming_languages_dict.clear()# Limpiar el diccionario
print(my_favorite_programming_languages_dict)



