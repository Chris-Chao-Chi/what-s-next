# BIG DAY
import pygame.font


class Button:
    def __init__(self, pig):
        self.settings = pig.settings
        self.screen = pig.screen
        self.screen_rect = self.screen.get_rect()

        self.button_color = (218, 162, 214)
        self.text_color = (255, 255, 255)
        self.hi_color = (255, 192, 203)
        self.tips_color = (188, 82, 82)

        self.rect = pygame.Rect(0, 0, 200, 50)
        self.rect.center = self.screen_rect.center


class SayHi(Button):
    def __init__(self, pig):
        super().__init__(pig)
        hi = 'Press "Space" to have a start!'
        # hihi = 'hope you have fun!'
        self.font0 = pygame.font.SysFont('impact', 34)
        self.font1 = pygame.font.SysFont('impact', 32)
        self.font2 = pygame.font.SysFont('georgia', 22)
        self.image0 = self.font0.render(
            'play', True, self.text_color, self.button_color)
        self.image1 = self.font1.render(
            'play', True, self.text_color, self.button_color)
        self.image2 = self.font2.render(
            hi, True, self.hi_color, self.settings.bg_color)

        self.image_rank_button = pygame.image.load('image/Top_Rank_Button.bmp')
        self.image_rank_button_hover = pygame.image.load('image/Top_Rank_Button_Hover.bmp')
        self.image_arrow = pygame.image.load('image/arrow.bmp')

        self.rect0 = self.image0.get_rect()
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()

        self.rect_rank_button = self.image_rank_button.get_rect()
        self.rect_rank_button_hover = self.image_rank_button_hover.get_rect()
        self.rect_arrow = self.image_arrow.get_rect()

        self.rect0 = (166, 300)
        self.rect1 = (168, 302)
        self.rect2 = (59, 347)

        self.rect_rank_button = (260, 400)
        self.rect_rank_button_hover = (258, 398)
        self.rect_arrow = (200, 380)

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.image1, self.rect1)
        self.screen.blit(self.image2, self.rect2)

        self.screen.blit(self.image_rank_button, self.rect_rank_button)
        self.screen.blit(self.image_arrow, self.rect_arrow)

    def draw_hover(self):
        self.screen.blit(self.image_rank_button_hover, self.rect_rank_button_hover)

    def draw_hover_h(self):
        self.screen.blit(self.image0, self.rect0)


class SayTips(Button):
    def __init__(self, pig):
        super().__init__(pig)
        tips_1 = 'Press "s" to fire the stars'
        tips_2 = 'Press "d" to launch a giant rocket'
        tips_3 = 'Press "f" to release cream halo'
        tips_4 = 'Press "Space" to transform the type of rocket'
        tips_5 = 'Press "a" to check the tips'
        self.font = pygame.font.SysFont('georgia', 14)
        self.image3 = self.font.render(
            tips_1, True, self.tips_color, self.settings.bg_color)
        self.image4 = self.font.render(
            tips_2, True, self.tips_color, self.settings.bg_color)
        self.image5 = self.font.render(
            tips_3, True, self.tips_color, self.settings.bg_color)
        self.image6 = self.font.render(
            tips_4, True, self.tips_color, self.settings.bg_color)
        self.image7 = self.font.render(
            tips_5, True, self.tips_color, self.settings.bg_color)

        self.rect3 = self.image3.get_rect()
        self.rect4 = self.image4.get_rect()
        self.rect5 = self.image5.get_rect()
        self.rect6 = self.image6.get_rect()
        self.rect7 = self.image7.get_rect()

        self.rect3.midtop = (315, 500)
        self.rect4.topright = (390, 520)
        self.rect5.topright = (390, 540)
        self.rect6.topright = (395, 560)
        self.rect7.topright = (390, 580)


    def draw_tips(self):
        self.screen.blit(self.image3, self.rect3)
        self.screen.blit(self.image4, self.rect4)
        self.screen.blit(self.image5, self.rect5)
        self.screen.blit(self.image6, self.rect6)
        self.screen.blit(self.image7, self.rect7)

