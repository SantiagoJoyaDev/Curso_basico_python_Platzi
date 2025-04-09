print("----------EJERCICIOS DE POLIMORFISMO----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Crea una clase base Figura con un método area()," 
      "y dos clases derivadas Cuadrado y Círculo que implementen el método según su fórmula.")#Polimorfismo de herencia
class BaseFigura:
    def area(self):
        return "El área de la figura es:"

class Cuadrado(BaseFigura):
    def __init__(self, l):
        self.l = l

    def area(self):
        area_del_cuadrado = self.l ** 2
        return f"Área del cuadrado: {area_del_cuadrado}"

class Circulo(BaseFigura):
    def __init__(self, r):
        self.r = r
        self.pi = 3.1416

    def area(self):
        area_del_circulo = self.pi * self.r ** 2
        return f"Área del círculo: {area_del_circulo}"

texto = BaseFigura()
cuadrado = Cuadrado(5)
print(texto.area())
print(cuadrado.area())

circulo = Circulo(4)
print(texto.area())
print(circulo.area())

print("----------FIN----------")

print("Ejercicio 2: Crea una clase base Animal con un método hacer_sonido(). Luego"
      "define clases Gato y Vaca que sobrescriban este método con su propio sonido.")#Polimorfismo de herencia
class Animal:
    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

perro = Perro()
gato = Gato()
animal = Animal()

print(perro.hacer_sonido())
print(gato.hacer_sonido())
print(animal.hacer_sonido())
print("----------FIN----------")

print("Ejercicio 3: Crea una clase Vehiculo con un método mover(). Luego,"
      "define clases Carro y Bicicleta que sobrescriban mover() con un comportamiento distinto.")#Polimorfismo de herencia
class Vehiculo:
      def mover(self):
            return "El vehiculo es:"

class Carro(Vehiculo):
      def mover(self):
            return "Carro --> Mazda Mustang -- 234-ASS se mueve hacia adelante"
      
class Moto(Vehiculo):
      def mover(self):
            return "Moto --> XTZ-- 344-4RS se mueve hacia atras"
      
vehiculo = Vehiculo()
carro = Carro()
moto = Moto()

print(vehiculo.mover())
print(carro.mover())

print(vehiculo.mover())
print(moto.mover())
print("----------FIN----------\n")

print("----------EJERCICIOS INTERMEDIO----------")

print("Ejercicio 4: Crea dos clases Guitarra y Piano, ambas con un método tocar(). Luego,"
      "usa Duck Typing en una función que reciba cualquier objeto con tocar().")#DUCK TYPING 
class Guitarra:
      def tocar(self):
            return "Esto es una guitarra"
      
class Piano:
      def tocar(self):
            return "Esto es un piano"

def instrumento(objeto):
      print(objeto.tocar())
      
instrumento(Guitarra())
instrumento(Piano())
print("----------FIN----------")

print("Ejercicio 5: Crea una clase Calculadora con un método multiplicar(), que funcione con 2 o 3 parámetros.")#Polimorfismo de inclusion
class Calculadora:
      def multiplicar(self,a,b=1,c=1,d=1):#se iguala a 1 porque es una multiplicacion
            multiplicacion = a*b*c*d
            return "El resultado de la multiplicacion es:",multiplicacion

multiplicar = Calculadora()
print(multiplicar.multiplicar(2,4,6,7))
print(multiplicar.multiplicar(2,4,6))
print(multiplicar.multiplicar(2,4))#Aqui el valor del 1 se sobreescribe al valor que se ingrese
print("----------FIN----------")

print("Ejercicio 6: Crea una clase base Empleado con un método calcular_salario(). Luego," 
      "define Gerente y Obrero, cada uno con su propia lógica de salario.")
class Empleado:
    def __init__(self, ingresos_netos, gastos_netos):
        self.ingresos_netos = ingresos_netos
        self.gastos_netos = gastos_netos

    def calcular_salario(self):
        sal_general = self.ingresos_netos - self.gastos_netos
        return sal_general

class Gerente(Empleado):
    def __init__(self, ingresos_netos,gastos_netos,gastos_pension, gastos_salud):
        super().__init__(ingresos_netos,gastos_netos)#Es necesario como tal heredad todo pero como tal no 
        #estoy usando todo solo ingresos_netos
        self.gastos_pension = gastos_pension
        self.gastos_salud = gastos_salud

    def calcular_salario(self):
        sal_gerente = self.ingresos_netos - self.gastos_pension - self.gastos_salud
        return sal_gerente

class Obrero(Empleado):
    def __init__(self, ingresos_netos, gastos_netos, gastos_pension, gastos_salud):
        super().__init__(ingresos_netos, gastos_netos)
        self.gastos_pension = gastos_pension
        self.gastos_salud = gastos_salud

    def calcular_salario(self):
        sal_obrero = self.ingresos_netos - self.gastos_pension - self.gastos_salud
        return sal_obrero

salario_general = Empleado(2315000,950000)
salario_gerente = Gerente(5000000,2300000,1150000,1150000)
salario_obrero = Obrero(1500000,650000,325000,325000)

print("El salario general es ",salario_general.calcular_salario())
print("El salario del gerente es ",salario_gerente.calcular_salario())
print("El salario del obrero es ",salario_obrero.calcular_salario())
print("----------FIN----------\n")

print("----------EJERCICIOS DIFICIL----------")
print("Ejercicio 7: Crea Perro, Gato y Robot con hacer_sonido(). Usa Duck Typing para permitir que cualquier" 
      "objeto con hacer_sonido() funcione.")#DUCK TYPING 
