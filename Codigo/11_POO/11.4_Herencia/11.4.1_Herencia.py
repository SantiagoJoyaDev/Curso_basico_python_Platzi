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
    def __init__(self,brand):
        self.brand = brand
        
    def presentacion(self):
        print("Este iphone es actualmente el mejor desarrollo de parte de Apple debido a su gran capacidad para tomar fotos en 4K....")

class Celular1(Celular):# Herencia simple
    def __init__(self,brand,camera,storage,port):
        super().__init__(brand)
        self.camera = camera
        self.storage = storage
        self.port = port

class Celular2(Celular1):# Herencia multiple
    """Clase que añade el atributo 'color' al celular."""
    def __init__(self, brand, camera, storage, port, color):
        super().__init__(brand, camera, storage, port)
        self.color = color
        
class Celular3(Celular):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model
    

celular = Celular("Iphone")
print(f"\nLa marca del celular es: {celular.brand}")

celular1 = Celular1("iPhone 15 Pro Max", "238 Mpx", "512 GB", "lightning")
print("\nLas características del celular son:")
print(f"- Brand: {celular1.brand}")
print(f"- Camera: {celular1.camera}")
print(f"- Storage: {celular1.storage}")
print(f"- Port: {celular1.port}")

celular2 = Celular2("iPhone 15 Pro Max", "238 Mpx", "512 GB", "lightning","Blanco perla")
print("\nLas características del celular son:")
print(f"- Brand: {celular2.brand}")
print(f"- Camera: {celular2.camera}")
print(f"- Storage: {celular2.storage}")
print(f"- Port: {celular2.port}")
print(f"- Port: {celular2.color}")
celular2.presentacion()

celular3 = Celular3("Iphone 16 pro max","2025")
print(f"El modelo del celular es: {celular3.brand} -- {celular3.model}")
celular3.presentacion()

class Persona:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def impresion_datos(self):
        print("Hola mi nombre es", self.name ,"y tengo ", self.age ," anios")
        
class Estudiante(Persona):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
    
    def impresion_grado(self):
        print("A demas estoy en grado",self.grade,"en el colegio")
        
estudiante = Estudiante("Santiago","23",11)
estudiante.impresion_datos()
estudiante.impresion_grado()