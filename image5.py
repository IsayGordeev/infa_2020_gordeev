from math import pi
import pygame
from pygame.draw import *

pygame.init()
FPS = 30
a = 1300
screen = pygame.display.set_mode((a, 1000))
# first mountain
polygon(screen, (248, 214, 169), [(0, 0), (a, 0),
                                  (a, 180), (0, 170)])
polygon(screen, (248, 214, 198), [(0, 170), (a, 180),
                                  (a, 360), (0, 350)])
circle(screen, (250, 237, 86), (550, 180), 60)
polygon(screen, (248, 214, 157), [(0, 340), (a, 350),
                                  (a, 530), (0, 520)])
polygon(screen, (172, 136, 148), [(0, 520), (a, 530),
                                  (a, 1000), (0, 1000)])
cliff = [(10 + i * 8, 330 - i ** (3 / 2)) for i in range(33)]
polygon(screen, (239, 156, 73),
        [(0, 390), *cliff, (266, 149), (316, 169), (336, 199), (470, 320), (560, 312), (600, 340)])
cliff1 = [(780 + i * 9, 255 - i ** (8 / 5)) for i in range(20)]
cliff2 = [(951 + i * 7, 143.82535239422486 + i ** (2)) for i in range(6)]
cliff3 = [(1086 + i * 11, 200 + i ** (2)) for i in range(7)]
polygon(screen, (239, 156, 73),
        [(600, 340), (680, 270), (750, 280), (780, 255), *cliff1, *cliff2, (986, 168.8), (1036, 208), (1086, 200),
         *cliff3, (1152, 236), (1202, 216), (a, 281.6)])
# second mountain range
polygon(screen, (160, 73, 58), [(0, 520), (0, 405), (20, 405), (45, 425), (100, 520)])
ellipse(screen, (160, 73, 58), (26, 335, 170, 400))
polygon(screen, (160, 73, 58), [(170, 525), (250, 410), (420, 525)])
polygon(screen, (160, 73, 58), [(330, 525), (430, 370), (540, 400), (610, 460), (680, 525)])
polygon(screen, (160, 73, 58), [(580, 450), (690, 440), (750, 525), (580, 525)])
polygon(screen, (160, 73, 58), [(0, 520), (0, 405), (20, 405), (45, 425), (100, 520)])
ellipse_1 = pygame.Surface((800, 800), pygame.SRCALPHA)
ellipse(ellipse_1, (160, 73, 58), (500, 100, 300, 150))
ellipse_1 = pygame.transform.rotate(ellipse_1, 45)
screen.blit(ellipse_1, (190, 225))

clx4 = 875
cly4 = 460

cliff4 = [((clx4 + 3 * i), cly4 - 100 * i ** (-0.2)) for i in range(1, 40)]
polygon(screen, (160, 73, 58), [(clx4 - 100, cly4 + 100), *cliff4, (clx4 + 200, cly4 + 100)])
polygon(screen, (160, 73, 58), [(clx4 + 200, cly4 + 100), (992, 411.94), (1060, 360), (1110, 390), (1160, 350), (1240, 380), (a, 300),(a,500)])
polygon(screen, (160, 73, 58), [(a,530), (a,400), (a- 200, 530)])
polygon(screen, (172, 136, 148), [(0, 520), (1200, 530),
                                  (1200, 1000), (0, 1000)])

polygon(screen, (160, 73, 58), [(0, 520), (0, 405), (20, 405), (45, 425), (100, 520)])


# def bird(x, y, size):
#     ellipse_4 = pygame.Surface((800, 800), pygame.SRCALPHA)
#     ellipse(ellipse_4, (181, 191, 191, 100), (120, 0, 500, 100))
#     ellipse_4 = pygame.transform.rotate(ellipse_4, 30)
#     screen.blit(ellipse_4, (205, 225))

# bird(500, 500, 100)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
