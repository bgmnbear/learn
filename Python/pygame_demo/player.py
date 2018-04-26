import pygame

import game_config
from bullet import Bullet


class Player(object):
    def __init__(self, screen_temp):
        self.x = 210
        self.y = 700
        self.life = 21
        self.image = pygame.image.load("./img/player.png")
        self.screen = screen_temp
        self.bullet_list = []
        self.hit = False

    def display(self):
        if self.hit:
            exit()
        else:
            if self.x < 0:
                self.x = 0
            elif self.x > 382:
                self.x = 382
            if self.y < 0:
                self.y = 0
            elif self.y > 750:
                self.y = 750
            self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def fire(self):
        bullet = Bullet(self.screen, self.x, self.y)
        self.bullet_list.append(bullet)

    def bomb(self):
        self.hit = True

    def judge(self):
        if game_config.life <= 0:
            self.bomb()
