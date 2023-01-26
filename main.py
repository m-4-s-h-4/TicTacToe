import pygame

pygame.init()

width = 600 #window size
height = 600
screen = pygame.display.set_mode((width, height))

game_grid = [["-" for x in range(3)] for y in range(3)] #a 3 by 3 grid 

active = True
while active:
    screen.fill((255, 255, 255)) # window colour

    for row in range(1, 3): #grid in black
        pygame.draw.line(screen, (0, 0, 0), (0, row*(height//3)), (width, row*(height//3)), 2)
    for col in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (col*(width//3), 0), (col*(width//3), height), 2)

    pygame.display.update() #update the window

pygame.quit()
