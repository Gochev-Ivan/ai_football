import pygame
from constants import *
# from player import Player
from functions import *
import numpy as np
from math import atan2


class Object:
    mass = 1
    x, y = 50, 50
    v_x, v_y = 0, 0
    v = 0
    alpha = 0
    radius = 10

    def init(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass


def render():
    pygame.display.flip()
    clock.tick(fps)


if __name__ == "__main__":
    pygame.init()
    myfont = pygame.font.SysFont("monospace", 15)
    clock = pygame.time.Clock()
    game = pygame.display.set_mode(resolution)
    pygame.display.set_caption(gameName)
    background = pygame.image.load(background_picture).convert()
    game.blit(background, (0, 0))
    pygame.display.flip()
    # define players/teams:
    gameExit = False
    x1, y1 = 50, 50
    x2, y2 = 150, 150
    dx1, dy1 = 0, 0
    dx2, dy2 = 0, 0
    ball_x, ball_y = 100, 100
    v = 0
    v_x1, v_y1 = 0, 0
    velocity_step = 100
    angle_step = 0.1
    player_1 = Object()
    player_2 = Object()
    player_3 = Object()
    player_1.x, player_1.y = 50, 50
    player_2.x, player_2.y = 150, 150
    player_3.x, player_3.y = 200, 200
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx1 = -5
                    v_x1 -= velocity_step
                    player_1.v_x -= velocity_step
                    player_1.alpha -= angle_step
                if event.key == pygame.K_RIGHT:
                    dx1 = 5
                    v_x1 += velocity_step
                    player_1.v_x += velocity_step
                    player_1.alpha += angle_step
                if event.key == pygame.K_UP:
                    dy1 = -5
                    v_y1 -= velocity_step
                    player_1.v_y -= velocity_step
                    player_1.v += velocity_step
                if event.key == pygame.K_DOWN:
                    dy1 = 5
                    v_y1 += velocity_step
                    player_1.v_y += velocity_step
                    player_1.v -= velocity_step
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
        """===================== Coordinates Eval =========================="""
        # x1 += v_x1 * dt
        # y1 += v_y1 * dt
        x2 += dx2
        y2 += dy2

        m = 1
        F = 50
        a = 50
        alfa = np.pi/2
        v += a * dt
        # v = np.clip(v, 0, v_max)
        ball_x += np.cos(alfa) * v * dt
        ball_y += np.sin(alfa) * v * dt
        player_1.x += np.cos(player_1.alpha) * player_1.v * dt
        player_1.y += np.sin(player_1.alpha) * player_1.v * dt
        player_2.x += np.cos(player_2.alpha) * player_2.v * dt
        player_2.y += np.sin(player_2.alpha) * player_2.v * dt
        player_3.x += np.cos(player_3.alpha) * player_3.v * dt
        player_3.y += np.sin(player_3.alpha) * player_3.v * dt
        # x2 += np.cos(alfa) * v * dt

        # x1, y1 = get_back(x1, y1)
        # x2, y2 = get_back(x2, y2)
        # ball_x, ball_y = get_back(ball_x, ball_y)
        """================================================================="""
        # check for collision:
        x = [x1, x2]
        y = [y1, y2]

        # for player in [player_1, player_2]:
        # player_1.x, player_1.y = get_back(player_1)
        player1 = snelius(player_1)
        player2 = snelius(player_2)
        player3 = snelius(player_3)

        if collision(player_1, player_2):
            print('sudar')
            resolve_collision(player_1, player_2)
        # player_2.x, player_2.y = get_back(player_2)

        game.blit(background, (0, 0))
        pygame.draw.circle(game, blue, [int(player_1.x), int(player_1.y)], player_1.radius)
        pygame.draw.circle(game, red, [int(player_2.x), int(player_2.y)], player_2.radius)
        pygame.draw.circle(game, green, [int(ball_x), int(ball_y)], ball_radius)
        pygame.draw.rect(game, black, [0, 0, *playground], 2)
        message = "player1: alpha: {:3f} v_x: {} v_y: {} v: {}".format(player_1.alpha * 180 / np.pi, player_1.v_x,
                                                                    player_1.v_y, player_1.v)
        label = myfont.render(message, 1, (0, 0, 0))
        game.blit(label, (20, 260))
        render()
    pygame.quit()
