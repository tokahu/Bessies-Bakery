import pygame
from startbutton import StartButton
from bakerybackgroundfile import Bakery

pygame.init()
# Setting game window dimensions
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Doughville!")

# set up variables for the display
SCREEN_HEIGHT = 597
SCREEN_WIDTH = 1000
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)# Loading the image


bg_image = Bakery(0,0)
play_button = StartButton(500, 200)

# Variables
game_start = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if play_button.rect.collidepoint(event.pos):
                game_start = True

    if not game_start:
        screen.blit(bg_image.image, (0, 0))
        screen.blit(play_button.image, (100, 150))
    else:
        screen.fill((0, 0, 0))

    pygame.display.update()
