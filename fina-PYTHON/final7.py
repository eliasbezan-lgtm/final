numeros = [ ]
for i in range (5):
    num = float(input(f"ingrese el numero {i + 1}:"))
    numeros.append(num)

print("lista de numeros: ", numeros)
print("suma de los numeros: ", sum(numeros))