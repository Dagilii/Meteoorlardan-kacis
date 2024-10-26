import pygame
import Oyuncu
from Meteor import Meteor
# pygame setup

ekran_boyutlar=(1280, 720)
pygame.init()
screen = pygame.display.set_mode(ekran_boyutlar)
clock = pygame.time.Clock()
meteor_resmi=pygame.image.load("Meteor.png")


arkaplan_resmi = pygame.image.load('uzay.jpg')

running = True
oyuncu = Oyuncu.Oyuncu()
font = pygame.font.Font(None, 50)
sayac = 0
olumyazi = font.render("Öldünüz yeniden başlamak için r ye basın ! ", True, "white")
meteor_list=[]

for i in range(0,5):
    meteor=Meteor()
    meteor.rastgele_yerlestir(ekran_boyutlar)
    meteor_list.append(meteor)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    tuslar = pygame.key.get_pressed()
    
    if tuslar[pygame.K_a]:
        oyuncu.yon=-1
    if tuslar[pygame.K_d]:
        oyuncu.yon=1

    if tuslar[pygame.K_s]:
        oyuncu.egilmek(True)
    else:
        oyuncu.egilmek(False)

    if tuslar[pygame.K_r]and oyuncu.can==False:
        oyuncu.can=True
        for meteor in meteor_list:
            meteor.rastgele_yerlestir(ekran_boyutlar)
        oyuncu.sure=0
        sayac=0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    oyuncu.update(ekran_boyutlar)

    for meteor in meteor_list:
        if meteor.hit_box.colliderect(oyuncu.hit_box):
            oyuncu.can=False

        meteor.update(ekran_boyutlar)
    
    sure = font.render("Süre = "+str(oyuncu.sure), True, "yellow")
    
    fps = 60
    
    sayac+=1
    if sayac==fps and oyuncu.can==True:
        oyuncu.sure+=1
        sayac=0

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(arkaplan_resmi, (0, 0))
    # RENDER YOUR GAME HERE
    
    oyuncu.render(screen)
    for meteor in meteor_list:
        if meteor.yon[0]==1:
            selfresim=pygame.transform.scale(meteor_resmi,meteor.boyut)
            selfresim = pygame.transform.rotate(selfresim,45)
        elif meteor.yon[0]==-1:
            selfresim=pygame.transform.scale(meteor_resmi,meteor.boyut)
            selfresim = pygame.transform.rotate(selfresim,-45)
        else:
            selfresim=pygame.transform.scale(meteor_resmi,meteor.boyut)
        meteor.render(screen,selfresim)

    if oyuncu.can==False:
        screen.blit(olumyazi,(300,365))

    screen.blit(sure,(100,25))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(fps)  # limits FPS to 60

pygame.quit()