print("----------VARIABLES---------")

mi_primer_variable = "Hola soy la primer variable"
print("Soy una variable de tipo String -->", mi_primer_variable)
#Para imprimir con algo mas como texto es decir la concatenacion es como esta arriba...print("Soy una variable de tipo String -->", mi_primer_variable)

mi_int_variable = 5600
print("Soy una variable de tipo int -- >", mi_int_variable)

mi_bool_variable = True
print("Soy una variable de tipo bool -- >", mi_bool_variable)

mi_float_variable = 3.89
print("Soy una variable de tipo float -- >", mi_float_variable)

mi_complex_variable = 3 + 3j
print("Soy una variable de tipo complex -- >", mi_complex_variable)

mi_lista_variable = [1,2,3,4,5]
print("Soy una variable de tipo list -- >", mi_lista_variable)

print("----------FUNCIONES CON VARIABLES EN PYTHON---------")
print("----------FUNCIONES PRE-CARGADAS DE PYTHON---------")

print("El numero de caracteres de la variable es = ")
print(len(mi_primer_variable))#esta funcion de len() solo funciona con variables de tipo String
print(f"El número de caracteres de la variable es = {len(mi_primer_variable)}")#ahora de esta manera no tengo que escribirlo arriba por separado el texto

print("----------VARIABLES EN UNA SOLA LINEA---------")

nombre , apellido , anios , alias = "Santiago" , "Joya" , 22 , "La Joyita"
print("Mi nombre es = ", nombre , apellido, " y tengo " , anios , " anos y mi alias es ", alias)

print("----------VARIABLES INGRESADAS POR CONSOLA---------")

nombre1 = input("Ingresa nombre: ")
apellido1 = input("Ingresa apellido: ")
anios1 = int(input("Ingresa edad: "))

print("Hola", nombre1 , apellido1 , " como estas ? tu edad es " , anios1)