class Perro1:
      def hacer_sonido(self):
            return "EL sonido del perro es --> Gua Gua Gua Gua"
      
class Gato1:
      def hacer_sonido(self):
            return "EL sonido del gato es --> Miau Miau Miau Miau"
      
class Robot:
      def hacer_sonido(self):
            return "EL sonido del robot es --> beep beep beep beep"
      
def sonidos(objeto):
      print(objeto.hacer_sonido())

sonidos(Perro1())
sonidos(Gato1())
sonidos(Robot())

print("----------FIN----------")

print("Ejercicio 8: Crea una clase base Archivo con leer(), y clases PDF y Word que sobrescriban leer().")
class Archivo:
      def leer(self):
            return "Estoy leyendo un archivo..."

class Pdf(Archivo):
      def leer(self):
            return "Estoy leyendo un archivo en PDF..."
            
class Word(Archivo):
      def leer(self):
            return "Estoy leyendo un archivo en WORD..."
            
archivo_general = Archivo()
archivo_pdf = Pdf()
archivo_word = Word()

print(archivo_general.leer())
print(archivo_pdf.leer())
print(archivo_word.leer())
print("----------FIN----------")

print("Ejercicio 9: Crea una clase Pago con procesar_pago(). Luego, crea TarjetaCredito y PayPal con su propia lógica de pago.")
class Pago:
    def __init__(self, costo_servicio, monto_usuario):
        self.costo_servicio = costo_servicio
        self.monto_usuario = monto_usuario

    def calcular_pago(self):
        return self.monto_usuario - self.costo_servicio

class TarjetaDeCredito(Pago):
    def __init__(self, costo_servicio, monto_usuario):
        super().__init__(costo_servicio, monto_usuario)
        self.impuesto = 0.2

    def calcular_servicio(self):
        imp = self.costo_servicio * self.impuesto
        return imp

    def calcular_total_con_impuesto(self):
        return self.costo_servicio + self.calcular_servicio()
    
    def calcular_monto_retante_usuario(self):
        imp = self.calcular_servicio()
        mont_final = self.monto_usuario - self.costo_servicio - imp
        return mont_final

class Paypal(Pago):
    def __init__(self, costo_servicio, monto_usuario):
        super().__init__(costo_servicio, monto_usuario)
        self.impuesto = 0.5

    def calcular_servicio(self):
        imp = self.costo_servicio * self.impuesto
        return imp

    def calcular_total_con_impuesto(self):
        return self.costo_servicio + self.calcular_servicio()
    
    def calcular_monto_retante_usuario(self):
        imp = self.calcular_servicio()
        mont_final = self.monto_usuario - self.costo_servicio - imp
        return mont_final

# Menú principal
print("Bienvenido al sistema de pagos de la plataforma de Disney+\n"
      "Ingrese 1 para pago con Tarjeta (Impuesto del 0.2)\n"
      "Ingrese 2 para pago con Paypal (Impuesto del 0.5)")

opcion = int(input("Ingrese la opción: "))

if opcion == 1:
    monto = float(input("Ingrese el monto del usuario: "))
    cost_servicio = float(input("Ingrese el costo del servicio: "))
    tarjeta = TarjetaDeCredito(cost_servicio, monto)
    impuesto = tarjeta.calcular_servicio()
    total_servicio = tarjeta.calcular_total_con_impuesto()
    restante = tarjeta.calcular_monto_retante_usuario()

    print("\n------ FACTURA DISNEY+ ------")
    print(f"Monto del usuario: ${monto:.2f}")
    print(f"Costo del servicio: ${cost_servicio:.2f}")
    print(f"Impuesto aplicado (20%): ${impuesto:.2f}")
    print(f"Total a pagar: ${total_servicio:.2f}")
    print(f"Saldo restante del usuario: ${restante:.2f}")
    print("-----------------------------")

elif opcion == 2:
    monto = float(input("Ingrese el monto del usuario: "))
    cost_servicio = float(input("Ingrese el costo del servicio: "))
    paypal = Paypal(cost_servicio, monto)
    impuesto = paypal.calcular_servicio()
    total_servicio = paypal.calcular_total_con_impuesto()
    restante = paypal.calcular_monto_retante_usuario()

    print("\n------ FACTURA DISNEY+ ------")
    print(f"Monto del usuario: ${monto:.2f}")
    print(f"Costo del servicio: ${cost_servicio:.2f}")
    print(f"Impuesto aplicado (50%): ${impuesto:.2f}")
    print(f"Total a pagar: ${total_servicio:.2f}")
    print(f"Saldo restante del usuario: ${restante:.2f}")
    print("-----------------------------")

else:
    print("Selecciona una opción válida.")
print("----------FIN----------")

print("Ejercicio 10: Crea Auto, Moto y Bicicleta, todos con acelerar(). Usa Duck Typing en una función para llamarlo"
      "sin importar el tipo de vehículo.")
class Auto1:
      def acelerar(self):
            return "Soy un carro ran ran ran"
      
class Moto1:
      def acelerar(self):
            return "Soy una moto run run run"
      
class Bicicleta1:
      def acelerar(self):
            return "Soy una bicicleta rin rin rin"
      
def sonidos1(objeto):
      print(objeto.acelerar())
      
sonidos1(Auto1())
sonidos1(Moto1())
sonidos1(Bicicleta1())
print("----------FIN----------")
