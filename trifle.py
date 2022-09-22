# BIG DAY
# Some trifle details color this game!
import pygame
import random


class Trifle:
    def __init__(self, pig):
        self.settings = pig.settings
        self.screen = pig.screen
        self.screen_rect = self.screen.get_rect()
        self.ship = pig.ship
        self.i = 0
        
        self.text_color = (180, 140, 160)
        
    def trifle_1(self, s, d, f, night):
        s = f'-(S)  {s}'
        x = f'-(D)  {d}'
        z = f'-(F)  {f}'
        self.font = pygame.font.SysFont('georgia', 15)

        if not night:
            self.image_star = pygame.image.load('image/day_star_mini.bmp')
            self.image_chick = pygame.image.load('image/day_chick_mini.bmp')
            self.image_cream = pygame.image.load('image/cream_circle_mini.bmp')
        else:
            self.image_star = pygame.image.load('image/night_star_mini.bmp')
            self.image_chick = pygame.image.load('image/night_chick_mini.bmp')
            self.image_cream = pygame.image.load('image/night_circle_mini.bmp')
        
        self.image_s = self.font.render(
            s, True, self.text_color, self.settings.bg_color)
        self.image_x = self.font.render(
            x, True, self.text_color, self.settings.bg_color)
        self.image_z = self.font.render(
            z, True, self.text_color, self.settings.bg_color)

        self.rect_s = self.image_s.get_rect()
        self.rect_x = self.image_x.get_rect()
        self.rect_z = self.image_z.get_rect()
        self.rect_star = self.image_star.get_rect()
        self.rect_chick = self.image_chick.get_rect()
        self.rect_cream = self.image_cream.get_rect()
        # self.rect2 = self.image2.get_rect()

        self.rect_star = (320, 300)
        self.rect_chick = (320, 350)
        self.rect_cream = (320, 400)
        self.rect_s = (350, 310)
        self.rect_x = (350, 360)
        self.rect_z = (350, 410)

    def display_1(self):
        self.screen.blit(self.image_star, self.rect_star)
        self.screen.blit(self.image_chick, self.rect_chick)
        self.screen.blit(self.image_cream, self.rect_cream)
        self.screen.blit(self.image_s, self.rect_s)
        self.screen.blit(self.image_x, self.rect_x)
        self.screen.blit(self.image_z, self.rect_z)
    
    def trifle_2(self):
        a = [0, 1, 2, 3, 4, 5, 6, 7]
        if a[self.i] == 0:
            tip_1 = 'Star: regular bullets, cute & useful'
            tip_2 = '" can be found in every bubble "'
            self.image = pygame.image.load('image/day_star_mini.bmp')
        elif a[self.i] == 1:
            tip_1 = 'Rocket: special bullets, robust & unstoppable'
            tip_2 = '" can be found only in bubble 2 "'
            self.image = pygame.image.load('image/day_chick_mini.bmp')
        elif a[self.i] == 2:
            tip_1 = 'Cream-holo: unalienable holo in 2.5s'
            tip_2 = '" can be found only in bubble 3 "'
            self.image = pygame.image.load('image/cream_circle_mini.bmp')
        elif a[self.i] == 3:
            tip_1 = 'Bubble 1: release a row of bullets'
            tip_2 = '" easy-showing, pick it anytime you see "'
            self.image = pygame.image.load('image/icon_1.bmp')
        elif a[self.i] == 4:
            tip_1 = 'Bubble 2: release a super plane'
            tip_2 = '" rare one, pick it at last line "'
            self.image = pygame.image.load('image/icon_2.bmp')
        elif a[self.i] == 5:
            tip_1 = 'Bubble 3: release a cream holo'
            tip_2 = '" very rare, pick it when necessary "'
            self.image = pygame.image.load('image/icon_3.bmp')
        elif a[self.i] == 6:
            tip_1 = 'Different types of ship have different'
            tip_2 = 'velocity in specific direction'
            self.image = pygame.image.load('image/rocket_turn_mini.bmp')
        elif a[self.i] == 7:
            tip_1 = "Don't try to deep into the red area"
            tip_2 = "try to live longer and goooooood luck !"
            self.image = pygame.image.load('image/laurel.bmp')
            self.i = -1

        self.i += 1

        self.font = pygame.font.SysFont('georgia', 15)
        self.image_tip_1 = self.font.render(
            tip_1, True, self.text_color, self.settings.bg_color)
        self.image_tip_2 = self.font.render(
            tip_2, True, self.text_color, self.settings.bg_color)
        self.rect_tip_1 = self.image_tip_1.get_rect()
        self.rect_tip_2 = self.image_tip_2.get_rect()
        self.rect_tip_1 = (80, 230)
        self.rect_tip_2 = (80, 250)

        self.rect = self.image.get_rect()
        self.rect = (30, 230)

    def display_2(self):
        self.screen.blit(self.image_tip_1, self.rect_tip_1)
        self.screen.blit(self.image_tip_2, self.rect_tip_2)
        self.screen.blit(self.image, self.rect)
