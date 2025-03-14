import pygame

class Character:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.is_jumping = False
        self.fall_speed = 0
        self.gravity = 0.5
        self.character_image = pygame.image.load('assets/run_sprite.png')  # Beispielbild
        self.rect = self.character_image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.fall_speed = -10

        if self.is_jumping:
            self.y += self.fall_speed
            self.fall_speed += self.gravity

        if self.y >= 500:  # Beispiel für den Boden
            self.y = 500
            self.is_jumping = False
            self.fall_speed = 0

        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.character_image, self.rect)

