from constants import *
import numpy as np


def collision(circle1, circle2):
    if (circle1.x - circle2.x)**2 + (circle1.y - circle2.y)**2 <= (circle1.radius + circle2.radius)**2:
        return True
    return False


def boundaries(x, y):
    x1, y1 = x[0], y[0]
    x2, y2 = x[1], y[1]
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
    x = [x1, x2]
    y = [y1, y2]
    return x, y


def get_back(circle):
    circle.x = np.clip(circle.x, radius, playground[0] - radius)
    circle.y = np.clip(circle.y, radius, playground[1] - radius)
    return circle


def resolve_collision(circle1, circle2, shoot_requsted):
    collision_angle = np.arctan2(circle2.y - circle1.y, circle2.x - circle1.x)

    new_x_speed_1 = circle1.v * np.cos(circle1.alpha - collision_angle)
    new_y_speed_1 = circle1.v * np.sin(circle1.alpha - collision_angle)
    new_x_speed_2 = circle2.v * np.cos(circle2.alpha - collision_angle)
    new_y_speed_2 = circle2.v * np.sin(circle2.alpha - collision_angle)

    final_x_speed_1 = ((circle1.mass - circle2.mass) * new_x_speed_1 + (circle2.mass + circle2.mass) * new_x_speed_2) \
                      / (circle1.mass + circle2.mass)
    final_x_speed_2 = ((circle1.mass + circle1.mass) * new_x_speed_1 + (circle2.mass - circle1.mass) * new_x_speed_2) \
                      / (circle1.mass + circle2.mass)
    final_y_speed_1 = new_y_speed_1
    final_y_speed_2 = new_y_speed_2

    cos_gamma = np.cos(collision_angle)
    sin_gamma = np.sin(collision_angle)
    circle1.v_x = cos_gamma * final_x_speed_1 - sin_gamma * final_y_speed_1
    circle1.v_y = sin_gamma * final_x_speed_1 + cos_gamma * final_y_speed_1
    circle2.v_x = cos_gamma * final_x_speed_2 - sin_gamma * final_y_speed_2
    circle2.v_y = sin_gamma * final_x_speed_2 + cos_gamma * final_y_speed_2

    pos1 = np.array([circle1.x, circle1.y])
    pos2 = np.array([circle2.x, circle2.y])

    # get the mtd
    pos_diff = pos1 - pos2
    d = np.linalg.norm(pos_diff)

    # minimum translation distance to push balls apart after intersecting
    mtd = pos_diff * (((circle1.radius + circle2.radius) - d) / d)

    # resolve intersection --
    # computing inverse mass quantities
    im1 = 1 / circle1.mass
    im2 = 1 / circle2.mass

    # push-pull them apart based off their mass
    pos1 = pos1 + mtd * (im1 / (im1 + im2))
    pos2 = pos2 - mtd * (im2 / (im1 + im2))
    circle1.x, circle1.y = pos1[0], pos1[1]
    circle2.x, circle2.y = pos2[0], pos2[1]

    if circle1.type_of_circle == 'player' and circle2.type_of_circle == 'player':
        circle1.v = 0.5 * np.sqrt(circle1.v_x**2 + circle1.v_y**2)
        circle2.v = 0.5 * np.sqrt(circle2.v_x**2 + circle2.v_y**2)
    if circle1.type_of_circle == 'player' and circle2.type_of_circle == 'ball':
        print("sudar na igrac so topka!")
        circle1.v = np.sqrt(circle1.v_x**2 + circle1.v_y**2)
        if shoot_requsted == True:
            circle2.v += 250
        else:
            circle2.v = 0.8 * np.sqrt(circle2.v_x**2 + circle2.v_y**2)
        # prior = 1 if shoot_requsted else 0.1
    circle1.alpha = np.arctan2(circle1.v_y, circle1.v_x)
    circle2.alpha = np.arctan2(circle2.v_y, circle2.v_x)

    snelius(circle1)
    snelius(circle2)

    return circle1, circle2


def snelius(circle):
    if circle.y + circle.radius >= playground[1] and np.sin(circle.alpha) > 0:
        circle.alpha = -circle.alpha
        if circle.type_of_circle == 'player':
            circle.v *= np.abs(np.cos(circle.alpha))
    if circle.y - circle.radius <= 0 and np.sin(circle.alpha) < 0:
        circle.alpha = -circle.alpha
        if circle.type_of_circle == 'player':
            circle.v *= np.abs(np.cos(circle.alpha))
    if circle.x + circle.radius >= playground[0] and np.cos(circle.alpha) > 0:
        circle.alpha = np.pi - circle.alpha
        if circle.type_of_circle == 'player':
            circle.v *= np.abs(np.sin(circle.alpha))
    if circle.x - circle.radius <= 0 and np.cos(circle.alpha) < 0:
        circle.alpha = -np.pi - circle.alpha
        if circle.type_of_circle == 'player':
            circle.v *= np.abs(np.sin(circle.alpha))
    return circle


def shoot(player, ball):
    # ball.v += 20*np.cos(player.alpha)
    rotation_speed = 5
    v_x = ball.v*np.cos(ball.alpha) + rotation_speed*np.cos(player.alpha)
    v_y = ball.v*np.sin(ball.alpha) + rotation_speed*np.sin(player.alpha)
    # ball.v_x = ball.v*np.cos(player.alpha)
    # ball.v_y = ball.v*np.sin(player.alpha)
    ball.v = np.sqrt(v_x**2 + v_y**2)
    ball.alpha = np.arctan2(v_y, v_x)
