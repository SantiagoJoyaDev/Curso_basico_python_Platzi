import json

with open('products.json', 'r') as file:
    products = json.load(file)  # Cargar el contenido del archivo JSON en un diccionario
    print("Contenido del archivo JSON:")
    print( products)
print("\n" + "="*100 + "\n")

#mostrar el contenido en columnas
print("Contenido del archivo JSON con formato por columnas:")
for product in products:
    # Imprimir cada producto en formato de columnas
    print(f"Product: {product['name']}," 
          f"Price: {product['price']}," 
          f"Quantity: {product['quantity']}," 
          f"Brand: {product['brand']}," 
          f"Category: {product['category']}")

# Escritura de un nuevo producto en el archivo JSON
new_product = {
    "name": "Wireless Mouse",
    "price": "25.99",
    "quantity": "50",
    "brand": "Logitech",
    "category": "Accessories"
}

with open('products.json', 'r') as file:
    products = json.load(file)  # Cargar el contenido del archivo JSON en un diccionario

products.append(new_product)  # Añadir el nuevo producto a la lista de productos

with open('products.json', 'w') as file:
    json.dump(products, file, indent=4)  # Guardar la lista actualizada de productos en el archivo JSON
    #el dump() convierte el objeto Python en una cadena JSON y lo escribe en el archivo.