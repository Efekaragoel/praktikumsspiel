import pygame
import sys
import random

# Initialisierung von pygame
pygame.init()

# Bildschirmabmessungen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump and Run Spiel")

# Farben
WHITE = (255, 255, 255)

# Spieler
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 30  # Spieler etwas weiter unten platzieren
player_vel = 5
player_jump = False
jump_count = 10

# Hintergrundbild laden und an Bildschirmgröße anpassen
background_image = pygame.image.load("background.png")  # Passe den Dateinamen an
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Spielerbild laden und skalieren
player_image = pygame.image.load("smiley.png")  # Passe den Dateinamen an
player_image = pygame.transform.scale(player_image, (player_size, player_size))

# Hindernisse
obstacle_width = 50
obstacle_height = player_size
obstacle_vel = 5
obstacle_spawn_rate = 100  # Rate, mit der Hindernisse spawnen (je höher, desto seltener)
obstacle_spacing = 200  # Abstand zwischen den Hindernissen
obstacles = []

# Hintergrundbewegung
background_x = 0
background_vel = 1  # Geschwindigkeit der Hintergrundbewegung

# Spielschleife
clock = pygame.time.Clock()

def draw_player():
    screen.blit(player_image, (player_x, player_y))

def move_background():
    global background_x
    background_x -= background_vel
    if background_x <= -WIDTH:  # Wenn das Bild aus dem Bildschirm verschwindet, setze es zurück
        background_x = 0
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + WIDTH, 0))

def spawn_obstacle():
    if len(obstacles) == 0 or WIDTH - obstacles[-1][0] >= obstacle_spacing:
        obstacles.append([WIDTH, player_y])

def update_obstacles():
    for obstacle in obstacles:
        obstacle[0] -= obstacle_vel
    if obstacles and obstacles[0][0] < -obstacle_width:
        obstacles.pop(0)

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x - player_vel > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x + player_vel < WIDTH - player_size:
        player_x += player_vel
    if not player_jump:
        if keys[pygame.K_SPACE]:
            player_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            player_jump = False
            jump_count = 10

    # Hindernisse aktualisieren
    update_obstacles()
    if random.randint(0, obstacle_spawn_rate) == 0:  # Hindernis mit einer gewissen Wahrscheinlichkeit spawnen
        spawn_obstacle()

    # Kollisionsüberprüfung
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for obstacle in obstacles:
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle_width, obstacle_height)
        if player_rect.colliderect(obstacle_rect):
            obstacles = []  # Hindernisse zurücksetzen
            break

    # Bildschirm mit Hintergrundbild füllen und bewegen
    move_background()

    # Hindernisse zeichnen
    for obstacle in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

    # Spieler zeichnen
    draw_player()

    # Bildschirm aktualisieren
    pygame.display.update()

pygame.quit()
sys.exit()
