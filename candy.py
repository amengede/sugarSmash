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
        self.highlighted = False
        self.state = state
        self.x_offset = 0
        super().__init__()
    
    def __str__(self):
        return str(self.type)

    def __repr__(self):
        return str(self.type)
    
    def update(self):
        if self.state=="fall":
            super().fall()
            dy = self.targetY - self.y
            if dy<=0:
                super().bounce()   
        else:
            self.x = self.targetX
            self.y = self.targetY
        
    
    def getPosition(self):
        return (self.x,self.y)

    def getType(self):
        return self.type

    def getBounds(self):
        return self.bounds

    def setHighlight(self,state):
        self.highlighted = state
    
    def draw(self):
        if self.highlighted and self.state=="stable":
            pygame.draw.rect(SCREEN,LIGHT,pygame.Rect(self.x,self.y,PIECE_SIZE,PIECE_SIZE))
        SCREEN.blit(GRAPHICS[self.type],(self.x+4+self.x_offset,self.y+4))
