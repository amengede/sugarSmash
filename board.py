import random as rnd
from config import *
from candy import CandyPiece

class GameBoard:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 240
        self.height = 480
        self.bounds = pygame.Rect(self.x,self.y,self.width,self.height)
        self.num_rows = self.height//PIECE_SIZE
        self.num_cols = self.width//PIECE_SIZE
        self.pieces = []
        self.populate()
        self.last_piece = None
    
    def populate(self):
        for row in range(self.num_rows):
            self.pieces.append([])
            for column in range(self.num_cols):
                x = BORDER+column*PIECE_SIZE
                y = BORDER+row*PIECE_SIZE
                self.pieces[row].append(CandyPiece(x,y-self.height,x,y,'fall'))
    
    def hasMouse(self,x,y):
        return (x >= self.x and x <= (self.width+40)) and (y >= self.y and y <= (self.height+30))
    
    def handleMouse(self):
        (mouse_x,mouse_y) = pygame.mouse.get_pos()
        if self.hasMouse(mouse_x,mouse_y):
            mouse_x_game_space = min(max(mouse_x-self.x,0),self.width-40)//PIECE_SIZE
            mouse_y_game_space = min(max(mouse_y-self.y,0),self.height-10)//PIECE_SIZE
            current_piece = self.pieces[mouse_y_game_space][mouse_x_game_space]
            if current_piece != self.last_piece:
                if current_piece.state=="stable":
                    current_piece.setHighlight(True)
                if self.last_piece != None:
                    self.last_piece.setHighlight(False)
            self.last_piece = current_piece
        else:
            if self.last_piece != None:
                self.last_piece.setHighlight(False)
    
    def update(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.pieces[row][column].update()

    
    def draw(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.pieces[row][column].draw()
        pygame.draw.rect(SCREEN,DARK,self.bounds,2)
