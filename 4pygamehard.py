import pygame
from pygame.draw import *
pygame.init()
FPS=30
screen = pygame.display.set_mode((1854,769))
surface = pygame.Surface((1854,769), pygame.SRCALPHA)

circle(screen, (0,129,0), (464,769), 225)
ellipse(screen, (234,199,176), rect(surface, (0,0,0), (45,40,70,90)))
ellipse(screen, (234,199,176), rect(surface, (0,0,0), (805,40,70,90)))
line(screen, (234,199,176), (75,105), (215,560), 30)
line(screen, (234,194,176), (845,105), (705,560), 30)
#(157,394) +927
x=82
y=220
polygon(screen, (0,129,0), [(96+x,356+y), (172+x,316+y), (229+x,382+y), (187+x,469+y), (102+x,459+y)])
polygon(screen, (0,0,0), [(96+x,356+y), (172+x,316+y), (229+x,382+y), (187+x,469+y), (102+x,459+y)], 1)
x=520
y=220
polygon(screen, (0,129,0), [(225+x,355+y), (150+x,310+y), (87+x,368+y), (120+x,459+y), (210+x,448+y)])
polygon(screen, (0,0,0), [(225+x,355+y), (150+x,310+y), (87+x,368+y), (120+x,459+y), (210+x,448+y)], 1)
circle(screen, (234,199,176), (464,410), 225)
circle(screen, (191,201,184), (394,380), 40)
circle(screen, (4, 0, 5), (394,380), 10)
circle(screen, (191,201,184), (534,380), 40)
circle(screen, (4, 0, 5), (534,380), 10)
polygon(screen, (103,58,25), [(448,420), (464,445), (480,420)])
polygon(screen, (233,37,40), [(344,475), (464,550), (584,475)])

polygon(screen, (255,213,38), [(250,250), (310,245), (270,300)])
polygon(screen, (255,213,38), [(303,257), (308,189), (349,215)])
polygon(screen, (255,213,38), [(341,223), (344,173), (390,198)])
polygon(screen, (255,213,38), [(384,197), (408,150), (434,186)])
polygon(screen, (255,213,38), [(419,188), (442,144), (462,181)])
polygon(screen, (255,213,38), [(451,183), (480,150), (488,181)])
polygon(screen, (255,213,38), [(484,182), (530,150), (535,194)])
polygon(screen, (255,213,38), [(535,194), (590,171), (590,220)])
polygon(screen, (255,213,38), [(577,215), (640,200), (621,245)])
polygon(screen, (255,213,38), [(609,232), (671,220), (645,270)])

#surf = pygame.Surface((927,769))
#surf.set_colorkey((0, 0, 0))
#polygon(surf, (233,237,40), [(344,475), (464,250), (384,475)])
#surf = pygame.transform.flip(surf, True, False)
#screen.blit(surf, (110, 110))


circle(screen, (255,102,0), (464+767,769), 225)
ellipse(screen, (234,199,176), rect(surface, (0,0,0), (45+767,40,70,90)))
ellipse(screen, (234,199,176), rect(surface, (0,0,0), (805+767,40,70,90)))
line(screen, (234,199,176), (75+767,105), (215+767,560), 30)
line(screen, (234,194,176), (845+767,105), (705+767,560), 30)
#(157,394)
x=82
y=220
polygon(screen, (250,102,0), [(96+x+767,356+y), (172+x+767,316+y), (229+x+767,382+y), (187+x+767,469+y), (102+x+767,459+y)])
polygon(screen, (0,0,0), [(96+x+767,356+y), (172+x+767,316+y), (229+x+767,382+y), (187+x+767,469+y), (102+x+767,459+y)], 1)
x=520
y=220
polygon(screen, (250,102,0), [(225+x+767,355+y), (150+x+767,310+y), (87+x+767,368+y), (120+x+767,459+y), (210+x+767,448+y)])
polygon(screen, (0,0,0), [(225+x+767,355+y), (150+x+767,310+y), (87+x+767,368+y), (120+x+767,459+y), (210+x+767,448+y)], 1)
circle(screen, (234,199,176), (464+767,410), 225)
circle(screen, (127,177,255), (394+767,380), 40)
circle(screen, (4, 0, 5), (394+767,380), 10)
circle(screen, (127,177,255), (534+767,380), 40)
circle(screen, (4, 0, 5), (534+767,380), 10)
polygon(screen, (103,58,25), [(448+767,420), (464+767,445), (480+767,420)])
polygon(screen, (233,37,40), [(344+767,475), (464+767,550), (584+767,475)])

polygon(screen, (212,42,254), [(250+767,250), (310+767,245), (270+767,300)])
polygon(screen, (212,42,254), [(303+767,257), (308+767,189), (349+767,215)])
polygon(screen, (212,42,254), [(341+767,223), (344+767,173), (390+767,198)])
polygon(screen, (212,42,254), [(384+767,197), (408+767,150), (434+767,186)])
polygon(screen, (212,42,254), [(419+767,188), (442+767,144), (462+767,181)])
polygon(screen, (212,42,254), [(451+767,183), (480+767,150), (488+767,181)])
polygon(screen, (212,42,254), [(484+767,182), (530+767,150), (535+767,194)])
polygon(screen, (212,42,254), [(535+767,194), (590+767,171), (590+767,220)])
polygon(screen, (212,42,254), [(577+767,215), (640+767,200), (621+767,245)])
polygon(screen, (212,42,254), [(609+767,232), (671+767,220), (645+767,270)])

