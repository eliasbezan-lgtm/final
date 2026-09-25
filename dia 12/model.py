import mysql.connector

class modelotraduccion:
    def __init__(self):
       self.conexion = mysql.connector.connect(
           host="localhost",
           user="root",
           password="",
           database="bd_traducciones_moi",
       )

def agregar_palabra(self, espanol, ingles ):
    cursor = self.conexion.cursor()
    sql = f"insert into traducciones values(default, `{espanol},`{ingles}`)"
    cursor.execute(sql)
    self.conexion.commit()
    cursor.close()

    def buscar_traduccion(self, espanol):
        cursor = self.conexion.cursor()
    sql= f"SELECT * FROM TRADUCCIONES WHERE palabra_espanol =  `{espanol}`"
    cursor.execute(sql)
    resultado = cursor.ferchome()
    cursor.close()
    return resultado