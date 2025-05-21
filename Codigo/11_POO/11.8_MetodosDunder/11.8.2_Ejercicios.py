from abc import ABC, abstractmethod
print("----------EJERCICIOS DE METODOS DUNDER----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: __init__ y __str__ Clase Libro"
"Crea una clase Libro con atributos titulo y autor. Implementa __init__ para inicializar los valores y __str__ para que al imprimir el objeto" 
"se vea algo como: 'El principito de Antoine de Saint-Exupéry'.")
class Libro:
    def __init__(self):
        self.titulo = input("Ingresa el título del libro: ")
        self.autor = input("Ingresa el autor del libro: ")
        
    def __str__(self):
        return f"{self.titulo} de {self.autor}"

libro1 = Libro()
print("----------FIN----------")

print("Ejercicio 2: __len__Clase Frase"
"Crea una clase Frase que recibe una cadena de texto. Implementa __len__ para que al usar len(obj) retorne la cantidad de palabras en la frase.")
class Frase:
    def __init__(self):
        self.frase = input("Ingresa una frase: ")
        
    def __len__(self):
        return len(self.frase.split())#divide la cadena en palabras y cuenta cuántas hay.
    
frase1 = Frase()
print(f"La cantidad de palabras en la frase es: {len(frase1)}")
print("----------FIN----------\n")

print("Ejercicio 3: __eq__Comparar dos personas por nombre"
"Crea una clase Persona con atributo nombre. Implementa __eq__ para que dos personas se consideren iguales si tienen el mismo nombre.")
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __eq__(self, otra_persona):# __eq__ se llama automáticamente al comparar dos objetos de la clase Persona
        # En este caso, se compara el nombre de ambas personas
        return self.nombre == otra_persona.nombre

persona1 = Persona("Juan")
persona2 = Persona("Juan")
persona3 = Persona("Pedro")
print(f"¿La persona 1 es igual a la persona 2? {persona1 == persona2}")#True
print("----------FIN----------\n")

print("----------EJERCICIOS INTERMEDIO----------")

print("Ejercicio 4: __add__Sumar vectores 2D"
"Crea una clase Vector2D con atributos x y y. Implementa __add__ para que al sumar dos vectores se retorne un nuevo vector con la suma"
"de sus componentes.")
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, otro_vector):# __add__ se llama automáticamente al sumar dos objetos de la clase Vector2D
        # En este caso, se suman las componentes x e y de ambos vectores
        return Vector2D(self.x + otro_vector.x, self.y + otro_vector.y)

vector1 = Vector2D(3, 4)
vector2 = Vector2D(1, 2)
vector3 = vector1 + vector2# __add__ se llama automáticamente al sumar dos objetos de la clase Vector2D
print(f"El resultado de la suma de los vectores es: ({vector3.x}, {vector3.y})")
print("----------FIN----------")

print("Ejercicio 5: __getitem__Acceso tipo lista"
"Crea una clase ColeccionNumeros que almacene una lista de números. Implementa __getitem__ para acceder a los elementos usando"
"la sintaxis de índice (obj[i])")
class ColeccionNumeros:
    def __init__(self):
        self.numeros = [1, 2, 3, 4, 5]
    
    def __getitem__(self, index):# __getitem__ se llama automáticamente al acceder a un elemento de la lista
        # En este caso, se devuelve el elemento en la posición index de la lista
        return self.numeros[index]

coleccion = ColeccionNumeros()
print(f"El número en la posición 2 es: {coleccion[2]}")# __getitem__ se llama automáticamente al acceder a un elemento de la lista
print("----------FIN----------")

print("Ejercicio 6: __repr__ vs __str__Clase Producto"
"Crea una clase Producto con nombre y precio. Implementa __str__ para mostrarlo amigablemente ('Zapato - $45') y __repr__ para mostrarlo"
"como código (Producto('Zapato', 45)).")
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):# __str__ se llama automáticamente al imprimir el objeto
        return f"{self.nombre} - ${self.precio}"
    
    def __repr__(self):# __repr__ se llama automáticamente al imprimir el objeto en modo de depuración
        # Se recomienda que el resultado de __repr__ sea un string que se pueda usar para crear el objeto nuevamente
        return f"Producto('{self.nombre}', {self.precio})"

producto = Producto("Zapato", 45.000)
print(f"El producto es: {producto}")# __str__ se llama automáticamente al imprimir el objeto
print(f"El producto es: {repr(producto)}")# __repr__ se llama automáticamente al imprimir el objeto en modo de depuración
print("----------FIN----------")

