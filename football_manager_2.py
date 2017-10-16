def decision(our_team, their_team, ball, your_side, half, time_left, our_score, their_score):
    manager_decision = [dict(), dict(), dict()]
    for i in range(3):
        player = our_team[i]
        manager_decision[i]['alpha'] = player['alpha']
        manager_decision[i]['force'] = 0
        manager_decision[i]['shot_request'] = True
        manager_decision[i]['shot_power'] = 100000
    # print(our_score, their_score)
    return manager_decision

