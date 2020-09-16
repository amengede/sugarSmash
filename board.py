import random as rnd
import math
from config import *
from candy import CandyPiece

class GameBoard:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 240
        self.height = 480
        self.bounds = pygame.Rect(self.x,self.y,self.width,self.height)
        self.last_piece = None
        self.selected_piece = None
        self.searched = False
        self.num_rows = self.height//PIECE_SIZE
        self.num_cols = self.width//PIECE_SIZE
        self.pieces = []
        self.old_board = []
        for row in range(self.num_rows):
            self.pieces.append([])
            self.old_board.append([])
            for column in range(self.num_cols):
                self.pieces[row].append(None)
                self.old_board[row].append(None)
        self.populate()
        self.t = 0
        self.state = "stable"
        self.x_offset = 0
        self.score = 0;
    
    def populate(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                x = BORDER+column*PIECE_SIZE
                y = BORDER+row*PIECE_SIZE
                self.pieces[row][column] = CandyPiece(x,y-self.height,x,y,'fall')
    
    def hasMouse(self,x,y):
        return (x >= self.x and x <= (self.width+40)) and (y >= self.y and y <= (self.height+30))
    
    def handleMouse(self):
        (mouse_x,mouse_y) = pygame.mouse.get_pos()
        if self.hasMouse(mouse_x,mouse_y):
            mouse_x_game_space = min(max(mouse_x-self.x,0),self.width-40)//PIECE_SIZE
            mouse_y_game_space = min(max(mouse_y-self.y,0),self.height-10)//PIECE_SIZE
            current_piece = self.pieces[mouse_y_game_space][mouse_x_game_space]
            if current_piece != self.last_piece and current_piece != None:
                if current_piece.state=="stable":
                    current_piece.setHighlight(True)
                if self.last_piece != None and self.last_piece != self.selected_piece:
                    self.last_piece.setHighlight(False)
            self.last_piece = current_piece
        else:
            if self.last_piece != None and self.last_piece != self.selected_piece:
                self.last_piece.setHighlight(False)
    
    def handleClick(self):
        (mouse_x,mouse_y) = pygame.mouse.get_pos()
        if self.hasMouse(mouse_x,mouse_y):
            if self.selected_piece == None:
                self.selected_piece = self.last_piece
            else:
                if self.selected_piece != None:
                    selected_type = self.selected_piece.type
                    self.selected_piece.type = self.last_piece.type
                    self.last_piece.type = selected_type
                    self.selected_piece = None
                    self.last_piece.setHighlight(False)
            self.searched = False

    def update(self):
        if self.state == "shake":
            self.x_offset = 32*math.sin(self.t)/(self.t+1)
            self.t += 1
            if self.t > 10*math.pi:
                self.state = "stable"
                self.t = 0
                self.x_offset = 0
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                if self.pieces[row][column] != None:
                    self.pieces[row][column].update()
                    self.pieces[row][column].x_offset = self.x_offset
        if self.isStable():
            for row in range(self.num_rows):
                for column in range(self.num_cols):
                    if self.pieces[row][column] != None:
                        self.search(row,column)
            self.dropPieces()
                
    def draw(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                if self.pieces[row][column] != None:
                    self.pieces[row][column].draw()
        pygame.draw.rect(SCREEN,DARK,self.bounds,2)
    
    def isStable(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                if self.pieces[row][column] != None:
                    if self.pieces[row][column].state != "stable":
                        return False
        return True

    def search(self,i,j):
        result = [[i,j,False]]
        done = False
        while not done:
            result = self.expandSearch(result)
            done = True
            for node in result:
                if not node[2]:
                    done = False
                    continue
        if len(result) >= 3:
            for node in result:
                i = node[0]
                j = node[1]
                self.pieces[i][j] = None
            self.state = "shake"
            self.score += len(result)

    def expandSearch(self,result):
        for node in result:
            if not node[2]:
                i = node[0]
                j = node[1]
                this_type = self.pieces[i][j].type
                if i > 0:
                    if self.pieces[i-1][j] != None:
                        if self.pieces[i-1][j].getType() == this_type:
                            result.append([i-1,j,False])
                if j > 0:
                    if self.pieces[i][j-1] != None:
                        if self.pieces[i][j-1].getType() == this_type:
                            result.append([i,j-1,False])
                node[2] = True
        return result

    def dropPieces(self):
        #cut-paste current list into temporary copy
        for column in range(self.num_cols):
            for row in range(self.num_rows):
                self.old_board[row][column] = self.pieces[row][column]
                self.pieces[row][column] = None
        
        #find gaps for each spot
        for column in range(self.num_cols):
            column_gaps = 0
            for row in range(self.num_rows):
                piece = self.old_board[row][column]
                gaps = 0
                for i in range(row,self.num_rows):
                    if self.old_board[i][column] == None:
                        gaps += 1
                column_gaps = max(column_gaps,gaps)
                if piece != None:
                    #shift the piece down
                    self.pieces[row+gaps][column] = piece
                    self.pieces[row+gaps][column].state = "fall"
                    self.pieces[row+gaps][column].targetY += PIECE_SIZE*gaps
            #fill gaps in column
            for row in range(column_gaps):
                x = BORDER+column*PIECE_SIZE
                target_y = BORDER+row*PIECE_SIZE
                y_offset = PIECE_SIZE*column_gaps
                self.pieces[row][column] = CandyPiece(x,target_y-y_offset,x,target_y,'fall')