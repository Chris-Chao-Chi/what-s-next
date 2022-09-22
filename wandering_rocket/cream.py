# BIG DAY
import pygame


class Cream:
    def __init__(self, pig, night):
        self.settings = pig.settings
        self.screen = pig.screen
        self.screen_rect = self.screen.get_rect()
        self.ship = pig.ship

        if night:
            self.image = pygame.image.load('image/night_circle.bmp')
        else:
            self.image = pygame.image.load('image/cream_circle.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.ship.rect.center

    def draw_cream(self):
        self.rect.center = self.ship.rect.center
        self.screen.blit(self.image, self.rect)
