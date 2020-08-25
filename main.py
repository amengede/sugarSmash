import pygame
from candy import candyPiece

pygame.init()

screenSize = (300,600)
border = 20

#colors
BACKGROUND = (150,200,100)
DARK = (105,55,155)

pieceSize = 60
gameSpace = pygame.Rect(border,border,screenSize[0]-2*border,screenSize[1]-5*border)
numRows = (screenSize[1]-6*border)//pieceSize
numCols = (screenSize[0]-3*border)//pieceSize

SCREEN  = pygame.display.set_mode(screenSize)

pygame.display.set_caption("Sugar Smash Allstars")

pieces = [[0]*numCols]*numRows
print(pieces)
for row in range(numRows):
    for column in range(numCols):
        x = border+column*pieceSize
        y = border+row*pieceSize
        #print("setting: ",x," , ",y)
        pieces[row][column] = candyPiece(x,y,SCREEN,DARK)
        (x,y) = pieces[row][column].getPosition()
        print("reading: ",x," , ",y)

for column in range(numCols):
    for row in range(numRows):
        print(row,column)
        (x,y) = pieces[row][column].getPosition()
        print("Reading once more: ",x," , ",y)
        

#game loop
running = True
while running:

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    #rendering
    SCREEN.fill(BACKGROUND)
    pygame.draw.rect(SCREEN,DARK,gameSpace,2)
    """
    for row in range(numRows):
        for column in range(numCols):
            pieces[row][column].draw()
            """
    pygame.display.update()