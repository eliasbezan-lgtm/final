with open("productos.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

for numero, linea in enumerate(lineas, start=1):
    print(f"{numero}. {linea.strip()}")
