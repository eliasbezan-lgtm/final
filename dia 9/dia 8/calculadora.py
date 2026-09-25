class Calculadora:
    numero1 = None       #atributos
    numero2 = None

    def __init__(self):   #es un constructor
        self.numero1 = 0
        self.numero2 = 0

    def sumar(self):
        return self.numero1 + self.numero2

    def restar(self):
        return self.numero1 - self.numero2
    
    def dividir(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2      #se puede redondear a dos decimales como self.numero2:.2f si quiero dos decimales
        else:
            return f"el divisor no puede ser cero"

    def multiplicar(self):
        return self.numero1 * self.numero2

casio = Calculadora()
casio.numero1 = 45
casio.numero2 = 30
print(casio.sumar())
print(casio.restar())
print(casio.multiplicar())
print(casio.dividir())


class CalculadoraCientifica(Calculadora):
    """calculadora cientifica hereda de calculadora"""
    historial = None

    def __init__(self):
        super()
        self.historial = []

    def factorial (self, n):
        fact = 1
        for x in range (2, n+1):
            fact = fact * x
        self.historial.append(f"{n}!={fact}")
        return fact

class CalculadoraProgramador(Calculadora):
    def __init__(self):
        super()

    def a_binario(sel, n):
        return bin(n)
 
print(f"Calculadora Científica")
casiofx = CalculadoraCientifica()
casiofx.numero1 = 20
casiofx.numero2 = 5
print(casiofx.sumar())
print(casiofx.restar())
print(casiofx.multiplicar())
print(casiofx.dividir())
print(casiofx.factorial(5))

print("-------------------")
print(casiofx.historial)

print("Calculadora Programador")

calcufxp = CalculadoraProgramador()
n = 10
print(f"Decimal {n} a binario {calcufxp.a_binario(n)}")
