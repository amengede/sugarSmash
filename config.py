import pygame
# for declaring global variables

pygame.init()

SCREEN_SIZE = (300,600)
BORDER = 30

#colors
BACKGROUND = (150,200,100)
LIGHT = (191,255,128)
DARK = (105,55,155)
WHITE = (255, 255, 255) 

PIECE_SIZE = 40

SCREEN  = pygame.display.set_mode(SCREEN_SIZE)

FONT = pygame.font.Font('freesansbold.ttf', 20)

CLOCK = pygame.time.Clock()