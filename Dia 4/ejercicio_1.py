productos = ["Arroz", "Aceite", "Fideos", "Azúcar"]

with open("productos.txt", "w", encoding="utf-8") as archivo:
    for producto in productos:
        archivo.write(producto + "\n")

print("Productos guardados correctamente.")
