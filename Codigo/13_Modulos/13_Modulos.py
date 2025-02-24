print("----------MODULOS----------")
print("Los módulos en Python son archivos que contienen definiciones y declaraciones de Python." 
      "Sirven para organizar el código en partes reutilizables y manejables.")

import Probando_los_modulos

Probando_los_modulos.suma(4,5)
Probando_los_modulos.my_function()
             
from Probando_los_modulos import suma
suma(2, 7)           

#En python los modulos no solo sirven para traer informacion de otras funciones 
# sino que tambien librerias como pandas,Matplotlib,NumPy entre otra o valores de ya fuciones predeterminada

import math
print(math.pi)
print(math.pow(2, 8))


