import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((1200, 1000))

polygon(screen, (250, 235, 215), [(0,0), (1200,0),
                               (300,100), (100,100)], 20)





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
