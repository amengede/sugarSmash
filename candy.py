import random as rnd
import pygame

pygame.init()

class CandyPiece:
    def __init__(self,x,y,screen,dark):
        self.type = rnd.randint(1,4)
        self.x = x
        self.y = y
        self.bounds = pygame.Rect(self.x,self.y,60,60)
        self.screen = screen
        self.dark = dark
    
    def getPosition(self):
        return (self.x,self.y)

    def getType(self):
        return self.type

    def getBounds(self):
        return self.bounds
    
    def draw(self):
        pygame.draw.rect(self.screen,self.dark,self.getBounds())
