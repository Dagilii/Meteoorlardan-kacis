import pygame
class Oyuncu:
    def __init__(self):
        self.x = 30
        self.y = 670
        self.boyut=(25,50)

        self.yon=1
        self.hiz=10

    def egilmek(self,aktif):
        if aktif:
            self.hiz=4
            self.y=670
            self.boyut=(25,25)
        else:
            self.hiz=10
            self.y=645
            self.boyut=(25,50)

    def update(self,ekranboyutlari):
        self.x+= self.yon*self.hiz
        if self.x>=ekranboyutlari[0]-self.boyut[0]:
            self.x=ekranboyutlari[0]-self.boyut[0]
        if self.x<=0:
            self.x=0
        
    def render(self,ekran):
        pygame.draw.rect(ekran ,(255,255,255),(self.x,self.y,*self.boyut))

