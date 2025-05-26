print("----------EJERCICIOS DE PRINCIPIOS SOLID----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: [SRP] Crea una clase Tarea con los atributos titulo y estado. Agrega un método para marcarla como completada y" 
      "otra clase separada para mostrarla en consola o HTML.")
class Tarea:
      def __init__(self,titulo,estado):
            self.titulo = titulo
            self.estado = estado
            
      def tarea_completada(self):
            self.estado = True
            print(f"Tarea '{self.titulo}' marcada como completada.")
            
      def tarea_no_nompletada(self):
            self.estado = False
            print(f"Tarea '{self.titulo}' marcada como pendiente.")

class MostrarTarea:
      def __init__(self, tarea):
            self.tarea = tarea
      
      def mostrar(self):
            # Códigos ANSI para colores
            COLOR_VERDE = '\033[92m'
            COLOR_ROJO = '\033[91m'
            RESET = '\033[0m'
            
            if self.tarea.estado is True:
                  estado = f"{COLOR_VERDE}Completada{RESET}"
            elif self.tarea.estado is False:
                  estado = f"{COLOR_ROJO}No Completada{RESET}"
            else:
                  estado = "Estado Desconocido"
                  
            print(f"Tarea: {self.tarea.titulo}, Estado: {estado}")

tarea1 = Tarea("Aprender Python", False)
tarea1.tarea_no_nompletada()
mostrar_tarea = MostrarTarea(tarea1)
mostrar_tarea.mostrar()
print("\n")
tarea2 = Tarea("Estudiar Principios SOLID", True)
tarea2.tarea_completada()
mostrar_tarea2 = MostrarTarea(tarea2)
mostrar_tarea2.mostrar()

print("----------FIN----------")

print("Ejercicio 2: [OCP] Crea una clase base Operacion con un método calcular(). Luego, crea subclases como Suma, Resta, etc." 
      "El sistema debe aceptar cualquier nueva operación sin alterar el código de la calculadora.")

class Operacion:
      def calcular(self,valor1, valor2):
            raise NotImplementedError("Subclases deben implementar este método")

class Suma(Operacion):
      def calcular(self, valor1, valor2):
            return valor1 + valor2
class Resta(Operacion):
      def calcular(self, valor1, valor2):
            return valor1 - valor2

class Multiplicacion(Operacion):
      def calcular(self, valor1, valor2):
            return valor1 * valor2

class Division(Operacion):
      def calcular(self, valor1, valor2):
            if valor2 == 0:
                  raise ValueError("No se puede dividir por cero")
            return valor1 / valor2

suma = Suma()
resultado_suma = suma.calcular(5, 3)
print(f"Resultado de la suma: {resultado_suma}")
resta = Resta()
resultado_resta = resta.calcular(5, 3)
print(f"Resultado de la resta: {resultado_resta}")
multiplicacion = Multiplicacion()
resultado_multiplicacion = multiplicacion.calcular(5, 3)
print(f"Resultado de la multiplicación: {resultado_multiplicacion}")
division = Division()
resultado_division = division.calcular(5, 3)
print(f"Resultado de la división: {resultado_division}")

print("----------FIN----------\n")

print("Ejercicio 3: [LSP] Crea una clase Forma con un método area(). Implementa Cuadrado, Rectángulo, Círculo, Trapecio y Rombo." 
      "Asegúrate de poder usar cualquier forma en un mismo ciclo sin problemas.")

class Figuras:
      def area(self):
            raise NotImplementedError("Subclases deben implementar este método")

class Cuadrado(Figuras):
      def __init__(self,lado):
            self.lado = lado
      
      def area(self):
            return self.lado * self.lado

class Rectangulo(Figuras):
      def __init__(self, base, altura):
            self.base = base
            self.altura = altura
      
      def area(self):
            return self.base * self.altura

class Circulo(Figuras):
      def __init__(self, radio):
            self.radio = radio
      
      def area(self):
            import math
            return math.pi * (self.radio ** 2)

class Trapecio(Figuras):
      def __init__(self, base_mayorB, base_menorA, altura):
            self.base_menorA = base_menorA
            self.base_mayorB = base_mayorB
            self.altura = altura
      
      def area(self):
            return ((self.base_menorA + self.base_mayorB) * self.altura) / 2

class Rombo(Figuras):
      def __init__(self, diagonal_menor, diagonal_mayor):
            self.diagonal_mayor = diagonal_mayor
            self.diagonal_menor = diagonal_menor
            
      
      def area(self):
            return (self.diagonal_mayor * self.diagonal_menor) / 2

Figuras = [Cuadrado(4), Rectangulo(5, 3), Circulo(2), Trapecio(6, 4, 3), Rombo(5, 7)]#Aqui creamos una lista de objetos de diferentes figuras
for figura in Figuras:
      print(f"El área de la figura {figura.__class__.__name__} es: {figura.area()}")

print("----------FIN----------\n")

print("----------EJERCICIOS INTERMEDIO----------")

print("Ejercicio 4: [ISP] Crea interfaces separadas como ImprimirHD, Imprimir4k, Escanear. EnviarFax, implementa dispositivos que usen" 
      "solo las necesarias (ej. una ImpresoraBasica no debería tener método scan()).")

class ImprimirHD:
      def imprimir_hd(self, documento):
            print(f"[Impresora HD]--> Imprimiendo en alta definición: {documento}")
class Imprimir4k:
      def imprimir_4k(self, documento):
            print(f"[Impresora 4K]--> Imprimiendo en 4K: {documento}")
            
