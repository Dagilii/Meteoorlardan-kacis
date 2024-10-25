import pygame
import random

class Meteor:

    def __init__(self,x=50,y=50,boyut=(50,50),yon=(1,1),hiz=10):
        self.x=x
        self.y=y
        self.boyut=boyut
        self.yon=yon
        self.hiz=hiz

    def rastgele_yerlestir(self,ekranboyutlar):
        self.x= random.randint(0,ekranboyutlar[0])
        self.y=-50
        self.yon = (random.randint(-1,1),1)
        self.hiz=random.randint(5,15)
        self.boyut=(random.randint(25,75),random.randint(25,75))

    def update(self,ekranboyutlar):
        self.x+=self.hiz*self.yon[0]
        self.y+=self.hiz*self.yon[1]
        if self.x<=0 or self.x>=ekranboyutlar[0] or self.y >= ekranboyutlar[1]:
            self.rastgele_yerlestir(ekranboyutlar)
   
    def render(self,ekran):
        pygame.draw.rect(ekran,(255,0,0),(self.x,self.y,*self.boyut))