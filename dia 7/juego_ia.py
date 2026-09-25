import pygame
import random
import math

pygame.init()

# ==========================================
# CONFIGURACIÓN
# ==========================================

ancho = 700
alto = 500

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("NEON ESCAPE")

reloj = pygame.time.Clock()

# ==========================================
# COLORES
# ==========================================

FONDO = (8, 12, 30)
FONDO2 = (15, 20, 45)

AZUL = (40, 150, 255)
AZUL_CLARO = (100, 220, 255)

ROJO = (255, 60, 70)
NARANJA = (255, 130, 30)

VERDE = (40, 255, 130)

AMARILLO = (255, 220, 40)

MORADO = (180, 70, 255)

BLANCO = (240, 245, 255)
NEGRO = (20, 20, 20)

GRIS = (70, 80, 110)

# ==========================================
# FUENTES
# ==========================================

fuente = pygame.font.Font(None, 28)
fuente_grande = pygame.font.Font(None, 65)
fuente_titulo = pygame.font.Font(None, 85)

# ==========================================
# JUGADOR
# ==========================================

size = 16

velocidad_normal = 5
velocidad = velocidad_normal

x_origen = ancho // 2
y_origen = alto - 45

x = x_origen
y = y_origen

# ==========================================
# NIVEL
# ==========================================

nivel = 1
max_niveles = 7

vidas = 3

puntos = 0
monedas_recogidas = 0

tiempo_maximo = 35
tiempo_restante = tiempo_maximo

# ==========================================
# PODERES
# ==========================================

escudo = False
tiempo_escudo = 0

velocidad_extra = False
tiempo_velocidad = 0

# ==========================================
# ESTADOS DEL JUEGO
# ==========================================

menu = True
juego_terminado = False
ganaste = False

# ==========================================
# META
# ==========================================

meta_ancho = 110
meta_alto = 30

meta_x = ancho // 2 - meta_ancho // 2
meta_y = 20

# ==========================================
# CREAR OBSTÁCULOS
# ==========================================

def crear_obstaculos(nivel):

    obstaculos = []

    cantidad = 3 + nivel

    for i in range(cantidad):

        ancho_obstaculo = random.randint(
            70 + nivel * 4,
            130 + nivel * 8
        )

        alto_obstaculo = random.randint(15, 25)

        x_obstaculo = random.randint(
            10,
            ancho - ancho_obstaculo - 10
        )

        y_obstaculo = random.randint(
            80,
            alto - 120
        )

        velocidad_obstaculo = random.uniform(
            2 + nivel * 0.3,
            4 + nivel * 0.6
        )

        tipo = random.choice([
            "horizontal",
            "vertical"
        ])

        direccion = random.choice([-1, 1])

        rect = pygame.Rect(
            x_obstaculo,
            y_obstaculo,
            ancho_obstaculo,
            alto_obstaculo
        )

        obstaculos.append({
            "rect": rect,
            "tipo": tipo,
            "velocidad": velocidad_obstaculo,
            "direccion": direccion
        })

    return obstaculos


# ==========================================
# CREAR PAREDES
# ==========================================

def crear_paredes(nivel):

    paredes = []

    if nivel >= 1:

        paredes.append(
            pygame.Rect(50, 120, 180, 15)
        )

        paredes.append(
            pygame.Rect(470, 120, 180, 15)
        )

    if nivel >= 2:

        paredes.append(
            pygame.Rect(0, 210, 140, 15)
        )

        paredes.append(
            pygame.Rect(560, 210, 140, 15)
        )

    if nivel >= 3:

        paredes.append(
            pygame.Rect(180, 280, 130, 15)
        )

        paredes.append(
            pygame.Rect(390, 280, 130, 15)
        )

    if nivel >= 4:

        paredes.append(
            pygame.Rect(70, 350, 160, 15)
        )

        paredes.append(
            pygame.Rect(470, 350, 160, 15)
        )

    if nivel >= 5:

        paredes.append(
            pygame.Rect(280, 80, 140, 15)
        )

    if nivel >= 6:

        paredes.append(
            pygame.Rect(250, 180, 200, 15)
        )

    if nivel >= 7:

        paredes.append(
            pygame.Rect(100, 400, 170, 15)
        )

        paredes.append(
            pygame.Rect(430, 400, 170, 15)
        )

    return paredes


