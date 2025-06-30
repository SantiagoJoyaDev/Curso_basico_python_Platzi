import csv

# Lectura de un archivo CSV
print("LEER UN ARCHIVO CSV Y MOSTRAR LOS PRODUCTOS COMO DICCIONARIO")
with open("products.csv", mode="r") as file:
     csv_reader = csv.DictReader(file)#El DictReader permite leer el archivo CSV y convertir cada fila en un diccionario
     for row in csv_reader:
         print(row)

print("\n" + "="*100 + "\n")#Esta linea es para separar la salida de la lectura del archivo CSV

# Lectura de un archivo CSV y mostrar productos con formato por columnas
print("LEER UN ARCHIVO CSV Y MOSTRAR LOS PRODUCTOS CON FORMATO POR COLUMNAS")   
with open("products.csv", mode="r") as file:
     csv_reader = csv.DictReader(file)
     for row in csv_reader:
            print(f"Product: {row['name']}, Price: {row['price']}")#Esta manera de imprimir permite mostrar 
            #los productos con un formato más legible

#escritura de un archivo CSV
new_products = {
    "name": "Wireless Mouse",
    "price": "25.99",
    "quantity": "50",
    "brand": "Logitech",
    "category": "Accessories"
}

print("\n" + "="*100 + "\n")

with open("new_products.csv", mode="a", newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames = new_products.keys())
    csv_writer.writerow(new_products)# Esto agrega una nueva fila al archivo CSV con los datos del nuevo producto

# Lectura del nuevo archivo CSV
with open("new_products.csv", mode="r") as file:
     csv_reader = csv.DictReader(file)
     for row in csv_reader:
         print(row)