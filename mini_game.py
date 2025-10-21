import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_SPEED = 5
BULLET_SIZE = 10
BULLET_SPEED = 10
POWER_UP_SIZE = 20
ENEMY_SIZE = 50
ENEMY_SPEED = 5

# Set up some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the player
player = pygame.Rect(WIDTH / 2, HEIGHT / 2, PLAYER_SIZE, PLAYER_SIZE)

# Set up the bullets
bullets = []

# Set up the power-ups
power_ups = []

# Set up the enemies
enemies = []

# Set up the clock
clock = pygame.time.Clock()

# Set up the score
score = 0

# Set up the font
font = pygame.font.Font(None, 36)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.center, player.top, BULLET_SIZE, BULLET_SIZE))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player.y += PLAYER_SPEED

    # Move the bullets
    for bullet in bullets:
        bullet.y -= BULLET_SPEED
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Move the enemies
    for enemy in enemies:
        enemy.y += ENEMY_SPEED
        if enemy.top > HEIGHT:
            enemies.remove(enemy)

    # Check for collisions
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

    # Add new enemies
    if random.random() < 0.05:
        enemies.append(pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), 0, ENEMY_SIZE, ENEMY_SIZE))

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)
    for bullet in bullets:
        pygame.draw.rect(screen, GREEN, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, BLUE, enemy)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)