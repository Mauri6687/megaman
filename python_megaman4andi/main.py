import pygame
import sys
from character import Character
from projectile import Projectile
from level import Level

# Initialisierung von pygame
pygame.init()

# Fenstergröße
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('MegaMan X 4 Andi')

# Charakter-Instanz erstellen
character = Character(x=width//2, y=500, width=50, height=100, speed=5)
level = Level(width, height)

# Projektile-Array
projectiles = []

# Spiel-Loop
running = True
while running:
    screen.fill((255, 255, 255))  # Hintergrund füllen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tasteneingaben prüfen
    keys = pygame.key.get_pressed()

    # Bewegungen des Charakters
    character.move(keys)

    # Schießen
    if keys[pygame.K_LSHIFT]:
        projectile = Projectile(character.x + 50, character.y + 50, 10, 5, 10)
        projectiles.append(projectile)

    # Projektile bewegen
    for projectile in projectiles:
        projectile.move()
        projectile.draw(screen)

    # Level zeichnen
    level.draw(screen)

    # Charakter zeichnen
    character.draw(screen)

    # Bildschirm aktualisieren
    pygame.display.flip()

    # Frame-Rate
    pygame.time.Clock().tick(60)

# pygame beenden
pygame.quit()
sys.exit()
