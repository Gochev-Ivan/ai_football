import pygame
from constants import *
from functions import *
import numpy as np


class Circle:
    mass = 1
    x, y = 50, 50
    v_x, v_y = 0, 0
    v = 0
    alpha = 0
    radius = 20
    type_of_circle = ''

    def init(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass

    def move(self):
        self.x += np.cos(self.alpha) * self.v * dt
        self.y += np.sin(self.alpha) * self.v * dt
        if self.type_of_circle == 'ball':
            self.v *= 0.99

    def draw(self):
        pygame.draw.circle(game, blue, [int(self.x), int(self.y)], self.radius)
        new_x = self.x + self.radius * np.cos(self.alpha)
        new_y = self.y + self.radius * np.sin(self.alpha)
        pygame.draw.line(game, black, [self.x, self.y], [new_x, new_y], cursor_width)


class Player(Circle):
    q = 1


class Ball(Circle):
    q = 1


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
    velocity_step = 10
    angle_step = 0.1
    angle_change = 0
    velocity_change = 0
    player_1 = Circle()
    player_2 = Circle()
    player_3 = Circle()
    player_1.x, player_1.y, player_1.mass = 50, 50, 100
    player_2.x, player_2.y, player_1.mass = 150, 150, 80
    player_3.x, player_3.y, player_1.mass = 200, 200, 72
    player_1.type_of_circle = 'player'
    player_2.type_of_circle = 'player'
    player_3.type_of_circle = 'player'
    ball = Circle()
    ball.radius = 10
    ball.x, ball.y = 100, 200
    ball.type_of_circle = 'ball'
    ball.mass = 0.5
    shoot_requst = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    angle_change = -angle_step
                if event.key == pygame.K_RIGHT:
                    angle_change = angle_step
                if event.key == pygame.K_UP:
                    velocity_change = velocity_step
                    player_1.v += velocity_change
                if event.key == pygame.K_DOWN:
                    velocity_change = -velocity_step
                    player_1.v += velocity_change
                if event.key == pygame.K_s:
                    print("sut na topka aktiviran!")
                    shoot_requst = True
                    # shoot(player_1, ball)
                if event.key == pygame.K_d:
                    print("sut na topka deaktiviran!")
                    shoot_requst = False
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    angle_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    angle_change = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    velocity_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    velocity_change = 0

        player_1.alpha += angle_change
        # player_1.v += velocity_change
        if player_1.v < 0:
            player_1.v = 0
        for player in [player_1, ball]:
            player.move()

        circles = [player_1, ball]
        for i in range(len(circles)):
            circles[i] = snelius(circles[i])
            for j in range(i+1, len(circles)):
                if collision(circles[i], circles[j]):
                    circles[i], circles[j] = resolve_collision(circles[i], circles[j], shoot_requsted=shoot_requst)

        game.blit(background, (0, 0))
        player_1.draw()
        for player in [player_1]:
            player.draw()
        pygame.draw.circle(game, green, [int(ball.x), int(ball.y)], ball.radius)
        pygame.draw.rect(game, black, [0, 0, playground[0], playground[1]], 2)
        message = "player_1: alpha: {:3f} v: {:3f} ball_v: {:3f}".format(player_1.alpha * 180 / np.pi, player_1.v, ball.v)
        label = myfont.render(message, 1, (0, 0, 0))
        game.blit(label, (20, 260))
        render()
    pygame.quit()
