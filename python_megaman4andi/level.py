import pygame

class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background = pygame.image.load('assets/background.png')
        self.platforms = [pygame.Rect(0, 500, self.width, 50)]  # Plattform am Boden

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), platform)
