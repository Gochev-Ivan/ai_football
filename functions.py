from constants import *
import numpy as np


def collision(object1, object2):
    if (object1.x - object2.x)**2 + (object1.y - object2.y)**2 <= (object1.radius + object2.radius)**2:
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
    # if circle.x < radius:
    #     circle.alpha =
    circle.x = np.clip(circle.x, radius, resolution[0] - radius)
    circle.y = np.clip(circle.y, radius, resolution[1] - radius)
    return circle


def resolve_collision(object1, object2):
    collision_angle = np.arctan2(object2.y - object1.y, object2.x - object1.x)
    # speed1 = np.sqrt(object1.v_x**2 + object1.v_y**2)
    # speed2 = np.sqrt(object2.v_x**2 + object2.v_y**2)

    # direction_1 = np.arctan2(object1.v_y, object1.v_x)
    # direction_2 = np.arctan2(object2.v_y, object2.v_x)
    new_x_speed_1 = object1.v * np.cos(object1.alpha - collision_angle)
    new_y_speed_1 = object1.v * np.sin(object1.alpha - collision_angle)
    new_x_speed_2 = object2.v * np.cos(object2.alpha - collision_angle)
    new_y_speed_2 = object2.v * np.sin(object2.alpha - collision_angle)

    final_x_speed_1 = ((object1.mass - object2.mass) * new_x_speed_1 + (object2.mass + object2.mass) * new_x_speed_2) \
                      / (object1.mass + object2.mass)
    final_x_speed_2 = ((object1.mass + object1.mass) * new_x_speed_1 + (object2.mass - object1.mass) * new_x_speed_2) \
                      / (object1.mass + object2.mass)
    final_y_speed_1 = new_y_speed_1
    final_y_speed_2 = new_y_speed_2

    cos_gamma = np.cos(collision_angle)
    sin_gamma = np.sin(collision_angle)
    object1.v_x = cos_gamma * final_x_speed_1 - sin_gamma * final_y_speed_1
    object1.v_y = sin_gamma * final_x_speed_1 + cos_gamma * final_y_speed_1
    object2.v_x = cos_gamma * final_x_speed_2 - sin_gamma * final_y_speed_2
    object2.v_y = sin_gamma * final_x_speed_2 + cos_gamma * final_y_speed_2

    pos1 = np.array([object1.x, object1.y])
    pos2 = np.array([object2.x, object2.y])

    # get the mtd
    pos_diff = pos1 - pos2
    d = np.linalg.norm(pos_diff)

    # minimum translation distance to push balls apart after intersecting
    mtd = pos_diff * (((object1.radius + object2.radius) - d) / d)

    # resolve intersection --
    # computing inverse mass quantities
    im1 = 1 / object1.mass
    im2 = 1 / object2.mass

    # push-pull them apart based off their mass
    pos1 = pos1 + mtd * (im1 / (im1 + im2))
    pos2 = pos2 - mtd * (im2 / (im1 + im2))
    object1.x, object1.y = pos1[0], pos1[1]
    object2.x, object2.y = pos2[0], pos2[1]

    object1.v = np.sqrt(object1.v_x**2 + object1.v_y**2)
    object2.v = np.sqrt(object2.v_x**2 + object2.v_y**2)
    object1.alpha = np.arctan2(object1.y, object1.x)
    object2.alpha = np.arctan2(object2.y, object2.x)

    snelius(object1)
    snelius(object2)

    # if object1.x + object1.radius >= playground[0] or object1.x - object1.radius <= 0:
    #     object1.v_x = -1 * object1.v_x
    #
    # if object1.y + object1.radius >= playground[1] or object1.y - object1.radius <= 0:
    #     object1.v_y = -1 * object1.v_y
    #
    # if object2.x + object2.radius >= playground[0] or object2.x - object2.radius <= 0:
    #     object2.v_x = -1 * object2.v_x
    #
    # if object2.y + object2.radius >= playground[1] or object2.y - object2.radius <= 0:
    #     object2.v_y = -1 * object2.v_y


def snelius(circle):
    # Snell's Law
    if circle.y + circle.radius >= playground[1]:
        circle.alpha = -circle.alpha
    if circle.y - circle.radius <= 0:
        circle.alpha = -circle.alpha
    if circle.x + circle.radius >= playground[0]:
        circle.alpha = np.pi - circle.alpha
    if circle.x - circle.radius <= 0:
        circle.alpha = -np.pi - circle.alpha
    return circle