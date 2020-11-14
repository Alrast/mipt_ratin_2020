import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))

#colors of balls
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

r = 50
score=0
score_in=0
def new_ball():
    '''рисует новый шарик '''
    global x, y, r, like_speed_x, like_speed_y, color
    x = randint(100, 1100)
    y = randint(100, 900)
    #r = randint(10, 100)
    like_speed_x = randint(-1, 1)
    like_speed_y = randint(-1, 1)
    color = COLORS[randint(0, 5)]
    return(x,y,color,like_speed_x,like_speed_y)


def click(score_in):
    score_in=0
    if (((event.pos[0] - x)**2) + (event.pos[1] - y)**2) <= (r**2):
        score_in+=1
    else:
        pass
    return score_in

pygame.display.update()
clock = pygame.time.Clock()
finished = False

new_ball()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print('Ваши очки', score)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score+=click(score_in)
            print('click',event.pos[0],event.pos[1])
            print('coords',x,y)
            if abs(event.pos[0]-x) <= r:
                if abs(event.pos[1]-y) <= r:
                    new_ball()
           
   
    pygame.display.update()
    screen.fill(BLACK)
    circle(screen, color, (x, y), r)
    
    if (x-r)>10 and (x+r)<1190 and (y-r)>10 and (y+r)<890:
        pygame.display.update()
        screen.fill(BLACK)
        x += like_speed_x
        y += like_speed_y
        circle(screen, color, (x, y), r)
    elif (x-r)<=10 or (x+r)>=1190:
        like_speed_x = -like_speed_x
        x += like_speed_x
        y += like_speed_y
    elif (y-r)<=10 or (y+r)>=890:
        like_speed_y = -like_speed_y
        x += like_speed_x
        y += like_speed_y


pygame.quit()
