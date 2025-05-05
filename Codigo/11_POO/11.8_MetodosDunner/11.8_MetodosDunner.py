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