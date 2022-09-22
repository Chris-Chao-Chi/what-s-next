# BIG DAY
import pygame


class Rank:
    def __init__(self, pig):
        self.screen = pig.screen
        self.image = pygame.image.load('image/Top_Rank_Board.bmp')
        self.image_cross = pygame.image.load('image/cross.bmp')
        self.image_cross_hover = pygame.image.load('image/cross_hover.bmp')
        self.image_congratulation = pygame.image.load('image/congratu.bmp')

        self.rect = self.image.get_rect()
        self.rect_cross = self.image_cross.get_rect()
        self.rect_cross_hover = self.image_cross_hover.get_rect()
        self.rect_congratulations = self.image_congratulation.get_rect()

        self.rect = (40, 200)
        self.rect_cross = (330, 220)
        self.rect_cross_hover = (328, 218)
        self.rect_congratulations = (122, 50)

        self.rank_time = []
        self.initial_the_time()
        self.minimum_time = (min(self.rank_time))

        self.text_color = (57, 55, 50)
        self.top_one_color = (161, 11, 75)
        self.top_two_color = (15, 64, 186)
        self.top_three_color = (160, 122, 6)
        self.board_color = (252, 247, 243)
        self.wow_color = (172, 86, 121)
        self.font = pygame.font.SysFont('georgia', 15)
        self.sweet_font = pygame.font.SysFont('georgia', 12)
        self.want2die(self.rank_time)

        self.era = False
        self.rank = 5

    def draw_board(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image_cross, self.rect_cross)

        self.screen.blit(self.image_0, self.rect_0)
        self.screen.blit(self.image_1, self.rect_1)
        self.screen.blit(self.image_2, self.rect_2)
        self.screen.blit(self.image_3, self.rect_3)
        self.screen.blit(self.image_4, self.rect_4)
        self.screen.blit(self.image_5, self.rect_5)

        if self.era and self.rank < 3:
            self.screen.blit(self.image_congratulation, self.rect_congratulations)
        if self.era:
            self.screen.blit(self.image_wow, self.rect_wow)

    def update(self, this_game_time):
        mino = float(self.minimum_time)
        mino = round(mino, 2)
        t = round(this_game_time, 2)
        if mino < t:
            self.rank_time.append(t)
            self.rank_time.sort(reverse=True)
            self.rank = self.new_era(t)
            for i in [0, 1, 2, 3, 4, 5]:
                with open(f'time/time_{i}', 'w') as file:
                    file.write(f'{self.rank_time[i]}')
            self.want2die(self.rank_time)
            return True
        else:
            return False

    def initial_the_time(self):
        for i in [0, 1, 2, 3, 4, 5]:
            with open(f'time/time_{i}') as file:
                cont = file.read()
                self.rank_time.append(float(cont))
                self.rank_time.sort(reverse=True)

    def want2die(self, rank_time):
        self.time_0 = rank_time[0]
        self.time_1 = rank_time[1]
        self.time_2 = rank_time[2]
        self.time_3 = rank_time[3]
        self.time_4 = rank_time[4]
        self.time_5 = rank_time[5]

        self.image_0 = self.font.render(f'{self.time_0}', True,
                                        self.top_one_color, self.board_color)
        self.image_1 = self.font.render(f'{self.time_1}', True,
                                        self.top_two_color, self.board_color)
        self.image_2 = self.font.render(f'{self.time_2}', True,
                                        self.top_three_color, self.board_color)
        self.image_3 = self.font.render(f'{self.time_3}', True,
                                        self.text_color, self.board_color)
        self.image_4 = self.font.render(f'{self.time_4}', True,
                                        self.text_color, self.board_color)
        self.image_5 = self.font.render(f'{self.time_5}', True,
                                        self.text_color, self.board_color)

        self.rect_0 = self.image_0.get_rect()
        self.rect_1 = self.image_1.get_rect()
        self.rect_2 = self.image_2.get_rect()
        self.rect_3 = self.image_3.get_rect()
        self.rect_4 = self.image_4.get_rect()
        self.rect_5 = self.image_5.get_rect()

        self.rect_0 = (120, 285)
        self.rect_1 = (120, 335)
        self.rect_2 = (120, 385)
        self.rect_3 = (265, 285)
        self.rect_4 = (265, 335)
        self.rect_5 = (265, 385)

    def draw_hover(self):
        self.screen.blit(self.image_cross_hover, self.rect_cross_hover)

    def new_era(self, t):
        self.era = True
        for i in [0, 1, 2, 3, 4, 5]:
            if t == self.rank_time[i]:
                self.image_wow = self.font.render('<-', True, self.wow_color, self.board_color)
                self.image_sweet = self.sweet_font.render(f'-->>new rank {i+1}', True, self.wow_color, (255, 255, 255))
                self.rect_wow = self.image_wow.get_rect()
                self.rect_sweet = self.image_sweet.get_rect()
                self.rect_sweet = (280, 440)

                if i < 3:
                    self.rect_wow = (185, 285+i*50)
                else:
                    self.rect_wow = (330, 285+(i-3)*50)
                return i

    def sweet_tips(self):
        self.screen.blit(self.image_sweet, self.rect_sweet)
