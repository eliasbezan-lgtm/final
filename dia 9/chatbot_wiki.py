import wikipedia
wikipedia.set_lang("es")

class Chatbot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.base_conocimiento = {
    "hola": "Hola, ¿En qué puedo ayudarte?",

    "que es una pelicula": "Una película es una obra audiovisual creada para contar una historia o transmitir una idea.",

    "que es cine": "El cine es el arte de crear y proyectar películas mediante imágenes en movimiento.",

    "generos de peliculas": "Algunos géneros son acción, comedia, terror, ciencia ficción, drama, romance, aventura y animación.",

    "pelicula de accion": "Las películas de acción suelen tener peleas, persecuciones, explosiones y escenas de mucha intensidad.",

    "pelicula de terror": "Las películas de terror buscan provocar miedo, tensión o suspenso en el espectador.",

    "pelicula de comedia": "Las películas de comedia buscan entretener y hacer reír al público.",

    "pelicula de ciencia ficcion": "La ciencia ficción suele tratar temas como el espacio, robots, viajes en el tiempo, tecnología avanzada y mundos futuristas.",

    "titanic": "Titanic es una película de 1997 dirigida por James Cameron y protagonizada por Leonardo DiCaprio y Kate Winslet.",

    "avatar": "Avatar es una película de ciencia ficción de 2009 dirigida por James Cameron. Está ambientada principalmente en el planeta Pandora.",

    "matrix": "Matrix es una película de ciencia ficción de 1999 protagonizada por Keanu Reeves como Neo.",

    "jurassic park": "Jurassic Park es una película de aventuras y ciencia ficción de 1993 dirigida por Steven Spielberg y basada en la novela de Michael Crichton.",

    "el padrino": "El Padrino es una película de 1972 dirigida por Francis Ford Coppola y protagonizada por Marlon Brando y Al Pacino.",

    "spiderman": "Spider-Man es un superhéroe de Marvel que obtiene poderes después de ser mordido por una araña modificada.",

    "batman": "Batman es un superhéroe de DC Comics que protege Gotham City. Su identidad es Bruce Wayne.",

    "superman": "Superman es un superhéroe de DC Comics originario del planeta Krypton.",

    "harry potter": "Harry Potter es una saga de películas basada en los libros de J. K. Rowling sobre un joven mago y sus aventuras en Hogwarts.",

    "star wars": "Star Wars es una famosa saga de ciencia ficción creada por George Lucas que cuenta historias sobre Jedi, Sith y la galaxia.",

    "el señor de los anillos": "El Señor de los Anillos es una trilogía de fantasía basada en las novelas de J. R. R. Tolkien.",

    "toy story": "Toy Story es una película animada de Pixar de 1995. Fue la primera película realizada completamente mediante animación por computadora.",

    "frozen": "Frozen es una película animada de Disney protagonizada por las hermanas Elsa y Anna.",

    "avengers": "Avengers es una saga de Marvel que reúne a varios superhéroes como Iron Man, Capitán América, Thor y Hulk.",

    "iron man": "Iron Man es un superhéroe de Marvel cuyo nombre es Tony Stark, un inventor y empresario que utiliza una avanzada armadura.",

    "thor": "Thor es un superhéroe de Marvel inspirado en el dios de la mitología nórdica y utiliza el martillo Mjolnir.",

    "hulk": "Hulk es un personaje de Marvel. Su identidad es Bruce Banner, un científico que se transforma en un ser de enorme fuerza.",

    "terminator": "Terminator es una saga de ciencia ficción relacionada con robots, inteligencia artificial y viajes en el tiempo.",

    "regreso al futuro": "Regreso al Futuro es una película de ciencia ficción y aventura protagonizada por Michael J. Fox como Marty McFly."
}
        self.historial = []

    def responder(self, mensaje):
        mensaje = mensaje.lower().strip()
        self.historial.append(mensaje)

        for clave, respuesta in self.base_conocimiento.items():
            if clave in mensaje:
                return respuesta

        try:
            return wikipedia.summary(mensaje, sentences=2)
        except Exception:
            return "No entendí tu mensaje, ¿Podrías reformularlo?"

    def agregar_conocimiento(self, clave, respuesta):
        self.base_conocimiento[clave.lower()] = respuesta 

def main():
    bot = Chatbot("Miki")
    print (f"{bot.nombre}: Hola, en qué puedo ayudarte?")

    while True:
        entrada = input("Tú:")

        if entrada.lower().strip()=="salir":
            print("Hasta luego")
            break

        respuesta = bot.responder(entrada)
        print(f"{bot.nombre}:{respuesta}")

if __name__ =="__main__":
    main()
  