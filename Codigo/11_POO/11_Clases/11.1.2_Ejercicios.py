print("----------EJERCICIOS DE CLASES----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Crea una clase Persona con los atributos nombre y edad. Luego, instancia un objeto y muestra sus atributos.")
class MyPersona:
    def __init__(self):
        self.name = "Santiago Joya"
        self.edad = 23

my_persona = MyPersona()
print(f"Hola mi nombre es {my_persona.name} y tengo {my_persona.edad} años.")
        
print("----------FIN----------")

print("Ejercicio 2: Crea una clase Coche con atributos marca, modelo y color. Inicializa color por defecto en 'Blanco'.")
class MyCoche:
    def __init__(self, marca, modelo, color = "Blanco"):
        self.marca = marca
        self.modelo = modelo
        self.color = color

my_coche = MyCoche("Lamborghini", "Zentorno")
print(f"La marca del coche es: {my_coche.marca}")
print(f"El modelo del coche es: {my_coche.modelo}")
print(f"El color del coche es: {my_coche.color}")
print("----------FIN----------")

print("Ejercicio 3: Crea una clase Perro con atributos nombre y raza y un método ladrar().")
class MyPerro:
    def __init__(self):
        self.nombre = "Zeus"
        self.raza = "Golden retriever"
    
    def ladrar(self):
        print(f"El perro {self.nombre} de raza {self.raza} esta ladrando demasiado y no deja dormir a los vecinos...")

my_perro = MyPerro()
my_perro.ladrar()
print("----------FIN----------\n")

print("----------EJERCICIOS INTERMEDIO----------")

print("Ejercicio 4: Crea una clase Estudiante con atributos nombre, notas (lista) y un método promedio().")
class MyPromedio:
    def __init__(self,nombre,notas):
        self.nombre = nombre
        self.notas = notas
    
    def promedio(self):
        return sum(self.notas) / len(self.notas)
        
my_estudiante = MyPromedio("Santiago Joya", [5.0,3.2,4.6,5.0,4.0])
print(f"El promedio del estudiante {my_estudiante.nombre} es: {my_estudiante.promedio()}")

print("----------FIN----------")

print("Ejercicio 5: Crea una clase CuentaBancaria con métodos para depositar y retirar dinero.")
class MyCuentaBancaria:
    def __init__(self,titular,saldo = 0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self,cantidad):
        depositar = self.saldo + cantidad
        print(f"Se realizo un deposito de {cantidad}.El saldo de la cuenta es de {depositar} ")
        
    def retirar(self,cantidad):
        if cantidad <= self.saldo:
            retirar = self.saldo - cantidad
            print(f"Se retiro el valor de {cantidad} .El saldo de la cuenta es de {retirar} ")
        else:
            print("Fondos insuficientes...")
        
my_cuenta_bancaria = MyCuentaBancaria("Santiago Joya", 2000000)
my_cuenta_bancaria.depositar(600000)
my_cuenta_bancaria.retirar(1000000)

#opcion #2
# class MyCuentaBancaria:
#     def __init__(self, titular, saldo=0):
#         self.titular = titular
#         self.saldo = saldo
    
#     def operaciones_bancarias(self, cantidad):
#         opcion = int(input("Digite 1 para depositar o 2 para retirar: "))

#         if opcion == 1:
#             self.saldo += cantidad
#             print(f"Se realizó un depósito de {cantidad}. El saldo de la cuenta es de {self.saldo}.")
        
#         elif opcion == 2:
#             if cantidad <= self.saldo:
#                 self.saldo -= cantidad
#                 print(f"Se retiró el valor de {cantidad}. El saldo de la cuenta es de {self.saldo}.")
#             else:
#                 print("Fondos insuficientes...")
        
#         else:
#             print("Opción inválida, intente nuevamente.")

# my_cuenta_bancaria = MyCuentaBancaria("Santiago Joya", 1000000)
# my_cuenta_bancaria.operaciones_bancarias(600000)
# my_cuenta_bancaria.operaciones_bancarias(600000)

print("----------FIN----------")

print("Ejercicio 6: Crea una clase Empleado con nombre y salario. Luego, crea una subclase Gerente con un atributo adicional departamento.")
class Empleado:
    def __init__(self,nombre,salario):
        self.nombre = nombre
        self.salario = salario
        
class Gerente(Empleado):#Aqui estoy utilizando la herencia de las clases en donde uso la clase anterior Empleado
    def __init__(self, nombre, salario,departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

datos = Gerente("Santiago Joya", 2200000, "Santander")
print(f"El usuario se llama {datos.nombre}, tiene un salario de {datos.salario} y por ultimo es del departamento de {datos.departamento}")
        
print("----------FIN----------\n")

print("----------EJERCICIOS DIFICL----------")
print("Ejercicio 7: Crea una clase Vehiculo y subclases Coche y Moto.")
class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        
class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        print(f"La marca del carro es {self.marca} y el modelo es {self.modelo}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        print(f"La marca de la moto es {self.marca} y el modelo es {self.modelo}")
        
carro = Coche("Ferrari", "WER-234 - 2025")
moto = Moto("Susuki", "234-WER - 2020")

print("----------FIN----------")

print("Ejercicio 8: Crea una clase Libro y usa __str__() para representar su información.")
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} de {self.autor}"

libro_1 = Libro("Cien años de soledad", "Gabriel García Márquez")
print(libro_1)

print("----------FIN----------")

print("Ejercicio 9: Crea una clase que cuente cuántas instancias han sido creadas.")
class Contador:
    instancias = 0

    def __init__(self):
        Contador.instancias += 1

a = Contador()
b = Contador()
c = Contador()
print(f"Instancias creadas: {Contador.instancias}")

print("----------FIN----------")
 
print("Ejercicio 10: Crea una clase Producto con atributos nombre, precio y un método que aplique un descuento.")
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * porcentaje / 100
        precio_final = self.precio - descuento
        print("El descuento es de", descuento)
        print("El precio final de el producto es de", precio_final)

producto1 = Producto("Laptop", 1000000)
producto1.aplicar_descuento(10)
print(f"Nombre de prodcuto: {producto1.nombre} valor sin el decuento del prodcuto: {producto1.precio}")

print("----------FIN----------")