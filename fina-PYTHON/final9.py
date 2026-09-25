notas = {"juan": 85, "maria": 90, "pedro": 78, "ana": 92}

nombre = input("ingresa el nombre del estudiante: ")

if nombre in notas:
    print(f"la nota de {nombre} es {notas[nombre]}")
else:
    print("el estudiante no encontrado ")