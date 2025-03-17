print("----------CLASES----------")

#Las clases: son plantillas para crear objetos (instancias) en Python.
#Permiten agrupar datos y funcionalidades relacionadas en una sola estructura.
#Un objeto: representa una entidad con atributos (características) y métodos (comportamientos). 
#En términos simples, es una estructura que combina datos y funciones que operan sobre esos datos en un solo paquete. 
#los métodos: son funciones que están definidas dentro de una clase y que describen los comportamientos de los objetos 
#creados a partir de esa clase.

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

class Operaciones:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def suma(self):
        return self.a + self.b
        #Esta es otra manera de poder realizarlo
        # resultado = self.a + self.b
        # print("La suma es:", resultado)
    
    def resta(self):
        return self.a - self.b
        #Esta es otra manera de poder realizarlo
        # resultado = self.a - self.b
        # print("La resta es:", resultado)
    
    def multiplicacion(self):
        return self.a * self.b
        #Esta es otra manera de poder realizarlo
        # resultado = self.a * self.b
        # print("La multiplicacion es:", resultado)
    
    def division(self):
        return self.a / self.b
        #Esta es otra manera de poder realizarlo
        # resultado = self.a / self.b
        # print("La division es:", resultado)

#Para la otra forma la impresion seria asi:
suma = Operaciones(4,6)
print("La suma es:", suma.suma())
suma = Operaciones(2025,23)
print("La otra suma es es:", suma.suma())
# suma = Operaciones(123,9)
# suma.suma() 

resta = Operaciones(34,4)
print("La resta es:", resta.resta())
# resta = Operaciones(45,63)
# resta.resta() 

multiplicacion = Operaciones(434,623)
print("La multiplicacion es:", multiplicacion.multiplicacion())
# multiplicacion = Operaciones(4543,633)
# multiplicacion.multiplicacion() 

division = Operaciones(44,56)
print("La division es:", division.division())
# division = Operaciones(455,633)
# division.division() 

class PresentacionDePersonas:
    def __init__(self,fullname,age,country):
        self.fullname = fullname
        self.age = age
        self.country = country
        
    def greeting_1(self):
        print("y es un gusto para mi poder estar en esta clase con ustedes")
        
    def greeting_2(self):
        print("y espero poder llevarme bien con todos ustedes")

persona_1 = PresentacionDePersonas("Adriana Uzcategui gamboa",23,"Venezuela")
print(f"\nHola mi nombre es {persona_1.fullname} tengo {persona_1.age} anios y soy del hermoso pais de {persona_1.country}")
persona_1.greeting_1()
print("\n")
persona_2 = PresentacionDePersonas("Julio Cesar Santodomingo",27,"Brasil")
print(f"Hola mi nombre es {persona_2.fullname} tengo {persona_2.age} anios y soy del pais de {persona_2.country}")
persona_2.greeting_2() 

class Estudiante:
    def __init__(self, name, edad, semestre):
        self.name = name
        self.age = edad
        self.semestre = semestre
        
    def estudiar(self):
        print(f"Hola, mi nombre es {self.name}, tengo {self.age} años y estoy en el semestre {self.semestre}. Y estoy estudiando Ingeniería de Software...")

# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
semestre = input("Ingrese su semestre: ")
# Crear una instancia de la clase Estudiante con los datos ingresados
estudiante1 = Estudiante(nombre, edad, semestre)
# Llamar al método estudiar
estudiante1.estudiar()

 




