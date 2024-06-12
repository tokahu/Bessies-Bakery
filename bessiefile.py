import pygame

class Bessie:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("bessie.png")
        self.image_size = self.image.get_size()
        #self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])