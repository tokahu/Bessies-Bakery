import pygame
import random
from startbutton import StartButton
from bakerybackgroundfile import Bakery
from counterbgfile import Counter
from closeupcounterfile import CloseCounter
from backbuttonfile import Back
from musicbuttonfile import MusicButton
from nomusicbuttonfile import NoMusicButton
from mixingbowlfile import Bowl
from butterfile import Butter
from buttermeltedfile import MeltedButter
from arrowfile import Arrow

pygame.init()
pygame.font.init()
pygame.mixer.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Doughville!")






# set up variables for the display
SCREEN_HEIGHT = 597
SCREEN_WIDTH = 1000
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)


bg_image = Bakery(0,0)
play_button = StartButton(400, 250)
counter_screen = Counter(0,0)
close_counter_screen = CloseCounter(0,0)
back_button = Back(895,20)
music_button = MusicButton(20, 20)
no_music_button = NoMusicButton(20,20)
mixing_bowl = Bowl(300, 250)
butter = Butter(700, 300)
meltedbutter = MeltedButter(500,250)
arrow = Arrow(895, 490)

music = pygame.mixer.music.load('BakerySoundtrack.mp3')
pygame.mixer.music.play(-1)

# Game Logic
toppings = ["chocolate_chips", "almonds", "coconut", "sprinkles", "marshmallows", "strawberries"]
selected_topping = random.choice(toppings)
print(selected_topping)




# Variables
game_start = False
cooking = False
music = True
dragging = False
butterin = False

# Main game loop

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if play_button.rect.collidepoint(event.pos):
                game_start = True
            if arrow.rect.collidepoint(event.pos):
                cooking = True
            if back_button.rect.collidepoint(event.pos):
                game_start = False
            if music_button.rect.collidepoint(event.pos):
                music = not music
            if butter.rect.collidepoint((500,250)):
                butterin = True
            elif event.button == 1:
                dragging = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if butter.rect.collidepoint(event.pos):
                    dragging = True
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                butter.rect.move_ip(event.rel)

    if not game_start:
        screen.fill((0, 0, 0))
        screen.blit(bg_image.image, (0, 0))
        screen.blit(play_button.image, (400, 250))
    else:
        screen.fill((0, 0, 0))
        screen.blit(counter_screen.image, (0, 0))
        screen.blit(back_button.image, (895, 20))
        screen.blit(music_button.image, (20, 20))
        screen.blit(arrow.image,(895, 490))
    if cooking:
        screen.fill((0,0,0))
        screen.blit(close_counter_screen.image, (0, 0))
        screen.blit(back_button.image, (895, 20))
        screen.blit(music_button.image, (20, 20))
        screen.blit(mixing_bowl.image, (230, 50))
        screen.blit(butter.image, butter.rect)
    if butterin:
        screen.blit(butter.image, (-10000, -10000))
        screen.blit(mixing_bowl.image, (230, 50))
        screen.blit(meltedbutter.image, (230, 80))

    if not music:
        pygame.mixer.music.pause()
        screen.blit(no_music_button.image, (20, 20))
    if music:
        pygame.mixer.music.unpause()
        screen.blit(music_button.image, (20, 20))




    pygame.display.update()
