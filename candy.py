import random as rnd
from config import *
from physics import *
import math

class CandyPiece(particle):

    def __init__(self,x,y,targetX,targetY,state):
        self.type = rnd.randint(0,4)
        self.x = x
        self.y = y
        self.targetX = targetX
        self.targetY = targetY
        self.graphic = GRAPHICS[self.type]
        self.highlighted = False
        self.state = state
        super().__init__()
    
    def update(self):
        if self.state=="fall":
            super().fall()
            dy = self.targetY - self.y
            if dy<=0:
                super().bounce()   
        else:
            self.x = self.targetX
            self.y = self.targetY
            #self.bounds = pygame.Rect(self.x,self.y,PIECE_SIZE,PIECE_SIZE)
        
    
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
            pygame.draw.rect(SCREEN,LIGHT,pygame.Rect(self.x,self.y,PIECE_SIZE,PIECE_SIZE))
        SCREEN.blit(self.graphic,(self.x+4,self.y+4))
