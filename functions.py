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


def dribble(player, ball):
    # ball.v += 20*np.cos(player.alpha)
    print("driblam!")
    # ball.v += ball.v / (1 + 0.02*ball.v*dt)

    dribble_speed = 1
    ball.v += 0.1
    Cl = 1/(2 + dribble_speed/(ball.v*ball.radius))
    Cd = 0.55 + 1/(22.5 + 4.2*(dribble_speed/(ball.v*ball.radius))**(2.5)**0.4)

    beta = 45
    A = ball.radius**2 * np.pi
    Fd = Cd * A * 1.21 * ball.v ** 2 / 2
    Fl = Cl * A * 1.21 * ball.v ** 2 / 2
    a_x = (1 / ball.mass) * ((-Fd) * np.cos(beta) - Fl * np.sin(beta)) * dt
    a_y = (1 / ball.mass) * (Fl * np.cos(beta) - Fd * np.sin(beta)) * dt


    ball.v_x += a_x*dt
    ball.v_y += a_y*dt
    # ball.v_x -= 1.21 * ball.v * (Cd * ball.v_x + Cl * ball.v_y)*dt
    # ball.v_y += 1.21 * ball.v * (Cl * ball.v_x - Cd * ball.v_y)*dt
    ball.v += np.sqrt(ball.v_x**2 + ball.v_y**2)
    # ball.move()
    # print("Cl, Cd , ball_v_x, ball_v_y, ball.alpha: ", Cl, Cd, ball.v_x, ball.v_y, ball.alpha)
    print("Cl: {:3f} Cd: {:3f} ball_v_x: {:3f} ball_v_y: {:3f}: ball_alpha: {:3f}".format(Cl, Cd, ball.v_x, ball.v_y, ball.alpha))

    ##
    # F = Cl*A*1.21*dribble_speed**2/2
    # a = F/ball.mass
    # ball.v += a*dt




    ##
    # rotation_speed = 5
    # v_x = ball.v*np.cos(ball.alpha) + rotation_speed*np.cos(player.alpha)
    # v_y = ball.v*np.sin(ball.alpha) + rotation_speed*np.sin(player.alpha)
    # # ball.v_x = ball.v*np.cos(player.alpha)
    # # ball.v_y = ball.v*np.sin(player.alpha)
    # ball.v = np.sqrt(v_x**2 + v_y**2)
    # ball.alpha = np.arctan2(v_y, v_x)
