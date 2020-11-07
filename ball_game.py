import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))
a=0
b=0
c=0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

example_to_save_coords=[]

def new_ball():
    global x, y, r,example_to_save_coords
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    f=x
    m=y
    l=r
    return(f,m,l)

def click(event):
    print('koords',event.pos)
    pos=pygame.mouse.get_pos()
    global example_to_save_coords
    for i in example_to_save_coords:
        f,m,l = i
        tmp_list=[]

        if (pos[0]-f)^2+(pos[1]-m)^2<=l^2:
            circle(screen, BLACK, (f, m), l)
            tmp_list.append(i)
    example_to_save_coords = [item for item in example_to_save_coords if item not in tmp_list]
    return(event.pos)
    # TODO: !!!!!

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS/30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
            print('Click!')
            #if (a-f)^2+(b-m)^2<=l^2:
                 #circle(screen, black, (f, m), l)

    example_to_save_coords.append(new_ball())
    pygame.display.update()

pygame.quit()