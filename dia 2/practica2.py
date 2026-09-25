saldo_disponible = 12500000
monto_transferencia = int(input("ingrese monto a transferir: "))

if monto_transferencia > saldo_disponible:
 print("saldo insuficiente")
else:
     saldo_disponible = saldo_disponible - monto_transferencia
     print("transferencia realizada con exito")
     print("su saldo actual es: " + str(saldo_disponible)) 