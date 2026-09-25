#Un comercio registró sus ventas diarias (en dólares) durante siete días. 
#A partir de la lista, calcular el total vendido, el promedio diario, 
#y el día (por posición) con la venta más alta.

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
ventas = [1200, 1450, 980, 1600, 1750, 2100, 1330]

# TODO: calcular el total de ventas de la semana usando sum()
total = sum(ventas)
cantidad_dias = len(dias)
promedio=total/cantidad_dias
 

# TODO: obtener el índice de la venta más alta usando ventas.index(max(ventas))
indice_mayor = ventas.index(max(ventas))

print(f"Total vendido: {total}")
print(f"Promedio diario: {promedio:.2f}")
print(f"El día con más ventas fue: {dias[indice_mayor]}")