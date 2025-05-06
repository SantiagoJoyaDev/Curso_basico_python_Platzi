from abc import ABC, abstractmethod
print("----------EJERCICIOS DE Enc----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: __init__ y __str__ Clase Libro"
"Crea una clase Libro con atributos titulo y autor. Implementa __init__ para inicializar los valores y __str__ para que al imprimir el objeto" 
"se vea algo como: 'El principito de Antoine de Saint-Exupéry'.")

print("----------FIN----------")

print("Ejercicio 2: __len__Clase Frase"
"Crea una clase Frase que recibe una cadena de texto. Implementa __len__ para que al usar len(obj) retorne la cantidad de palabras en la frase.")

print("----------FIN----------\n")

print("Ejercicio 3: __eq__Comparar dos personas por nombre"
"Crea una clase Persona con atributo nombre. Implementa __eq__ para que dos personas se consideren iguales si tienen el mismo nombre.")

print("----------FIN----------\n")

print("----------EJERCICIOS INTERMEDIO----------")

print("Ejercicio 4: __add__Sumar vectores 2D"
"Crea una clase Vector2D con atributos x y y. Implementa __add__ para que al sumar dos vectores se retorne un nuevo vector con la suma de sus componentes.")

print("----------FIN----------")

print("Ejercicio 5: __getitem__Acceso tipo lista"
"Crea una clase ColeccionNumeros que almacene una lista de números. Implementa __getitem__ para acceder a los elementos usando la sintaxis de índice (obj[i])")

print("----------FIN----------")

print("Ejercicio 6: __repr__ vs __str__Clase Producto"
"Crea una clase Producto con nombre y precio. Implementa __str__ para mostrarlo amigablemente ('Zapato - $45') y __repr__ para mostrarlo"
"como código (Producto('Zapato', 45)).")

print("----------FIN----------")

print("----------EJERCICIOS DIFICIL----------")

print("Ejercicio 7: __lt__, __gt__, __eq__Comparar empleados por salario"
"Crea una clase Empleado con nombre y salario. Implementa __lt__, __gt__ y __eq__ para poder comparar empleados entre sí por salario" 
"con <, >, ==, etc.")
     
print("----------FIN----------")

print("Ejercicio 8: __contains__Verificar palabra en frase"
"Crea una clase Texto con una cadena. Implementa __contains__ para que puedas usar 'palabra' in obj y ver si la palabra está en el texto.")

print("----------FIN----------")

print("Ejercicio 9: __call__Clase contador de llamadas"
"Crea una clase Contador que, cada vez que se llame como función (obj()), aumente un contador interno. Implementa __call__ y un método"
"para ver cuántas veces se ha llamado.")

print("----------FIN----------")

print("Ejercicio 10: __setitem__, __delitem__Diccionario personalizado"
"Crea una clase DiccionarioPersonalizado que use un diccionario internamente. Implementa __setitem__ y __delitem__ para poder"
"usar obj[key] = val y del obj[key] como si fuera un diccionario.")

print("----------FIN----------")
