print("Los principios SOLID son un conjunto de cinco principios de diseño de software orientado a objetos que buscan crear sistemas más mantenibles,"
      "escalables y comprensibles. Son:"
      "1. Single Responsibility Principle (SRP): Una clase debe tener una única responsabilidad o razón para cambiar."
      "2. Open/Closed Principle (OCP): Las clases deben estar abiertas para extensión, pero cerradas para modificación."
      "3. Liskov Substitution Principle (LSP): Los objetos de una clase derivada deben poder reemplazar a los de su clase"
      "base sin alterar el comportamiento del programa."
      "4. Interface Segregation Principle (ISP): Una clase no debe estar obligada a implementar interfaces que no utiliza."
      "5. Dependency Inversion Principle (DIP): Las clases deben depender de abstracciones, no de implementaciones concretas.")

# Ejemplo de SRP
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_report(self):
        return f"Report Title: {self.title}\nContent: {self.content}"
#Este código sigue el principio de responsabilidad única (SRP) porque la clase Report tiene una única responsabilidad: generar un informe.
# Si quisiéramos agregar la funcionalidad de enviar el informe por correo electrónico, tendríamos que crear una nueva clase o método 
# para manejar esa responsabilidad.

#Ejemplo de OCP
class Notificater:
      def __init__(self,usuario,mensaje):
          self.usuario = usuario
          self.mensaje = mensaje
      
      def notify(self):
            raise NotImplementedError("Subclasses should implement this method...")# este metodo hace que la clase Notificater sea abstracta y 
      #no se pueda instanciar directamente.         
           
class EmailNotificater(Notificater):
      def notify(self):
            print(f"Enviando correo a {self.usuario} con el mensaje: {self.mensaje}")

class SMSNotificater(Notificater):
      def notify(self):
            print(f"Enviando SMS a {self.usuario} con el mensaje: {self.mensaje}")

#Ejemplo de LSP
# Clase base
class Bird:
    def make_sound(self):
        return "Pío"

# Subclase para aves que vuelan
class FlyingBird(Bird):
    def fly(self):
        return "Estoy volando"

# Subclase para aves que nadan
class SwimmingBird(Bird):
    def swim(self):
        return "Estoy nadando"

# Aves específicas
class Sparrow(FlyingBird):  # Gorrión
    pass

class Eagle(FlyingBird):  # Águila
    pass

class Penguin(SwimmingBird):  # Pingüino
    pass

class Duck(FlyingBird, SwimmingBird):  # Pato, hereda ambas capacidades
    def fly(self):
        return "El pato está volando"

    def swim(self):
        return "El pato está nadando"
#Este código sigue el principio de sustitución de Liskov (LSP) porque las subclases Sparrow, Eagle, Penguin y Duck pueden ser utilizadas
#en lugar de la clase base Bird sin alterar el comportamiento del programa.

ave1 = Sparrow()
print(ave1.make_sound())  # Salida: Pío
print(ave1.fly())  # Salida: Estoy volando
ave2 = Penguin()
print(ave2.make_sound())  # Salida: Pío
print(ave2.swim())  # Salida: Estoy nadando
ave3 = Duck()
print(ave3.make_sound())  # Salida: Pío
print(ave3.fly())  # Salida: El pato está volando
print(ave3.swim())  # Salida: El pato está nadando
print("")

#Ejemplo de ISP
# === Interfaces simples ===

class Printer:
    def print(self, document):
        print(f"[Printer] Imprimiendo: {document}")

class Scanner:
    def scan(self, document):
        print(f"[Scanner] Escaneando: {document}")

class Fax:
    def send_fax(self, document):
        print(f"[Fax] Enviando fax: {document}")


# === Dispositivos concretos ===

class BasicPrinter(Printer):
    pass

class BasicScanner(Scanner):
    pass

class MultiFunctionPrinter(Printer, Scanner):
    pass

class SuperDevice(Printer, Scanner, Fax):
    pass


# === Uso directo ===

# Instanciar dispositivos
impresora = BasicPrinter()
escáner = BasicScanner()
multi = MultiFunctionPrinter()
todo_en_uno = SuperDevice()

# Usarlos directamente
impresora.print("Documento1.pdf")

escáner.scan("Documento2.pdf")

multi.print("Documento3.pdf")
multi.scan("Documento3.pdf")

todo_en_uno.print("Documento4.pdf")
todo_en_uno.scan("Documento4.pdf")
todo_en_uno.send_fax("Documento4.pdf")
print("")

#Este código sigue el principio de segregación de interfaces (ISP) porque las clases Printer y Scanner tienen interfaces separadas y 
#no están obligadas a implementar métodos que no utilizan.

#Ejemplo de DIP
# Clase base
# Abstracción (Interfaz común)
class Database:
    def connect(self):
        raise NotImplementedError("Debe implementarse en la subclase")# eso del raise NotImplementedError hace que la clase Database sea 
  #abstracta y no se pueda instanciar directamente.

# Implementaciones concretas
class MySQLDatabase(Database):
    def connect(self):
        print("Conectando a MySQL...")

class MongoDBDatabase(Database):
    def connect(self):
        print("Conectando a MongoDB...")

# Módulo de alto nivel que depende de la abstracción
class App:
    def __init__(self, database: Database):
        self.database = database

    def start(self):
        print("Iniciando aplicación...")
        self.database.connect()
# Uso
mysql_db = MySQLDatabase()
app = App(mysql_db)
app.start()  # Salida: Iniciando aplicación... Conectando a MySQL...
print("")
mongo_db = MongoDBDatabase()
app = App(mongo_db)
app.start()  # Salida: Iniciando aplicación... Conectando a MongoDB...

#Este código sigue el principio de inversión de dependencias (DIP) porque las clases MySQLDatabase y MongoDBDatabase dependen de la 
#abstracción Database y no de implementaciones concretas. Esto permite cambiar la base de datos sin modificar el código que la utiliza.