from functions import *
import numpy as np
import football_manager as football_manager_1
import football_manager as football_manager_2
import time


def render(screen, team_1, team_2, ball, posts, team_1_score, team_2_score, time_to_play, start, countdown=False):
    # screen.blit(background, (0, 0))
    pygame.draw.rect(screen, white, resolution_rect)
    pygame.draw.rect(screen, grass, ground_rect)
    pygame.draw.rect(screen, black, resolution_rect, 2)
    pygame.draw.rect(screen, black, ground_rect, 2)
    pygame.draw.rect(screen, white, playground_rect, 2)
    pygame.draw.rect(screen, white, half_playground_rect, 2)
    pygame.draw.circle(screen, white, center, 100, 2)
    pygame.draw.circle(screen, white, center, 5)

    for player in team_1:
        player.draw(screen, team_1_color)
    for player in team_2:
        player.draw(screen, team_2_color)
    ball.draw(screen)
    for post in posts:
        post.draw(screen)

    if countdown:
        short_pause_countdown_time = 3
        myfont = pygame.font.SysFont("monospace", 750)
        short_pause_countdown = "{}".format(short_pause_countdown_time - int(time.time() - start))
        label = myfont.render(short_pause_countdown, 1, (0, 0, 0))
        screen.blit(label, (460, 85))
    else:
        myfont = pygame.font.SysFont("monospace", 150)
        message = "{} сек.".format(time_to_play - int(time.time() - start))
        label = myfont.render(message, 1, (0, 0, 0))
        screen.blit(label, (700, 0))

    myfont = pygame.font.SysFont("monospace", 150)
    message = "{}:{}".format(team_2_score, team_1_score)
    label = myfont.render(message, 1, (0, 0, 0))
    screen.blit(label, (300, 0))

    pygame.display.flip()
    pygame.time.Clock().tick(fps)


def play(screen, team_1, team_2, ball, posts, time_to_play, team_1_score, team_2_score, half):
    start = time.time()
    while time.time() - start < 3:
        render(screen, team_1, team_2, ball, posts, team_1_score, team_2_score, time_to_play, start, True)

    start = time.time()
    velocity_step = 100000
    angle_step = 0.1
    angle_change = 0
    velocity_change = 0

    circles = [team_1[0], team_1[1], team_1[2], team_2[0], team_2[1], team_2[2], ball, posts[0], posts[1], posts[2],
               posts[3]]
    goal = False
    game_exit = False
    while not game_exit:
        if time.time() - start >= time_to_play:
            return False, 0, team_1_score, team_2_score

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    angle_change = -angle_step
                if event.key == pygame.K_RIGHT:
                    angle_change = angle_step
                if event.key == pygame.K_UP:
                    velocity_change = velocity_step
                if event.key == pygame.K_DOWN:
                    velocity_change = -velocity_step
                if event.key == pygame.K_ESCAPE:
                    game_exit = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    angle_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    angle_change = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    velocity_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    velocity_change = 0

        if not goal:
            manager_1_decision = football_manager_1.decision(
                our_team=[team_1[0].data(), team_1[1].data(), team_1[2].data()],
                their_team=[team_2[0].data, team_2[1].data, team_2[2].data],
                ball=ball.data(),
                your_side='left' if half == 1 else 'right',
                half=half,
                time_left=time_to_play - int(time.time() - start))
            manager_2_decision = football_manager_2.decision(
                our_team=[team_2[0].data(), team_2[1].data(), team_2[2].data()],
                their_team=[team_1[0].data(), team_1[1].data(), team_1[2].data()],
                ball=ball.data(),
                your_side='right' if half == 1 else 'left',
                half=half,
                time_left=time_to_play - int(time.time() - start))

        manager_decision = [manager_1_decision[0], manager_1_decision[1], manager_1_decision[2],
                            manager_2_decision[0], manager_2_decision[1], manager_2_decision[2]]

        manager_decision[0]['alpha'] += angle_change
        manager_decision[0]['force'] += velocity_change

        for i, player in enumerate(circles[:-4]):
            if isinstance(player, Player):
                player.move(manager_decision[i])
            else:
                player.move()

        if not goal:
            goal_team_1 = post_screen_top < ball.y < post_screen_bottom and ball.x < post_screen_left
            goal_team_2 = post_screen_top < ball.y < post_screen_bottom and ball.x > post_screen_right
            if goal_team_1:
                team_1_score += 1
            if goal_team_2:
                team_2_score += 1
            goal = goal_team_1 or goal_team_2
        else:
            return True, time_to_play - int(time.time() - start), team_1_score, team_2_score

        if not goal:
            for i in range(len(circles[:-4])):
                circles[i].snelius()
                for j in range(i + 1, len(circles)):
                    if collision(circles[i], circles[j]):
                        circles[i], circles[j] = resolve_collision(circles[i], circles[j])

        render(screen, team_1, team_2, ball, posts, team_1_score, team_2_score, time_to_play, start)


def game(team_1, team_2, ball, posts):
    pygame.init()
    # screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption(game_name)
    # background = pygame.image.load(background_picture).convert()
    # screen.blit(background, (0, 0))
    # pygame.display.flip()
    team_1_score, team_2_score = 0, 0

    time_to_play = half_time_duration
    while time_to_play:
        for i, player in enumerate(team_1):
            player.reset(initial_positions_team_left[i], 0)
        for i, player in enumerate(team_2):
                player.reset(initial_positions_team_right[i], np.pi)
        ball.reset()
        goal, time_to_play, team_1_score, team_2_score = \
            play(screen, team_1, team_2, ball, posts, time_to_play, team_1_score, team_2_score, 1)

    time_to_play = half_time_duration
    while time_to_play:
        for i, player in enumerate(team_2):
            player.reset(initial_positions_team_left[i], 0)
        for i, player in enumerate(team_1):
                player.reset(initial_positions_team_right[i], np.pi)
        ball.reset()
        goal, time_to_play, team_2_score, team_1_score = \
            play(screen, team_1, team_2, ball, posts, time_to_play, team_2_score, team_1_score, 2)

    pygame.quit()


def main():
    team_1_players = [Player(500), Player(1), Player(2)]
    team_2_players = [Player(3), Player(4), Player(5)]
    ball = Ball(420, 250, 15, 0.5)
    posts = [Post(post_screen_left, post_screen_top, post_radius, 0),
             Post(post_screen_left, post_screen_bottom, post_radius, 0),
             Post(post_screen_right, post_screen_top, post_radius, 0),
             Post(post_screen_right, post_screen_bottom, post_radius, 0)]
    game(team_1_players, team_2_players, ball, posts)

if __name__ == "__main__":
    main()
