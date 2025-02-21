print("----------Strings----------")
my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string +" "+ my_other_string)#con el + lo que hago es concatenar Strings...

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab__string = "\tEste es un String con tabulacion"#Para tabular un texto podriamos utilizar el \t
print(my_tab__string)

my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string)

print("----------FORMATEO DE STRINGS----------")

name, surname, edad = "Santiago" , "Joya" , 22

#El formateo para las diferentes variables es int(%d) float(%f) string(%s)
print("Mi nombre es %s %s y mi edad es %d" %(name,surname, edad))
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, edad))#aqui se utiliza una funcion definida la cual me ayuda a formatear el String
print(f"Mi nombre es {name} {surname} y mi edad es {edad}")

print("----------DESEMPAQUETADO DE CARACTERES----------")
language = "python"
a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print("----------DIVISION DE CARACTERES----------")
lenguage_slice = language[:3]#me cuenta las letras o caracteres pero sin contar el 1 y el 3 dependiento de como se coloque 
#si se coloca [2:5] me contaria del 3 al al 4 o si por ejemplo se coloca [1:]me contaria todo empezando desde el 2
#o al reves tambien funciona [:4]solo me contaria del inicio hasta el carater numero 4
print(lenguage_slice)

print("----------FUNCIONES DE CARACTERES----------")
caracter = "Hola soy un caracter"
print(caracter.capitalize())#Empieza con la primer letra del texto que se tenga con mayuscula
print(caracter.upper())#Todas las letras estarian en mayusculas
print(caracter.lower())#Todas la letras en minusculas
print(caracter.count("l"))#Me cuentas cuantas letras repetidas hay
print(caracter.isnumeric())#Me dice si un string es numerico o no
print(caracter.upper().islower())#Me compara en si es Mayuscula o no
print(caracter.upper().isupper())#Me compara si es Minuscula o no

