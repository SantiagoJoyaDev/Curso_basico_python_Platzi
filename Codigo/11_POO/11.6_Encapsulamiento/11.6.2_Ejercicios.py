print("----------EJERCICIOS DE Encapsulamiento----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: Crear una clase Libro con atributos privados: Atributos: título, autor, año.Crea métodos get para acceder a cada uno."
      "Imprime los datos usando los métodos.")
class Libro:
      def __init__(self,titulo,autor,anio):
            self._titulo = titulo
            self._autor = autor
            self._anio = anio
      
      def get_titulo(self):
            return self._titulo
      
      def get_autor(self):
            return self._autor
      
      def get_anio(self):
            return self._anio

lib = Libro("Satanas","Mario mendoza","2002")
titulo = lib.get_titulo()
autor = lib.get_autor()
anio = lib.get_anio()
print("-----Libro-----")
print("Nombre:",titulo,
      "\nAutor:",autor,
      "\nanio:",anio)           
print("----------FIN----------")

print("Ejercicio 2: Modificar el nombre de un estudiante usando setters: Clase Estudiante con nombre y matrícula.Usa get_nombre()" 
      "y set_nombre().Cambia el nombre e imprime el nuevo.")
class Estudiante:
      def __init__(self,name,enroll):
            self.name = name
            self.enroll = enroll
            
      def get_name(self):
            return self.name
      
      def get_enroll(self):
            return self.enroll
      
      def set_new_name(self,new_name):
            self.name = new_name

estudiante = Estudiante("Santiago Joya Blanco",2500000)
#Get
nombre = estudiante.get_name()
matricula = estudiante.get_enroll()
print("El nombre del estudiante es", nombre ," y el valor de la matricula es", matricula ,"COP")
#SET
estudiante.set_new_name("Diego chavarro beltran")
nuevo_nombre = estudiante.get_name()
print("NUEVO ESTUDIANTE")
print("El nombre del estudiante es", nuevo_nombre ," y el valor de la matricula es", matricula ,"COP")
print("----------FIN----------")

print("Ejercicio 3: Usar decoradores para imprimir antes y después de una función: Crea un decorador"
      "@anuncio que imprima “Inicio” antes y “Fin” después de ejecutar una función presentacion().")
def decorador(funcion):
      def funcion_modificada():
            print("Antes de llamar a la funcion")
            funcion()
            print("Despues de llamar a la funcion")
            print("FIN")
      return funcion_modificada

@decorador
def estados():
      print("INICIO")
estados()
print("----------FIN----------\n")

print("----------EJERCICIOS INTERMEDIO----------")

print("Ejercicio 4: Clase CuentaBancaria con encapsulamiento: Atributos privados: número de cuenta, saldo.Métodos: get_saldo()," 
      "depositar(), retirar().Valida que no se pueda retirar más del saldo.")
class CuentaBancaria:
    def __init__(self, num_cuenta, saldo):
        self._num_cuenta = num_cuenta
        self._saldo = saldo
        
    def get_saldo(self):
        return self._saldo
    
    def depositar(self, cantidad_ingresada):
        if cantidad_ingresada > 0:
            self._saldo = self._saldo + cantidad_ingresada  # Actualizamos el saldo
            print("La cantidad ingresada es:", cantidad_ingresada)
            print("El nuevo saldo es:", self._saldo)
        else:
            print("La cantidad a depositar debe ser mayor a cero.")
    
    def retirar(self, cantidad_retirar):
        if cantidad_retirar <= self._saldo:
            self._saldo = self._saldo - cantidad_retirar  # Restamos del saldo actual
            print("Has retirado:", cantidad_retirar)
            print("Saldo restante:", self._saldo)
        else:
            print("Fondos insuficientes. No puedes retirar esa cantidad.")

# Ejemplo de uso
cuenta = CuentaBancaria(12302345234, 500000)

# Consultar saldo
print("Saldo inicial:", cuenta.get_saldo())

# Depositar dinero
cuenta.depositar(250000)

# Retirar dinero
cuenta.retirar(600000)

# Ver saldo actual
print("Saldo final:", cuenta.get_saldo())
print("----------FIN----------")

print("Ejercicio 5: Usar @property en clase Empleado: Atributos: nombre y salario.Usa @property y @salario.setter"
      "para evitar que el salario sea negativo.Prueba asignar un salario inválido y muestra un mensaje de error.")
class Empleado:
      def __init__(self,nombre,salario):
            self._nombre = nombre
            self._salario = salario
      
      @property
      def nombre(self):
            return self._nombre
      
      @property
      def salario(self):
            return self._salario
      
      @salario.setter
      def salario(self,new_salario):
            self._salario = new_salario

empleado = Empleado("Santiago Joya",-2315000)
nombre = empleado.nombre
salario = empleado.salario
print("Salario negativo")
print("El empleado se llama",nombre,"y el salario es",salario)
#SET
salario = empleado.salario = 23150000
print("Salario positivo")
print("El empleado se llama",nombre,"y el salario es",salario)
print("----------FIN----------")

print("Ejercicio 6: Eliminar un atributo con @deleter: Clase Mascota con atributo nombre.Usa @property, @setter y @deleter."
      "Borra el nombre y verifica que ya no esté disponible.")
class Mascota:
      def __init__(self,nombre):
            self._nombre = nombre
      
      @property
      def nombre(self):
            return self._nombre
      
      @nombre.setter
      def nombre(self,new_nombre):
            self._nombre = new_nombre
            
      @nombre.deleter
      def nombre(self):
            del self._nombre
      
