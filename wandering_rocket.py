# BIG DAY
import sys
import pygame

from settings import Settings
from ship import Ship
from scoring import Scoring
from cream import Cream
from trifle import Trifle
from rank import Rank
from button import SayHi, SayTips
import icon
import bullets
import super_bullets
import plane
import random

import time


class WanderRock:
    def __init__(self):
        pygame.init()
        self.time_1 = None
        self.time_2 = None
        self.p = 0.000
        self.volume = 5
        self.clock = pygame.time.Clock()
        self.chick_vol = 1
        self.cream_times = 0
        self.hip = False
        self.butt = False
        self.bee = False
        self.nightmare = False
        self.onehour = False
        self.ring_true = False
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        """self.board_rect = pygame"""
        # For we need to rectify screen later
        self.line = pygame.Rect(0, 0, 400, 100)
        self.button_hi = SayHi(self)
        self.button_tips = SayTips(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bull_plane = pygame.sprite.Group()
        self.chickens = pygame.sprite.Group()
        self.planes_1 = pygame.sprite.Group()
        self.planes_2 = pygame.sprite.Group()
        # For we need to control each not single bullets, here need Group.
        self.icons_1 = pygame.sprite.Group()
        self.icons_2 = pygame.sprite.Group()
        self.icons_3 = pygame.sprite.Group()

        self.scoring = Scoring(self)
        self.trifle = Trifle(self)
        self.rank = Rank(self)

        pygame.display.set_caption('Rocket Rocket!!')
        self.game_state = False
        # self._start_timer(1)

    def run_game(self):
        # Tiny little quit a few time in each circle
        while True:
            self._check_event()
            # Block of fresh parts
            if self.game_state:
                self.ship.update()
                self._update_icon()
                self._update_bullets()
                self._update_planes()

            self._update_screen()
            # Pay attention to the order!!

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            if event.type == pygame.KEYUP:
                self._check_keyup(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mouse()

    def _update_bullets(self):
        self.bullets.update()
        self.bull_plane.update()
        self.chickens.update()

        for bullet in self.bullets.copy():
            if bullet.rect.y < 0:
                self.bullets.remove(bullet)

        for bull in self.bull_plane.copy():
            if bull.rect.y < 0:
                self.bullets.remove(bull)

        for chick in self.chickens.copy():
            if chick.rect.y < 0 or chick.rect.x < 0:
                self.chickens.remove(chick)

        collisions_1 = pygame.sprite.groupcollide(
            self.bullets, self.planes_1, True, True)

        collisions_2 = pygame.sprite.groupcollide(
            self.bullets, self.planes_2, True, True)

        collision_3 = pygame.sprite.groupcollide(
            self.bull_plane, self.planes_1, False, True)

        collision_4 = pygame.sprite.groupcollide(
            self.bull_plane, self.planes_2, False, True)

        collision_5 = pygame.sprite.groupcollide(
            self.chickens, self.planes_1, False, True)

        collision_6 = pygame.sprite.groupcollide(
            self.chickens, self.planes_2, False, True)

        if self.hip and self.butt:
            pygame.sprite.spritecollide(self.cream, self.planes_1, True)
            pygame.sprite.spritecollide(self.cream, self.planes_2, True)

        # if collisions_1 or collision_3 or collision_5:
        #     self.scoring.score += 1
        # if collisions_2 or collision_4 or collision_6:
        #     self.scoring.score += 5

        self.time_2 = time.time()
        gap = self.time_2 - self.time_1
        self.scoring.time = gap

        self.p += 0.002
        if round(self.p, 3) == int(self.p) + 0.002:
            self._start_timer()

    def _update_planes(self):
        # self.planes.add(*self.planes_1, *self.planes_2)
        # It's hard to remove every elements, so we don't use
        self.planes_1.update()
        self.planes_2.update()

        for plane in self.planes_1.copy():
            if plane.rect.x < 0 or plane.rect.right > self.settings.screen_width:
                plane.billiard()
            if plane.rect.y > self.settings.screen_height:
                self.planes_1.remove(plane)
        for plane in self.planes_2.copy():
            if plane.rect.x < 0 or plane.rect.right > self.settings.screen_width:
                plane.billiard()
            if plane.rect.y > self.settings.screen_height:
                self.planes_2.remove(plane)

        for bull in self.bull_plane.copy():
            if bull.rect.x < 0 or bull.rect.right > self.settings.screen_width:
                bull.billiard()
            if bull.rect.y < 0:
                self.bull_plane.remove(bull)

        if pygame.sprite.spritecollideany(self.ship, self.planes_1):
            self._ship_hit()
        if pygame.sprite.spritecollideany(self.ship, self.planes_2):
            self._ship_hit()

    def _update_icon(self):
        self.icons_1.update()
        self.icons_2.update()
        self.icons_3.update()

        for icon in self.icons_1.copy():
            if icon.rect.x < 0 or icon.rect.right > self.settings.screen_width:
                icon.billiard_x()
            if icon.rect.y < 0 or icon.rect.bottom > self.settings.screen_height:
                icon.billiard_y()
        for icon in self.icons_2.copy():
            if icon.rect.x < 0 or icon.rect.right > self.settings.screen_width:
                icon.billiard_x()
            if icon.rect.y < 0 or icon.rect.bottom > self.settings.screen_height:
                icon.billiard_y()
        for icon in self.icons_3.copy():
            if icon.rect.x < 0 or icon.rect.right > self.settings.screen_width:
                icon.billiard_x()
            if icon.rect.y < 0 or icon.rect.bottom > self.settings.screen_height:
                icon.billiard_y()

        sign_1 = pygame.sprite.spritecollideany(self.ship, self.icons_1)
        if sign_1:
            self.icons_1.remove(sign_1)
            self._surprise_1()

        sign_2 = pygame.sprite.spritecollideany(self.ship, self.icons_2)
        if sign_2:
            self.icons_2.remove(sign_2)
            self._surprise_2()

        sign_3 = pygame.sprite.spritecollideany(self.ship, self.icons_3)
        if sign_3:
            self.icons_3.remove(sign_3)
            self._surprise_3()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        if self.ship.rect.top < 200:
            self.screen.fill((240, 230, 230), self.line)
        if self.bee:
            if self.game_state:
                self.trifle.display_1()
            else:
                self.trifle.display_2()
        if self.hip:
            if self.time_2 - self.t < float(2.5):
                self.butt = True
                self.cream.draw_cream()
            else:
                self.butt = False
                self.ship.decelerate()
        self.ship.draw_rocket()
        if self.game_state:
            for bullet in self.bullets.sprites():
                bullet.draw()
            for plane in self.planes_1.sprites():
                plane.draw_plane()
            for plane in self.planes_2.sprites():
                plane.draw_plane()
            for icon in self.icons_1.sprites():
                icon.draw()
            for icon in self.icons_2.sprites():
                icon.draw()
            for icon in self.icons_3.sprites():
                icon.draw()
            for bull in self.bull_plane.sprites():
                bull.draw_plane()
            for chick in self.chickens.sprites():
                chick.draw()
        elif not self.game_state:
            self.mouse = pygame.mouse.get_pos()
            if not self.nightmare:
                self.button_hi.draw_button()
                self.button_tips.draw_tips()
                if 260 < self.mouse[0] < 360 and 400 < self.mouse[1] < 433:
                    self.button_hi.draw_hover()
                elif 168 < self.mouse[0] < 233 and 302 < self.mouse[1] < 348:
                    self.button_hi.draw_hover_h()
                if self.ring_true:
                    self.rank.sweet_tips()
            else:
                self.rank.draw_board()
                if 330 < self.mouse[0] < 350 and 220 < self.mouse[1] < 240:
                    self.rank.draw_hover()
                self.bee = False

        self.scoring.show_timing()

        pygame.display.flip()

    def _check_keydown(self, event):
        # Actually you cannot press two different key at a same time
        # So if-elif is OK!
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE and not self.nightmare:
            self._daisy()
        elif event.key == pygame.K_s:
            self._create_superb()
        elif event.key == pygame.K_a:
            self._check_trifles()
        elif event.key == pygame.K_b:
            self._create_icon()
        elif event.key == pygame.K_d:
            self._chick_chick()
        elif event.key == pygame.K_f:
            self._cream()
        elif event.key == pygame.K_r and not self.game_state:
            self._nightmare()

        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    def _check_keyup(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_mouse(self):
        if 260 < self.mouse[0] < 360 and 400 < self.mouse[1] < 433 and not self.nightmare:
            self._nightmare()
        elif 330 < self.mouse[0] < 350 and 220 < self.mouse[1] < 240 and self.nightmare:
            self._nightmare()
        elif 168 < self.mouse[0] < 233 and 302 < self.mouse[1] < 348 and not self.nightmare:
            self._daisy()

    def _create_bullet(self):
        new_bullet1 = bullets.Bullets1(self)
        new_bullet2 = bullets.Bullets2(self)
        self.bullets.add(new_bullet1, new_bullet2)

    def _create_superb(self):
        if self.volume > 0:
            new_superb_1 = super_bullets.SuperB1(self, self.onehour)
            new_superb_2 = super_bullets.SuperB2(self, self.onehour)
            new_superb_3 = super_bullets.SuperB3(self, self.onehour)
            self.bullets.add(new_superb_1, new_superb_2, new_superb_3)

            self.volume -= 1

    def _create_planes(self):
        a = random.randint(1, 6)
        if a < 6:
            new_plane_1 = plane.Plane1(self)
            self.planes_1.add(new_plane_1)
        else:
            new_plane_2 = plane.Plane2(self)
            self.planes_2.add(new_plane_2)

    def _start_timer(self):
        self._create_planes()
        a = random.randint(1, 30)
        if a < 2:
            self._create_icon()
        # timer = threading.Timer(interval, self._start_timer, [interval])
        # timer.start()

    def _ship_hit(self):
        time.sleep(0.2)
        self.game_state = False
        self.bee = False
        self.ship.rect.midbottom = self.screen.get_rect().midbottom
        self.topRank()

    def _daisy(self):
        if not self.game_state:
            self.game_state = True
            self.bee = False
            self.onehour = False
            self.nightmare = False
            self.ring_true = False
            self.bullets.empty()
            self.planes_1.empty()
            self.planes_2.empty()
            self.bull_plane.empty()
            self.icons_1.empty()
            self.icons_2.empty()
            self.icons_3.empty()
            self.time_1 = time.time()
            self.volume = 5
            self.chick_vol = 1
            self.cream_times = 1
            self.ship = Ship(self)
            self.cream = Cream(self, self.onehour)
            self.scoring = Scoring(self)
        else:
            self.ship.transform()
            if self.scoring.time > 90 and not self.onehour:
                self.ship.day2night()
                self.onehour = True
                self.cream = Cream(self, self.onehour)
                self.scoring.show_nighttime()
            # self._create_bullet()

    def _create_icon(self):
        a = random.randint(1, 6)
        if a == 1 or a == 2:
            new_icon_1 = icon.Icon_1(self)
            self.icons_1.add(new_icon_1)
        elif a == 3:
            new_icon_2 = icon.Icon_2(self)
            self.icons_2.add(new_icon_2)
        elif a == 4:
            new_icon_3 = icon.Icon_3(self)
            self.icons_3.add(new_icon_3)
        elif a == 5 and not self.onehour:
            new_icon_1 = icon.Icon_1(self)
            self.icons_1.add(new_icon_1)
        elif a == 6 and not self.onehour:
            new_icon_2 = icon.Icon_2(self)
            self.icons_2.add(new_icon_2)

    def _surprise_1(self):
        for i in range(1, 13):
            demo = super_bullets.SuperB4(self, self.onehour)
            demo.rect.x = 30 * i
            self.bullets.add(demo)

        self.volume += 2

    def _surprise_2(self):
        demo_yo = plane.Plane3(self)
        self.bull_plane.add(demo_yo)
        self.volume += 2
        self.chick_vol += 1

    def _surprise_3(self):
        self.volume += 4
        self.cream_times += 2
        self._cream()

    def _chick_chick(self):
        if self.game_state and self.chick_vol > 0:
            new_chick = super_bullets.SuperB5(self, self.onehour)
            self.chickens.add(new_chick)

            self.chick_vol -= 1

    def _cream(self):
        if self.game_state and self.cream_times > 0:
            self.t = self.time_2
            self.hip = True
            self.ship.accelerate()
            self.cream_times -= 1

    def _check_trifles(self):
        if not self.bee:
            self.bee = True
        elif self.bee and self.game_state:
            self.bee = False

        if self.game_state and self.bee:
            self.trifle.trifle_1(self.volume, self.chick_vol,
                                 self.cream_times, self.onehour)

        if not self.game_state and self.bee:
            self.trifle.trifle_2()

    def _nightmare(self):
        if not self.nightmare:
            self.nightmare = True
        else:
            self.nightmare = False

    def topRank(self):
        self.ring_true = self.rank.update(self.scoring.time)
        self.nightmare = self.ring_true


if __name__ == '__main__':
    pig = WanderRock()
    pig.run_game()
