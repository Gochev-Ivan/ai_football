import math
infinity = float('inf')

class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Defender(metaclass=Singleton):
    x_position_left = 60
    x_position_right = 1306

    def __init__(self):
        self.player = None
        self.ball = None
        self.side = None

    def update_vals(self, player, ball, side):
        self.player = player
        self.ball = ball
        self.side = side

    def update(self):
        max_force = self.player['a_max'] * self.player['mass']
        x_position = self.x_position_left
        if self.side == 'right':
            x_position = self.x_position_right
        result = dict()
        if self.side == 'left':
            if self.player['x'] >= x_position + self.player['radius']:
                result['alpha'] = math.pi
                result['force'] = max_force
            else:
                if 343 <= self.ball['y'] <= 578:
                    if self.player['y'] > self.ball['y']:
                        result['alpha'] = math.pi * 3 / 2
                        result['force'] = max_force
                    elif self.player['y'] < self.ball['y']:
                        result['alpha'] = math.pi / 2
                        result['force'] = max_force
                    else:
                        result['force'] = 0
                        result['alpha'] = 0
                else:
                    if self.ball['y'] < 343:
                        if self.player['y'] > 343:
                            result['alpha'] = math.pi / 2
                            result['force'] = max_force
                    else:
                        if self.player['y'] < 578:
                            result['alpha'] = math.pi * 3 / 2
                            result['force'] = max_force
                    result['force'] = 0
                    result['alpha'] = 0
        else:
            if self.player['x'] + self.player['radius'] <= x_position:
                result['alpha'] = 0
                result['force'] = max_force
            else:
                if 343 <= self.ball['y'] <= 578:
                    if self.player['y'] > self.ball['y']:
                        result['alpha'] = math.pi * 3 / 2
                        result['force'] = max_force
                    elif self.player['y'] < self.ball['y']:
                        result['alpha'] = math.pi / 2
                        result['force'] = max_force
                    else:
                        result['force'] = 0
                        result['alpha'] = math.pi
                else:
                    if self.ball['y'] < 343:
                        if self.player['y'] > 343:
                            result['alpha'] = math.pi / 2
                            result['force'] = max_force
                    else:
                        if self.player['y'] < 578:
                            result['alpha'] = math.pi * 3 / 2
                            result['force'] = max_force
                    result['force'] = 0
                    result['alpha'] = math.pi
        result['shot_power'] = self.player['shot_power_max']
        result['shot_request'] = True
        return result

class Middle(metaclass=Singleton):
    x_position_left = 370
    x_position_right = 996

    def __init__(self):
        self.player = None
        self.ball = None
        self.side = None

    def update_vals(self, player, ball, side):
        self.player = player
        self.ball = ball
        self.side = side

    def in_front_of_ball(self):
        if self.side == 'left':
            return self.player['x'] > self.ball['x']
        return self.player['x'] < self.ball['x']

    def update(self):
        max_force = self.player['a_max'] * self.player['mass']
        x_position = self.x_position_left
        if self.side == 'right':
            x_position = self.x_position_right
        result = dict()
        if self.in_front_of_ball():
            result['shot_request'] = False
            result['shot_power'] = 0
            result['alpha'] = math.pi
            if self.side == 'right':
                result['alpha'] = 0
            result['force'] = -infinity
        else:
            if self.side == 'left':
                if self.player['x'] >= x_position:
                    result['alpha'] = math.pi
                    result['force'] = max_force
                else:
                    if self.player['y'] > self.ball['y']:
                        result['alpha'] = math.pi * 3 / 2
                        result['force'] = max_force
                    elif self.player['y'] < self.ball['y']:
                        result['alpha'] = math.pi / 2
                        result['force'] = max_force
                    else:
                        result['force'] = 0
                        result['alpha'] = 0
            else:
                if self.player['x'] <= x_position:
                    result['alpha'] = 0
                    result['force'] = max_force
                else:
                    if self.player['y'] > self.ball['y']:
                        result['alpha'] = math.pi * 3 / 2
                        result['force'] = max_force
                    elif self.player['y'] < self.ball['y']:
                        result['alpha'] = math.pi / 2
                        result['force'] = max_force
                    else:
                        result['alpha'] = math.pi
                        result['force'] = 0
            result['shot_power'] = self.player['shot_power_max']
            result['shot_request'] = True
        return result

class Forward(metaclass=Singleton):
    def __init__(self):
        self.player = None
        self.ball = None
        self.side = None

    def update_vals(self, player, ball, side):
        self.player = player
        self.ball = ball
        self.side = side

    def update(self):
        result = dict()
        if not self.behind_the_ball():
            result = self.get_behind_the_ball()
        else:
            result = self.get_posession()
        return result

    def behind_the_ball(self):
        if self.side == 'left':
            return self.player['x'] + self.player['radius'] < self.ball['x'] - self.ball['radius']
        return self.player['x'] - self.player['radius'] > self.ball['x'] + self.ball['radius']

    def get_behind_the_ball(self):
        result = dict()
        result['alpha'] = math.pi
        if self.side == 'right':
            result['alpha'] = 0
        result['force'] = self.player['mass'] * self.player['a_max']
        result['shot_power'] = 0
        result['shot_request'] = False
        return result

    def get_posession(self):
        goalx=1316
        if self.side == 'right':
            goalx = 50
        goaly=460 
        angle=math.atan((goaly-self.ball['y'])/(goalx-self.ball['x']))
        angle2=math.atan((goaly-self.player['y'])/(goalx-self.player['x']))
        newx=self.ball['x']-math.cos(angle)*(self.ball['radius']+self.player['radius'])
        newy=self.ball['y']-math.sin(angle)*(self.ball['radius']+self.player['radius'])
        result = dict()
        result['force'] = self.player['mass'] * self.player['a_max']
        if self.side == 'left':
            result['alpha'] = math.atan((self.player['y'] - newy) / (self.player['x'] - newx))
        else:
            result['alpha'] = math.atan((self.player['y'] - self.ball['y']) / (self.player['x'] - self.ball['x'])) - math.pi
        result['shot_power'] = 1000
        result['shot_request'] = True
        return result

def decision(our_team, their_team, ball, your_side, half, time_left, our_score, their_score):
    manager_decision = [dict(), dict(), dict()]

    defender = Defender()
    defender.update_vals(our_team[1], ball, your_side)

    middle = Middle()
    middle.update_vals(our_team[2], ball, your_side)

    forward = Forward()
    forward.update_vals(our_team[0], ball, your_side)

    for i in range(3):
        if i == 1:
            player = defender.update()
        elif i == 2:
            player = middle.update()
        else:
            player = forward.update()
        manager_decision[i] = player
    # print(our_score, their_score, end=' -- ')
    return manager_decision