print("----------EJERCICIOS DIFICIL----------")

print("Ejercicio 7: __lt__, __gt__, __eq__Comparar empleados por salario"
"Crea una clase Empleado con nombre y salario. Implementa __lt__, __gt__ y __eq__ para poder comparar empleados entre sí por salario" 
"con <, >, ==, etc.")
class Empleado:
    def __init__(self):
        self.nombre = input("Ingresa el nombre del empleado: ")
        self.salario = float(input("Ingresa el salario del empleado: "))
    
    def __lt__(self, otro_empleado):# __lt__ realiza la comparación menor que
        # __lt__ se llama automáticamente al comparar dos objetos de la clase Empleado
        return self.salario < otro_empleado.salario
    
    def __gt__(self, otro_empleado):# __gt__ realiza la comparación mayor que
        # __gt__ se llama automáticamente al comparar dos objetos de la clase Empleado
        return self.salario > otro_empleado.salario
    
    def __eq__(self, otro_empleado):# __eq__ realiza la comparación igual
        # __eq__ se llama automáticamente al comparar dos objetos de la clase Empleado
        return self.salario == otro_empleado.salario


empleado1 = Empleado()
empleado2 = Empleado()
print(f"El empleado 1 tiene un salario menor que el empleado 2: {empleado1 < empleado2}")
print(f"El empleado 1 tiene un salario mayor que el empleado 2: {empleado1 > empleado2}")
print(f"El empleado 1 tiene un salario igual al empleado 2: {empleado1 == empleado2}")
print("----------FIN----------")

print("Ejercicio 8: __contains__Verificar palabra en frase"
"Crea una clase Texto con una cadena. Implementa __contains__ para que puedas usar 'palabra' in obj y ver si la palabra está en el texto.")
class Texto:
    def __init__(self):
        self.texto = input("Ingresa un texto: ")
        self.texto = self.texto.lower()# convierte el texto a minúsculas
        self.texto = self.texto.split() #separa el texto en palabras
        self.texto = set(self.texto)# el set elimina los duplicados y convierte el texto en un conjunto
        
    def __contains__(self, pal):# __contains__ se llama automáticamente al usar 'palabra' in obj
        # En este caso, se verifica si la palabra está en el texto
        return pal.lower() in self.texto

texto = Texto()
palabra = input("Ingresa una palabra: ")
print(f"La palabra '{palabra}' está en el texto: {palabra in texto}")# __contains__ se llama automáticamente al usar 'palabra' in obj
print("----------FIN----------")

print("Ejercicio 9: __call__Clase contador de llamadas"
"Crea una clase Contador que, cada vez que se llame como función (obj()), aumente un contador interno. Implementa __call__ y un método"
"para ver cuántas veces se ha llamado.")
class Contador:
    def __init__(self):
        self.contador = 0
    
    def __call__(self):# __call__ sirve especificamente para hacer que un objeto de la clase se comporte como una función
        self.contador += 1
    
    def ver_contador(self):# método para ver cuántas veces se ha llamado
        return self.contador
    
contador = Contador()
c = contador()
c = contador()
c = contador()
c = contador()
c = contador()
print(f"El contador ha sido llamado {contador.ver_contador()} veces.")# __call__ se llama automáticamente al usar el objeto como función
print("----------FIN----------")

print("Ejercicio 10: __setitem__, __delitem__Diccionario personalizado"
"Crea una clase DiccionarioPersonalizado que use un diccionario internamente. Implementa __setitem__ y __delitem__ para poder"
"usar obj[key] = val y del obj[key] como si fuera un diccionario.")
class Diccionario:
    def __init__(self):
        self.diccionario = {}
    
    def __setitem__(self, key, value):# __setitem__ se utiliza para asignar un valor a una clave en el diccionario
        self.diccionario[key] = value
    
    def __delitem__(self, key):# __delitem__ se utiliza para eliminar un elemento del diccionario
        del self.diccionario[key]

personas = Diccionario()
personas["Juan"] = 25
personas["Andres"] = 45
personas["Santiago"] = 35
print(f"El diccionario es: {personas.diccionario}")
del personas["Juan"]# __delitem__ se utiliza para eliminar un elemento del diccionario
print(f"Se eliminó a Juan del diccionario.")
print(f"El diccionario es: {personas.diccionario}")
print("----------FIN----------")