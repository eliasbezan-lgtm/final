producto = input("Producto vendido: ")
cantidad = input("Cantidad: ")

with open("registro.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{producto} - {cantidad} unidades\n")

print("Movimiento registrado.")
