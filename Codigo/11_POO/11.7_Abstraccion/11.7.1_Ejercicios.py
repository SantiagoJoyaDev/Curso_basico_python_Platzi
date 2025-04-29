from abc import ABC, abstractmethod
print("----------EJERCICIOS DE Encapsulamiento----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Crea una clase abstracta Animal con un método abstracto hacer_sonido(). Luego crea dos clases hijas (Perro y Gato)" 
      "que implementen ese método.")
class Animal(ABC):
      def __init__(self,nombre,raza,color_pelo):
            self.nombre = nombre
            self.raza = raza
            self.color_pelo = color_pelo
      
      @abstractmethod
      def tipo_de_animal(self):
            pass
      
      def presentacion_del_animal(self):
            print(f"el nombre del animal {self.nombre} la raza es {self.raza} el color de pelo es {self.color_pelo}")
      
class Perro(Animal):
      def __init__(self, nombre, raza, color_pelo,tipo):
            super().__init__(nombre, raza, color_pelo)
            self.tipo = tipo
            
      def tipo_de_animal(self):
            print(f"El tipo de animal es un {self.tipo}")

class Gato(Animal):
      def __init__(self, nombre, raza, color_pelo,tipo):
            super().__init__(nombre, raza, color_pelo)
            self.tipo = tipo
            
      def tipo_de_animal(self):
            print(f"El tipo de animal es un {self.tipo}")
      
perro = Perro("Pluto","Golden retriever","Crema dorado","Perro")
perro.tipo_de_animal()
perro.presentacion_del_animal()

gato = Gato("morfeo","Persa","Negro","Gato")
gato.tipo_de_animal()
gato.presentacion_del_animal()

print("----------FIN----------")

print("Ejercicio 2: Crea una clase abstracta Forma con un método abstracto area(). Crea dos clases concretas: Cuadrado (con lado) y Círculo"
      "(con radio) que calculen el área.")

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

    def presentacion_del_area(self):
        print(f"El área de la figura es:")

class Cuadrado(Figura):
      def __init__(self, lado,tipo):
            self.lado = lado
            self.tipo = tipo
            
      def area(self):
            return self.lado ** 2
      
      def tipo_de_figura(self):
            print(f"Y la figura es: {self.tipo}")
      
class Circulo(Figura):
      def __init__(self,radio,tipo,pi=3.1416):
            self.radio = radio
            self.pi = pi
            self.tipo = tipo
            
      def area(self):
            return self.pi * (self.radio ** 2)
      
      def tipo_de_figura(self):
            print(f"Y la figura es: {self.tipo}")


cuadrado = Cuadrado(5,"Cuadrado")
circulo = Circulo(3,"Circulo")

cuadrado.presentacion_del_area()
print(cuadrado.area())
cuadrado.tipo_de_figura()

circulo.presentacion_del_area()
print(circulo.area())
circulo.tipo_de_figura()

print("----------FIN----------\n")

print("Ejercicio 3: Crea una clase abstracta Vehiculo con un método abstracto mover(). Implementa dos clases hijas: Auto y Bicicleta que" 
      "digan cómo se mueven.")

class Vehiculo1(ABC):
    @abstractmethod
    def mover(self):
        pass

class Auto1(Vehiculo1):
    def mover(self):
        print("El auto se mueve usando un motor.")

class Bicicleta(Vehiculo1):
    def mover(self):
        print("La bicicleta se mueve pedaleando.")


auto = Auto1()
bicicleta = Bicicleta()

auto.mover()
bicicleta.mover()

print("----------FIN----------\n")

print("----------EJERCICIOS INTERMEDIO----------")

print("Ejercicio 4: Crea una clase abstracta Modelo con: una propiedad abstracta tabla,un método abstracto guardar(),un método de clase" 
      "buscar_por_id() que imprima la tabla y el ID Crea una subclase Usuario que defina tabla = 'usuarios' y un método guardar()" 
      "que imprima 'Guardando usuario'.")

