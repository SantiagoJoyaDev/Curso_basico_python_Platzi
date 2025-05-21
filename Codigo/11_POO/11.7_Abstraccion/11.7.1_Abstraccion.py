from abc import ABC, abstractmethod
print("----------ABSTRACCION----------")
#La abstracción es un principio fundamental de la programación orientada a objetos que permite representar entidades del mundo real de manera 
# simplificada dentro del código. Este principio consiste en identificar y separar las características esenciales de un objeto de aquellas que 
# no son relevantes para el contexto en el que se está utilizando.En otras palabras, la abstracción permite crear una representación lógica de 
# un objeto centrada únicamente en lo que ese objeto debe hacer, sin necesidad de preocuparse en ese momento por cómo lo hace. Esto favorece un 
# diseño más limpio, modular y mantenible, ya que permite trabajar con interfaces simples mientras los detalles internos permanecen ocultos.

class Auto:
   def __init__(self):
       self._estado = "Apagado"
       
   def encender(self):
       self._estado = "Encendido"
       print("El auto esta encendido")
    
   def conducir(self):
       if self._estado == "Apagado":
           self.encender()
           print("Conduciendo el auto")
           
mi_auto = Auto()
mi_auto.conducir()#Se llama al metodo conducir pero como tal no se sabe en general la logica de todo lo que esta dentro de el metodo conducir()
#en cuanto el usuario se oculta la complejidad interna de el metodo conducir

print("----------CLASES ABSTRACTAS----------")
# Una clase abstracta es una clase que no puede ser instanciada directamente, y que está pensada
# para servir como modelo o plantilla para otras clases. Su principal propósito es definir una 
# interfaz común que otras clases deben seguir. Contiene uno o más métodos abstractos, es decir,
# métodos que se definen pero no se implementan —las clases hijas están obligadas a implementarlos.

class Persona(ABC):
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        
    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años sexo: {self.sexo}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, carrera):
        super().__init__(nombre, edad, sexo)
        self.carrera = carrera

    def hacer_actividad(self):
        print(f"Y estoy estudiando: {self.carrera}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, profesion):
        super().__init__(nombre, edad, sexo)
        self.profesion = profesion

    def hacer_actividad(self):
        print(f"Y actualmente trabajo en el ámbito de la {self.profesion}")

# Instancias válidas
santiago = Estudiante("Santiago", 23, "Masculino", "Programación")
kathe = Trabajador("Katherine", 32, "Femenino", "Programación")

santiago.presentarse()
santiago.hacer_actividad()

kathe.presentarse()
kathe.hacer_actividad()


#Con el uso de @classmethod

class Persona1(ABC):
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    @property
    @abstractmethod
    def actividad(self):
        pass

    @abstractmethod
    def hacer_actividad(self):
        pass

    @classmethod
    @abstractmethod
    def crear(cls, nombre, edad, sexo, actividad):
        pass

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años sexo: {self.sexo}")

class Estudiante1(Persona1):
    def __init__(self, nombre, edad, sexo, carrera):
        super().__init__(nombre, edad, sexo)
        self.carrera = carrera

    @property
    def actividad(self):
        return self.carrera

    def hacer_actividad(self):
        print(f"Y estoy estudiando: {self.actividad}\n")

    @classmethod
    def crear(cls, nombre, edad, sexo, actividad):
        return cls(nombre, edad, sexo, actividad)

class Trabajador1(Persona1):
    def __init__(self, nombre, edad, sexo, profesion):
        super().__init__(nombre, edad, sexo)
        self.profesion = profesion

    @property
    def actividad(self):
        return self.profesion

    def hacer_actividad(self):
        print(f"Y actualmente trabajo en el ámbito de la {self.actividad}")

    @classmethod
    def crear(cls, nombre, edad, sexo, actividad):
        return cls(nombre, edad, sexo, actividad)

# Ahora usamos el método de clase para crear los objetos
santiago = Estudiante1.crear("Santiago", 23, "Masculino", "Programación")
kathe = Trabajador1.crear("Katherine", 32, "Femenino", "Programación")

santiago.presentarse()
santiago.hacer_actividad()

kathe.presentarse()
kathe.hacer_actividad()

class Model(ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(cls, _id):
        print(f"Buscando por id {_id} en la tabla {cls().tabla}")

class Usuario(Model):
    def __init__(self):
        self._tabla = "Usuario"

    @property
    def tabla(self):
        return self._tabla

    def guardar(self):
        print("Guardando usuario")
        
# Uso
usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)

#Solo con @property
class Persona2:
    def __init__(self, nacimiento):
        self.nacimiento = nacimiento

    @property
    def edad(self):
        return 2025 - self.nacimiento 

p = Persona2(2000)
print(p.edad)  # Output: 25

#@property + @abstractmethod
class Figura(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    @property
    def area(self):
        return self.lado * self.lado

c = Cuadrado(4)
print(c.area)  # Output: 16

#@classmethod
class Usuario1:
    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def anonimo(cls):
        return cls("Anónimo")

u = Usuario1.anonimo()
print(u.nombre)  # Output: Anónimo


#@classmethod + @abstractmethod
from abc import ABC, abstractmethod

class Conexion(ABC):
    @classmethod
    @abstractmethod
    def conectar(cls):
        pass

class ConexionMySQL(Conexion):
    @classmethod
    def conectar(cls):
        print("Conectando a MySQL...")

ConexionMySQL.conectar()  # Output: Conectando a MySQL...
