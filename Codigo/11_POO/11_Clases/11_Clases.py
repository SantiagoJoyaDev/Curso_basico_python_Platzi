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

#Biblioteca...
class Book:
    """
    Representa un libro en la biblioteca.
    
    Atributos:
        title (str): Título del libro.
        author (str): Autor del libro.
        available (bool): Indica si el libro está disponible para ser prestado.
    """
    def __init__(self, title, author):
        """
        Inicializa un libro con su título y autor. Por defecto, está disponible.
        
        Parámetros:
            title (str): Título del libro.
            author (str): Autor del libro.
        """
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        """
        Permite prestar el libro si está disponible. Si no lo está, informa al usuario.
        """
        if self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no está disponible")

    def return_book(self):
        """
        Permite devolver un libro prestado, marcándolo nuevamente como disponible.
        """
        self.available = True
        print(f"El libro {self.title} ha sido devuelto")


class User:
    """
    Representa un usuario de la biblioteca.
    
    Atributos:
        name (str): Nombre del usuario.
        user_id (int): Identificador único del usuario.
        borrowed_books (list): Lista de libros que el usuario ha tomado prestados.
    """
    def __init__(self, name, user_id):
        """
        Inicializa un usuario con su nombre y un identificador único.
        
        Parámetros:
            name (str): Nombre del usuario.
            user_id (int): Identificador del usuario.
        """
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Permite al usuario tomar prestado un libro si está disponible.

        Parámetros:
            book (Book): Objeto de tipo Book que el usuario desea tomar prestado.
        """
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} no está disponible")

    def return_book(self, book):
        """
        Permite al usuario devolver un libro que haya tomado prestado.

        Parámetros:
            book (Book): Objeto de tipo Book que el usuario desea devolver.
        """
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} no está en la lista de prestados")


class Library:
    """
    Representa una biblioteca que contiene libros y usuarios.

    Atributos:
        books (list): Lista de libros disponibles en la biblioteca.
        users (list): Lista de usuarios registrados en la biblioteca.
    """
    def __init__(self):
        """
        Inicializa la biblioteca con listas vacías de libros y usuarios.
        """
        self.books = []
        self.users = []
    
    def add_book(self, book):
        """
        Agrega un libro a la colección de la biblioteca.

        Parámetros:
            book (Book): Objeto de tipo Book que se agregará a la biblioteca.
        """
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado")

    def register_user(self, user):
        """
        Registra un usuario en la biblioteca.

        Parámetros:
            user (User): Objeto de tipo User que se registrará en la biblioteca.
        """
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def show_available_books(self):
        """
        Muestra en la consola la lista de libros disponibles en la biblioteca.
        """
        print("Libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.author}")


#Crear los libros
book1 = Book("El principito", "Antoine de Saint-Exupéry")
book2 = Book("1984", "George Orwell")

#Crear usuario
user1 = User("Carli", "001")

#Crear Biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)

#Mostrar libros
library.show_available_books()

#Realizar prestamo
user1.borrow_book(book1)

#Mostrar libros
library.show_available_books()

#Devolver libro
user1.return_book(book1)

#Mostrar libros
library.show_available_books()
 
#Concesionario de carros...
#Realiza un ejercicio en donde se pueda realizar la compra y venta de carros a demas un usuario podra preguntar cuales
#carros estan disponibles
print("\n")
class Car:
    def __init__(self, model, brand, year, price):
        self.model = model
        self.brand = brand
        self.year = year
        self.price = price
        self.available = True  # Estado de disponibilidad del carro

    def sell(self):
        """Marca el carro como vendido si está disponible."""
        if self.available:
            self.available = False
            print(f"El carro {self.model} de la marca {self.brand} del año {self.year} ya ha sido comprado")
        else:
            print(f"El carro {self.model} de la marca {self.brand} del año {self.year} no está disponible")

    def return_car(self):
        """Marca el carro como disponible nuevamente."""
        self.available = True
        print(f"El carro {self.model} de la marca {self.brand} del año {self.year} está de nuevo disponible para la venta")


class User1:
    def __init__(self, name, user_id, balance):
        self.name = name
        self.user_id = user_id
        self.balance = balance  # Saldo del usuario
        self.purchased_cars = []  # Lista de carros comprados

    def buy_car(self, car):
        """Permite al usuario comprar un carro si está disponible y tiene suficiente dinero."""
        if car.available:
            if self.balance >= car.price:
                self.balance -= car.price
                car.sell()
                self.purchased_cars.append(car)
                print(f"{self.name} ha comprado el carro {car.model} por ${car.price}. Saldo restante: ${self.balance}")
            else:
                print(f"{self.name} no tiene suficiente dinero para comprar el carro {car.model}")
        else:
            print(f"El carro {car.model} no está disponible para la venta")

    def sell_car(self, car, dealership):
        """Permite al usuario vender su carro al concesionario."""
        if car in self.purchased_cars:
            self.balance += car.price * 0.8  # Se paga el 80% del precio original al usuario
            car.return_car()
            self.purchased_cars.remove(car)
            dealership.add_car(car)
            print(f"{self.name} ha vendido el carro {car.model} y ha recibido ${car.price * 0.8}. Saldo actual: ${self.balance}")
        else:
            print(f"{self.name} no posee el carro {car.model}")


class Dealership:
    def __init__(self):
        self.cars = []  # Lista de carros en el concesionario
        self.users = []  # Lista de usuarios registrados

    def add_car(self, car):
        """Agrega un carro al concesionario."""
        self.cars.append(car)
        print(f"El carro {car.model} de la marca {car.brand} del año {car.year} ha sido agregado al concesionario por ${car.price}")

    def register_user(self, user):
        """Registra un nuevo usuario en el concesionario."""
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado con un saldo de ${user.balance}")

    def show_available_cars(self):
        """Muestra los carros disponibles para la venta."""
        print("Carros disponibles en el concesionario:")
        available_cars = [car for car in self.cars if car.available]
        if available_cars:
            for car in available_cars:
                print(f"{car.model} de la marca {car.brand} del año {car.year} - Precio: ${car.price}")
        else:
            print("No hay carros disponibles en este momento")


# ----------------------------------
# Ejemplo de uso del concesionario 🚗
# ----------------------------------

# Crear concesionario
concesionario = Dealership()

# Agregar carros
carro1 = Car("Corolla", "Toyota", 2022, 20000)
carro2 = Car("Civic", "Honda", 2023, 25000)
carro3 = Car("Mustang", "Ford", 2021, 40000)

concesionario.add_car(carro1)
concesionario.add_car(carro2)
concesionario.add_car(carro3)

# Registrar usuarios
usuario1 = User1("Carlos", 101, 30000)
usuario2 = User1("Ana", 102, 50000)

concesionario.register_user(usuario1)
concesionario.register_user(usuario2)

# Mostrar carros disponibles antes de la compra
concesionario.show_available_cars()

# Usuario compra un carro
usuario1.buy_car(carro1)  # Carlos compra un Toyota Corolla
usuario2.buy_car(carro3)  # Ana compra un Ford Mustang

# Mostrar carros disponibles después de la compra
concesionario.show_available_cars()

# Usuario vende un carro al concesionario
usuario1.sell_car(carro1, concesionario)  # Carlos vende su Corolla

# Mostrar carros disponibles después de la venta
concesionario.show_available_cars()


