#ordenamiento burbuja
precio = [5,2,9,1,6]
print(f"Lista original: {precio}")
n = len(precio)
for i in range (n-1):
    for j in range (n-1-i):
        if precio[j]>precio[j+1]:
            aux = precio[j]
            precio[j]=precio[j+1]
            precio[j+1]=aux

print(f"Lista ordenada:{precio}")