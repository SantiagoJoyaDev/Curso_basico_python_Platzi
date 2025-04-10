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

print("----------FIN----------\n")

print("----------EJERCICIOS INTERMEDIO----------")

print("Ejercicio 4: Clase CuentaBancaria con encapsulamiento: Atributos privados: número de cuenta, saldo.Métodos: get_saldo()," 
      "depositar(), retirar().Valida que no se pueda retirar más del saldo.")

print("----------FIN----------")

print("Ejercicio 5: Usar @property en clase Empleado: Atributos: nombre y salario.Usa @property y @salario.setter"
      "para evitar que el salario sea negativo.Prueba asignar un salario inválido y muestra un mensaje de error.")

print("----------FIN----------")

print("Ejercicio 6: Eliminar un atributo con @deleter: Clase Mascota con atributo nombre.Usa @property, @setter y @deleter."
      "Borra el nombre y verifica que ya no esté disponible.")

print("----------FIN----------")

print("----------EJERCICIOS DIFICIL----------")

print("Ejercicio 7: Sistema de notas con validación: Clase Alumno con nombre y lista de notas (privadas).Métodos para agregar nota,"
      "calcular promedio.Usa setters para asegurarte que las notas estén entre 0 y 5.")

print("----------FIN----------")

print("Ejercicio 8: Registro de usuarios con decoradores de seguridad:Crea un decorador @autenticado que verifique si el usuario" 
      "tiene permiso antes de ejecutar una función.Si no está autenticado, muestra un error.")

print("----------FIN----------")

print("Ejercicio 9: Clase Producto con múltiples niveles de privacidad:Atributos: _nombre, __precio, _stock.Usa getters y setters."
      "Crea un método que ajuste el stock solo si hay suficiente en inventario.")

print("----------FIN----------")

print("Ejercicio 10: Logger decorador que registre el uso de funciones:Crea un decorador @logger que guarde en un archivo de" 
      "texto cada vez que una función es ejecutada (nombre, hora, argumentos).Aplícalo a una función como comprar_producto().")

print("----------FIN----------")
