# BIG DAY
import pygame


class Scoring:
    def __init__(self, pig):
        self.settings = pig.settings
        self.screen = pig.screen
        self.screen_rect = self.screen.get_rect()


        self.text_color = (150, 10, 30)
        self.font = pygame.font.SysFont('georgia', 22)

        self.score = 0
        self.time = 0
        self.time = float(self.time)

    def show_timing(self):
        self.t = round(self.time, 2)
        time = str(self.t)
        self.image = self.font.render(
            time, True, self.text_color, self.settings.bg_color)
        self.rect = self.image.get_rect()
        self.rect.left = self.screen_rect.left + 15
        self.rect.top = 15

        self.screen.blit(self.image, self.rect)

    def show_nighttime(self):
        self.text_color = (10, 10, 50)
