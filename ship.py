# BIG DAY
import pygame


class Ship:
    def __init__(self, pig):
        self.screen = pig.screen
        self.settings = pig.settings
        self.screen_rect = pig.screen.get_rect()
        self.sign = 0
        self.toe = False
        self.r = None
        self.onehour = False

        self.image = pygame.image.load('image/rocket.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # If outside code haven't refresh signal to True, then it's False.
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        # self.sign means the type of rocket!
        if not self.toe:
            if self.moving_left and self.rect.left >= 0:
                self.x -= (0.15 + self.sign/6.66)
            if self.moving_right and self.rect.right < self.settings.screen_width:
                self.x += (0.15 + self.sign/6.66)
            if self.moving_up and self.rect.top >= 0:
                self.y -= (0.3 - self.sign/6.66)
            if self.moving_down and self.rect.bottom <= self.settings.screen_height:
                self.y += (0.3 - self.sign/6.66)
        else:
            if self.moving_left and self.rect.left >= 0:
                self.x -= (0.3 + self.sign/3.33)
            if self.moving_right and self.rect.right < self.settings.screen_width:
                self.x += (0.3 + self.sign/3.33)
            if self.moving_up and self.rect.top >= 0:
                self.y -= (0.6 - self.sign/3.33)
            if self.moving_down and self.rect.bottom <= self.settings.screen_height:
                self.y += (0.6 - self.sign/3.33)


        self.rect.x = self.x
        self.rect.y = self.y

    def draw_rocket(self):
        # Method blit used to draw image
        if self.sign == 0:
            if self.onehour:
                self.image = pygame.image.load('image/night_rocket.bmp')
            else:
                self.image = pygame.image.load('image/rocket.bmp')
            self.r = self.image.get_rect()
            self.r.center = self.rect.center
            self.rect = self.r
        elif self.sign == 1:
            if self.onehour:
                self.image = pygame.image.load('image/night_rocket_turn.bmp')
            else:
                self.image = pygame.image.load('image/rocket_turn.bmp')
            self.r = self.image.get_rect()
            self.r.center = self.rect.center
            self.rect = self.r

        self.screen.blit(self.image, self.rect)

    def transform(self):
        if self.sign == 0:
            self.sign = 1
        else:
            self.sign = 0

    def accelerate(self):
        self.toe = True

    def decelerate(self):
        self.toe = False

    def day2night(self):
        self.onehour = True

