# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:40:28 2017

@author: andri_000
"""

import math
import numpy as np
import time

def find_keeper(opponent_team, your_side):
    X_opponents = []
    for k in range(3):
        X_opponents.append(opponent_team[k]['x'])
    X_opponents = np.array(X_opponents)
    if(your_side=='right'):
        return np.argmin(X_opponents)
    else:
        return np.argmax(X_opponents)

def gol1(x0,y0,x1,y1):
    if(x1!=x0):
        k=(y1-y0)/(x1-x0)
        n=y0-k*x0
        y=k*50+n
        return y
    return 0
def gol2(x0,y0,x1,y1):
    if(x1!=x0):
        k=(y1-y0)/(x1-x0)
        n=y0-k*x0
        y=k*1316+n
        return y
    return 0 

def find_closest(players,ball):
    distances = []
    for k in range(0,2):
        distances.append(distance(players[k]['x'], players[k]['y'], ball['x'], ball['y']))
    return [np.argmin(distances), np.min(distances)]

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def ugao(x0,y0,x1,y1):
    if (x0<x1):
        return math.atan((y1-y0)/(x1-x0))
    elif(x0==x1):
        return 0
    return math.pi-math.atan((y1-y0)/(x0-x1))

def blocked (player,alpha,ball,v0,force):
    t=0.1
    acc=force/player['mass']
    v=v0+acc*t
    s=acc*t*t/2+v0*t
    x_next=player['x']+s*math.cos(alpha)
    y_next=player['y']-s*math.sin(alpha)
    dist=distance(x_next,y_next,ball['x'],ball['y'])
    if dist<=(ball['radius']+player['radius']):
        return True
    else:
        return False
    
def blocked_shot (their_players,biza,alpha,ball_x,ball_y,v0):
    times=np.linspace(0,5,10)
    for t in times:
        s=v0*t
        x_next=ball_x+s*math.cos(alpha)
        y_next=ball_y-s*math.sin(alpha)
        for k in range(0,3):
            player = their_players[k]
            dist=distance(x_next,y_next,player['x'],player['y'])
            if dist<=(15+player['radius']):
                return True
        distb = distance(x_next,y_next,biza['x'],biza['y'])
        if distb<=(15+biza['radius']):
            return True
    return False

def find_shot_path(their_players, biza, ball_x, ball_y,your_side):
    if(your_side=='left'):
        post1 = [1316,343]
        post2 = [1316,578]
        # da ne bi gadjao bas u post1 i post2
        post1 = [1316,380]
        post2 = [1316,540]
        min_alpha = np.arctan2(post1[1]-ball_y,post1[0]-ball_x)
        max_alpha = np.arctan2(post2[1]-ball_y,post2[0]-ball_x)
        alphas = np.linspace(min_alpha,max_alpha,10)
        for alpha in alphas:
            if(not blocked_shot(their_players,biza,alpha,ball_x,ball_y,300)):
                return alpha
        return find_shot_martinela(their_players,biza,ball_x, ball_y,your_side)
    else:
        post1 = [50,380]
        post2 = [50,540]
        # PROVERI!!!
        min_alpha = ugao(ball_x,ball_y,post1[0],post1[1])
        max_alpha = ugao(ball_x,ball_y,post2[0],post2[1])
        alphas = np.linspace(min_alpha,max_alpha,10)
        for alpha in alphas:
            if(not blocked_shot(their_players,biza,alpha,ball_x,ball_y,300)):
                return alpha
        return find_shot_martinela(their_players,biza,ball_x, ball_y,your_side)


def find_shot_path_2(their_players, biza,ball_x, ball_y,your_side):
    if(your_side=='left'):
        post1 = [1316,343]
        post2 = [1316,578]
        # da ne bi gadjao bas u post1 i post2
        post1 = [1316,380]
        post2 = [1316,540]
        min_alpha = np.arctan2(post1[1]-ball_y,post1[0]-ball_x)
        max_alpha = np.arctan2(post2[1]-ball_y,post2[0]-ball_x)
        alphas = np.linspace(min_alpha,max_alpha,10)
        for alpha in alphas:
            if(not blocked_shot(their_players,biza,alpha,ball_x,ball_y,300)):
                return alpha
        return find_shot_martinela(their_players,biza,ball_x, ball_y,your_side)
    else:
        post1 = [50,380]
        post2 = [50,540]
        # PROVERI!!!
        min_alpha = ugao(ball_x,ball_y,post1[0],post1[1])
        max_alpha = ugao(ball_x,ball_y,post2[0],post2[1])
        alphas = np.linspace(min_alpha,max_alpha,10)
        for alpha in alphas:
            if(not blocked_shot(their_players,biza,alpha,ball_x,ball_y,300)):
                return alpha
        return False

def find_shot_martinela(their_players,biza,ball_x,ball_y,your_side):
    if(your_side=='left'):
        post1 = [1316,380]
        post2 = [1316,540]
        y_preslikano = 0 
        if(ball_y>384):
            y_preslikano = 718+718-ball_y
        else:
            y_preslikano = -ball_y
        mart = find_shot_path_2(their_players,biza,ball_x,y_preslikano,your_side)
        if(isinstance(mart, bool)):
            return False
        return mart
    else:
        post1 = [50,380]
        post2 = [50,540]
        y_preslikano = 0
        if(ball_y>384):
            y_preslikano = 718+718-ball_y
        else:
            y_preslikano = -ball_y
        mart = find_shot_path_2(their_players,biza,ball_x,y_preslikano,your_side)
        if(isinstance(mart, bool)):
            return False
        return mart

def find_path(player,ball,v0,force):
    dalpha=0.1
    alpha=player['alpha']
    while (blocked(player,alpha,ball,v0,force)):
        alpha=alpha+dalpha
    return alpha
    


def computeAlpha(player,ball, beta,v0,your_side,half,force):
    if ((your_side=='left') and player['x']>=(ball['x']-40)) or (your_side=='right' and player['x']<=(ball['x']+40)):
        alpha=find_path(player,ball,v0,force)
    else:
        x1=ball['x']-math.cos(beta)*(ball['radius']+player['radius']-4)
        y1=ball['y']-math.sin(beta)*(ball['radius']+player['radius']-4)
        alpha=math.atan2((y1-player['y']),(x1-player['x']))
    return alpha

def computeBeta(ball,their_team):
    beta=math.atan((550-ball['y'])/(50-ball['x']))
    return beta


v0=0
resolution = 1366, 768
playground = [50, 50 + int(resolution[1]/5), resolution[0] - 50, resolution[1] - 50]
center = [int((playground[2] - playground[0]) / 2) + playground[0],
          int((playground[3] - playground[1]) / 2) + playground[1]]
x=int((center[0] - playground[0])/2) + playground[0]
y=center[1]
t=0

D=340
iter=0
d=0
iter=0
iter1=0
x0=0
y0=0
tL=0
tR=0
positionL=False
positionR=False
rezultat=0
firstL=True
firstR=True
def decision(our_team, their_team, ball, your_side, half, time_left, our_score, their_score):
    manager_decision = [dict(), dict(), dict()]
    global v0
    global x
    global y
    global D
    global iter
    global iter1
    global x0
    global y0
    global tL
    global tR
    global rezultat
    global positionL
    global positionR
    global d
    global firstL
    global firstR
    for i in range(3):
        player = our_team[i]
        if (i==2):
            if (your_side=='left'):
                if firstL==True:
                    iter=0
                    firstL=False
                if not(positionL):
                    s=distance(our_team[i]['x'],our_team[i]['y'],50,460)
                    manager_decision[i]['alpha'] =ugao(our_team[i]['x'],our_team[i]['y'],50,460)
                    if (iter== iter1+1) or (iter==0):
                        D=s
                    if (s<D/2):
                        manager_decision[i]['force'] = -30000
                    else:
                        manager_decision[i]['force'] =30000
                else:
                    x1=ball['x']
                    y1=ball['y']
                    t=gol1(x0,y0,x1,y1)
                    if (t<our_team[i]['y']) and (t>353):
                        manager_decision[i]['alpha']=-math.pi/2
                        s=distance(our_team[i]['x'],our_team[i]['y'],50,t)
                        if (t!=tL):
                            d=s
                        if (s < d / 2):
                            manager_decision[i]['force'] = -200000
                        else:
                            manager_decision[i]['force'] = 200000
                    else:
                        if (t>our_team[i]['y']) and (t<568):
                            manager_decision[i]['alpha'] = math.pi / 2
                            s = distance(our_team[i]['x'], our_team[i]['y'], 50, t)
                            if (t != tL):
                                d = s
                            if (s < d / 2):
                                manager_decision[i]['force'] = -1000000
                            else:
                                manager_decision[i]['force'] = 1000000
                        else:
                            q=True
                            koef=(1-ball['x']/1366)
                            if (ball['y'] <= 460) and (our_team[i]['y']>343+10+our_team[i]['radius']) and not(math.isnan(t)):
                                manager_decision[i]['force'] = 40000*koef
                                manager_decision[i]['alpha'] = -math.pi / 2
                                q=False
                            else:
                                if (our_team[i]['y'] <= 343+10+our_team[i]['radius'])  or math.isnan(t):
                                    manager_decision[i]['force'] = 0
                                    manager_decision[i]['alpha'] = ((-1) ** iter) * math.pi / 2
                            if (ball['y'] > 460) and (our_team[i]['y'] <578-10-our_team[i]['radius'])and not(math.isnan(t)):
                                manager_decision[i]['force'] = 40000*koef
                                manager_decision[i]['alpha'] = math.pi / 2
                            else:
                                if ((our_team[i]['y']>=578-10-our_team[i]['radius']) or math.isnan(t)) and q:
                                    manager_decision[i]['force'] = 0
                                    manager_decision[i]['alpha'] = ((-1) ** iter) * math.pi / 2
                        tL=t
                        x0=x1
                        y0=y1
                manager_decision[i]['shot_request'] = True
                manager_decision[i]['shot_power'] = 100000
                if (int(our_team[i]['x']) in range (40,60)) and (int(our_team[i]['y']) in range (450,470)):
                    positionL=True
                if  ((our_team[i]['x'])<30) or ((our_team[i]['x'])>70):
                    positionL=False
                    iter1=iter
                if (rezultat!=(their_score+our_score)):
                    positionL=False
                rezultat=their_score+our_score
            if (your_side=='right'):
                if not(positionR):
                    if firstR==True:
                        iter=0
                        firstR=False
                    s=distance(our_team[i]['x'],our_team[i]['y'],1316,460)
                    manager_decision[i]['alpha'] =ugao(our_team[i]['x'],our_team[i]['y'],1316,460)
                    if (iter== iter1+1) or (iter==0):
                        D=s
                    if (s<D/2):
                        manager_decision[i]['force'] = -30000
                    else:
                        manager_decision[i]['force'] =30000


                else:
                    x1=ball['x']
                    y1=ball['y']
                    t=gol2(x0,y0,x1,y1)

                    if (t<our_team[i]['y']) and (t>353):
                        manager_decision[i]['alpha']=-math.pi/2
                        s=distance(our_team[i]['x'],our_team[i]['y'],50,t)
                        if (t!=tR):
                            d=s
                        if (s < d / 2):
                            manager_decision[i]['force'] = -50000
                        else:
                            manager_decision[i]['force'] = 50000
                    else:
                        if (t>our_team[i]['y']) and (t<568):
                            manager_decision[i]['alpha'] = math.pi / 2
                            s = distance(our_team[i]['x'], our_team[i]['y'], 50, t)
                            if (t != tR):
                                d = s
                            if (s < d / 2):
                                manager_decision[i]['force'] = -50000
                            else:
                                manager_decision[i]['force'] = 50000
                        else:
                            q = True
                            koef = (1 - ball['x'] / 1366)
                            if (ball['y'] <= 460) and (our_team[i]['y'] > 343 + 10 + our_team[i]['radius']) and not (
                            math.isnan(t)):
                                manager_decision[i]['force'] = 40000 * koef
                                manager_decision[i]['alpha'] = -math.pi / 2
                                q = False
                            else:
                                if (our_team[i]['y'] <= 343 + 10 + our_team[i]['radius']) or math.isnan(t):
                                    manager_decision[i]['force'] = 0
                                    manager_decision[i]['alpha'] = ((-1) ** iter) * math.pi / 2
                            if (ball['y'] > 460) and (our_team[i]['y'] < 578 - 10 - our_team[i]['radius']) and not (
                            math.isnan(t)):
                                manager_decision[i]['force'] = 40000 * koef
                                manager_decision[i]['alpha'] = math.pi / 2
                            else:
                                if ((our_team[i]['y'] >= 578 - 10 - our_team[i]['radius']) or math.isnan(t)) and q:
                                    manager_decision[i]['force'] = 0
                                    manager_decision[i]['alpha'] = ((-1) ** iter) * math.pi / 2
                        tR=t
                        x0=x1
                        y0=y1
                manager_decision[i]['shot_request'] = True
                manager_decision[i]['shot_power'] = 100000

                if (int(our_team[i]['x']) in range (1305,1320)) and (int(our_team[i]['y']) in range (450,475)):
                    positionR=True
                if  ((our_team[i]['x'])<1300) or ((our_team[i]['x'])>1340):
                    positionL=False
                    iter1=iter
                if (rezultat!=(their_score+our_score)):
                    positionR=False
                rezultat=their_score+our_score
        else:
            manager_decision[i]['alpha'] = player['alpha']
            manager_decision[i]['force'] = 0
            manager_decision[i]['shot_request'] = True
            manager_decision[i]['shot_power'] = 100000
    #print(our_score, their_score, end=' -- ')
    iter=iter+1
    
    
    
    
    
    
    
    
    for i in range(2):
        player = our_team[i]
        manager_decision[i]['alpha'] = player['alpha']
        manager_decision[i]['force'] = 0
        manager_decision[i]['shot_request'] = True
        manager_decision[i]['shot_power'] = 100000

    #lista=find_closest(our_team, ball)
    #min_player=lista[0]
    #min_dist=lista[1]
    min_player = 1
    min_dist = distance(our_team[1]['x'],our_team[1]['y'],ball['x'],ball['y'])

    if min_dist>(ball['radius']+player['radius']+150):
        manager_decision[min_player]['alpha'] = math.atan2((ball['y']-our_team[min_player]['y']),(ball['x']-our_team[min_player]['x']))
        manager_decision[min_player]['force']=1000000
        
        
    else:
        biza = our_team[0]
        beta=find_shot_path(their_team, biza, ball['x'],ball['y'],your_side)
        if(isinstance(beta, bool)):
            beta = 0 
        manager_decision[min_player]['force']=1000000
        manager_decision[min_player]['alpha']=computeAlpha(our_team[min_player],ball, beta, our_team[min_player]['v_max'], your_side, half,manager_decision[min_player]['force'])

   

    acc=manager_decision[min_player]['force']/our_team[min_player]['mass']
    
    #print(our_score, their_score)
    keeper_ind = find_keeper(their_team,your_side)
    keeper = their_team[keeper_ind]
    izbacivac = our_team[0]
    if(your_side=='left'):
        izbacivac_desired = [keeper['x'],keeper['y']]
        #if(izbacivac['x']<keeper['x']+izbacivac['radius']+keeper['radius']):
        izbacivac['alpha'] = np.arctan2((keeper['y']-izbacivac['y']),(izbacivac_desired[0]-izbacivac['x']))
    else:
        izbacivac_desired = [keeper['x'],keeper['y']]
        #if(izbacivac['x']>keeper['x']-izbacivac['radius']-keeper['radius']):
        izbacivac['alpha'] = np.arctan2((-izbacivac_desired[0]+izbacivac['x']),(keeper['y']-izbacivac['y']))+math.pi/2 
        izbacivac['force'] = 1000000
        #izbacivac['alpha'] = np.arctan2(izbacivac['y']-keeper['y'],izbacivac['x']-keeper['x'])
    manager_decision[0]['alpha']=izbacivac['alpha']
    manager_decision[0]['shot_request']=False
    manager_decision[0]['force'] = 1000000
    print(izbacivac['x'])
    return manager_decision

