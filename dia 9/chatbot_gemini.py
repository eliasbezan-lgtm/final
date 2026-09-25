import wikipedia
wikipedia.set_lang("es")

import os
from google import genai
from google.genai import types


# ==========================================
# CONEXIÓN CON GEMINI
# ==========================================

API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    print("ADVERTENCIA: No se encontró GEMINI_API_KEY")


client = genai.Client(
    api_key=API_KEY
)


# ==========================================
# CHATBOT
# ==========================================

class Chatbot:

    def __init__(self, nombre):

        self.nombre = nombre

        self.base_conocimiento = {

            "hola":
                "Hola, ¿Qué película quieres ver?",

            "que es una pelicula":
                "Una película es una obra audiovisual creada para contar una historia o transmitir una idea.",

            "que es cine":
                "El cine es el arte de crear y proyectar películas mediante imágenes en movimiento.",

            "generos de peliculas":
                "Algunos géneros son acción, comedia, terror, ciencia ficción, drama, romance, aventura y animación.",

            "pelicula de accion":
                "Las películas de acción suelen tener peleas, persecuciones, explosiones y escenas de mucha intensidad.",

            "pelicula de terror":
                "Las películas de terror buscan provocar miedo, tensión o suspenso en el espectador.",

            "pelicula de comedia":
                "Las películas de comedia buscan entretener y hacer reír al público.",

            "pelicula de ciencia ficcion":
                "La ciencia ficción suele tratar temas como el espacio, robots, viajes en el tiempo, tecnología avanzada y mundos futuristas.",

            "titanic":
                "Titanic es una película de 1997 dirigida por James Cameron y protagonizada por Leonardo DiCaprio y Kate Winslet.",

            "avatar":
                "Avatar es una película de ciencia ficción de 2009 dirigida por James Cameron.",

            "matrix":
                "Matrix es una película de ciencia ficción de 1999 protagonizada por Keanu Reeves como Neo.",

            "jurassic park":
                "Jurassic Park es una película de aventuras y ciencia ficción de 1993 dirigida por Steven Spielberg.",

            "el padrino":
                "El Padrino es una película de 1972 dirigida por Francis Ford Coppola.",

            "spiderman":
                "Spider-Man es un superhéroe de Marvel cuya identidad es Peter Parker.",

            "batman":
                "Batman es un superhéroe de DC Comics. Su identidad es Bruce Wayne.",

            "superman":
                "Superman es un superhéroe de DC Comics originario del planeta Krypton.",

            "harry potter":
                "Harry Potter es una saga de películas sobre un joven mago y sus aventuras en Hogwarts.",

            "star wars":
                "Star Wars es una famosa saga de ciencia ficción creada por George Lucas.",

            "el señor de los anillos":
                "El Señor de los Anillos es una trilogía de fantasía basada en las novelas de J. R. R. Tolkien.",

            "toy story":
                "Toy Story es una película animada de Pixar de 1995.",

            "frozen":
                "Frozen es una película animada de Disney protagonizada por Elsa y Anna.",

            "avengers":
                "Avengers es una saga de Marvel que reúne a varios superhéroes.",

            "iron man":
                "Iron Man es un superhéroe de Marvel cuyo nombre es Tony Stark.",

            "thor":
                "Thor es un superhéroe de Marvel inspirado en el dios de la mitología nórdica.",

            "hulk":
                "Hulk es un personaje de Marvel. Su identidad es Bruce Banner.",

            "terminator":
                "Terminator es una saga de ciencia ficción relacionada con robots, inteligencia artificial y viajes en el tiempo.",

            "regreso al futuro":
                "Regreso al Futuro es una película de ciencia ficción y aventura protagonizada por Michael J. Fox.",

            "interstellar":
                "Interstellar es una película de ciencia ficción dirigida por Christopher Nolan.",

            "barbie":
                "Barbie es una película de 2023 dirigida por Greta Gerwig.",

            "oppenheimer":
                "Oppenheimer es una película dirigida por Christopher Nolan sobre J. Robert Oppenheimer.",

            "el rey leon":
                "El Rey León es una película animada de Disney que cuenta la historia de Simba.",

            "piratas del caribe":
                "Piratas del Caribe es una saga de aventuras protagonizada principalmente por Johnny Depp como Jack Sparrow."
        }

        self.historial = []


    # ==========================================
    # RESPONDER
    # ==========================================

    def responder(self, mensaje):

        mensaje = mensaje.lower().strip()

        self.historial.append(mensaje)


        # ======================================
        # 1. BUSCAR EN NUESTRO DICCIONARIO
        # ======================================

        for clave, respuesta in self.base_conocimiento.items():

            if clave in mensaje:

                return respuesta


        # ======================================
        # 2. INTENTAR WIKIPEDIA
        # ======================================

        try:

            respuesta_wikipedia = wikipedia.summary(
                mensaje,
                sentences=2
            )

            return respuesta_wikipedia

        except Exception:

            print("Wikipedia no encontró una respuesta.")


        # ======================================
        # 3. USAR GEMINI
        # ======================================

        try:

            response = client.models.generate_content(

                model="gemini-3.8-flash",

                contents=(
                    "Eres Miki, un chatbot especializado en "
                    "películas, cine, actores y entretenimiento. "
                    "Responde en español de manera clara y sencilla.\n\n"
                    "Pregunta del usuario:\n"
                    + mensaje
                ),

                config=types.GenerateContentConfig(
                    temperature=0.7
                )
            )

            return response.text


        except Exception as e:

            return (
                "No pude obtener una respuesta de Gemini.\n"
                "Error: "
                + str(e)
            )


    # ==========================================
    # AGREGAR CONOCIMIENTO
    # ==========================================

    def agregar_conocimiento(self, clave, respuesta):

        self.base_conocimiento[
            clave.lower().strip()
        ] = respuesta


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main():

    bot = Chatbot("Miki")

    print()
    print("====================================")
    print("          CHATBOT MIKI")
    print("====================================")
    print()

    print("Miki: Hola, ¿en qué puedo ayudarte?")
    print("Miki: Pregúntame sobre películas, cine, actores, etc.")
    print("Miki: Escribe 'salir' para terminar.")
    print()


    while True:

        entrada = input("Tú: ")


        # ==================================
        # SALIR
        # ==================================

        if entrada.lower().strip() == "salir":

            print()
            print("Miki: Hasta luego.")
            break


        # ==================================
        # RESPUESTA
        # ==================================

        respuesta = bot.responder(entrada)

        print()
        print("Miki:", respuesta)
        print()


# ==========================================
# INICIAR
# ==========================================

if __name__ == "__main__":
    main()