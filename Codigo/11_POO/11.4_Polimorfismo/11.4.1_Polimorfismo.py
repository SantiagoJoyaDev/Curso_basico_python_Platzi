print("----------POLIMORFISMO----------")
#El polimorfismo es un concepto clave en la programación orientada a objetos (POO) que permite que una misma interfaz o método 
# pueda tener múltiples comportamientos dependiendo del contexto en el que se use. Esto facilita la reutilización del código y 
# la flexibilidad en el diseño de software.

class Gato:
    def sonido(self):
        return "Miau"
    
class Perro:
    def sonido(self):
        return "Guau"
    
perro = Gato()
gato = Perro()

print("El sonido es:",perro.sonido)
