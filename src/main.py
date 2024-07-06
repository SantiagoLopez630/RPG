import pygame
import sys
from player import Player

def load_spritesheet(filename, width, height):
    sheet = pygame.image.load(filename).convert_alpha()
    sheet_width, sheet_height = sheet.get_size()
    cols = sheet_width // width
    rows = sheet_height // height

    sprites = []
    for y in range(rows):
        row_sprites = []
        for x in range(cols):
            rect = pygame.Rect(x * width, y * height, width, height)
            sprite = sheet.subsurface(rect)
            row_sprites.append(sprite)
        sprites.append(row_sprites)
    
    return sprites

def load_all_sprites():
    walk_spritesheet = load_spritesheet('../assets/images/Unarmed_Walk/Unarmed_Walk_full.png', 64, 64)
    run_spritesheet = load_spritesheet('../assets/images/Unarmed_Run/Unarmed_Run_full.png', 64, 64)
    idle_spritesheet = load_spritesheet('../assets/images/Unarmed_Idle/Unarmed_Idle_full.png', 64, 64)
    
    sprite_data = {
        'walk': {
            'down': walk_spritesheet[0],
            'left': walk_spritesheet[1],
            'right': walk_spritesheet[2],
            'up': walk_spritesheet[3]
        },
        'run': {
            'down': run_spritesheet[0],
            'left': run_spritesheet[1],
            'right': run_spritesheet[2],
            'up': run_spritesheet[3]
        },
        'idle': {
            'down': idle_spritesheet[0],
            'left': idle_spritesheet[1],
            'right': idle_spritesheet[2],
            'up': idle_spritesheet[3]
        }
    }
    return sprite_data

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

# Cargar los sprites desde los spritesheets
sprites = load_all_sprites()

# Crear el jugador
player = Player(100, 100, sprites)
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
