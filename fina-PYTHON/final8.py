meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

num_es = int(input("ingrese un numero del 1 al 12: "))

if 1 <= num_es <= 12:
    print(f"el mes correspondiente es {meses [num_es - 1]}")
else:
    print("numero invalido.")