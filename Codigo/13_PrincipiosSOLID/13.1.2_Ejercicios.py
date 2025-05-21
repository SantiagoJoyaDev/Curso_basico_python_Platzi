print("----------EJERCICIOS DE PRINCIPIOS SOLID----------")
print("----------EJERCICIOS FACIL----------")
print("Ejercicio 1: [SRP] Crea una clase Tarea con los atributos titulo y completada. Agrega un método para marcarla como completada y" 
      "otra clase separada para mostrarla en consola o HTML.")

print("----------FIN----------")

print("Ejercicio 2: [OCP] Crea una clase base Operacion con un método calcular(). Luego, crea subclases como Suma, Resta, etc." 
      "El sistema debe aceptar cualquier nueva operación sin alterar el código de la calculadora.")

print("----------FIN----------\n")

print("Ejercicio 3: [LSP] Crea una clase Forma con un método area(). Implementa Cuadrado, Rectángulo, Círculo." 
      "Asegúrate de poder usar cualquier forma en un mismo ciclo sin problemas.")

print("----------FIN----------\n")

print("----------EJERCICIOS INTERMEDIO----------")

print("Ejercicio 4: [ISP] Crea interfaces separadas como Imprimible, Escaneable, Fotocopiable. Luego, implementa dispositivos que usen" 
      "solo las necesarias (ej. una ImpresoraBasica no debería tener método scan()).")

print("----------FIN----------")

print("Ejercicio 5: [DIP + SRP] Crea una clase LoginService que reciba un proveedor de autenticación (GoogleAuth, EmailAuth) basado" 
      "en una interfaz AuthProvider. No debe depender de clases concretas.")

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