# ==========================================
# CREAR MONEDAS
# ==========================================

def crear_monedas(nivel):

    monedas = []

    cantidad = 3 + nivel

    for i in range(cantidad):

        moneda_x = random.randint(30, ancho - 30)
        moneda_y = random.randint(60, alto - 70)

        tipo = random.choice([
            "normal",
            "normal",
            "especial"
        ])

        monedas.append({
            "x": moneda_x,
            "y": moneda_y,
            "tipo": tipo,
            "radio": 8
        })

    return monedas


# ==========================================
# CREAR PODERES
# ==========================================

def crear_poderes(nivel):

    poderes = []

    if nivel >= 2:

        poderes.append({
            "x": random.randint(40, ancho - 40),
            "y": random.randint(80, alto - 80),
            "tipo": "escudo"
        })

    if nivel >= 4:

        poderes.append({
            "x": random.randint(40, ancho - 40),
            "y": random.randint(80, alto - 80),
            "tipo": "velocidad"
        })

    return poderes


# ==========================================
# CREAR NIVEL
# ==========================================

obstaculos = crear_obstaculos(nivel)
paredes = crear_paredes(nivel)
monedas = crear_monedas(nivel)
poderes = crear_poderes(nivel)


# ==========================================
# REINICIAR JUGADOR
# ==========================================

def reiniciar_jugador():

    global x
    global y

    x = x_origen
    y = y_origen


# ==========================================
# NUEVO NIVEL
# ==========================================

def siguiente_nivel():

    global nivel
    global obstaculos
    global paredes
    global monedas
    global poderes
    global tiempo_restante
    global x
    global y

    nivel += 1

    if nivel > max_niveles:

        return

    x = x_origen
    y = y_origen

    obstaculos = crear_obstaculos(nivel)

    paredes = crear_paredes(nivel)

    monedas = crear_monedas(nivel)

    poderes = crear_poderes(nivel)

    tiempo_restante = tiempo_maximo - nivel * 2


# ==========================================
# REINICIAR TODO EL JUEGO
# ==========================================

def reiniciar_juego():

    global nivel
    global vidas
    global puntos
    global monedas_recogidas
    global tiempo_restante
    global juego_terminado
    global ganaste
    global menu
    global escudo
    global velocidad_extra

    nivel = 1

    vidas = 3

    puntos = 0

    monedas_recogidas = 0

    tiempo_restante = tiempo_maximo

    escudo = False

    velocidad_extra = False

    juego_terminado = False

    ganaste = False

    menu = False

    reiniciar_jugador()

    global obstaculos
    global paredes
    global monedas
    global poderes

    obstaculos = crear_obstaculos(nivel)

    paredes = crear_paredes(nivel)

    monedas = crear_monedas(nivel)

    poderes = crear_poderes(nivel)


# ==========================================
# TIEMPO
# ==========================================

ultimo_tiempo = pygame.time.get_ticks()

# ==========================================
# BUCLE PRINCIPAL
# ==========================================

corriendo = True

