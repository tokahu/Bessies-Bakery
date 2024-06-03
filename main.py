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
from forwardarrowfile import ForwardArrow
from backwardsarrowfile import BackArrow
from speechbubblefile import SpeechBubble
from wholeeggfile import WholeEgg

pygame.init()
pygame.font.init()
pygame.mixer.init()
my_font = pygame.font.SysFont('elephant', 40)
fonts = pygame.font.get_fonts()
print(fonts)
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
forwardarrow = ForwardArrow(895, 490)
backarrow = BackArrow(20,490)
bubble = SpeechBubble(150, 100)
wholeegg = WholeEgg(230, 80)

music = pygame.mixer.music.load('BakerySoundtrack.mp3')
pygame.mixer.music.play(-1)

# Game Logic
toppings = ["chocolate_chips", "almonds", "coconut", "sprinkles", "marshmallows", "strawberries"]
selected_topping = random.choice(toppings)
print(selected_topping)
display_topping_text = my_font.render(selected_topping, True, (0, 0, 0))



# Variables
scene = 0
# scene 0 = home screen
# scene 1 = order station
# scene 2 = ingredient mixing place
game_start = False
cooking = False
music = True
draggingbutter = False
draggingegg = False
butterin = False

# Main game loop

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if play_button.rect.collidepoint(event.pos) and scene == 0:
                scene += 1
            if forwardarrow.rect.collidepoint(event.pos):
                scene += 1
            if backarrow.rect.collidepoint(event.pos):
                scene -= 1
            if back_button.rect.collidepoint(event.pos):
                scene = 0
            if music_button.rect.collidepoint(event.pos):
                music = not music
            if butter.rect.collidepoint((500,250)):
                butterin = True
            elif event.button == 1:
                dragging = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if butter.rect.collidepoint(event.pos):
                    draggingbutter = True
                if wholeegg.rect.collidepoint(event.pos):
                    draggingegg = True
        elif event.type == pygame.MOUSEMOTION:
            if draggingbutter:
                butter.rect.move_ip(event.rel)
            if draggingegg:
                wholeegg.rect.move_ip(event.rel)

    if scene == 0:
        screen.fill((0, 0, 0))
        screen.blit(bg_image.image, (0, 0))
        screen.blit(play_button.image, (400, 250))
    elif scene == 1:
        screen.fill((0, 0, 0))
        screen.blit(counter_screen.image, (0, 0))
        screen.blit(back_button.image, (895, 20))
        screen.blit(music_button.image, (20, 20))
        screen.blit(forwardarrow.image,(895, 490))
        screen.blit(backarrow.image, (20, 490))
        screen.blit(bubble.image, (150,100))
        screen.blit(display_topping_text, (195, 200))
    elif scene == 2:
        screen.fill((0,0,0))
        screen.blit(close_counter_screen.image, (0, 0))
        screen.blit(back_button.image, (895, 20))
        screen.blit(forwardarrow.image,(895, 490))
        screen.blit(backarrow.image, (20, 490))
        screen.blit(music_button.image, (20, 20))
        screen.blit(mixing_bowl.image, (230, 50))
        if not butterin:
            screen.blit(butter.image, butter.rect)
        elif butterin:
            screen.blit(meltedbutter.image, (230, 80))
        screen.blit(wholeegg.image, (230, 80))
    elif scene == 3:
        screen.fill((0,0,0))
        screen.blit(forwardarrow.image, (895, 490))
        screen.blit(backarrow.image, (20, 490))
        screen.blit(back_button.image, (895, 20))

    if not music:
        pygame.mixer.music.pause()
        screen.blit(no_music_button.image, (20, 20))
    if music:
        pygame.mixer.music.unpause()
        screen.blit(music_button.image, (20, 20))


    pygame.display.update()
