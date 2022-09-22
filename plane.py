# BIG DAY
import pygame
from pygame.sprite import Sprite
import random


class Plane(Sprite):
    def __init__(self, pig):
        super().__init__()

        self.screen = pig.screen
        self.settings = pig.settings
        self.ship = pig.ship

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.right = random.randint(
            self.rect.width, self.settings.screen_width)

        self.a = random.choice([0, 1])
        self.b = random.choice([0, 1, 2])

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.b == 0:
            self.y += 0.015
        elif self.b == 1:
            self.y += 0.025
        elif self.b == 2:
            self.y += 0.035

        self.rect.y = self.y

        if self.a == 0:
            self.x -= 0.06
        elif self.a == 1:
            self.x += 0.06

        self.rect.x = self.x

    def draw_plane(self):
        self.screen.blit(self.image, self.rect)

    def billiard(self):
        if self.a == 1:
            self.a = 0
        elif self.a == 0:
            self.a = 1


class Plane1(Plane):
    def __init__(self, pig):
        self.image = pygame.image.load('image/pure_plane.bmp')
        super().__init__(pig)


class Plane2(Plane):
    def __init__(self, pig):
        self.image = pygame.image.load('image/reddish_plane.bmp')
        super().__init__(pig)
        self.x_velocity = random.choice([3, 5, 7, 8])
        self.y_velocity = random.choice([2, 3, 4, 5])

    def update(self):
        self.y += self.y_velocity/100

        if self.a == 0:
            self.x -= self.x_velocity/100
        elif self.a == 1:
            self.x += self.x_velocity/100

        self.rect.x = self.x
        self.rect.y = self.y

    def billiard(self):
        if self.a == 1:
            self.a = 0
        elif self.a == 0:
            self.a = 1


class Plane3(Sprite):
    def __init__(self, pig):
        super().__init__()
        self.screen = pig.screen
        self.ship = pig.ship
        self.a = random.choice([0, 1])
        if self.a == 0:
            self.image = pygame.image.load('image/biplane_turn.bmp')
        elif self.a == 1:
            self.image = pygame.image.load('image/biplane.bmp')

        self.rect = self.image.get_rect()
        self.rect.midtop = self.ship.rect.midtop

        if self.rect.x < 30:
            self.rect.x = 40
        if self.rect.x > 320:
            self.rect.x = 320

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.a == 0:
            self.x -= 0.05
        elif self.a == 1:
            self.x += 0.05

        self.y -= 0.06
        self.rect.x = self.x
        self.rect.y = self.y

    def billiard(self):
        if self.a == 1:
            self.a = 0
            self.image = pygame.image.load('image/biplane_turn.bmp')
        elif self.a == 0:
            self.a = 1
            self.image = pygame.image.load('image/biplane.bmp')

        self.rect = self.image.get_rect()

    def draw_plane(self):
        self.screen.blit(self.image, self.rect)

