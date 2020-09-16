from config import *
from candy import CandyPiece
from board import GameBoard

game_board = GameBoard(BORDER,BORDER)

pygame.display.set_caption("Sugar Smash Allstars")

borders = (pygame.Rect(0,0,SCREEN_SIZE[0],BORDER),
            pygame.Rect(0,BORDER,BORDER,SCREEN_SIZE[1] - 4*BORDER),
            pygame.Rect(SCREEN_SIZE[0] - BORDER+1,BORDER,BORDER,SCREEN_SIZE[1] - 4*BORDER),
            pygame.Rect(0,SCREEN_SIZE[1] - 3*BORDER +1,SCREEN_SIZE[0],4*BORDER))
bottom_left_rect = pygame.Rect(30,530,100,20)
bottom_right_rect = pygame.Rect(170,530,100,20)

#game loop
running = True
while running:
    #event handling
    game_board.handleMouse()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            game_board.handleClick()
        if event.type == pygame.QUIT:
            running = False
    
    #object update
    game_board.update()
    
    #rendering
    SCREEN.fill(BACKGROUND)
    game_board.draw()
    for border in borders:
        pygame.draw.rect(SCREEN,BACKGROUND,border)
    pygame.draw.rect(SCREEN,DARK,bottom_left_rect)
    pygame.draw.rect(SCREEN,DARK,bottom_right_rect)
    
    
    pygame.display.update()

    #timing: 60fps
    CLOCK.tick(60)