import pygame
import datetime
from random import randint

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((800, 480), pygame.FULLSCREEN)

clock = pygame.time.Clock()

digits = [[[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 0]],
        [[0, 0, 0], [0, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1], [0, 0, 0]],
        [[0, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 0]],
        [[0, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
        [[0, 0, 0], [1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 0]],
        [[0, 0, 0], [1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
        [[0, 0, 0], [1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 0]],
        [[0, 0, 0], [1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 0]],
        [[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 0]],
        [[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]

#digits_color = [[0, 0, 0], [0, 209, 251]]
digits_color = [[0, 0, 0], [170, 12, 12]]

pixel_size = 40
pixel_space = 8

colon = ''

offset_x = 19
offset_y = 0

last_minute = ''

while True:
    screen.fill((0, 0, 0))
    full_time = str(datetime.datetime.now().time()).split(':')
    if int(full_time[2].split('.')[0]) % 2 == 0:
        colon = ':'
    else:
        colon = ' '
    if last_minute != full_time[1]:
        last_minute = full_time[1]
        offset_y = randint(0, 255)
    time = full_time[0] + colon + full_time[1]
    for d in range(len(time)):
        for y in range(7):
            for x in range(3):
                if time[d] == ':':
                    n = 10
                elif time[d] == ' ':
                    n = 11
                else:
                    n = int(time[d])
                r, g, b = (digits_color[digits[n][y][x]][0] - (y * 16), digits_color[digits[n][y][x]][1] - (y * 16), digits_color[digits[n][y][x]][2] - (y * 32))
                if r < 0:
                    r = 0
                if g < 0:
                    g = 0
                if b < 0:
                    b = 0
                pygame.draw.rect(screen, (r, g, b), ((x * pixel_size) + (pixel_size * 4 * d) + offset_x, (y * pixel_size) + offset_y, pixel_size - pixel_space, pixel_size - pixel_space))
    pygame.display.flip()
    clock.tick(1)
