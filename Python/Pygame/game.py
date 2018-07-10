# -*- coding:utf-8 -*-
import random

import pygame
from pygame.locals import *

from bullet import BombBullet
from enemy import EnemyPlanes
from player import Player


def judge(hero, enemy):
    for bullet1 in hero.bullet_list:
        if bullet1.y in range(int(enemy.y), int(enemy.y + 30)) and bullet1.x in range(int(enemy.x - 10),
                                                                                      int(enemy.x + 50)):
            hero.bullet_list.remove(bullet1)
            enemy.bomb()
        if bullet1.y < 0 or bullet1.x < 0 or bullet1.x > 480:
            hero.bullet_list.remove(bullet1)


def clear_enemy(enemies):
    global goal, goal0
    for enemy in enemies.enemy_list:
        if enemy.hit == True and enemy.image_index == 3:
            enemies.enemy_list.remove(enemy)
            enemies.num -= 1
            goal += 1
            goal0 += 5
            print("goal = %d" % goal)
        if enemy.y >= 850:
            enemies.enemy_list.remove(enemy)
            enemies.num -= 1


def judge_num(enemies):
    n = random.randint(1, 5)
    if len(enemies.enemy_list) == 0:
        enemies.add_enemy(n)


def creat_bomb(screen_temp):
    bomb = BombBullet(screen_temp)
    bomb_list = []
    bomb_list.append(bomb)


def main():
    move_x = 0
    move_y = 0
    pygame.init()
    screen = pygame.display.set_mode((480, 852), 0, 32)

    background = pygame.image.load("./img/background.png")
    pygame.display.set_caption("辣鸡飞机大战")

    hero = Player(screen)

    enemies = EnemyPlanes(screen)
    enemies.add_enemy(5)

    bomb = BombBullet(screen)

    left_key, right_key, up_key, down_key, done = 0, 0, 0, 0, 0

    while True:
        if done:
            if done % 8 == 0:
                done = 1
                hero.fire()
            else:
                done += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()

            if event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:

                    move_x = -5
                    left_key += 1

                elif event.key == K_d or event.key == K_RIGHT:

                    move_x = 5
                    right_key += 1

                elif event.key == K_w or event.key == K_UP:
                    move_y = -5
                    up_key += 1

                elif event.key == K_s or event.key == K_DOWN:
                    move_y = 5
                    down_key += 1


                elif event.key == K_SPACE:
                    hero.fire()
                    done = 1


                elif event.key == K_b:
                    print('b')
                    hero.bomb()

            if event.type == KEYUP:
                if event.key == K_a or event.key == K_LEFT:
                    left_key -= 1
                    if right_key == 0:
                        move_x = 0
                    else:
                        move_x = 5

                if event.key == K_d or event.key == K_RIGHT:
                    right_key -= 1
                    if left_key == 0:
                        move_x = 0
                    else:
                        move_x = -5

                if event.key == K_w or event.key == K_UP:
                    up_key -= 1
                    if down_key == 0:
                        move_y = 0
                    else:
                        move_y = 5

                if event.key == K_s or event.key == K_DOWN:
                    down_key -= 1
                    if up_key == 0:
                        move_y = 0
                    else:
                        move_y = -5

                if event.key == K_SPACE:
                    done = 0

        screen.blit(background, (0, 0))
        hero.move(move_x, move_y)
        hero.display()
        hero.judge()
        enemies.display(hero)
        enemies.move()
        bomb.display()
        bomb.judge(hero)
        bomb.move()

        for i in range(enemies.num):
            judge(hero, enemies.enemy_list[i])
        clear_enemy(enemies)
        judge_num(enemies)
        pygame.display.update()


if __name__ == "__main__":
    main()
