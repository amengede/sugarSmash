from config import *
from candy import CandyPiece

game_space = pygame.Rect(BORDER,BORDER,240,480)
num_rows = 480//PIECE_SIZE
num_cols = 240//PIECE_SIZE

pygame.display.set_caption("Sugar Smash Allstars")

pieces = []
for row in range(num_rows):
    pieces.append([])
    for column in range(num_cols):
        x = BORDER+column*PIECE_SIZE
        y = BORDER+row*PIECE_SIZE
        pieces[row].append(CandyPiece(x,y))

bottom_left_rect = pygame.Rect(30,530,100,20)
bottom_right_rect = pygame.Rect(170,530,100,20)

#which piece is currently under the mouse, and which was last frame
current_piece = None
last_piece = None

#game loop
running = True
while running:

    #event handling
    (mouse_x,mouse_y) = pygame.mouse.get_pos()
    mouse_in_gamespace = (mouse_x >= BORDER and mouse_x <= 280) and (mouse_y >= BORDER and mouse_y <= 510)
    if mouse_in_gamespace:
        mouse_x_game_space = min(max(mouse_x-BORDER,0),230)//PIECE_SIZE
        mouse_y_game_space = min(max(mouse_y-BORDER,0),470)//PIECE_SIZE
        current_piece = pieces[mouse_y_game_space][mouse_x_game_space]
        if current_piece != last_piece:
            current_piece.setHighlight(True)
            if last_piece != None:
                last_piece.setHighlight(False)
        last_piece = current_piece
        mouse_message = FONT.render('('+str(mouse_x_game_space)+','+str(mouse_y_game_space)+')', True, DARK)
    else:
        mouse_message = FONT.render(' ', True, DARK)
        if last_piece != None:
                last_piece.setHighlight(False)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    #rendering
    SCREEN.fill(BACKGROUND)
    SCREEN.blit(mouse_message, bottom_left_rect)
    #pygame.draw.rect(SCREEN,DARK,bottom_left_rect)
    pygame.draw.rect(SCREEN,DARK,bottom_right_rect)
    for row in range(num_rows):
        for column in range(num_cols):
            pieces[row][column].draw()
    pygame.draw.rect(SCREEN,DARK,game_space,2)
    
    pygame.display.update()

    #timing: 60fps
    CLOCK.tick(60)