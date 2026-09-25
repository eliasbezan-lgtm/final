import pygame
import random

pygame.init()

# Tamaño de la ventana
ANCHO = 800
ALTO = 500

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Cazador de Monedas")

reloj = pygame.time.Clock()

# Colores
NEGRO = (20, 20, 30)
BLANCO = (255, 255, 255)
AZUL = (50, 120, 255)
AMARILLO = (255, 215, 0)
VERDE = (50, 220, 100)

# Jugador
jugador = pygame.Rect(100, 200, 40, 40)

velocidad = 5

# Moneda
moneda = pygame.Rect(
    random.randint(50, 750),
    random.randint(50, 450),
    25,
    25
)

# Puntuación
puntos = 0

fuente = pygame.font.Font(None, 36)

ejecutando = True

while ejecutando:

    # Eventos
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

    # Teclas
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        jugador.x -= velocidad

    if teclas[pygame.K_RIGHT]:
        jugador.x += velocidad

    if teclas[pygame.K_UP]:
        jugador.y -= velocidad

    if teclas[pygame.K_DOWN]:
        jugador.y += velocidad

    # Evitar salir de la ventana
    if jugador.left < 0:
        jugador.left = 0

    if jugador.right > ANCHO:
        jugador.right = ANCHO

    if jugador.top < 0:
        jugador.top = 0

    if jugador.bottom > ALTO:
        jugador.bottom = ALTO

    # Detectar moneda
    if jugador.colliderect(moneda):

        puntos += 1

        moneda.x = random.randint(30, ANCHO - 30)
        moneda.y = random.randint(60, ALTO - 30)

    # Fondo
    ventana.fill(NEGRO)

    # Jugador
    pygame.draw.rect(
        ventana,
        AZUL,
        jugador
    )

    # Moneda
    pygame.draw.circle(
        ventana,
        AMARILLO,
        moneda.center,
        13
    )

    # Texto
    texto = fuente.render(
        f"Puntos: {puntos}",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (20, 20)
    )

    pygame.display.update()

    reloj.tick(60)

pygame.quit()