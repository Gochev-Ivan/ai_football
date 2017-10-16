from defender import Defender
from middle import Middle
from forward import Forward

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
    print(our_score, their_score, end=' -- ')
    return manager_decision

