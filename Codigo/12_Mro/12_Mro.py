print("----------MRO EN PYTHON----------")
#MRO es un acrónimo en inglés que significa "Orden de Resolución de Métodos". Es un conjunto de reglas que establece el orden 
# en que Python busca métodos y atributos en una clase. El MRO es útil cuando hay herencia múltiple, es decir, 
# cuando una clase hija hereda de varias clases padre. En estos casos, el MRO de la clase hija decide dónde buscará Python 
# un método determinado y a qué método llamará si hay un conflicto.

class A:
    def hablar(self):
        print("Hola desde la clase A")
        
class B(A):
    def hablar(self):
        print("Hola desde la clase B")
        
class C(A):
    def hablar(self):
        print("Hola desde la clase C")
        
class D(B,C):
    pass#Entonces se le da la prioridad a B debido a que es la primera que hereda
    # def hablar(self):
    #     print("Hola desde la clase D")
        
impresion = D()
print(D.mro())
impresion.hablar()

print("\n")

class Animal:
    def comer(self):
        print("Este es un animal y puede 'COMER'")
        
class Mamifero(Animal):
    def amamantar(self):
        print("Este es un mamifero y puede 'AMAMANTAR'")

class Ave(Animal):
    def volar(self):
        print("Este es un ave y puede 'VOLAR'")
        
class Murcielago(Mamifero,Ave):
    def volar(self):
        print("Este es un ave y puede 'VOLAR'")
       

murcielago = Murcielago()
murcielago.comer()
murcielago.amamantar()
murcielago.volar()
print(Murcielago.mro())