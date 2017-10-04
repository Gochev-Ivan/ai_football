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
                if event.key == pygame.K_a:
                    dx2 = -5
                if event.key == pygame.K_d:
                    dx2 = 5
                if event.key == pygame.K_w:
                    dy2 = -5
                if event.key == pygame.K_s:
                    dy2 = 5
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dx1 = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    dy1 = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    dx2 = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    dy2 = 0
        if x1 < (radius + width):
            x1 = (radius + width)
        if y1 < (radius + width):
            y1 = (radius + width)
        if x1 > resolution[0] - (radius + width):
            x1 = resolution[0] - (radius + width)
        if y1 > resolution[1] - (radius + width):
            y1 = resolution[1] - (radius + width)
        if x2 < (radius + width):
            x2 = (radius + width)
        if y2 < (radius + width):
            y2 = (radius + width)
        if x2 > resolution[0] - (radius + width):
            x2 = resolution[0] - (radius + width)
        if y2 > resolution[1] - (radius + width):
            y2 = resolution[1] - (radius + width)
        print "(x1, y1)", player1
        print "(x2, y2)", (x2,y2)
        x1 += dx1
        y1 += dy1
        x2 += dx2
        y2 += dy2
        gameDisplay.blit(background,(0,0))
        pygame.draw.circle(gameDisplay,blue,(x1,y1),radius,width)
        pygame.draw.circle(gameDisplay,red,(x2,y2),radius,width)
        render()
    pygame.quit()