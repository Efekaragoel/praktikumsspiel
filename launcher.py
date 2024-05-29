# launcher.py
import pygame
import sys
import subprocess

pygame.init()

# Bildschirmabmessungen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Launcher")

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Hintergrundbild laden
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (800, 600))

# Buttons zeichnen
def draw_button(text, rect, color):
    pygame.draw.rect(screen, color, rect)
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

# Hauptschleife
running = True
multiplayer_mode = False
input_box = pygame.Rect(300, 250, 200, 36)
input_active = False
input_text = ''

while running:
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if multiplayer_mode:
                if input_box.collidepoint(event.pos):
                    input_active = not input_active
                else:
                    input_active = False
            else:
                if singleplayer_button.collidepoint(event.pos):
                    subprocess.Popen([sys.executable, 'singleplayer.py'])
                    running = False
                if multiplayer_button.collidepoint(event.pos):
                    multiplayer_mode = True
        if event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                subprocess.Popen([sys.executable, 'multiplayer.py', input_text])
                running = False
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    if multiplayer_mode:
        draw_button("Connect", pygame.Rect(300, 300, 200, 50), GRAY)
        pygame.draw.rect(screen, WHITE, input_box, 2 if input_active else 1)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(input_text, True, BLACK)
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        input_box.w = max(200, text_surface.get_width() + 10)
    else:
        singleplayer_button = pygame.Rect(300, 200, 200, 50)
        multiplayer_button = pygame.Rect(300, 300, 200, 50)
        draw_button("Singleplayer", singleplayer_button, GRAY)
        draw_button("Multiplayer", multiplayer_button, GRAY)

    pygame.display.flip()

pygame.quit()
sys.exit()
