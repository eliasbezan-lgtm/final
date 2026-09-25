#distancia entre sucursales
#tuplas
ubicacion_sucursal = (-25.2637, -57.5759)
latitud, longitud = ubicacion_sucursal
sucursal_a=(-25.2637, -57.5759)
sucursal_b=(-25.2968, -57.6350)
lat_a, long_a=sucursal_a
lat_b, long_b=sucursal_b

distancia=((lat_b-lat_a)**2+(long_b-long_a)**2)**(0.5)
print(f"la distancia entre sucursales es: {distancia:.2f} grados")
#2f es la cantidad de decimales
