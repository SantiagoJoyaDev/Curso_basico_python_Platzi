print("----------CLASES----------")

#Las clases son plantillas para crear objetos (instancias) en Python.
#Permiten agrupar datos y funcionalidades relacionadas en una sola estructura.

class MyEmpyPersona:#Para las clases en python ya no la definimos con "snake_case" las definimos con "CamelCase"
    pass#El pass se utiliza como un marcador de posición temporal para el cuerpo de la clase.

print(MyEmpyPersona)

class MyPersona:
    def __init__(self, name, surname):#Esta es una funcion reservada del sistema que sirve para crear un constructor de la clase
        self.name = name 
        self.surname = surname
        #En resumen, self.name = name y self.surname = surname guarda el valor del parámetro name en el atributo name del objeto, 
        #permitiendo que cada instancia de la clase MyPersona tenga su propio nombre. 

# El constructor es un método especial que se llama automáticamente cuando se crea una instancia de la clase. 
# Se utiliza para inicializar los atributos del objeto y realizar cualquier configuración necesaria. En Python, 
# el constructor se define con el método __init__.

my_persona = MyPersona("Santiago", "Joya")#Aqui creamos una variable en la cual le ingresamos los parametros de name y surname lo cual entonces
#se convierte en un objeto
print(f"{my_persona.name}", f"{my_persona.surname}")


class MyAnimal:
    def __init__(self):
        self.name = "Loro"
        self.color = "Rojo"

my_animal = MyAnimal()
print(f"Name: {my_animal.name} Color: {my_animal.color}")


class MyPlane:
    def __init__(self, name, type):
        self.full_model = f"{name} {type}"
        
my_plane = MyPlane("Vascal Rush", "234-ASD")
print(my_plane.full_model)

class MyFutbolista:
    def __init__(self):
        self.name = "Santiago"
        self.surname = "Joya"
        self.tshirt = 7
    
    def run(self):
        print(f"El jugador {self.name} {self.surname} con el dorsal {self.tshirt} hizo un golazo!!!!....")
        
my_player = MyFutbolista()
print(f"Name: {my_player.name} surname: {my_player.surname} Dorsal: {my_player.tshirt}")
my_player.run()