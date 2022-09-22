# BIG DAY
import pygame
from pygame.sprite import Sprite


class SuperBullets(Sprite):
    def __init__(self, pig, night):
        super().__init__()
        self.ship = pig.ship
        self.screen = pig.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = pig.settings

        if not night:
            self.image = pygame.image.load('image/day_star.bmp')
        else:
            self.image = pygame.image.load('image/night_star.bmp')
        self.rect = self.image.get_rect()
        self.rect.midtop = self.ship.rect.midtop

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y -= 0.45
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)


class SuperB1(SuperBullets):
    def __init__(self, pig, night):
        super().__init__(pig, night)


class SuperB2(SuperBullets):
    def __init__(self, pig, night):
        super().__init__(pig, night)

    def update(self):
        self.x -= 0.12
        self.y -= 0.45
        self.rect.x = self.x
        self.rect.y = self.y


class SuperB3(SuperBullets):
    def __init__(self, pig, night):
        super().__init__(pig, night)

    def update(self):
        self.x += 0.12
        self.y -= 0.45
        self.rect.x = self.x
        self.rect.y = self.y


class SuperB4(SuperBullets):
    def __init__(self, pig, night):
        super().__init__(pig, night)

        if not night:
            self.image = pygame.image.load('image/daffodil&daisy.bmp')
        else:
            self.image = pygame.image.load('image/sky&wish.bmp')
        self.rect = self.image.get_rect()

    def update(self):
        self.y -= 0.4
        self.rect.y = self.y


class SuperB5(SuperBullets):
    def __init__(self, pig, night):
        super().__init__(pig, night)

        if not night:
            self.image = pygame.image.load('image/day_chick.bmp')
        else:
            self.image = pygame.image.load('image/night_chick.bmp')
        self.rect = self.image.get_rect()

    def update(self):
        self.y -= 0.5
        self.rect.x = self.x
        self.rect.y = self.y
