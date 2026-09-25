productos = ["arroz", "aceite", "fideo", "azucar"]

with open("archivo.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p} \n")

print("lista de productos desde archivo")
with open("archivo.txt", "r") as archivo :
    lineas = archivo.readlines()

    for p in lineas:
        print(f"{p.strip()}")