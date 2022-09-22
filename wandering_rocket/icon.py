# BIG DAY
import random
from pygame.sprite import Sprite
import pygame


class Icon(Sprite):
    def __init__(self, pig):
        super().__init__()
        self.settings = pig.settings
        self.screen = pig.screen
        self.screen_rect = self.screen.get_rect()

        self.a = random.choice([0, 1])
        self.b = 0

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.right = random.randint(
            self.rect.width, self.settings.screen_width)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.b == 0:
            self.y += 0.08
        elif self.b == 1:
            self.y -= 0.08

        self.rect.y = self.y

        if self.a == 0:
            self.x -= 0.05
        elif self.a == 1:
            self.x += 0.05

        self.rect.x = self.x

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def billiard_x(self):
        if self.a == 1:
            self.a = 0
        elif self.a == 0:
            self.a = 1

    def billiard_y(self):
        if self.b == 0:
            self.b = 1
        else:
            self.b = 0



class Icon_1(Icon):
    def __init__(self, pig):
        self.image = pygame.image.load('image/icon_1.bmp')
        super().__init__(pig)


class Icon_2(Icon):
    def __init__(self, pig):
        self.image = pygame.image.load('image/icon_2.bmp')
        super().__init__(pig)


class Icon_3(Icon):
    def __init__(self, pig):
        self.image = pygame.image.load('image/icon_3.bmp')
        super().__init__(pig)
