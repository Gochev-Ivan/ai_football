import pygame
from constants import *

def render():
    pygame.display.flip()
    clock.tick(frames)

if __name__ == "__main__":
    clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode(resolution)
    pygame.display.set_caption(gameName)
    background = pygame.image.load(background_picture).convert()
    gameDisplay.blit(background,(0,0))
    pygame.display.flip()
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx1 = -5
                if event.key == pygame.K_RIGHT:
                    dx1 = 5
                if event.key == pygame.K_UP:
                    dy1 = -5
                if event.key == pygame.K_DOWN:
                    dy1 = 5
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dx1 = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    dy1 = 0
        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0
        if x1 > resolution[0] - 50:
            x1 = resolution[0] - 50
        if y1 > resolution[1] - 50:
            y1 = resolution[1] - 50
        print "(x1, y1)", (x1,y1)
        x1 += dx1
        y1 += dy1
        gameDisplay.blit(background,(0,0))
        pygame.draw.circle(gameDisplay,blue,(x1,y1),10,10)
        render()
    pygame.quit()