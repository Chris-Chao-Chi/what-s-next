# BIG DAY
import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):
    def __init__(self, pig):
        super().__init__()

        self.screen = pig.screen
        self.settings = pig.settings
        self.ship = pig.ship
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = self.ship.rect.midtop

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y -= 0.4
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bullets1(Bullets):
    def __init__(self, pig):
        super().__init__(pig)

        self.rect.x -= 4


class Bullets2(Bullets):
    def __init__(self, pig):
        super().__init__(pig)

        self.rect.x += 4



