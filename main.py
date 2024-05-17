import pygame
from startbutton import StartButton
from bakerybackgroundfile import Bakery
from counterbgfile import Counter
from backbuttonfile import Back
from musicbuttonfile import MusicButton

pygame.init()
pygame.font.init()
pygame.mixer.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Doughville!")



music = pygame.mixer.music.load('BakerySoundtrack.mp3')



# set up variables for the display
SCREEN_HEIGHT = 597
SCREEN_WIDTH = 1000
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)


bg_image = Bakery(0,0)
play_button = StartButton(400, 250)
counter_screen = Counter(0,0)
back_button = Back(895,20)
music_button = MusicButton(20, 20)

# Variables
game_start = False
music = False
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if play_button.rect.collidepoint(event.pos):
                game_start = True
            if back_button.rect.collidepoint((event.pos)):
                game_start = False
            if music_button.rect.collidepoint((event.pos)):
                music = True



    if not game_start:
        screen.blit(bg_image.image, (0, 0))
        screen.blit(play_button.image, (400, 250))
    else:
        screen.fill((0, 0, 0))
        screen.blit(counter_screen.image, (0, 0))
        screen.blit(back_button.image, (895, 20))
    if music:
        pygame.mixer.music.play(-1)
    screen.blit(music_button.image, (20, 20))

    pygame.display.update()
