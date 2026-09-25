notas = []
tam = 3 
sumatoria = 0

for x in range(tam):
    nota = 0
    while nota < 1 or nota > 5:
        nota = int(input(f"nota : {x + 1}: "))

    notas .append(nota)

for x in range (len(notas)):
    sumatoria = sumatoria + notas [x]

print("----estadisticas-----")
print(f"promedio: {sumatoria / tam}")
estado = ""
if(float(sumatoria / tam) > 1.7):
    estado = "aprobado"
else:
    estado = "reprobado"

print (f"estado: {estado}")