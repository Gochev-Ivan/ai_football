def decision(our_team, their_team, ball, your_side, half, time_left):
    manager_decision = [dict(), dict(), dict()]
    for i in range(3):
        player = our_team[i]
        manager_decision[i]['alpha'] = player['alpha']
        manager_decision[i]['force'] = 0
        manager_decision[i]['shot_request'] = True
        manager_decision[i]['shot_power'] = 100000
    return manager_decision

