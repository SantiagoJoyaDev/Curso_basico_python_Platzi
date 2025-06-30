#Leer un archivo de texto linea por linea
print("LEER UN ARCHIVO DE TEXTO LINEA POR LINEA")
with open("Cuento_Caperucita.txt", "r") as file:
    for lineas in file:
        print(lineas.strip())#La funcion strip() elimina los espacios en blanco al principio y al final de cada línea.
print("")
print("-----------------------------------------\n")
print("\nLEER UN ARCHIVO DE TEXTO Y ALMACENARLO EN UNA LISTA")
#Leer todas las lineas en una lista
with open("Cuento_Caperucita.txt", "r") as file:
    lineas = file.readlines()  # Lee todas las líneas y las almacena en una lista
    for linea in lineas:
        print(linea.strip())  # Imprime cada línea sin espacios al principio o al final
print("")
print("-----------------------------------------\n")       
print("ANADIR UNA LINEA AL FINAL DEL ARCHIVO")
#Anadir una linea al final del archivo
with open("Cuento_Caperucita.txt", "a") as file:
    file.write("\nEsta es una nueva línea añadida al final del archivo.")
    
# #Sobre un archivo de texto y escribir en el
# print("\nESCRIBIR EN UN ARCHIVO DE TEXTO")
# with open("Cuento_Caperucita.txt", "w") as file:
#     file.write("Esta es una nueva línea escrita en el archivo.\n")
#     file.write("Otra línea más para demostrar la escritura en el archivo.\n")

#Conteo de lineas, palabras y caracteres
print("\nCONTAR LINEAS EN UN ARCHIVO DE TEXTO")
def contar_lineas(archivo):
    with open(archivo, "r") as file:
        lineas = file.readlines()
        print(f"Total de líneas: {len(lineas)}")

contar_lineas("Cuento_Caperucita.txt")
