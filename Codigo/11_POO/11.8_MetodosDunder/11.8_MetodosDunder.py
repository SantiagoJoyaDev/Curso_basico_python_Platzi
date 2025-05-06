print("----------METODOS DUNDER----------")
#Los métodos dunder (de double underscore) son funciones especiales en Python que tienen dos guiones bajos al principio y al final 
# de su nombre (como __init__ o __str__). Sirven para definir o personalizar el comportamiento de los objetos cuando se usan con 
# funciones o operadores incorporados del lenguaje, como print(), +, ==, len(), entre otros.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    
    def __str__(self):# __str__ se llama automáticamente al imprimir el objeto
        return f"{self.nombre} tiene {self.edad} años."
    
    def __repr__(self):# __repr__ se llama automáticamente al imprimir el objeto en modo de depuración
        # Se recomienda que el resultado de __repr__ sea un string que se pueda usar para crear el objeto nuevamente
        return f"Persona --> {self.nombre} tiene {self.edad} años."
    
    def __add__(self, otra_persona):# __add__ se llama automáticamente al sumar dos objetos de la clase Persona
        # En este caso, se suman las edades de las dos personas y se crea una nueva persona con el nombre combinado
        nuevo_valor = self.edad + otra_persona.edad
        return Persona(f"{self.nombre} y {otra_persona.nombre}", nuevo_valor)
    
    def __len__(self):# __len__ se llama automáticamente al usar la función len() en el objeto  
        # En este caso, se devuelve la edad de la persona como el valor de longitud
        return self.edad
    

santiago = Persona("Santiago", 25)
andres = Persona("Andres", 45)
juan = Persona("Juan", 75)
print(santiago) # __str__ se llama automáticamente al imprimir el objeto
print(repr(santiago)) # __repr__ se llama automáticamente al imprimir el objeto en modo de depuración
print(santiago + andres) # __add__ se llama automáticamente al sumar dos objetos de la clase Persona
print(santiago + andres + juan) # __add__ se llama automáticamente al sumar dos objetos de la clase Persona
print(len(santiago)) # __len__ se llama automáticamente al usar la función len() en el objeto
print(len(andres)) # __len__ se llama automáticamente al usar la función len() en el objeto
print(len(juan)) # __len__ se llama automáticamente al usar la función len() en el objeto

#Ejercicio de fusion (Personajes)
#Crear un juego que consiste en crear personajes de un juego y que esos personajes se puedan fusionar para formar personajes mas poderosos
# que tengas mas poder, para ello debemos cambiar el comportamiento del operador + para que cuando se fusionen, salga un nuevo pesonaje con
#habilidades mejoradas
nombre_usuario = input("Ingresa tu nombre de usuario: ")
print(f"\n¡Bienvenido {nombre_usuario}! Este es un juego en el cual podrás crear hasta un máximo de 2 personajes y fusionarlos.")
print("¡Sin más que decir... a crear tus personajes! :)\n")

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"El personaje se llama {self.nombre} y tiene un poder de {self.fuerza} con una velocidad de {self.velocidad}"

    def __add__(self, otro_personaje):
        nuevo_nombre = self.nombre + "-" + otro_personaje.nombre
        nueva_fuerza = (self.fuerza + otro_personaje.fuerza) ** 2
        nueva_velocidad = (self.velocidad + otro_personaje.velocidad) ** 2
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

# Inicio del bucle principal
while True:
    print("\nMenú Principal:")
    print("1. Crear nuevos personajes")
    print("2. Salir del juego")
    seleccion = int(input("Ingrese su selección: "))

    if seleccion == 1:
        nuevo_nombre_personaje_1 = input("\nIngrese el nombre del personaje 1: ")
        nueva_fuerza_personaje_1 = int(input("Ingrese la fuerza del personaje 1: "))
        nueva_velocidad_personaje_1 = int(input("Ingrese la velocidad del personaje 1: "))
        personaje1 = Personaje(nuevo_nombre_personaje_1, nueva_fuerza_personaje_1, nueva_velocidad_personaje_1)
        print(personaje1)
        print("---------------/////---------------")

        nuevo_nombre_personaje_2 = input("Ingrese el nombre del personaje 2: ")
        nueva_fuerza_personaje_2 = int(input("Ingrese la fuerza del personaje 2: "))
        nueva_velocidad_personaje_2 = int(input("Ingrese la velocidad del personaje 2: "))
        personaje2 = Personaje(nuevo_nombre_personaje_2, nueva_fuerza_personaje_2, nueva_velocidad_personaje_2)
        print(personaje2)
        print("---------------/////---------------")

        print("¿Quieres fusionar los personajes para crear uno nuevo?")
        fusion = int(input("Ingresa 1 para SÍ\nIngresa 2 para NO\n"))

        if fusion == 1:
            fusionado = personaje1 + personaje2
            print("\n¡Personaje fusionado creado!")
            print(fusionado)
        elif fusion == 2:
            print("No se ha realizado la fusión. Volviendo al menú...\n")

    elif seleccion == 2:
        print("\nGracias por jugar. ¡Hasta la próxima, " + nombre_usuario + "!")
        break  # termina el bucle y cierra el programa

    else:
        print("Opción no válida. Por favor, selecciona 1 o 2.")

    