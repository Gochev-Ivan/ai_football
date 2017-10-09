game_name = 'AI Football'
fps = 60
dt = 1/fps

resolution = 1366, 768
resolution_rect = [0, 0, resolution[0], resolution[1]]
ground = [0, int(resolution[1]/5), resolution[0], resolution[1]]
ground_rect = [ground[0], ground[1], resolution[0], resolution[1]]
playground = [50, 50 + int(resolution[1]/5), resolution[0] - 50, resolution[1] - 50]
playground_rect = [playground[0], playground[1], playground[2] - playground[0], playground[3] - playground[1]]
half_playground_rect = [playground_rect[0], playground_rect[1], int(playground_rect[2]/2), playground_rect[3]]
center = [int((playground[2] - playground[0]) / 2) + playground[0],
          int((playground[3] - playground[1]) / 2) + playground[1]]

post_radius = 10
post_screen_top = 343
post_screen_bottom = 578
post_screen_left = playground[0]
post_screen_right = playground[2]

player_1_initial_position = [int((center[0] - playground[0])/2) + playground[0], post_screen_top]
player_2_initial_position = [int((center[0] - playground[0])/2) + playground[0], center[1]]
player_3_initial_position = [int((center[0] - playground[0])/2) + playground[0], post_screen_bottom]
player_4_initial_position = [player_1_initial_position[0] + half_playground_rect[2], post_screen_top]
player_5_initial_position = [player_2_initial_position[0] + half_playground_rect[2], center[1]]
player_6_initial_position = [player_3_initial_position[0] + half_playground_rect[2], post_screen_bottom]

initial_positions_team_left = [player_1_initial_position, player_2_initial_position, player_3_initial_position]
initial_positions_team_right = [player_4_initial_position, player_5_initial_position, player_6_initial_position]

# Colors:
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
yellow = [255, 255, 0]
green = [0, 255, 0]
sky_blue = [135, 206, 250]
blue = [0, 0, 255]
grass = [1, 142, 14]

# Background:
background_color = white
background_picture = "background.png"

# Agent parameters:
cursor_width = 5

ball_restitution = 0.6
player_player_restitution = 0.5
ball_restitution_under_player_control = 0.4
player_post_restitution = 0.5
half_time_duration = 45

team_1_color = red
team_2_color = yellow
