#Un producto está representado como diccionario con su nombre, 
#precio y stock disponible. Al registrarse una venta de una cierta cantidad de unidades, 
#descontar del stock y calcular el monto total de la venta.
producto= {
    "nombre" :"Arroz 1Kg",
    "precio" : 6500,
    "stock"  : 120
}

cantidad_vendida=15
producto["stock"]=producto["stock"]-cantidad_vendida
venta=producto["precio"]*cantidad_vendida
print(f"El stock restante es: {producto["stock"]} unidades")
print(f"El total de la venta es: {venta} gs")
print(f"La venta registrada es de {cantidad_vendida}unidades de {producto["nombre"]}")