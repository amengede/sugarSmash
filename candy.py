import random as rnd
from config import *

class CandyPiece:

    graphics = (pygame.image.load("img/gem.png"),
                pygame.image.load("img/gem1.png"),
                pygame.image.load("img/gem2.png"),
                pygame.image.load("img/gem3.png"),
                pygame.image.load("img/gem4.png"))

    def __init__(self,x,y):
        self.type = rnd.randint(0,4)
        self.x = x
        self.y = y
        self.bounds = pygame.Rect(self.x,self.y,PIECE_SIZE,PIECE_SIZE)
        self.graphic = CandyPiece.graphics[self.type]
        self.highlighted = False
        
    
    def getPosition(self):
        return (self.x,self.y)

    def getType(self):
        return self.type

    def getBounds(self):
        return self.bounds

    def setHighlight(self,state):
        self.highlighted = state
    
    def draw(self):
        if self.highlighted:
            pygame.draw.rect(SCREEN,LIGHT,self.getBounds())
        SCREEN.blit(self.graphic,(self.x+4,self.y+4))