rect(screen, (50,255,50), (0,0,927+927,82))

line(screen, (0,0,0), (36+300,59), (36+300,18), 10)
circle(screen, (0,0,0), (45+300,28), 15)
circle(screen, (50,255,50), (45+300,28), 8)

line(screen, (0,0,0), (86+300,59), (86+300,38), 10)
line(screen, (0,0,0), (86+300,38), (66+300,18), 10)
line(screen, (0,0,0), (86+300,38), (106+300,18), 10)

line(screen, (0,0,0), (136+300,59), (136+300,18), 10)
line(screen, (0,0,0), (116+300,18), (156+300,18), 10)

line(screen, (0,0,0), (176+300,59), (176+300,18), 10)
line(screen, (0,0,0), (196+300,59), (196+300,18), 10)
line(screen, (0,0,0), (176+300,38), (196+300,38), 10)

circle(screen, (0,0,0), (236+300,38), 25)
circle(screen, (50,255,50), (236+300,38), 19)

line(screen, (0,0,0), (276+300,59), (276+300,18), 10)
line(screen, (0,0,0), (296+300,59), (296+300,18), 10)
line(screen, (0,0,0), (276+300,18), (296+300,59), 10)

line(screen, (0,0,0), (366+300,59), (366+300,28), 10)
line(screen, (0,0,0), (366+300,22), (366+300,18), 10)

line(screen, (0,0,0), (386+300,18), (426+300,18), 10)
line(screen, (0,0,0), (386+300,59), (426+300,59), 10)
line(screen, (0,0,0), (386+300,18), (426+300,59), 10)

line(screen, (0,0,0), (36+787,59), (36+787,18), 10)
circle(screen, (0,0,0), (45+787,28), 15)
circle(screen, (50,255,50), (45+787,28), 8)
line(screen, (0,0,0), (36+787,39), (36+807,59), 10)

line(screen, (0,0,0), (36+827,59), (36+827,18), 10)
line(screen, (0,0,0), (36+827,18), (36+857,18), 10)
line(screen, (0,0,0), (36+827,59), (36+857,59), 10)
line(screen, (0,0,0), (36+827,39), (36+857,39), 10)

line(screen, (0,0,0), (36+877,59), (56+877,18), 10)
line(screen, (0,0,0), (76+877,59), (56+877,18), 10)
line(screen, (0,0,0), (46+877,46), (66+877,46), 10)

line(screen, (0,0,0), (36+937,59), (36+937,18), 10)
line(screen, (0,0,0), (36+937,59), (36+977,59), 10)

line(screen, (0,0,0), (86+937,59), (86+937,18), 10)
line(screen, (0,0,0), (86+937,59), (86+977,59), 10)


line(screen, (0,0,0), (86+1000,59), (86+1000,38), 10)
line(screen, (0,0,0), (86+1000,38), (66+1000,18), 10)
line(screen, (0,0,0), (86+1000,38), (106+1000,18), 10)



line(screen, (0,0,0), (446+787,59), (466+787,18), 10)
line(screen, (0,0,0), (486+787,59), (466+787,18), 10)
line(screen, (0,0,0), (456+787,46), (476+787,46), 10)

line(screen, (0,0,0), (496+787,59), (496+787,18), 10)
line(screen, (0,0,0), (536+787,59), (536+787,18), 10)
line(screen, (0,0,0), (516+787,46), (496+787,18), 10)
line(screen, (0,0,0), (516+787,46), (536+787,18), 10)

line(screen, (0,0,0), (546+787,59), (566+787,18), 10)
line(screen, (0,0,0), (586+787,59), (566+787,18), 10)
line(screen, (0,0,0), (556+787,46), (576+787,46), 10)

line(screen, (0,0,0), (606+787,18), (646+787,18), 10)
line(screen, (0,0,0), (606+787,59), (646+787,59), 10)
line(screen, (0,0,0), (606+787,59), (646+787,18), 10)

line(screen, (0,0,0), (656+787,59), (656+787,28), 10)
line(screen, (0,0,0), (656+787,22), (656+787,18), 10)

line(screen, (0,0,0), (676+787,59), (676+787,18), 10)
line(screen, (0,0,0), (696+787,59), (696+787,18), 10)
line(screen, (0,0,0), (676+787,18), (696+787,59), 10)



circle(screen, (0,0,0), (736+787,38), 25)
circle(screen, (50,255,50), (736+787,38), 19)
rect(screen, (50,255,50), (746+787,5,40,40))
line(screen, (0,0,0), (736+787,42), (761+787,42), 6)


line(screen, (0,0,0), (366+787+420,59), (366+787+420,55), 10)
line(screen, (0,0,0), (366+787+420,48), (366+787+420,18), 10)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()