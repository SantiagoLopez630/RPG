import pygame
import sys
from player import Player

# Inicializa Pygame
pygame.init()

# Obtener la resolución de la pantalla
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

# Configura la ventana para que ocupe toda la pantalla
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("RPG de Acción y Aventuras")

# Colores
NEGRO = (0, 0, 0)

# Cargar el fondo del mapa
background = pygame.image.load('../assets/images/map.png')
background = pygame.transform.scale(background, (screen_width, screen_height))  # Ajusta el tamaño del mapa si es necesario

# Crear el jugador
player = Player(100, 100)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Salir del modo fullscreen con ESC
                running = False

    # Obtener teclas presionadas
    keys = pygame.key.get_pressed()

    # Actualizar el jugador
    all_sprites.update(keys)

    # Dibujar en la pantalla
    screen.blit(background, (0, 0))  # Dibuja el fondo del mapa
    all_sprites.draw(screen)

    # Actualiza la pantalla
    pygame.display.flip()

pygame.quit()
sys.exit()
