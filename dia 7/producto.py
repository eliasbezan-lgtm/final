class producto :
    nombre = None

    def __init__(self,n):
        self.nombre = n

    def ver_datos(self):
        return f"producto: {self.nombre}"

#crear un objeto

p1 = producto("computadora")

print(p1.ver_datos())