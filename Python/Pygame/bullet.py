import random

import pygame


class Bullet(object):
    def __init__(self, screen_temp, x_temp, y_temp):
        self.x = x_temp + 40
        self.y = y_temp - 20
        self.image = pygame.image.load("./img/bullet.png")
        self.screen = screen_temp

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 10


class Base(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)
        self.alive = True

    def display(self):
        if self.alive:
            self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 5


class BombBullet(Base):
    def __init__(self, screen_temp):
        Base.__init__(self, screen_temp, random.randint(45, 400), 0, "./img/bomb.png")

    def judge(self, hero):
        if (hero.y <= self.y <= hero.y + 40) and (hero.x <= self.x and self.x <= hero.x + 100):
            self.alive = False
            hero.bomb()

        if self.y >= 850:
            self.y = 0
            self.x = random.randint(45, 400)


class CleanBullet(Base):
    def __init__(self, screen_temp):
        self.alive = False

    def judge(self, hero, enemies):
        global q
        q += 1
        if q == 20:
            self.alive = True
            q = 0
            if (hero.y <= self.y and self.y <= hero.y + 40) and (hero.x <= self.x and self.x <= hero.x + 100):
                self.alive = False
                for enemy in enemies:
                    enemy.hit = True
