# singleplayer.py
import pygame
import sys
import random
import const
import util

# Initialisierung von pygame
pygame.init()

# Bildschirmabmessungen
screen = pygame.display.set_mode((const.get_window_width(), const.get_window_height()))
pygame.display.set_caption("Jump and Run Spiel")

# Farben
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Spieler
player_size = const.get_size()
player_x = const.get_window_width() // 2
player_y = const.get_ground_height() - const.get_size()
player_vel = const.get_player_vel()
player_jump = False
jump_count = 10

# Hintergrundbild laden und an Bildschirmgröße anpassen
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (const.get_window_width(), const.get_window_height()))

# Spielerbild laden und skalieren
player_image = pygame.image.load("smiley.png")
player_image = pygame.transform.scale(player_image, (player_size, player_size))

# Hindernisse
obstacle_width = const.get_size()
obstacle_height = const.get_size()
obstacle_vel = const.get_vel()
obstacle_spawn_rate = 100
obstacle_spacing = 200
obstacles = []

# Hintergrundbewegung
background_x = 0
background_vel = const.get_vel()

# Spielschleife
clock = pygame.time.Clock()

def draw_player():
    screen.blit(player_image, (player_x, player_y))

def move_background():
    global background_x
    background_x -= background_vel
    if background_x <= -const.get_window_width():
        background_x = 0
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + const.get_window_width(), 0))

def spawn_obstacle():
    if len(obstacles) == 0 or const.get_window_width() - obstacles[-1][0] >= obstacle_spacing:
        new_spawn_height = util.generate_spawn_height(player_y)
        obstacles.append([const.get_window_width(), new_spawn_height])

def update_obstacles():
    for obstacle in obstacles:
        obstacle[0] -= obstacle_vel
    if obstacles and obstacles[0][0] < -obstacle_width:
        obstacles.pop(0)

running = True
game_active = False

def init():
    move_background()
    draw_player()
    pygame.display.update()

init()

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x - player_vel > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x + player_vel < const.get_window_width() - player_size:
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

    update_obstacles()
    if random.randint(0, obstacle_spawn_rate) == 0:
        spawn_obstacle()

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for obstacle in obstacles:
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle_width, obstacle_height)
        if player_rect.colliderect(obstacle_rect):
            obstacles = []
            break

    move_background()

    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

    draw_player()

    pygame.display.update()

pygame.quit()
sys.exit()
