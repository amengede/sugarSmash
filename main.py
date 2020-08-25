import pygame
from candy import CandyPiece

pygame.init()

screen_size = (300,600)
border = 30

#colors
BACKGROUND = (150,200,100)
DARK = (105,55,155)

piece_size = 60
game_space = pygame.Rect(border,border,240,480)
num_rows = 480//piece_size
num_cols = 240//piece_size

SCREEN  = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Sugar Smash Allstars")

pieces = []
for row in range(num_rows):
    pieces.append([])
    for column in range(num_cols):
        x = border+column*piece_size
        y = border+row*piece_size
        pieces[row].append(CandyPiece(x,y,SCREEN,DARK))
        

#game loop
running = True
while running:

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    #rendering
    SCREEN.fill(BACKGROUND)
    pygame.draw.rect(SCREEN,DARK,game_space,2)
    for row in range(num_rows):
        for column in range(num_cols):
            pieces[row][column].draw()
    pygame.display.update()