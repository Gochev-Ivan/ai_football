import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, color, radius, width):
        # Call the parent class (Sprite) constructor
        super(Player,self).__init__()
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([radius, width])
        self.image.fill(white)
        self.image.set_colorkey(white)
        # Draw the player (a circle!)
#        pygame.draw.circle(gameDisplay,blue,(x1,y1),radius,width)
#        pygame.draw.circle(gameDisplay,red,(x2,y2),radius,width)
#        pygame.draw.rect(self.image, color, [0, 0, radius, width])
        # Instead we could load a proper pciture of the player...
        if color[0] == 0 and color[1] == 0 and color[2] == 255:
            self.image = pygame.image.load("player_blue.png").convert_alpha()
        if color[0] == 255 and color[1] == 0 and color[2] == 0:
            self.image = pygame.image.load("player_red.png").convert_alpha()
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()