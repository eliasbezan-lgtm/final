ingreso_mensual = 4800000
historial_positivo = True
deuda_total = 1200000

if historial_positivo and ingreso_mensual >= deuda_total *3:
   print("prestamo_aprobado")
elif historial_positivo:
   print("aprobado con monto reducido")
else:
   print("prestamo rechazado")