import random

import pygame


class EnemyPlane(object):
    def __init__(self, screen_temp):
        self.x = random.randint(15, 480)
        self.y = 0
        self.image = pygame.image.load("./img/enemy.png")
        self.screen = screen_temp
        self.bullet_list = []
        self.hit = False
        self.bomb_list = []
        self.image_num = 0
        self.image_index = 0

        self.k = random.randint(1, 20)
        if self.k <= 10:
            self.direction = "right"
        elif self.k > 10:
            self.direction = "left"

    def display(self, hero):

        if not self.hit:
            self.screen.blit(self.image, (self.x, self.y))
        else:
            pass

        for bullet in self.bullet_list:
            bullet.display()
            if (bullet.move(hero)):
                self.bullet_list.remove(bullet)

    def move(self):

        d1 = random.uniform(1, 3)
        d2 = random.uniform(0.2, 3)
        p1 = random.uniform(50, 100)
        p2 = random.uniform(-200, 0)
        if self.direction == "right":
            self.x += d1
        elif self.direction == "left":
            self.x -= d1

        if self.x > 480 - p1:

            self.direction = "left"
        elif self.x < p2:
            self.direction = "right"
        self.y += d2

    def bomb(self):
        self.hit = True


class EnemyPlanes(EnemyPlane):
    def __init__(self, screen_temp):
        EnemyPlane.__init__(self, screen_temp)
        self.num = 0
        self.enemy_list = []
        self.screen = screen_temp

    def add_enemy(self, num):

        self.num = num
        for i in range(num):
            enemy = EnemyPlane(self.screen)
            self.enemy_list.append(enemy)

    def display(self, hero):
        for i in range(self.num):
            self.enemy_list[i].display(hero)

    def move(self):
        for i in range(self.num):
            self.enemy_list[i].move()