from model import modelotraduccion

class controlladortraduccion:
    def __init__(self):
        self.modelo = modelotraduccion

    def cargar_palabra(self, esp, ing): 
        self.modelo.agregar_palabra(esp, ing)

    def traducir(self, palabra): 
        resultado = self.modelo.buscar_palabra(palabra)
        if resultado != None:
            return resultado

        return None