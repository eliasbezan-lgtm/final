num1 = float(input("ingresa el primer numero: "))
num2 = float(input("ingresa el segundo numero: "))

print(F"suma: {num1 + num2}")
print(f"resta: {num1 - num2}")
print(f"multiplica: {num1 * num2}")
print(f"divide: {num1 / num2 if num2 != 0 else 'no se puede dividir entre 0' }")
