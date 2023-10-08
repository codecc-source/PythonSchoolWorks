import pygame
from pygame.locals import *

from random import randint

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

direction_a = 1
direction_b = -1
direction_c = 1
direction_d = -1
direction_e = 1
direction_f = -1

cube_rect = Rect(100, 100, 30, 30)
cube_rect2 = Rect(200, 200, 30, 30)
cube_rect3 = Rect(300, 100, 30, 30)
cube_rect4 = Rect(400, 200, 30, 30)
cube_rect5 = Rect(500, 100, 30, 30)
cube_rect6 = Rect(600, 200, 30, 30)

speed_x1 = 5
speed_y1 = 5

speed_x2 = 5
speed_y2 = 5

speed_x3 = 5
speed_y3 = 5

speed_x4 = 5
speed_y4 = 5

speed_x5 = 5
speed_y5 = 5

speed_x6 = 5
speed_y6 = 5

while True:
    clock.tick(60)

    if cube_rect.left < 0 or cube_rect.right > 600 or cube_rect.top <= 0 or cube_rect.bottom >= 600:
        direction_a *= -1
        speed_x1 = randint(0, 8)
        speed_y1 = randint(0, 8)

        if speed_x1 == 0 and speed_y1 == 0:
            speed_x1 = randint(2, 8)
            speed_y1 = randint(2, 8)


    if cube_rect2.left < 0 or cube_rect2.right > 600 or cube_rect2.top <= 0 or cube_rect2.bottom >= 600:
        direction_b *= -1
        speed_x2 = randint(0, 8)
        speed_y2 = randint(0, 8)

        if speed_x2 == 0 and speed_y2 == 0:
            speed_x2 = randint(2, 8)
            speed_y2 = randint(2, 8)


    if cube_rect3.left < 0 or cube_rect3.right > 600 or cube_rect3.top <= 0 or cube_rect3.bottom >= 600:
        direction_c *= -1
        speed_x3 = randint(0, 8)
        speed_y3 = randint(0, 8)

        if speed_x3 == 0 and speed_y3 == 0:
            speed_x3 = randint(2, 8)
            speed_y3 = randint(2, 8)


    if cube_rect4.left < 0 or cube_rect4.right > 600 or cube_rect4.top <= 0 or cube_rect4.bottom >= 600:
        direction_d *= -1
        speed_x4 = randint(0, 8)
        speed_y4 = randint(0, 8)

        if speed_x4 == 0 and speed_y4 == 0:
            speed_x4 = randint(2, 8)
            speed_y4 = randint(2, 8)


    if cube_rect5.left < 0 or cube_rect5.right > 600 or cube_rect5.top <= 0 or cube_rect5.bottom >= 600:
        direction_e *= -1
        speed_x5 = randint(0, 8)
        speed_y5 = randint(0, 8)

        if speed_x5 == 0 and speed_y5 == 0:
            speed_x5 = randint(2, 8)
            speed_y5 = randint(2, 8)


    if cube_rect6.left < 0 or cube_rect6.right > 600 or cube_rect6.top <= 0 or cube_rect6.bottom >= 600:
        direction_f *= -1
        speed_x6 = randint(0, 8)
        speed_y6 = randint(0, 8)

        if speed_x6 == 0 and speed_y6 == 0:
            speed_x6 = randint(2, 8)
            speed_y6 = randint(2, 8)

    cube_rect.left += speed_x1 * direction_a
    cube_rect.top += speed_y1 * direction_a
    cube_rect.right += speed_x1 * direction_a
    cube_rect.bottom += speed_y1 * direction_a

    cube_rect2.left += speed_x2 * direction_b
    cube_rect2.top += speed_y2 * direction_b
    cube_rect2.right += speed_x2 * direction_b
    cube_rect2.bottom += speed_y2 * direction_b

    cube_rect3.left += speed_x3 * direction_c
    cube_rect3.top += speed_y3 * direction_c
    cube_rect3.right += speed_x3 * direction_c
    cube_rect3.bottom += speed_y3 * direction_c

    cube_rect4.left += speed_x4 * direction_d
    cube_rect4.top += speed_y4 * direction_d
    cube_rect4.right += speed_x4 * direction_d
    cube_rect4.bottom += speed_y4 * direction_d

    cube_rect5.left += speed_x5 * direction_e
    cube_rect5.top += speed_y5 * direction_e
    cube_rect5.right += speed_x5 * direction_e
    cube_rect5.bottom += speed_y5 * direction_e

    cube_rect6.left += speed_x6 * direction_f
    cube_rect6.top += speed_y6 * direction_f
    cube_rect6.right += speed_x6 * direction_f
    cube_rect6.bottom += speed_y6 * direction_f

    collide = pygame.Rect.colliderect(cube_rect, cube_rect2)
    collide2 = pygame.Rect.colliderect(cube_rect3, cube_rect4)
    collide3 = pygame.Rect.colliderect(cube_rect5, cube_rect6)

    if collide and collide2 and collide3:
        direction_a *= -1
        direction_b *= -1
        direction_c *= -1
        direction_d *= -1
        direction_e *= -1
        direction_f *= -1

    pygame.draw.rect(screen, (255, 0, 0), cube_rect)
    pygame.draw.rect(screen, (0, 255, 0), cube_rect2)
    pygame.draw.rect(screen, (0, 0, 255), cube_rect3)
    pygame.draw.rect(screen, (255, 255, 0), cube_rect4)
    pygame.draw.rect(screen, (255, 0, 255), cube_rect5)
    pygame.draw.rect(screen, (0, 255, 255), cube_rect6)

    pygame.display.update()
    screen.fill("BLACK")