while corriendo:

    # ======================================
    # EVENTOS
    # ======================================

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            corriendo = False

        if evento.type == pygame.KEYDOWN:

            # Empezar
            if menu:

                if evento.key == pygame.K_RETURN:

                    reiniciar_juego()

            # Reiniciar
            if evento.key == pygame.K_r:

                reiniciar_juego()

            # Salir
            if evento.key == pygame.K_ESCAPE:

                corriendo = False

    # ======================================
    # MENÚ PRINCIPAL
    # ======================================

    if menu:

        ventana.fill(FONDO)

        titulo = fuente_titulo.render(
            "NEON ESCAPE",
            True,
            AZUL_CLARO
        )

        subtitulo = fuente.render(
            "Llega hasta la META y evita los obstáculos",
            True,
            BLANCO
        )

        comenzar = fuente_grande.render(
            "Presiona ENTER",
            True,
            AMARILLO
        )

        controles = fuente.render(
            "Usa las flechas para moverte",
            True,
            GRIS
        )

        ventana.blit(
            titulo,
            (
                ancho // 2 - titulo.get_width() // 2,
                100
            )
        )

        ventana.blit(
            subtitulo,
            (
                ancho // 2 - subtitulo.get_width() // 2,
                190
            )
        )

        ventana.blit(
            comenzar,
            (
                ancho // 2 - comenzar.get_width() // 2,
                250
            )
        )

        ventana.blit(
            controles,
            (
                ancho // 2 - controles.get_width() // 2,
                330
            )
        )

        pygame.display.flip()

        reloj.tick(60)

        continue

    # ======================================
    # JUEGO
    # ======================================

    if not juego_terminado and not ganaste:

        # ==================================
        # VELOCIDAD
        # ==================================

        if velocidad_extra:

            velocidad = 8

        else:

            velocidad = velocidad_normal

        # ==================================
        # MOVIMIENTO DEL JUGADOR
        # ==================================

        teclas = pygame.key.get_pressed()

        nuevo_x = x
        nuevo_y = y

        if teclas[pygame.K_RIGHT]:

            nuevo_x += velocidad

        if teclas[pygame.K_LEFT]:

            nuevo_x -= velocidad

        if teclas[pygame.K_UP]:

            nuevo_y -= velocidad

        if teclas[pygame.K_DOWN]:

            nuevo_y += velocidad

        # ==================================
        # LÍMITES
        # ==================================

        if nuevo_x < size:

            nuevo_x = size

        if nuevo_x > ancho - size:

            nuevo_x = ancho - size

        if nuevo_y < size:

            nuevo_y = size

        if nuevo_y > alto - size:

            nuevo_y = alto - size

        # ==================================
        # RECTÁNGULO DEL JUGADOR
        # ==================================

        jugador = pygame.Rect(
            nuevo_x - size,
            nuevo_y - size,
            size * 2,
            size * 2
        )

        # ==================================
        # PAREDES
        # ==================================

        choco_pared = False

        for pared in paredes:

            if jugador.colliderect(pared):

                choco_pared = True

        if not choco_pared:

            x = nuevo_x
            y = nuevo_y

        # ==================================
        # MOVER OBSTÁCULOS
        # ==================================

        for obstaculo in obstaculos:

            rect = obstaculo["rect"]

            velocidad_obstaculo = obstaculo["velocidad"]

            direccion = obstaculo["direccion"]

            if obstaculo["tipo"] == "horizontal":

                rect.x += velocidad_obstaculo * direccion

                if rect.left <= 0:

                    rect.left = 0

                    obstaculo["direccion"] = 1

                if rect.right >= ancho:

                    rect.right = ancho

                    obstaculo["direccion"] = -1

            else:

                rect.y += velocidad_obstaculo * direccion

                if rect.top <= 50:

                    rect.top = 50

                    obstaculo["direccion"] = 1

                if rect.bottom >= alto:

                    rect.bottom = alto

                    obstaculo["direccion"] = -1

        # ==================================
        # COLISIÓN OBSTÁCULOS
        # ==================================

        jugador = pygame.Rect(
            x - size,
            y - size,
            size * 2,
            size * 2
        )

        choco = False

        for obstaculo in obstaculos:

            if jugador.colliderect(
                obstaculo["rect"]
            ):

                choco = True

        # ==================================
        # SI CHOCA
        # ==================================

        if choco:

            if escudo:

                escudo = False

                tiempo_escudo = 0

                puntos += 25

            else:

                vidas -= 1

                puntos -= 20

                if puntos < 0:

                    puntos = 0

                reiniciar_jugador()

                if vidas <= 0:

                    juego_terminado = True

        # ==================================
        # RECOGER MONEDAS
        # ==================================

        for moneda in monedas[:]:

            distancia = math.sqrt(
                (x - moneda["x"]) ** 2 +
                (y - moneda["y"]) ** 2
            )

            if distancia < size + moneda["radio"]:

                if moneda["tipo"] == "normal":

                    puntos += 25

                else:

                    puntos += 100

                monedas_recogidas += 1

                monedas.remove(moneda)

        # ==================================
        # RECOGER PODERES
        # ==================================

        for poder in poderes[:]:

            distancia = math.sqrt(
                (x - poder["x"]) ** 2 +
                (y - poder["y"]) ** 2
            )

            if distancia < size + 12:

                if poder["tipo"] == "escudo":

                    escudo = True

                    tiempo_escudo = 8

                if poder["tipo"] == "velocidad":

                    velocidad_extra = True

                    tiempo_velocidad = 8

                poderes.remove(poder)

        # ==================================
        # TEMPORIZADOR
        # ==================================

        tiempo_actual = pygame.time.get_ticks()

        if tiempo_actual - ultimo_tiempo >= 1000:

            tiempo_restante -= 1

            ultimo_tiempo = tiempo_actual

        # ==================================
        # TIEMPO DEL ESCUDO
        # ==================================

        if escudo:

            tiempo_escudo -= 1 / 60

            if tiempo_escudo <= 0:

                escudo = False

        # ==================================
        # TIEMPO DE VELOCIDAD
        # ==================================

        if velocidad_extra:

            tiempo_velocidad -= 1 / 60

            if tiempo_velocidad <= 0:

                velocidad_extra = False

        # ==================================
        # SE ACABÓ EL TIEMPO
        # ==================================

        if tiempo_restante <= 0:

            vidas -= 1

            reiniciar_jugador()

            tiempo_restante = tiempo_maximo - nivel * 2

            if vidas <= 0:

                juego_terminado = True

        # ==================================
        # META
        # ==================================

        meta = pygame.Rect(
            meta_x,
            meta_y,
            meta_ancho,
            meta_alto
        )

        if jugador.colliderect(meta):

            puntos += 200 * nivel

            if nivel >= max_niveles:

                ganaste = True

            else:

                siguiente_nivel()

    # ======================================
    # DIBUJAR FONDO
    # ======================================

    ventana.fill(FONDO)

    # ======================================
    # DECORACIÓN DEL FONDO
    # ======================================

    for i in range(20):

        estrella_x = (i * 97) % ancho

        estrella_y = (i * 53) % alto

        pygame.draw.circle(
            ventana,
            (30, 40, 70),
            (estrella_x, estrella_y),
            2
        )

    # ======================================
    # META
    # ======================================

    pygame.draw.rect(
        ventana,
        VERDE,
        meta
    )

    texto_meta = fuente.render(
        "META",
        True,
        NEGRO
    )

    ventana.blit(
        texto_meta,
        (
            meta_x + 30,
            meta_y + 4
        )
    )

    # ======================================
    # PAREDES
    # ======================================

    for pared in paredes:

        pygame.draw.rect(
            ventana,
            MORADO,
            pared
        )

    # ======================================
    # OBSTÁCULOS
    # ======================================

    for i, obstaculo in enumerate(obstaculos):

        rect = obstaculo["rect"]

        if i % 2 == 0:

            color = ROJO

        else:

            color = NARANJA

        pygame.draw.rect(
            ventana,
            color,
            rect
        )

    # ======================================
    # MONEDAS
    # ======================================

    for moneda in monedas:

        if moneda["tipo"] == "normal":

            color = AMARILLO

            radio = 8

        else:

            color = (255, 100, 255)

            radio = 12

        pygame.draw.circle(
            ventana,
            color,
            (
                int(moneda["x"]),
                int(moneda["y"])
            ),
            radio
        )

        pygame.draw.circle(
            ventana,
            BLANCO,
            (
                int(moneda["x"]),
                int(moneda["y"])
            ),
            radio,
            2
        )

    # ======================================
    # PODERES
    # ======================================

    for poder in poderes:

        if poder["tipo"] == "escudo":

            color = AZUL_CLARO

            letra = "S"

        else:

            color = VERDE

            letra = "V"

        pygame.draw.circle(
            ventana,
            color,
            (
                int(poder["x"]),
                int(poder["y"])
            ),
            12
        )

        texto = fuente.render(
            letra,
            True,
            NEGRO
        )

        ventana.blit(
            texto,
            (
                poder["x"] - 7,
                poder["y"] - 10
            )
        )

    # ======================================
    # JUGADOR
    # ======================================

    pygame.draw.circle(
        ventana,
        AZUL,
        (
            int(x),
            int(y)
        ),
        size
    )

    pygame.draw.circle(
        ventana,
        AZUL_CLARO,
        (
            int(x),
            int(y)
        ),
        size,
        3
    )

    # ======================================
    # ESCUDO VISUAL
    # ======================================

    if escudo:

        pygame.draw.circle(
            ventana,
            AZUL_CLARO,
            (
                int(x),
                int(y)
            ),
            size + 8,
            2
        )

    # ======================================
    # INFORMACIÓN
    # ======================================

    texto_nivel = fuente.render(
        f"Nivel: {nivel}/{max_niveles}",
        True,
        BLANCO
    )

    texto_vidas = fuente.render(
        f"Vidas: {vidas}",
        True,
        BLANCO
    )

    texto_puntos = fuente.render(
        f"Puntos: {puntos}",
        True,
        AMARILLO
    )

    texto_monedas = fuente.render(
        f"Monedas: {monedas_recogidas}",
        True,
        AMARILLO
    )

    texto_tiempo = fuente.render(
        f"Tiempo: {int(tiempo_restante)}",
        True,
        BLANCO
    )

    ventana.blit(
        texto_nivel,
        (10, 5)
    )

    ventana.blit(
        texto_vidas,
        (120, 5)
    )

    ventana.blit(
        texto_puntos,
        (220, 5)
    )

    ventana.blit(
        texto_monedas,
        (350, 5)
    )

    ventana.blit(
        texto_tiempo,
        (500, 5)
    )

    # ======================================
    # GAME OVER
    # ======================================

    if juego_terminado:

        ventana.fill((5, 5, 15))

        texto = fuente_titulo.render(
            "GAME OVER",
            True,
            ROJO
        )

        texto2 = fuente_grande.render(
            f"Puntaje: {puntos}",
            True,
            AMARILLO
        )

        texto3 = fuente.render(
            "Presiona R para volver a jugar",
            True,
            BLANCO
        )

        ventana.blit(
            texto,
            (
                ancho // 2 - texto.get_width() // 2,
                120
            )
        )

        ventana.blit(
            texto2,
            (
                ancho // 2 - texto2.get_width() // 2,
                210
            )
        )

        ventana.blit(
            texto3,
            (
                ancho // 2 - texto3.get_width() // 2,
                290
            )
        )

    # ======================================
    # VICTORIA
    # ======================================

    if ganaste:

        ventana.fill((5, 35, 25))

        texto = fuente_titulo.render(
            "¡VICTORIA!",
            True,
            VERDE
        )

        texto2 = fuente_grande.render(
            f"Puntaje: {puntos}",
            True,
            AMARILLO
        )

        texto3 = fuente.render(
            "Completaste todos los niveles",
            True,
            BLANCO
        )

        texto4 = fuente.render(
            "Presiona R para jugar otra vez",
            True,
            BLANCO
        )

        ventana.blit(
            texto,
            (
                ancho // 2 - texto.get_width() // 2,
                90
            )
        )

        ventana.blit(
            texto2,
            (
                ancho // 2 - texto2.get_width() // 2,
                180
            )
        )

        ventana.blit(
            texto3,
            (
                ancho // 2 - texto3.get_width() // 2,
                250
            )
        )

        ventana.blit(
            texto4,
            (
                ancho // 2 - texto4.get_width() // 2,
                300
            )
        )

    # ======================================
    # ACTUALIZAR
    # ======================================

    pygame.display.flip()

    reloj.tick(60)


pygame.quit()