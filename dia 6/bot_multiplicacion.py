import random

puntaje = 0

for pregunta in range (5) :
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    respuesta = int(input(f"cuanto es : {num1} * {num2} "))

    if respuesta == num1 * num2:
        print("excelente")
        puntaje += 1
    else:
        print("oh, fallaste")
print(f"acertaste al {puntaje} de 5")
if(puntaje <3):
    print("debes practicar mas")
elif(puntaje <5):
    print("eres pero debes practicar mas")
else: 
    print("eres genial con las multiplicaciones")