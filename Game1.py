import pygame

pygame.init()
W=400
H=600

sc=pygame.display.set_mode((W,H))
pygame.display.set_caption("SuperMegaGame")

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)

FPS=60

clock=pygame.time.Clock()

x=W//2
y=550#H//2
#x1=200
#y1=50
speed=5
#
speed_sm1=1
x_smail1=200
y_smail1=50
pi = 3.14
VPravo=True
Vistrel=False
New_Vistrel=True
Popal=False

X_Pulya=-10
Y_Pulya=-10
speed_pl=5



def draw_smail1(x1,y1):
    # кгуг смайлика
    pygame.draw.circle(sc, YELLOW, (x1, y1), 15)
    # дуга
    pygame.draw.arc(sc, BLACK, (x1 - 10, y1 - 8, 20, 20), pi, 2 * pi, 2)
    # овал
    pygame.draw.ellipse(sc, BLACK, (x1 - 6, y1 - 6, 3, 6))
    pygame.draw.ellipse(sc, BLACK, (x1 + 4, y1 - 6, 3, 6))

#draw_smail1(200,50)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if New_Vistrel:
                    Vistrel=True
                    New_Vistrel=False
                    X_Pulya=x
                    Y_Pulya=y
                    Popal=False
                #выстрел


    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    sc.fill(BLACK)# Фон


    if x_smail1>20 and VPravo:
        x_smail1-=speed_sm1
        draw_smail1(x_smail1,y_smail1)
    if x_smail1<=20:
        VPravo=False
    if x_smail1<380 and (not VPravo):
        x_smail1 += speed_sm1
        draw_smail1(x_smail1, y_smail1)
    if x_smail1>=380:
        VPravo=True
    #прорисовка персонажа -стрелялка
    pygame.draw.polygon(sc,GREEN,[[x-15,y+10],[x,y-10],[x+15,y+10]])
    #Пуля
    if Vistrel:
        Y_Pulya-=speed_pl
        pygame.draw.rect(sc, GREEN, (X_Pulya, Y_Pulya, 2, 6))
    if Y_Pulya<0:
        New_Vistrel=True
    if (x_smail1-10)<=X_Pulya<=(x_smail1+10) and (y_smail1)<=Y_Pulya<=(y_smail1+20):
        Popal=True
    if Popal:
        myfont = pygame.font.Font('freesansbold.ttf', 12)
        text_p = myfont.render('Попал!', True, GREEN)
        sc.blit(text_p,(200,300))


    #обновление экрана
    pygame.display.update()

    #задержка цикла
    clock.tick(FPS)