class Modelo(ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(cls, _id):
        print(f"Buscando en la tabla '{cls.tabla}' el ID {_id}")


class Usuario(Modelo):
    tabla = "Santiago"

    def guardar(self):
        print("Guardando usuario")

# Crear instancia de Usuario
usuario = Usuario()
usuario.guardar()

# Buscar por ID
Usuario.buscar_por_id(123)

print("----------FIN----------")

print("Ejercicio 5: Crea una clase abstracta Empleado con: un método abstracto calcular_salario(),una propiedad abstracta cargo"
      "Crea clases hijas: Desarrollador y Gerente con diferentes formas de calcular salario y definir cargo.")
class Empleado(ABC):
    @property
    @abstractmethod
    def cargo(self):
        pass

    @abstractmethod
    def calcular_salario(self):
        pass

class Desarrollador(Empleado):
    def __init__(self, sueldo_base, proyectos):
        self.sueldo_base = sueldo_base
        self.proyectos = proyectos

    @property
    def cargo(self):
        return "Desarrollador"

    def calcular_salario(self):
        # Cada proyecto aumenta el salario en 500
        salario = self.sueldo_base + (self.proyectos * 500)
        print(f"Salario de {self.cargo}: {salario}")

class Gerente(Empleado):
    def __init__(self, sueldo_base, bonus):
        self.sueldo_base = sueldo_base
        self.bonus = bonus

    @property
    def cargo(self):
        return "Gerente"

    def calcular_salario(self):
        # El salario es base más un bono adicional
        salario = self.sueldo_base + self.bonus
        print(f"Salario de {self.cargo}: {salario}")


dev = Desarrollador(3000, 3)
ger = Gerente(5000, 2000)

dev.calcular_salario()
ger.calcular_salario()

print("----------FIN----------")

print("Ejercicio 6: Clase abstracta Dispositivo con métodos: encender() y apagar() (abstractos) propiedad modelo (abstracta)"
      "Implementa Smartphone y Laptop.")

class Dispositivo(ABC):
      @abstractmethod
      def enceder(self):
            pass
      
      @abstractmethod
      def apagar(self):
            pass
      
      @property
      @abstractmethod
      def modelo(self):
            pass

class Smartphone:
      @property
      def modelo(self):
            return "Iphone 16 pro max"
      
      def encender(self):
            print(f"El Smartphone {self.modelo} esta encendido...")
            
      def apagar(self):
            print(f"El Smartphone {self.modelo} esta apagado...")
            
class Laptop:
      @property
      def modelo(self):
            return "Ipad super pro Apple"
      
      def encender(self):
            print(f"El Smartphone {self.modelo} esta encendido...")
            
      def apagar(self):
            print(f"El Smartphone {self.modelo} esta apagado...")
      
smartphone = Smartphone()
laptop = Laptop()

smartphone.encender()
smartphone.apagar()
laptop.encender()
laptop.apagar()

print("----------FIN----------")

print("----------EJERCICIOS DIFICIL----------")

print("Ejercicio 7: Crea una clase abstracta Archivo con métodos abstractos abrir(), cerrar() y una propiedad tipo."
      "Implementa ArchivoTexto y ArchivoImagen. Luego crea una función que recorra una lista de archivos y los abra/cierre dinámicamente.")

class Archivo(ABC):
      @abstractmethod
      def abrir(self):
            pass
      
      def cerrar(self):
            pass
      
      @property
      @abstractmethod
      def tipo(self):
            pass
      
class ArchivoTexto(Archivo):
      def __init__(self,nombre):
            self.nombre = nombre
               
      @property
      def tipo(self):
            return "TEXTO"
      
      def abrir(self):
            print(f"EL archivo de {self.tipo} se esta abriendo.....")
            
      def cerrar(self):
            print(f"EL archivo de {self.tipo} se esta cerrando.....")
            
class ArchivoImagen(Archivo):
      def __init__(self,nombre):
            self.nombre = nombre
            
      @property
      def tipo(self):
            return "IMAGEN"
      
      def abrir(self):
            print(f"EL archivo de {self.tipo} se esta abriendo.....")
            
      def cerrar(self):
            print(f"EL archivo de {self.tipo} se esta cerrando.....")

def apertura_y_cerrado(lista_archivos):
      for archivo in lista_archivos:
            archivo.abrir()
            archivo.cerrar()

archivo1 = ArchivoTexto("documento.txt")
archivo2 = ArchivoImagen("foto.png")

archivos = [archivo1,archivo2]
apertura_y_cerrado(archivos)
            
print("----------FIN----------")

print("Ejercicio 8: Crea una clase abstracta Plugin con: método de clase abstracto cargar(),método abstracto ejecutar(),"
      "Implementa dos plugins (PluginA, PluginB) y una clase Sistema que los instancie dinámicamente a partir de sus nombres.")

class Plugin(ABC):
      @classmethod
      @abstractmethod
      def cargar(cls):
            pass
      
      @abstractmethod
      def ejecutar(self):
            pass

class PluginA(Plugin):
    @classmethod
    def cargar(cls):
        print("Cargando Plugin A")
        return cls()

    def ejecutar(self):
        print("Ejecutando Plugin A")

# PluginB
class PluginB(Plugin):
    @classmethod
    def cargar(cls):
        print("Cargando Plugin B")
        return cls()

    def ejecutar(self):
        print("Ejecutando Plugin B")

# Clase Sistema que carga plugins dinámicamente
class Sistema:
    def __init__(self):
        self.plugins = []

    def cargar_plugin(self, nombre_plugin):
        # Buscar la clase por nombre y cargarla
        if nombre_plugin == "PluginA":
            plugin = PluginA.cargar()
        elif nombre_plugin == "PluginB":
            plugin = PluginB.cargar()
        else:
            print(f"No existe el plugin {nombre_plugin}")
            return
        
        self.plugins.append(plugin)

    def ejecutar_plugins(self):
        for plugin in self.plugins:
            plugin.ejecutar()

# Uso
sistema = Sistema()
sistema.cargar_plugin("PluginA")
sistema.cargar_plugin("PluginB")
sistema.ejecutar_plugins()

print("----------FIN----------")

print("Ejercicio 9: Clase abstracta Reporte con: propiedad abstracta tipo,método abstracto generar(),Crea ReportePDF y ReporteExcel."
      "Luego haz una función que reciba una lista de reportes y los genere según su tipo.")
class Reporte(ABC):
      @property
      @abstractmethod
      def tipo(self):
            pass
      
      @abstractmethod
      def generar(self):
            pass

class ReportePDF(Reporte):
      @property
      def tipo(self):
            return "PDF"
      
      def generar(self):
            print(f"Generando reporte en formato {self.tipo}")

class ReporteExcel(Reporte):
      @property
      def tipo(self):
            return "EXCEL"
      
      def generar(self):
            print(f"Generando reporte en formato {self.tipo}")

def generaer_reportes(lista_reportes):
      for reporte in lista_reportes:
            reporte.generar()

reportes = [ReportePDF(), ReporteExcel()]
generaer_reportes(reportes)

print("----------FIN----------")

print("Ejercicio 10: Clase abstracta Vehiculo con: método abstracto fabricar(),Clase abstracta FabricaVehiculos con: método de clase abstracto" 
      "crear_vehiculo()Implementa subclases como Auto y Moto con sus fábricas respectivas.")
class Vehiculo(ABC):
      @abstractmethod
      def fabricar(self):
            pass

class FabricaVehiculos(ABC):
      @classmethod
      @abstractmethod
      def crear_vehiculo(cls):
            pass

class Auto(Vehiculo):
      def fabricar(self):
            print("Fabricando un auto")
      
      @classmethod
      def crear_vehiculo(cls):
            print("Creando un auto")
            return cls()
      
class Moto(Vehiculo):
      def fabricar(self):
            print("Fabricando una Moto")
      
      @classmethod
      def crear_vehiculo(cls):
            print("Creando una Moto")
            return cls()

auto = Auto.crear_vehiculo()
moto = Moto.crear_vehiculo()
auto.fabricar()
moto.fabricar()

print("----------FIN----------")
