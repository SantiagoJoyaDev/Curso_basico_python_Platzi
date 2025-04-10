print("----------ENCAPSULAMIENTO----------")
#El encapsulamiento es uno de los pilares de la Programación Orientada a Objetos (POO). Su objetivo principal es ocultar 
# los detalles internos de un objeto y proteger su estado, permitiendo que solo se acceda o modifique a través de métodos específicos.

#¿Para qué sirve el encapsulamiento?
# Protección de datos → Evita que los atributos sean modificados directamente.
# Control de acceso → Define qué puede modificarse desde fuera de la clase.
# Modularidad → Facilita la organización del código.
# Mantenimiento → Permite hacer cambios internos sin afectar a otras partes del programa.

class MiClase:
    def __init__(self):
        self._name = "Santiago Joya Blanco"#Los atributos escritos asi --> son entendidos como privados _name,_color, etc etc......
        self._id = 1005233962
        self._city = "Bucaramanga"
        #self.__edad = 23#Este es un atributo muy privado por lo que si quiero acceder a el me va arrojar error y de identifican
        #debido a que ahora se define con doble "__" es decir __name,__color, etc etc....
        
    def _presentacion(self):#Tambien existen atributos privados
        print(f"Hola me llamo {self._name} mi cedula es {self._id} y vivo en {self._city}")
        
    def __edad(self):#Tambien existen atributos muy privados
        print(f" Y mi edad es {self.__edad} ")
        
        
persona = MiClase()
print(persona._name,persona._id,persona._city)#Si quiero agregar aqui el __edad me arroja error ya que es un atributo muy privado
persona._presentacion()
#persona.__edad() #entonces esto me arroja error porque como es privado no se puede acceder al metodo privado

print("\n----------GETTERS Y SETTERS----------")
#Los getters y setters son métodos que permiten controlar el acceso y la modificación de los atributos de una clase. 
#Se utilizan principalmente para proteger atributos privados y validar datos antes de asignarlos.

#Encapsulamiento → Protegen los atributos de acceso directo.
# Validación → Permiten validar datos antes de asignarlos.
# Modificación segura → Se pueden cambiar las reglas sin afectar el código externo.
# Control de acceso → Se puede hacer que ciertos atributos sean solo de lectura.

#GETTERS
class Persona:#Con metodo privados
    def __init__(self,name,age):
        self._name = name
        self._age = age
    
    def get_nombre(self):
        return self._name
    
    def get_edad(self):
        return self._age

persona = Persona("Santiago Joya Blanco",23)
nombre = persona.get_nombre()
edad = persona.get_edad()
print("Aqui accedemos con metodos privados getter")
print("Hola mi nombre es", nombre ,"y mi edad es", edad ,"anios")

class Persona1:#Con metodos muy privados
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    
    def get_nombre(self):
        return self.__name
    
    def get_edad(self):
        return self.__age

persona = Persona("Santiago Joya Blanco",23)
nombre = persona.get_nombre()
edad = persona.get_edad()
print("Aqui accedemos con metodos muy privados getter")
print("Hola mi nombre es", nombre ,"y mi edad es", edad ,"anios")

#SETTERS
class Persona2:#Con metodo privados
    def __init__(self,name,age):
        self._name = name
        self._age = age
    
    def get_nombre(self):
        return self._name
    
    def get_edad(self):
        return self._age
    
    def set_nombre(self,new_name):
        self._name = new_name

persona = Persona2("Santiago Joya Blanco",23)
nombre = persona.get_nombre()
edad = persona.get_edad()
print("\nAqui accedemos con metodos privados setter")
print("Hola mi nombre es", nombre ,"y mi edad es", edad ,"anios")
#SET
persona.set_nombre("Dawin")
nombre_nuevo = persona.get_nombre()
print("Aqui accedemos con metodos privados setter")
print("Hola mi nombre es", nombre_nuevo ,"y mi edad es", edad ,"anios")

class Persona3:#Con metodos muy privados
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    
    def get_nombre(self):
        return self.__name
    
    def set_nombre(self,new_name):
        self.__name = new_name
    
    def get_edad(self):
        return self.__age

persona = Persona3("Santiago Joya Blanco",23)
nombre = persona.get_nombre()
edad = persona.get_edad()
print("\nAqui accedemos con metodos muy privados setter")
print("Hola mi nombre es", nombre ,"y mi edad es", edad ,"anios")
#SET
persona.set_nombre("Wendy")
nombre_nuevo = persona.get_nombre()
print("Aqui accedemos con metodos muy privados setter")
print("Hola mi nombre es", nombre_nuevo ,"y mi edad es", edad ,"anios")

print("\n----------DECORADORES----------")
#Los decoradores en Python son una forma elegante y poderosa de modificar el comportamiento de funciones o métodos 
#sin modificar su código fuente. Se utilizan con el símbolo @ antes del nombre de la función.

#Añadir funcionalidades a funciones o métodos sin modificar su código.
# Reutilización de código, evitando duplicación.
# Mayor legibilidad y organización en el código.
# Ejecutar código antes o después de una función sin cambiar su estructura.

"""Basicamente lo que se realiza es que realizamos una funcionalidad antes y despues de del llamado de la funcion es decir
realizamos mas acciones o funcionalidades en una sola funcion y a eso se le llama decorar la funcion es decir la funcion pricipal
sigue siendo la misma pero se puede agregar una funcionalidad antes o despues...
"""
print("Usando el decorador de manera incorrecta")
def decorador(funcion):#Como tal esta no es la forma de utilizar decorador
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada

def saludo():
    print("Hola Santiago como vamos ?")
    
saludo_modificado = decorador(saludo)#Llamada del decorador
saludo_modificado()

#Forma correcta de utilizar el decorador
print("\nUsando el decorador de manera correcta")
@decorador
def saludo1():
    print("Hola Santiago como vamos ?")
saludo()

print("\n----------DECORADOR PROPERTY----------")
class Persona4:#Con metodo privados
    def __init__(self,name,age):
        self._name = name
        self._age = age
    
    @property
    def nombre(self):#de esta manera ocultamos el nombre verdadero de la varibale _name y no es necesario colocar la variable asi sino
        #sino colocamos nombre y usamos el property
        return self._name
    
    @nombre.setter
    def nombre(self,new_name):
        self._name = new_name
        
    @nombre.deleter
    def nombre(self):
        del self._name
    
    @property
    def edad(self):
        return self._age
    

#GET CON DECORADOR
persona = Persona4("Santiago Joya Blanco",23)
nombre = persona.nombre#La diferencia es que al final ya no le tengo que colocar () ya que estoy usando el @property
#es decir ya no lo uso como una funcion si no como una PROPIEDAD
edad = persona.edad
print("Aqui accedemos con metodos privados getter")
print("Hola mi nombre es", nombre ,"y mi edad es", edad ,"anios")
#SET CON DECORADOR
nombre = persona.nombre = "Dawin valenzuela"
print("Aqui accedemos con metodos privados setter")
print("Hola mi nombre es", nombre ,"y mi edad es", edad ,"anios")
nombre = persona.nombre = "Antonio joya"
print("Aqui accedemos con metodos privados setter")
print("Hola mi nombre es", nombre ,"y mi edad es", edad ,"anios")
#DEL CON DECORADOR
# del persona.nombre
# nombre = persona.nombre#Aqui lo borramos por lo tanto si no quito esa linea me arroja un error debido a que ya se borro el atributo
# print(nombre)