class Escanear:   
      def escanear(self, documento):
            print(f"[Escáner]--> Escaneando: {documento}")
            
class EnviarFax:
      def enviar_fax(self, documento):
            print(f"[Fax]--> Enviando fax: {documento}")

class ImpresoraBasica(ImprimirHD):
      def imprimir_hd(self, documento):
            print(f"[Impresora Básica]--> Imprimiendo: {documento}")

class ImpresoraAvanzada(ImprimirHD, Imprimir4k, Escanear):
      def imprimir_hd(self, documento):
            print(f"[Impresora Avanzada]--> Imprimiendo en alta definición: {documento}")
      
      def imprimir_4k(self, documento):
            print(f"[Impresora Avanzada]--> Imprimiendo en 4K: {documento}")
      
      def escanear(self, documento):
            print(f"[Impresora Avanzada]--> Escaneando: {documento}")

class ImpresoraFull(ImprimirHD, Imprimir4k, Escanear, EnviarFax):
      def imprimir_hd(self, documento):
            print(f"[Impresora Full]--> Imprimiendo en alta definición: {documento}")
      
      def imprimir_4k(self, documento):
            print(f"[Impresora Full--> Imprimiendo en 4K: {documento}")
      
      def escanear(self, documento):
            print(f"[Impresora Full]--> Escaneando: {documento}")
      
      def enviar_fax(self, documento):
            print(f"[Impresora Full]--> Enviando fax: {documento}")

impresora_basica = ImpresoraBasica()
impresora_basica.imprimir_hd("Documento1.pdf")
print("")
impresora_avanzada = ImpresoraAvanzada()
impresora_avanzada.imprimir_hd("Documento2.pdf")
impresora_avanzada.imprimir_4k("Documento3.pdf")
impresora_avanzada.escanear("Documento4.pdf")
print("")
impresora_full = ImpresoraFull()
impresora_full.imprimir_hd("Documento5.pdf")
impresora_full.imprimir_4k("Documento6.pdf")
impresora_full.escanear("Documento7.pdf")
impresora_full.enviar_fax("Documento8.pdf")

print("----------FIN----------")

print("Ejercicio 5: [DIP + SRP] Crea una clase LoginService que reciba un proveedor de autenticación (GoogleAuth, EmailAuth) basado" 
      "en una interfaz AuthProvider. No debe depender de clases concretas.")

class AuthProvider:
      def autenticar(self, usuario, contrasena):
            raise NotImplementedError("Subclases deben implementar este método")

class GoogleAuth(AuthProvider):
      def autenticar(self, usuario, contrasena):
            # Simulación de autenticación con Google
            if usuario == "usuario_google" and contrasena == "contrasena_google":
                  return True
            return False

class EmailAuth(AuthProvider):
      def autenticar(self, usuario, contrasena):
            # Simulación de autenticación por email
            if usuario == "usuario_email" and contrasena == "contrasena_email":
                  return True
            return False
      
class LoginService:
      def __init__(self, auth_provider:AuthProvider):
            self.auth_provider = auth_provider
      
      def login(self, usuario, contrasena):
            return self.auth_provider.autenticar(usuario, contrasena)

# Uso del LoginService con diferentes proveedores de autenticación
google_auth = GoogleAuth()
login_service_google = LoginService(google_auth)
resultado_google = login_service_google.login("usuario_google", "contrasena_google")
if resultado_google:
      print("Autenticación exitosa con Google")
else:
      print("Error de autenticación con Google")
     
email_auth = EmailAuth()
login_service_email = LoginService(email_auth)
resultado_email = login_service_email.login("usuario_email", "contrasena_email")
if resultado_email:
      print("Autenticación exitosa con Email")
else:
      print("Error de autenticación con Email")
          
print("----------FIN----------")

print("Ejercicio 6: [OCP + LSP] Crea una clase Exportador con subclases ExportadorCSV, ExportadorJSON, etc. Asegúrate de que cada" 
      "exportador pueda usarse sin romper el sistema.")

print("----------FIN----------")

print("----------EJERCICIOS DIFICIL----------")

print("Ejercicio 7: [DIP + OCP] Crea una clase RecommendationEngine que dependa de una abstracción RecommendationStrategy" 
      "(por historial, por popularidad, etc). Debe poder agregar nuevas estrategias sin modificar la clase principal.")
         
print("----------FIN----------")

print("Ejercicio 8: [SRP + LSP + OCP] Diseña una clase base MetodoPago con subclases TarjetaCredito, PayPal, Cripto. El sistema debe aceptar nuevas" 
      "sin modificarse. Cada clase debe tener su lógica separada y sustituible.")

print("----------FIN----------")

print("Ejercicio 9: [ISP + DIP] Define interfaces como TemperaturaSensor, HumedadSensor, MovimientoSensor. Crea una clase MonitorIoT que" 
      "use estos sensores sin conocer su implementación.")

print("----------FIN----------")

print("Ejercicio 10: [TODOS LOS PRINCIPIOS] Crea un sistema con:"
"Curso y Estudiante (SRP)"
"RepositorioCurso con distintas implementaciones (DIP)"
"Exportador con extensiones (OCP)"
"Notificaciones (Email, SMS) intercambiables (LSP)"
"Interfaces segregadas para funcionalidades separadas (ISP)")

print("----------FIN----------")

print("----------EJERCICIO FINAL----------")
print("CHAT ANALIZADOR DE SENTIMIENTOS")
print("En este proyecto desarrolla un chatbot en python, que nos pida que le digamos algo y tome eso que le decimos, analice el sentimiento"
      " y nos responde cual es el sentimiento que ha detectado.")

