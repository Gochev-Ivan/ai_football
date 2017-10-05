import pygame
from constants import *
from player import Player
from functions import boundaries, collision

def render():
    pygame.display.flip()
    clock.tick(frames)

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode(resolution)
    pygame.display.set_caption(gameName)
    background = pygame.image.load(background_picture).convert()
    gameDisplay.blit(background,(0,0))
    pygame.display.flip()
    # define players/teams:
    player1 = Player(blue,radius,width)
    player2 = Player(red,radius,width)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player1)
    all_sprites_list.add(player2)
    while not gameExit:
        all_sprites_list.update()
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
        print "(x1, y1)", (x1,y1)
        print "(x2, y2)", (x2,y2)
        """===================== Coordinates Eval =========================="""
        x = [x1,x2] # x-coord for players
        y = [y1,y2] # y-coord for players
        x,y = boundaries(x,y)
        x1,y1 = x[0],y[0]
        x2,y2 = x[1],y[1]
        x1 += dx1
        y1 += dy1
        x2 += dx2
        y2 += dy2
        x = [x1,x2]
        y = [y1,y2]
        # update player coord:
        player1.rect.x = x1
        player1.rect.y = y1
        player2.rect.x = x2
        player2.rect.y = y2
        """================================================================="""
        # check for collision:
        if collision(x,y) == True:
            print "SUDAR"
        gameDisplay.blit(background,(0,0))
        all_sprites_list.draw(gameDisplay)
        render()
    pygame.quit()