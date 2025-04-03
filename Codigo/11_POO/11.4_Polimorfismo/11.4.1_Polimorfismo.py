print("----------POLIMORFISMO----------")
#El polimorfismo es un concepto clave en la programación orientada a objetos (POO) que permite que una misma interfaz o método 
# pueda tener múltiples comportamientos dependiendo del contexto en el que se use. Esto facilita la reutilización del código y 
# la flexibilidad en el diseño de software.

print("---------POLIMORFISMO DE INCLUSION (AD-HOC)----------")
#En este polimorfismo lo que se hace es que se utiliza el mismo metodo pero cuando se ingresan los parametos cambiamos como tal
#los argumentos de esta manera usamos el mismo metodo pero usamos valores diferentes
class Calculadora:
    def suma(self, a, b=0, c=0):
        return a + b + c

calc = Calculadora()
print(calc.suma(5, 3))      # 8
print(calc.suma(5, 3, 2))   # 10

print("---------POLIMORFISMO POR HERENCIA----------")
#En este polimorfismo lo que se hace es que como tal se definen todas las funciones con el mismo metodo pero cuando voy a retorna
#como tal el valor cambia por lo tanto si llamo el mismo metodo pero con diferente objeto tendria la rta dependiendo del objeto
#mas no del metodo
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

print(perro.hacer_sonido())
print(gato.hacer_sonido())

print("---------POLIMORFISMO POR DUCK TYPING (TIPADO DINAMICO)----------")
#En este polimorfismo lo que importa es que aunque se use el mismo metodo dependiendo de la clase se comporta diferente
class Pato:
    def hacer_sonido(self):
        return "Cuac Cuac"

class Persona:
    def hacer_sonido(self):
        return "Hola!"

def hacer_hablar(objeto):
    print(objeto.hacer_sonido())

# No importa el tipo, solo que tenga el método `hacer_sonido`
hacer_hablar(Pato())    # Cuac Cuac
hacer_hablar(Persona()) # Hola!
 