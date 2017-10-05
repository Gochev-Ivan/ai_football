import pygame
from constants import *

def collision(x,y):
    # da se napravat x i y za site igraci od tim:
    x1,y1 = x[0],y[0]
    x2,y2 = x[1],y[1]
    if ( ((x1-x2)**2)+((y1-y2)**2) ) <= ( (2*radius)**2 ):
        return True
    elif ( ((x1-x2)**2)+((y1-y2)**2) ) > ( (2*radius)**2 ):
        return False

def boundaries(x,y):
    x1,y1 = x[0],y[0]
    x2,y2 = x[1],y[1]
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
    x = [x1,x2]
    y = [y1,y2]
    return x,y