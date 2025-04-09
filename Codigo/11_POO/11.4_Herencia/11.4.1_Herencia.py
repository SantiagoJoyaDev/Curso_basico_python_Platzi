print("----------HERENCIA----------")
#La herencia en programación es un mecanismo que permite a una clase 
# (llamada subclase o clase hija) heredar atributos y métodos de otra clase (llamada superclase o clase padre).
# Esto permite reutilizar código y evitar la duplicación, ya que la subclase puede usar 
# y extender la funcionalidad de la superclase.

#Ejemplo de la herencia simple
class Galleta():
    def __init__(self,harina,huevos,agua):
        self.harina = harina
        self.huevos = huevos
        self.agua = agua
        
class GalletaDeChocolate(Galleta):
    def __init__(self,harina,huevos,agua,chocolate,name):
        super().__init__(harina,huevos,agua)
        self.name = name
        self.chocolate = chocolate
        
class GalletaDeVainilla(Galleta):
    def __init__(self, harina, huevos, agua,vainilla,name):
        super().__init__(harina, huevos, agua)
        self.name = name
        self.vainilla = vainilla
        
class GalletaDePasas(Galleta):
    def __init__(self, harina, huevos, agua,uvas_pasas,name):
        super().__init__(harina, huevos, agua)
        self.name = name
        self.uvas_pasas = uvas_pasas


galleta_general = Galleta("20gr (Arinapan)","20 (Huevos Kikes)","200ml (Agua manantial)")
print(f"La galleta basica es {galleta_general.harina},{galleta_general.huevos} y por ultimo {galleta_general.agua}")

galleta_de_chocolate = GalletaDeChocolate("20gr (Arinapan)","20 (Huevos Kikes)","200ml (Agua manantial",
                                          "5 (tabletas de chocolate)","Galleta de chocolate")
print(f"\nEl nombre de la galleta es {galleta_de_chocolate.name} y los ingredientes son: "
      f"{galleta_de_chocolate.harina}, {galleta_de_chocolate.huevos}, {galleta_de_chocolate.agua}"
      "y por último {galleta_de_chocolate.chocolate}.")


galleta_de_vainilla = GalletaDeVainilla("20gr (Arinapan)","20 (Huevos Kikes)","200ml (Agua manantial",
                                        "5gr (escencia de vainilla)","Galleta de vainilla")
print(f"\nEl nombre de la galleta es {galleta_de_vainilla.name} y los ingredientes son: "
      f"{galleta_de_vainilla.harina}, {galleta_de_vainilla.huevos}, {galleta_de_vainilla.agua}"
      "y por último {galleta_de_vainilla.vainilla}.")

galleta_de_uvas_pasas = GalletaDePasas("20gr (Arinapan)","20 (Huevos Kikes)","200ml (Agua manantial",
                                       "5unid (uvas pasas)","Galleta de uvas pasas")
print(f"\nEl nombre de la galleta es {galleta_de_uvas_pasas.name} y los ingredientes son: "
      f"{galleta_de_uvas_pasas.harina}, {galleta_de_uvas_pasas.huevos}, {galleta_de_uvas_pasas.agua}"
      "y por último {galleta_de_uvas_pasas.uvas_pasas}.")

#Ejemplo de la herencia multiple
class Celular:
    def __init__(self, brand):
        self.brand = brand

    def presentacion(self):
        print("Este iPhone es actualmente el mejor desarrollo de Apple con cámara 4K...")

# Clase con características técnicas
class CaracteristicasTecnicas:
    def __init__(self, camera, storage, port):
        self.camera = camera
        self.storage = storage
        self.port = port

# Clase que añade el color
class Color:
    def __init__(self, color):
        self.color = color

# Herencia múltiple: esta clase hereda de Celular, CaracteristicasTecnicas y Color
class CelularAvanzado(Celular, CaracteristicasTecnicas, Color):
    def __init__(self, brand, camera, storage, port, color, model):
        Celular.__init__(self, brand)
        CaracteristicasTecnicas.__init__(self, camera, storage, port)
        Color.__init__(self, color)
        self.model = model

    def mostrar_info(self):
        print("\n=== Información del Celular ===")
        print(f"Marca: {self.brand}")
        print(f"Modelo: {self.model}")
        print(f"Cámara: {self.camera}")
        print(f"Almacenamiento: {self.storage}")
        print(f"Puerto: {self.port}")
        print(f"Color: {self.color}")

# Crear una instancia(objeto)
celular = CelularAvanzado(brand="iPhone",camera="238 Mpx",storage="512 GB",port="Lightning",color="Blanco perla",model="15 Pro Max")

# Mostrar información
celular.mostrar_info()
celular.presentacion()

class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def impresion_datos(self):
        print("Hola, mi nombre es", self.name, "y tengo", self.age, "años.")

# Clase separada que maneja los datos académicos
class Academico:
    def __init__(self, grade):
        self.grade = grade

    def impresion_grado(self):
        print("Además, estoy en grado", self.grade, "en el colegio.")

# Herencia múltiple: combina Persona y Academico
class Estudiante(Persona, Academico):
    def __init__(self, name, age, grade):
        Persona.__init__(self, name, age)
        Academico.__init__(self, grade)

# Crear un estudiante
estudiante = Estudiante("Santiago", "23", 11)

# Usar métodos de ambas clases base
estudiante.impresion_datos()
estudiante.impresion_grado()