mascota = Mascota("Firulais")
nombre_de_mascota = mascota.nombre
print("Sin modificar")
print("El nombre de la mastoca es",nombre_de_mascota)
#SET
nombre_de_mascota = mascota.nombre = "Fifi"
print("Modificado")
print("El nombre de la mastoca es",nombre_de_mascota)
#DEL
del mascota.nombre
# nombre_de_mascota = mascota.nombre
# print("Borrado")
# # print(nombre_de_mascota) con este metodo verificamos que ya no existe el nombre
print("----------FIN----------")

print("----------EJERCICIOS DIFICIL----------")

print("Ejercicio 7: Sistema de notas con validación: Clase Alumno con nombre y lista de notas (privadas).Métodos para agregar nota,"
      "calcular promedio.Usa setters para asegurarte que las notas estén entre 0 y 5.")
class Alumno:
    def __init__(self, nombre):
        self._nombre = nombre
        self._notas = []  # Lista privada de notas

    # Getter del nombre
    def get_nombre(self):
        return self._nombre

    # Setter del nombre
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # Método para agregar una nota validada (0 a 5)
    def agregar_nota(self, nota):
        if 0 <= nota <= 5:
            self._notas.append(nota)
            print(f"Nota {nota} agregada correctamente.")
        else:
            print(" Error: La nota debe estar entre 0 y 5.")

    # Método para mostrar todas las notas
    def mostrar_notas(self):
        print(f"Estudiante: {self._nombre} Notas: {self._notas}")

    # Método para calcular el promedio
    def calcular_promedio(self):
        if len(self._notas) == 0:
              return "No hay notas registradas"
        promedio = sum(self._notas) / len(self._notas)
        print(f"Promedio de {self._nombre}: {promedio:.2f}")
        return promedio


# ----------------- USO --------------------
alumno = Alumno("Santiago Joya Blanco")

# Intentamos agregar varias notas
alumno.agregar_nota(4.5)
alumno.agregar_nota(3.7)
alumno.agregar_nota(5.0)
alumno.agregar_nota(6.0)  # Esta nota es inválida
alumno.agregar_nota(-1)   # También es inválida

# Mostrar notas y promedio
alumno.mostrar_notas()
alumno.calcular_promedio()
print("----------FIN----------")

print("Ejercicio 8: Registro de usuarios con decoradores de seguridad:Crea un decorador @autenticado que verifique si el usuario" 
      "tiene permiso antes de ejecutar una función.Si no está autenticado, muestra un error.")
# Decorador que verifica si el usuario está autenticado
def autenticado(func):
    def wrapper(usuario, *args, **kwargs):
        if usuario["autenticado"]:
            return func(usuario, *args, **kwargs)
        else:
            print(f"Acceso denegado para el usuario '{usuario['nombre']}'. Debes estar autenticado.")
    return wrapper

# Función protegida por el decorador
@autenticado
def ver_datos_privados(usuario):
    print(f"Bienvenido, {usuario['nombre']}! Aquí están tus datos privados.")

# ------------------- USO -------------------

# Usuario NO autenticado
usuario1 = {"nombre": "Carlos", "autenticado": False}

# Usuario autenticado
usuario2 = {"nombre": "Laura", "autenticado": True}

# Pruebas
ver_datos_privados(usuario1)  # No debería permitir acceso
ver_datos_privados(usuario2)  # Acceso permitido
print("----------FIN----------")

print("Ejercicio 9: Clase Producto con múltiples niveles de privacidad:Atributos: _nombre, __precio, _stock.Usa getters y setters."
      "Crea un método que ajuste el stock solo si hay suficiente en inventario.")
class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre          # Atributo privado
        self.__precio = precio         # Atributo muy privado
        self._stock = stock            # Atributo privado

    # -------- GETTERS ----------
    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self._stock

    # -------- SETTERS ----------
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("El precio no puede ser negativo.")

    def set_stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self._stock = nuevo_stock
        else:
            print("El stock no puede ser negativo.")

    # -------- MÉTODO PARA AJUSTAR STOCK --------
    def vender(self, cantidad):
        if cantidad <= self._stock:
            self._stock -= cantidad #Es lo mismo que self._stock = self._stock - cantidad 
            print(f"Venta realizada: {cantidad} unidades vendidas.")
            print(f"Stock restante: {self._stock}")
        else:
            print(f"No hay suficiente stock. Disponibles: {self._stock} unidades.")

# ------------------- USO -------------------
producto = Producto("Audífonos Bluetooth", 120000, 10)

# Obtener valores
print("Producto:", producto.get_nombre())
print("Precio:", producto.get_precio())
print("Stock:", producto.get_stock())

# Intentar vender unidades
producto.vender(4)   # Stock suficiente
producto.vender(7)   # Stock insuficiente
print("----------FIN----------")

print("Ejercicio 10: Crear una clase PaginaWeb con un atributo privado _visitas. Cada vez que se llama al método visitar()," 
      "el contador aumenta. Usa un getter para mostrar cuántas visitas tiene.")
class PaginaWeb:
    def __init__(self):
        self._visitas = 0

    def visitar(self):
        self._visitas += 1
        print("Visita registrada.")

    def get_visitas(self):
        return self._visitas

# ---------------- USO ----------------
pagina = PaginaWeb()

# Simular visitas
pagina.visitar()
pagina.visitar()
pagina.visitar()

# Mostrar visitas totales
print("Total de visitas:", pagina.get_visitas())
print("----------FIN----------")
