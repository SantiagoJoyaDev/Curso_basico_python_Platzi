print("----------EJERCICIOS DE STRINGS----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Declara dos variables tipo string: una con tu nombre y otra con tu apellido."
    "Concátelas en una nueva variable e imprime el resultado.")
nombre = "Santiago"
apellido = "Joya"
nombreyapellido = nombre , apellido
print("Hola ", nombreyapellido , " como te encuentras el dia de hoy ? ")
print("-----FIN-----\n")

print("Ejercicio 2: Escribe un string que contenga una frase completa y usa la función len() para imprimir la cantidad total de caracteres en el string.")
frase = "Hola estoy muy bien gracias por preguntar..."
print(frase)
print(f"El numero de caraceres de la frase es",len(frase))
print("-----FIN-----\n")

print("Ejercicio 3: Declara un string con todas las vocales en minúsculas. Usa una función para convertirlo a mayúsculas y luego imprime el resultado.")
vocales = "a e i o u"
print("Vocales en minusculas ", vocales)
print(f"Ahora las vocales en mayusculas",vocales.upper())
print("-----FIN-----\n") 

print("----------EJERCICIOS INTERMEDIO----------")
print("Ejercicio 4: Escribe un string que contenga una palabra de 8 caracteres."
      "Luego, usa rebanado (slicing) para imprimir los primeros 4 caracteres y los últimos 4.")
palabra = "Holasara"
rebanadoprimeros = palabra[:4]
rebanadoultimos = palabra[4:]
print(palabra)
print("Mostrando los primeros 4 caracteres",rebanadoprimeros)
print("Mostrando los ultimos 4 caracteres",rebanadoultimos)
print("-----FIN-----\n")

print("Ejercicio 5: Declara un string que diga: 'Hola mundo, bienvenido al mundo de Python.'"
      "Usa una función para reemplazar la palabra 'mundo' por 'universo' y muestra el resultado.")
frase = "Hola Mundo, bienvenido al mundo de Python."
reemplazando = frase.replace("mundo" , "universo")
print("La frase original -->",frase)
print("Frase reemplazada -->",reemplazando)
print("-----FIN-----\n")

print("Ejercicio 6: Escribe un string con una frase completa y usa la función count() "
      "para contar cuántas veces aparece una letra específica (por ejemplo, la letra 'a').")
frase = "HoLA, como estas ? me parece que te vi ayer con un chico y estabas muy feliz segun te vi"
print(frase)
print("El numero de veces que se repite el caracter --> e", frase.count("e"))
print("-----FIN-----\n") 

print("----------EJERCICIOS DIFICIL----------")
print("Ejercicio 7: Declara un string con una palabra de exactamente 7 letras y úsalo para desempaquetar cada carácter en una variable diferente."
      "Luego imprime cada carácter en una línea separada.\n")
frase = "calamar"
a, b, c, d, e, f, g = frase
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print("-----FIN-----\n")

print("Ejercicio 8: Crea una variable con un string que contenga tanto letras como números (por ejemplo, 'abc123')."
      "Usa funciones como isalpha(), isdigit(), o isalnum() para validar si el string cumple ciertas condiciones (solo letras, solo números, o mixto")
string = "Abc123"

print("El string contiene solo letras --> ", string.isalnum(), " Verdadero porque hay numeros y letras")#num es para alfanumericos
print("El string contiene solo dígitos --> ", string.isdigit(), " Falso porque el string contiene letras")
print("El string es alfanumérico --> ", string.isnumeric(), "Falso porque hay letras tambien")
print("El string es alfanumérico --> ", string.isalpha(), " Flaso porque hay numero tambien")#si solo son letras
print("-----FIN-----\n")

print("Ejercicio 9: Declara tres variables: tu nombre, tu edad, y tu ocupación."
"Usa las tres técnicas de formateo (%, .format() y f-strings) para imprimir esta frase:"
"'Hola, soy [nombre], tengo [edad] años y soy [ocupación].'")

nombre, edad, ocupacion = "Santiago" , 23 , "Ingeniero de Software"

print("Hola, soy %s, tengo %d, anios y soy %s" %(nombre,edad,ocupacion))
print("Hola, soy {}, tengo {} anios y soy {}".format(nombre,edad,ocupacion))
print(f"Hola, soy {nombre}, tengo {edad} anios y soy {ocupacion}")
print("-----FIN-----\n")

print("Ejercicio 10: Declara un string que diga: 'hOla mUnDo'."
"Usa una combinación de funciones para convertirlo a una versión correctamente capitalizada ('Hola Mundo')"
"y luego verifica si está en mayúsculas o minúsculas con las funciones isupper() o islower().")
frase = "hOla mUnDo"
print(frase)
print(frase.capitalize())
print(frase.upper().islower(), "es falso porque no esta en minusculas esta con una capitalize y luego en minuscula")
print(frase.lower().isupper(), "es falso porque no esta en mayusculas esta con una capitalize y luego en minuscula")
print(frase.upper())
print(frase.upper().isupper(), "es verdadero porque porque todo esta en mayusculas")
print("-----FIN-----\n") 