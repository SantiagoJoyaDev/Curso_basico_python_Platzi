print("----------EJERCICIOS DE DICCIONARIOS----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Crea un diccionario que contenga tres frutas como claves y sus colores como valores. Imprime el diccionario.")
my_frutas_dict = {"Manzana":"Rojo",
                  "Banana":"Amarillo",
                  "Uva":"Morado"}
print(my_frutas_dict)
print("-----FIN-----\n")
print("Ejercicio 2: Usa un diccionario que contenga tres países como claves y sus capitales como valores. Imprime la capital de un país específico.")
my_paises_dict = {"Mexico":"CDMX",
                    "USA":"Washington",
                    "Canada":"Ottawa"}
print(my_paises_dict["Mexico"])
print(my_paises_dict["USA"])
print(my_paises_dict["Canada"])
print("-----FIN-----\n")
print("Ejercicio 3: Crea un diccionario con tres lenguajes de programación y sus años de creación. Agrega un nuevo lenguaje al diccionario.")
my_lenguajes_dict = {"Python":1991,
                      "Java":1995,
                      "JavaScript":1995}
print(my_lenguajes_dict)
my_lenguajes_dict["C#"] = 2000
print(my_lenguajes_dict)
print("-----FIN-----\n")
print("----------EJERCICIOS INTERMEDIO----------")
print("Ejercicio 4: Crea un diccionario con cinco animales como claves y sus hábitats como valores. Elimina uno de los animales del diccionario.")
my_animals_dict = {"Perro":"Casa",
                    "Gato":"Casa",
                    "Leon":"Selva",
                    "Tigre":"Selva",
                    "Pez":"Mar"}
print(my_animals_dict)
my_animals_dict.pop("Pez")
print(my_animals_dict)
print("-----FIN-----\n")
print("Ejercicio 5: Usa un diccionario con tres deportes como claves y el número de jugadores por equipo como valores. Cambia el valor de uno de los deportes.")
my_atheltics_dict = {"Futbol":11,
                        "Baloncesto":5,
                        "Voleibol":6}
print(my_atheltics_dict)
my_atheltics_dict["Voleibol"] = 30
print(my_atheltics_dict)
print("-----FIN-----\n")
print("Ejercicio 6: Crea un diccionario con tres lenguajes de programación. Verifica si un lenguaje específico está en el diccionario.")
my_lenguajes2_dict = {"Python":1991,
                        "Java":1995,
                        "JavaScript":1995}
print("C#" in my_lenguajes2_dict, "El lenguaje de C# no se encuentra en el diccionario")
print("-----FIN-----\n")
print("----------EJERCICIOS DIFICIL----------")
print("Ejercicio 7: Crea un diccionario con cuatro ciudades como claves y sus poblaciones como valores. Obtén todas las claves y valores del diccionario.")
my_cities_dict = {"Bucaramanga":1000000,
                      "Bogota":10000000,
                      "Medellin":2000000,
                      "Cali":3000000}
print(my_cities_dict.keys())
print(my_cities_dict.values())
print("-----FIN-----\n")
print("Ejercicio 8: Combina dos diccionarios usando el método update. Imprime el diccionario resultante..")
my_cities2_dict = {"Barranquilla":2000000,
                      "Cartagena":1500000}
print(my_cities_dict)
print(my_cities2_dict)
my_cities_dict.update(my_cities2_dict)
print(my_cities_dict)
print("-----FIN-----\n")
print("Ejercicio 9: Crea un diccionario con tres tipos de vehículos y sus precios. Usa el método get para obtener el precio de un vehículo existente y otro que no existe.")
my_vehicles_dict = {"Carro":50000,
                      "Moto":20000,
                      "Bicicleta":1000}
print(my_vehicles_dict.get("Carro"))
print("500" in my_vehicles_dict, "el precio de 500 no se encuentra en el diccionario")
print("-----FIN-----\n")
print("Ejercicio 10: Crea un diccionario con cinco elementos. Luego, usa el método clear para eliminar todos los elementos y verifica que el diccionario está vacío.")
my_vehicles2_dict = {"Carro":50000,
                      "Moto":20000,
                      "Bicicleta":1000,
                      "Avion":1000000,
                      "Barco":500000}
print(my_vehicles2_dict)
my_vehicles2_dict.clear()
print(my_vehicles2_dict)
print("-----FIN-----\n")