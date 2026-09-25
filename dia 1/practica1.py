# programa para calcular IMC 
print("Calculadora de IMC")
peso = float(input("Ingrese su peso :"))
estatura = float(input("Ingrese su estatura"))
IMC = peso / (estatura * estatura )
print("IMC es :" + str(IMC))