import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# --- CONSTANTS AND COLORS ---
WIDTH, HEIGHT = 800, 600
SCREEN_SIZE = (WIDTH, HEIGHT)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)      # Player Color
GREEN = (0, 255, 0)    # Bullet Color
BLUE = (0, 0, 255)     # Enemy Color
BLACK = (0, 0, 0)      # Text Color

# Entity Constants
PLAYER_SIZE = 50
PLAYER_SPEED = 7  # Increased speed for better feel
BULLET_SIZE = 10
BULLET_SPEED = 12
ENEMY_SIZE = 50
ENEMY_SPEED_BASE = 3 # Base speed for enemies

# --- GAME CLASSES (Using Pygame Sprites for Performance) ---

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([PLAYER_SIZE, PLAYER_SIZE])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - PLAYER_SIZE)
        self.speed = PLAYER_SPEED

    def update(self):
        """Update player position based on key presses and clamp to screen."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        
        # Performance/Design Improvement: Clamp position to screen bounds
        self.rect.clamp_ip(screen.get_rect())

    def shoot(self):
        """Creates a new bullet instance."""
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets_group.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([BULLET_SIZE, BULLET_SIZE])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.speed = BULLET_SPEED

    def update(self):
        """Moves the bullet and checks if it goes off-screen."""
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill() # Sprite method to remove it from all groups

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.Surface([ENEMY_SIZE, ENEMY_SIZE])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - ENEMY_SIZE)
        self.rect.y = 0
        self.speed = speed

    def update(self):
        """Moves the enemy down and checks if it goes off-screen."""
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill() # Removed from all groups upon leaving screen

# --- GAME SETUP ---
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Optimized Pygame Shooter")

# Initialize Sprite Groups (Performance Improvement)
# all_sprites manages drawing and updating all entities
all_sprites = pygame.sprite.Group()
# dedicated groups for faster collision checks
bullets_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()

# Set up the player
player = Player()
all_sprites.add(player)

# Set up the clock and font
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
score = 0

# --- GAME LOOP ---
def run_game():
    global score
    # We must declare player as global because we re-assign it during restart
    global player
    
    # New game state variable
    game_active = True
    
    # Difficulty Scaling Variables
    # The enemy spawn chance and speed will increase slightly as the score goes up.
    initial_spawn_rate = 0.015
    max_spawn_rate = 0.1
    speed_increase_factor = 0.1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if game_active and event.key == pygame.K_SPACE:
                    player.shoot()
                
                # Restart game on ENTER key press when game is over
                elif not game_active and event.key == pygame.K_RETURN:
                    # Reset game state
                    score = 0
                    all_sprites.empty()
                    bullets_group.empty()
                    enemies_group.empty()
                    
                    # Re-create the player
                    player = Player() 
                    all_sprites.add(player)
                    game_active = True

        screen.fill(BLACK)

        if game_active:
            # --- UPDATE ALL ENTITIES ---
            all_sprites.update()

            # --- COLLISION DETECTION (Bullet vs Enemy) ---
            
            # dokill=True removes the colliding sprites (bullets and enemies) from their groups.
            hits = pygame.sprite.groupcollide(bullets_group, enemies_group, True, True)

            # Update score based on collisions
            for bullet in hits:
                score += len(hits[bullet])

            # --- COLLISION DETECTION (Player vs Enemy) - NEW GAME OVER LOGIC ---
            
            # Check for player collision with any enemy
            player_hits = pygame.sprite.spritecollide(player, enemies_group, True)
            if player_hits:
                game_active = False # End the game!
            
            # --- ENEMY SPAWNING (Difficulty Scaling) ---
            
            # Calculate dynamic spawn rate and speed
            difficulty_multiplier = score // 10 # Increases every 10 points
            
            # Spawn chance increases up to max_spawn_rate
            current_spawn_rate = initial_spawn_rate + (difficulty_multiplier * 0.005)
            current_spawn_rate = min(current_spawn_rate, max_spawn_rate)
            
            # Enemy speed increases slightly based on score
            current_enemy_speed = ENEMY_SPEED_BASE + (difficulty_multiplier * speed_increase_factor)

            if random.random() < current_spawn_rate:
                enemy = Enemy(current_enemy_speed)
                all_sprites.add(enemy)
                enemies_group.add(enemy)

            # --- DRAWING (Active Game) ---
            
            # Draw all sprites (Player, Bullets, Enemies)
            all_sprites.draw(screen)
            
            # Draw Score
            text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(text, (10, 10))

        else:
            # --- DRAWING (Game Over Screen) ---
            game_over_text = font.render("GAME OVER", True, RED)
            score_text = font.render(f"Final Score: {score}", True, WHITE)
            restart_text = font.render("Press ENTER to Restart", True, WHITE)
            
            # Centering the texts
            game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
            score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
            
            screen.blit(game_over_text, game_over_rect)
            screen.blit(score_text, score_rect)
            screen.blit(restart_text, restart_rect)

        # Update the full display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

# Run the game and exit Pygame cleanly
if __name__ == '__main__':
    run_game()
    pygame.quit()
    sys.exit()
