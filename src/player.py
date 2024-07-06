import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, sprites):
        super().__init__()
        self.sprites = sprites
        self.action = 'idle'
        self.direction = 'down'
        self.frame = 0
        self.image = self.get_sprite()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 0  # Reducir la velocidad de movimiento del personaje
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 200  # Aumentar este valor para hacer la animación más lenta
        self.is_moving = False
        self.idle_timer = pygame.time.get_ticks()
        self.idle_animation_interval = 30000  # 30 segundos en milisegundos

    def update(self, keys):
        self.handle_movement(keys)
        self.animate()

    def handle_movement(self, keys):
        self.is_moving = False  # Resetear el estado de movimiento
        self.action = 'idle'

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.direction = 'left'
            self.action = 'walk'
            self.is_moving = True
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = 'right'
            self.action = 'walk'
            self.is_moving = True
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.direction = 'up'
            self.action = 'walk'
            self.is_moving = True
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.direction = 'down'
            self.action = 'walk'
            self.is_moving = True

        # Cambiar a correr si se presiona Shift
        if self.is_moving and keys[pygame.K_LSHIFT]:
            self.action = 'run'

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            if self.is_moving:
                self.frame = (self.frame + 1) % len(self.sprites[self.action][self.direction])
            else:
                if now - self.idle_timer > self.idle_animation_interval:
                    self.idle_timer = now
                    self.frame = (self.frame + 1) % len(self.sprites['idle'][self.direction])
                else:
                    self.frame = 0

            self.image = self.get_sprite()

    def get_sprite(self):
        action_sprites = self.sprites[self.action][self.direction]
        sprite = action_sprites[self.frame]
        return sprite
