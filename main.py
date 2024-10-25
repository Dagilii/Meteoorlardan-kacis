import pygame
import Oyuncu
from Meteor import Meteor
# pygame setup

ekran_boyutlar=(1280, 720)
pygame.init()
screen = pygame.display.set_mode(ekran_boyutlar)
clock = pygame.time.Clock()

arkaplan_resmi = pygame.image.load('uzay.jpg')

running = True
oyuncu = Oyuncu.Oyuncu()



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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    oyuncu.update(ekran_boyutlar)
    for meteor in meteor_list:
        meteor.update(ekran_boyutlar)
    
    # fill the screen with a color to wipe away anything from last frame
    screen.blit(arkaplan_resmi, (0, 0))



    # RENDER YOUR GAME HERE

    oyuncu.render(screen)
    for meteor in meteor_list:
        meteor.render(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()