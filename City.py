import numpy as np
import math
import pygame

class Counter:
    x=0
class Counterlast:
    x=0
    
class Counter2:
    x=0

class Counter3:
    x=0  

class Tactic:
    t=0
class Counter4:
    x=0  

class Counter5:
    x=0
    
class Counter2_2:
    x=0

class Counter3_2:
    x=0  

class F:
    flag=False

class F4:
    flag=False
  
class F5:
    flag=False

class F6:
    flag=False
        
class F2:
    flag=False
    
class F3:
    flag=False

class F2_2:
    flag=False

class F3_2:
    flag=False
    
class Goals:
    x=0
def goforballalpha(player,ball,your_side):
    if(your_side=="left"):
        return math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
    return math.pi+math.atan((ball['y']-player['y'])/(ball['x']-player['x']))

def vo_pole_defense_0_left(ball):
    return True if (ball['x']<=450 and ball['y']<=578) else False

def vo_pole_defense_0_right(ball):
    return True if ball['x']>=900 and ball['y']<=578 else False

def vo_pole_defense_2_left(ball):
    return True if ball['x']<=250 and ball['y']>=466 else False
def vo_pole_defense_2_right(ball):
    return True if ball['x']>=1100 and ball['y']>=466 else False

def closer_to_ball(player1,player2,ball):
    """Returns true if player1 is closer to the ball than player2"""
    distance_1=math.sqrt((player1['x']-ball['x'])**2+(player1['y']-ball['y'])**2)
    distance_2=math.sqrt((player2['x']-ball['x'])**2+(player2['y']-ball['y'])**2)
    return True if distance_1<distance_2 else False

class Defense_0_angle:
    flag=True
class Defense_2_angle:
    flag=True
    
def defense_0(player,player2,ball,your_side):
    """Ako sakash da ja smenish pozicijata- ne zaboravaj na vo_pole funkciite"""
    manager_decision_defense=dict()
    if(your_side=='left'):
        if(vo_pole_defense_0_left(ball)):
            if(ball['x']>=player['x']):
                manager_decision_defense['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
            elif(closer_to_ball(player,player2,ball)):
                manager_decision_defense['alpha'] = math.pi+math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = False
                manager_decision_defense['shot_power'] =player['shot_power_max']
            else:
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                else:
                    manager_decision_defense['alpha']=-3*math.pi/2
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
                
        else:
            if(player['x']<=350):
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                if(ball['y']>=player['y'] and ball['y']<=578):
                    manager_decision_defense['alpha']=-3*math.pi/2
                elif(ball['y']>player['y'] and Defense_0_angle.flag):
                    manager_decision_defense['alpha']=-3*math.pi/2
                    Defense_0_angle.flag=False
                else:
                    manager_decision_defense['alpha']=-math.pi/2
                    Defense_0_angle.flag=True
            else:
                manager_decision_defense['alpha']=math.pi
            
                
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']

            
    if(your_side=='right'):
        if(vo_pole_defense_0_right(ball)):
            if(ball['x']<=player['x']):
                manager_decision_defense['alpha'] =math.pi+ math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
            elif(closer_to_ball(player,player2,ball)):
                manager_decision_defense['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = False
                manager_decision_defense['shot_power'] =player['shot_power_max']
            else:
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                else:
                    manager_decision_defense['alpha']=-3*math.pi/2
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
        else:
            if(player['x']>=1000):
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                if(ball['y']>=player['y'] and ball['y']<=578):
                    manager_decision_defense['alpha']=-3*math.pi/2
                elif(ball['y']>player['y'] and Defense_0_angle.flag):
                    manager_decision_defense['alpha']=-3*math.pi/2
                    Defense_0_angle.flag=False
                else:
                    manager_decision_defense['alpha']=-math.pi/2
                    Defense_0_angle.flag=True
            else:
                manager_decision_defense['alpha']=0
                
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
            
        
            

            
            
            
            
    
    return manager_decision_defense
def defense_2(player,player0,ball,your_side):
    """Ako sakash da ja smenish pozicijata- ne zaboravaj na vo_pole funkciite"""
    manager_decision_defense=dict()
    if(your_side=='left'):
        if(vo_pole_defense_2_left(ball)):
            if(ball['x']>=player['x']):
                manager_decision_defense['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
            elif(closer_to_ball(player,player0,ball)):
                manager_decision_defense['alpha'] = math.pi+math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = False
                manager_decision_defense['shot_power'] =player['shot_power_max']
            else:
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                else:
                    manager_decision_defense['alpha']=-3*math.pi/2
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
                
        else:
            if(player['x']<=150):
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                if(ball['y']>=player['y'] and ball['y']>=466):
                    manager_decision_defense['alpha']=-3*math.pi/2
                elif(ball['y']>player['y'] and Defense_2_angle.flag):
                    manager_decision_defense['alpha']=-3*math.pi/2
                    Defense_2_angle.flag=False
                else:
                    manager_decision_defense['alpha']=-math.pi/2
                    Defense_2_angle.flag=True
            else:
                manager_decision_defense['alpha']=math.pi
                
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']

            
    if(your_side=='right'):
        if(vo_pole_defense_2_right(ball)):
            if(ball['x']<=player['x']):
                manager_decision_defense['alpha'] =math.pi+ math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
            elif(closer_to_ball(player,player0,ball)):
                manager_decision_defense['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = False
                manager_decision_defense['shot_power'] =player['shot_power_max']
            else:
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                else:
                    manager_decision_defense['alpha']=-3*math.pi/2
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
        else:
            if(player['x']>=1150):
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                if(ball['y']>=player['y'] and ball['y']>=466):
                    manager_decision_defense['alpha']=-3*math.pi/2
                elif(ball['y']>player['y'] and Defense_2_angle.flag):
                    manager_decision_defense['alpha']=-3*math.pi/2
                    Defense_2_angle.flag=False
                else:
                    manager_decision_defense['alpha']=-math.pi/2
                    Defense_2_angle.flag=True
            else:
                manager_decision_defense['alpha']=0
                
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
            
    return manager_decision_defense
    

def defender(player,ball,your_side):
    manager_decision_defense=dict()
    if(your_side=='left'):
        if(ball['x']<=400 and ball['x']>=player['x']):
            manager_decision_defense['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
        elif(ball['x']<player['x'] and ball['x']>=100 ):
            manager_decision_defense['alpha'] =math.pi+math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = False
            manager_decision_defense['shot_power'] =player['shot_power_max']  
        else:
            if(player['x']<=300):
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                else:
                    manager_decision_defense['alpha']=-3*math.pi/2
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
            else:
                manager_decision_defense['alpha']=math.pi+math.atan((ball['y']-player['y'])/(300-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
    else:
        if(ball['x']>=966 and ball['x']<=player['x']):
            manager_decision_defense['alpha'] =math.pi+math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
        elif(ball['x']>player['x'] and ball['x']>1060):
            manager_decision_defense['alpha'] =math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = False
            manager_decision_defense['shot_power'] =player['shot_power_max']  
        else:
            if(player['x']>=1066):
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                else:
                    manager_decision_defense['alpha']=-3*math.pi/2
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
            else:
                manager_decision_defense['alpha']=math.atan((ball['y']-player['y'])/(1166-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
        

        
    return manager_decision_defense


def readytoshoot1(player,ball,your_side):

    if(your_side=="left"):
        goalx=1316
        goaly=460 
        res=dict()
        angle=math.atan((goaly-ball['y'])/(goalx-ball['x']))
        angle2=math.atan((goaly-player['y'])/(goalx-player['x']))
        #newx=ball['x']-math.cos(angle)*(ball['radius']+player['radius']+30)
        newy=ball['y']-math.sin(angle)*(ball['radius']+player['radius'])
        if(ball['y']<460):
            if (player['y']<=newy-5):
                if(angle-angle2<0):
                    F2.flag=True
                    Counter2.x=0
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F2.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi
                    res['force'] = player['a_max']*player['mass']
                else:
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter2.x+=1
                if(Counter2.x==2):
                    F2.flag=False
            
            else:
                if(angle-angle2<0):
                    F3.flag=True
                    Counter3.x=0
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F3.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = -math.pi/2
                    res['force'] = player['a_max']*player['mass']
                else:
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter3.x+=1
                if(Counter3.x==2):
                    F3.flag=False   
        else:
            if (player['y']<=newy+5):
                if(angle2-angle<0):
                    F2.flag=True
                    Counter2.x=0
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi+math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F2.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi/2
                    res['force'] = player['a_max']*player['mass']
                else:
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter2.x+=1
                if(Counter2.x==2):
                    F2.flag=False
            
            else:
                if(angle-angle2<0):
                    F3.flag=True
                    Counter3.x=0
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F3.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = 0
                    res['force'] = player['a_max']*player['mass']
                else:
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter3.x+=1
                if(Counter3.x==2):
                    F3.flag=False   
    else:
        goalx=50
        goaly=460 
        res=dict()
        angle=math.pi+math.atan((goaly-ball['y'])/(goalx-ball['x']))
        angle2=math.pi + math.atan((goaly-player['y'])/(goalx-player['x']))
        #newx=ball['x']-math.cos(angle)*(ball['radius']+player['radius']+30)
        newy=ball['y']-math.sin(angle)*(ball['radius']+player['radius'])
        if(ball['y']<460):
            if (player['y']<=newy-5):
                if(angle2-angle<0):
                    F2.flag=True
                    Counter2.x=0
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F2.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = 0
                    res['force'] = player['a_max']*player['mass']
                else:
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter2.x+=1
                if(Counter2.x==2):
                    F2.flag=False
            
            else:
                if(angle2-angle<0):
                    F3.flag=True
                    Counter3.x=0
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F3.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = -math.pi/2
                    res['force'] = player['a_max']*player['mass']
                else:
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter3.x+=1
                if(Counter3.x==2):
                    F3.flag=False   
        else:
            if (player['y']<=newy+5):
                if(angle-angle2<0):
                    F2.flag=True
                    Counter2.x=0
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F2.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi/2
                    res['force'] = player['a_max']*player['mass']
                else:
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi +  math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter2.x+=1
                if(Counter2.x==2):
                    F2.flag=False
            
            else:
                if(angle2-angle<0):
                    F3.flag=True
                    Counter3.x=0
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F3.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = 0
                    res['force'] = player['a_max']*player['mass']
                else:
                    res['shot_request']=True
                    F5.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter3.x+=1
                if(Counter3.x==2):
                    F3.flag=False            
    return res    

def followball(player,ball,your_side):
    if(your_side=="left"):
        if(player['x']<ball['x']-60):
            return 0
        else:
            return math.pi
    else:
        if(player['x']>ball['x']+60):
            return math.pi
        else:
            return 0

def walknext(player1,player2,your_side):
    if(your_side=="left"):
        if(player1['x']<player2['x']-60):
            return 0
        else:
            return math.pi
    else:
        if(player1['x']>player2['x']+60):
            return math.pi
        else:
            return 0

def readytoshoot2(player,ball,your_side):

    
    if(your_side=="left"):
        goalx=1316
        goaly=460 
        res=dict()
        angle=math.atan((goaly-ball['y'])/(goalx-ball['x']))
        angle2=math.atan((goaly-player['y'])/(goalx-player['x']))
        #newx=ball['x']-math.cos(angle)*(ball['radius']+player['radius']+30)
        newy=ball['y']-math.sin(angle)*(ball['radius']+player['radius'])
        if(ball['y']<460):
            if (player['y']<=newy-5):
                if(angle-angle2<0):
                    F2_2.flag=True
                    Counter2_2.x=0
                    res['shot_request']=True
                    F6.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F2_2.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi
                    res['force'] = player['a_max']*player['mass']
                else:
                    res['shot_request']=True
                    F6.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter2_2.x+=1
                if(Counter2_2.x==2):
                    F2_2.flag=False
            
            else:
                if(angle-angle2<0):
                    F3_2.flag=True
                    Counter3_2.x=0
                    res['shot_request']=True
                    F6.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F3_2.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = -math.pi/2
                    res['force'] = player['a_max']*player['mass']
                else:
                    res['shot_request']=True
                    F6.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter3_2.x+=1
                if(Counter3_2.x==2):
                    F3_2.flag=False   
        else:
            if (player['y']<=newy+5):
                if(angle2-angle<0):
                    F2_2.flag=True
                    Counter2_2.x=0
                    res['shot_request']=True
                    F6.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi+math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F2_2.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi/2
                    res['force'] = player['a_max']*player['mass']
                else:
                    res['shot_request']=True
                    F6.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter2_2.x+=1
                if(Counter2_2.x==2):
                    F2_2.flag=False
            
            else:
                if(angle-angle2<0):
                    F3_2.flag=True
                    Counter3_2.x=0
                    F6.flag=False
                    Counter5.x=0
                    res['shot_request']=True
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F3_2.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = 0
                    res['force'] = player['a_max']*player['mass']
                else:
                    res['shot_request']=True
                    F6.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter3_2.x+=1
                if(Counter3_2.x==2):
                    F3_2.flag=False   
    else:
        goalx=50
        goaly=460 
        res=dict()
        angle=math.pi+math.atan((goaly-ball['y'])/(goalx-ball['x']))
        angle2=math.pi + math.atan((goaly-player['y'])/(goalx-player['x']))
        #newx=ball['x']-math.cos(angle)*(ball['radius']+player['radius']+30)
        newy=ball['y']-math.sin(angle)*(ball['radius']+player['radius'])
        if(ball['y']<460):
            if (player['y']<=newy-5):
                if(angle2-angle<0):
                    F2_2.flag=True
                    Counter2_2.x=0
                    res['shot_request']=True
                    F6.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F2_2.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = 0
                    res['force'] = player['a_max']*player['mass']
                else:
                    res['shot_request']=True
                    F6.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter2_2.x+=1
                if(Counter2_2.x==2):
                    F2_2.flag=False
            
            else:
                if(angle2-angle<0):
                    F3_2.flag=True
                    Counter3_2.x=0
                    F6.flag=False
                    Counter5.x=0
                    res['shot_request']=True
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F3_2.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = -math.pi/2
                    res['force'] = player['a_max']*player['mass']
                else:
                    res['shot_request']=True
                    F6.flag=False       
                    Counter5.x=0             
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter3_2.x+=1
                if(Counter3_2.x==2):
                    F3_2.flag=False   
        else:
            if (player['y']<=newy+5):
                if(angle-angle2<0):
                    F2_2.flag=True
                    Counter2_2.x=0
                    F6.flag=False
                    Counter5.x=0
                    res['shot_request']=True
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F2_2.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi/2
                    res['force'] = player['a_max']*player['mass']
                else:
                    F6.flag=False
                    Counter5.x=0
                    res['shot_request']=True
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi +  math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter2_2.x+=1
                if(Counter2_2.x==2):
                    F2_2.flag=False
            
            else:
                if(angle2-angle<0):
                    F3_2.flag=True
                    Counter3_2.x=0
                    F6.flag=False
                    Counter5.x=0
                    res['shot_request']=True
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                    
                elif (F3_2.flag==False):
                    res['shot_request']=False
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = 0
                    res['force'] = player['a_max']*player['mass']
                else:
                    res['shot_request']=True
                    F6.flag=False
                    Counter5.x=0
                    res['shot_power'] = player['shot_power_max']
                    res['alpha'] = math.pi + math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                    res['force'] = player['a_max']*player['mass']
                Counter3_2.x+=1
                if(Counter3_2.x==2):
                    F3_2.flag=False            
    return res    
   
            
def defencealpha(player,ball,your_side):
    if(your_side=="left"):
        return math.pi    
    return 0
         
def forward1(player,ball,your_side):
        res=dict()
        if(your_side=="left"):
            if(F.flag==False):
                    distance=math.sqrt(math.pow((ball['x']-player['x']), 2)+math.pow((ball['y']-player['y']), 2))
                    goalx=1316
                    goaly=460 
                    if(distance-(player['radius']+ball['radius'])<3):
                        res=shoot1(player,ball,your_side)
                    else:
                        res['alpha'] = goforballalpha(player,ball,your_side) #math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                        res['force'] = player['a_max']*player['mass']
                        res['shot_request'] = False
                        res['shot_power'] = player['shot_power_max']
            else:
                 res['alpha'] = defencealpha(player,ball,your_side)
                 res['force'] = player['a_max']*player['mass']
                 res['shot_request'] = False
                 res['shot_power'] = player['shot_power_max']
                 Counter.x=Counter.x+1      
                 if(Counter.x==5):
                     Counter.x=0
                     F.flag=False  
        else:
            if(F.flag==False):
                    distance=math.sqrt(math.pow((ball['x']-player['x']), 2)+math.pow((ball['y']-player['y']), 2))
                    goalx=50
                    goaly=460 
                    if(distance-(player['radius']+ball['radius'])<3):
                        res=shoot1(player,ball,your_side)
                    else:
                        res['alpha'] = goforballalpha(player,ball,your_side) #math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                        res['force'] = player['a_max']*player['mass']
                        res['shot_request'] = False
                        res['shot_power'] = player['shot_power_max']
            else:
                 res['alpha'] = defencealpha(player,ball,your_side)
                 res['force'] = player['a_max']*player['mass']
                 res['shot_request'] = False
                 res['shot_power'] = player['shot_power_max']
                 Counter.x=Counter.x+1      
                 if(Counter.x==5):
                     Counter.x=0
                     F.flag=False  
        return res    
                   
def shoot1(player,ball,your_side):   
    
    res=dict()
    if(your_side=="left"):
        if(ball['x']>950):
            res=readytoshoot1(player,ball,your_side)
        else:
            res['alpha'] = goforballalpha(player,ball,your_side) #math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
            res['force'] = player['a_max']*player['mass']
            res['shot_request'] = False
            res['shot_power'] = player['shot_power_max']
    else:
        if(ball['x']<416):
            res=readytoshoot1(player,ball,your_side)
        else:
            res['alpha'] = goforballalpha(player,ball,your_side) #math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
            res['force'] = player['a_max']*player['mass']
            res['shot_request'] = False
            res['shot_power'] = player['shot_power_max']        
    return res

def forward2(player,ball,your_side):
        res=dict()
        if(your_side=="left"):
            if(F.flag==False):
                    distance=math.sqrt(math.pow((ball['x']-player['x']), 2)+math.pow((ball['y']-player['y']), 2))
                    if(distance-(player['radius']+ball['radius'])<3):
                        res=shoot2(player,ball,your_side)
                    else:
                        res['alpha'] = goforballalpha(player,ball,your_side) #math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                        res['force'] = player['a_max']*player['mass']
                        res['shot_request'] = False
                        res['shot_power'] = player['shot_power_max']
            else:
                 res['alpha'] = defencealpha(player,ball,your_side)
                 res['force'] = player['a_max']*player['mass']
                 res['shot_request'] = False
                 res['shot_power'] = player['shot_power_max']
                 Counter4.x=Counter4.x+1      
                 if(Counter4.x==5):
                     Counter4.x=0
                     F.flag=False  
        else:
            if(F.flag==False):
                    distance=math.sqrt(math.pow((ball['x']-player['x']), 2)+math.pow((ball['y']-player['y']), 2))
                    if(distance-(player['radius']+ball['radius'])<3):
                        res=shoot2(player,ball,your_side)
                    else:
                        res['alpha'] = goforballalpha(player,ball,your_side) #math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                        res['force'] = player['a_max']*player['mass']
                        res['shot_request'] = False
                        res['shot_power'] = player['shot_power_max']
            else:
                 res['alpha'] = defencealpha(player,ball,your_side)
                 res['force'] = player['a_max']*player['mass']
                 res['shot_request'] = False
                 res['shot_power'] = player['shot_power_max']
                 Counter4.x=Counter4.x+1      
                 if(Counter4.x==5):
                     Counter4.x=0
                     F.flag=False  
        return res    
                   
def closer(player1,player2,ball):
    distance1=math.sqrt(math.pow((ball['x']-player1['x']), 2)+math.pow((ball['y']-player1['y']), 2))
    distance2=math.sqrt(math.pow((ball['x']-player2['x']), 2)+math.pow((ball['y']-player2['y']), 2))
    if(distance1<distance2):
        return True
    return False

def vo_pole_defense_0_left(ball):
    return True if (ball['x']<=450 and ball['y']<=578) else False

def vo_pole_defense_0_right(ball):
    return True if ball['x']>=900 and ball['y']<=578 else False

def vo_pole_defense_2_left(ball):
    return True if ball['x']<=250 and ball['y']>=466 else False
def vo_pole_defense_2_right(ball):
    return True if ball['x']>=1100 and ball['y']>=466 else False

def closer_to_ball(player1,player2,ball):
    """Returns true if player1 is closer to the ball than player2"""
    distance_1=math.sqrt((player1['x']-ball['x'])**2+(player1['y']-ball['y'])**2)
    distance_2=math.sqrt((player2['x']-ball['x'])**2+(player2['y']-ball['y'])**2)
    return True if distance_1<distance_2 else False

class Defense_0_angle:
    flag=True
class Defense_2_angle:
    flag=True
    
def defense_0(player,player2,ball,your_side):
    """Ako sakash da ja smenish pozicijata- ne zaboravaj na vo_pole funkciite"""
    manager_decision_defense=dict()
    if(your_side=='left'):
        if(vo_pole_defense_0_left(ball)):
            if(ball['x']>=player['x']):
                manager_decision_defense['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
            elif(closer_to_ball(player,player2,ball)):
                manager_decision_defense['alpha'] = math.pi+math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = False
                manager_decision_defense['shot_power'] =player['shot_power_max']
            else:
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                else:
                    manager_decision_defense['alpha']=-3*math.pi/2
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
                
        else:
            if(player['x']<=350):
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                if(ball['y']>=player['y'] and ball['y']<=578):
                    manager_decision_defense['alpha']=-3*math.pi/2
                elif(ball['y']>player['y'] and Defense_0_angle.flag):
                    manager_decision_defense['alpha']=-3*math.pi/2
                    Defense_0_angle.flag=False
                else:
                    manager_decision_defense['alpha']=-math.pi/2
                    Defense_0_angle.flag=True
            else:
                manager_decision_defense['alpha']=math.pi
            
                
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']

            
    if(your_side=='right'):
        if(vo_pole_defense_0_right(ball)):
            if(ball['x']<=player['x']):
                manager_decision_defense['alpha'] =math.pi+ math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
            elif(closer_to_ball(player,player2,ball)):
                manager_decision_defense['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = False
                manager_decision_defense['shot_power'] =player['shot_power_max']
            else:
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                else:
                    manager_decision_defense['alpha']=-3*math.pi/2
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
        else:
            if(player['x']>=1000):
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                if(ball['y']>=player['y'] and ball['y']<=578):
                    manager_decision_defense['alpha']=-3*math.pi/2
                elif(ball['y']>player['y'] and Defense_0_angle.flag):
                    manager_decision_defense['alpha']=-3*math.pi/2
                    Defense_0_angle.flag=False
                else:
                    manager_decision_defense['alpha']=-math.pi/2
                    Defense_0_angle.flag=True
            else:
                manager_decision_defense['alpha']=0
                
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
            
        
            

            
            
            
            
    
    return manager_decision_defense
def defense_2(player,player0,ball,your_side):
    """Ako sakash da ja smenish pozicijata- ne zaboravaj na vo_pole funkciite"""
    manager_decision_defense=dict()
    if(your_side=='left'):
        if(vo_pole_defense_2_left(ball)):
            if(ball['x']>=player['x']):
                manager_decision_defense['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
            elif(closer_to_ball(player,player0,ball)):
                manager_decision_defense['alpha'] = math.pi+math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = False
                manager_decision_defense['shot_power'] =player['shot_power_max']
            else:
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                else:
                    manager_decision_defense['alpha']=-3*math.pi/2
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
                
        else:
            if(player['x']<=150):
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                if(ball['y']>=player['y'] and ball['y']>=466):
                    manager_decision_defense['alpha']=-3*math.pi/2
                elif(ball['y']>player['y'] and Defense_2_angle.flag):
                    manager_decision_defense['alpha']=-3*math.pi/2
                    Defense_2_angle.flag=False
                else:
                    manager_decision_defense['alpha']=-math.pi/2
                    Defense_2_angle.flag=True
            else:
                manager_decision_defense['alpha']=math.pi
                
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']

            
    if(your_side=='right'):
        if(vo_pole_defense_2_right(ball)):
            if(ball['x']<=player['x']):
                manager_decision_defense['alpha'] =math.pi+ math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
            elif(closer_to_ball(player,player0,ball)):
                manager_decision_defense['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = False
                manager_decision_defense['shot_power'] =player['shot_power_max']
            else:
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                else:
                    manager_decision_defense['alpha']=-3*math.pi/2
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
        else:
            if(player['x']>=1150):
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                if(ball['y']>=player['y'] and ball['y']>=466):
                    manager_decision_defense['alpha']=-3*math.pi/2
                elif(ball['y']>player['y'] and Defense_2_angle.flag):
                    manager_decision_defense['alpha']=-3*math.pi/2
                    Defense_2_angle.flag=False
                else:
                    manager_decision_defense['alpha']=-math.pi/2
                    Defense_2_angle.flag=True
            else:
                manager_decision_defense['alpha']=0
                
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
            
    return manager_decision_defense
    

def defender(player,ball,your_side):
    manager_decision_defense=dict()
    if(your_side=='left'):
        if(ball['x']<=400 and ball['x']>=player['x']):
            manager_decision_defense['alpha'] = math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
        elif(ball['x']<player['x'] and ball['x']>=100 ):
            manager_decision_defense['alpha'] =math.pi+math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = False
            manager_decision_defense['shot_power'] =player['shot_power_max']  
        else:
            if(player['x']<=300):
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                else:
                    manager_decision_defense['alpha']=-3*math.pi/2
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
            else:
                manager_decision_defense['alpha']=math.pi+math.atan((ball['y']-player['y'])/(300-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
    else:
        if(ball['x']>=966 and ball['x']<=player['x']):
            manager_decision_defense['alpha'] =math.pi+math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
        elif(ball['x']>player['x'] and ball['x']>1060):
            manager_decision_defense['alpha'] =math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = False
            manager_decision_defense['shot_power'] =player['shot_power_max']  
        else:
            if(player['x']>=1066):
                if(ball['y']<=player['y']):
                    manager_decision_defense['alpha']=-math.pi/2
                else:
                    manager_decision_defense['alpha']=-3*math.pi/2
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
            else:
                manager_decision_defense['alpha']=math.atan((ball['y']-player['y'])/(1166-player['x']))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
        

        
    return manager_decision_defense



def goal_keeper1(player,ball,your_side):
    """Returns the strategy for the defence player - our_team[1]"""
    """Neshto menuvav no ne e gotovo"""
    manager_decision_defense=dict()
    bx=ball['x']
    by=ball['y']
    px=player['x']
    py=player['y']
    if(your_side=='left'):
        if(bx<200 and bx>px and by>=(343-30) and by<=(578+30)):
            manager_decision_defense['alpha'] = math.atan((by-py)/(bx-px))
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
        elif(bx<px and by>=(343-30) and by<=(578+30)):
            manager_decision_defense['alpha'] =math.pi+math.atan((by-py)/(bx-px))
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = False
            manager_decision_defense['shot_power'] =player['shot_power_max']              
        else:
            if(px<=95):
                if(by<=py and by>=(343-20)):
                    manager_decision_defense['alpha']=-math.pi/2
                elif(by>py and by<=(578+20)):
                    manager_decision_defense['alpha']=-3*math.pi/2
                elif(by<=player['y'] and py<=(343-20)):
                    manager_decision_defense['alpha']=-3*math.pi/2
                elif(by<py):
                    manager_decision_defense['alpha']=-math.pi/2
                elif(by>py and py>=(578+20)):
                    manager_decision_defense['alpha']=-math.pi/2
                else:
                    manager_decision_defense['alpha']=-3*math.pi/2
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
            else:
                manager_decision_defense['alpha']=math.pi+math.atan((460-by)/(50-bx))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
        return manager_decision_defense
                    
                
        
                
    if(your_side=='right'):
        if(bx>1166 and bx<px and by>=(343-30) and by<=(578+30)):
            manager_decision_defense['alpha'] = math.pi+math.atan((by-py)/(bx-px))
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = True
            manager_decision_defense['shot_power'] =player['shot_power_max']
        elif(bx>px and by>=(343-30) and by<=(578+30)):
            manager_decision_defense['alpha'] = math.atan((by-py)/(bx-px))
            manager_decision_defense['force']=player['a_max']*player['mass']
            manager_decision_defense['shot_request'] = False
            manager_decision_defense['shot_power'] =player['shot_power_max']              
        else:
            if(px>=1273):
                if(by<=py and by>=(343-20)):
                    manager_decision_defense['alpha']=-math.pi/2
                elif(by>py and by<=(578+20)):
                    manager_decision_defense['alpha']=-3*math.pi/2
                elif(by<=player['y'] and py<=(343-20)):
                    manager_decision_defense['alpha']=-3*math.pi/2
                elif(by<py):
                    manager_decision_defense['alpha']=-math.pi/2
                elif(by>py and py>=(578+20)):
                    manager_decision_defense['alpha']=-math.pi/2
                else:
                    manager_decision_defense['alpha']=-3*math.pi/2
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
            else:
                manager_decision_defense['alpha']=math.atan((460-by)/(50-bx))
                manager_decision_defense['force']=player['a_max']*player['mass']
                manager_decision_defense['shot_request'] = True
                manager_decision_defense['shot_power'] =player['shot_power_max']
        
    return manager_decision_defense      

def shoot2(player,ball,your_side):   
    
    res=dict()
    if(your_side=="left"):
        if(ball['x']>950):
            res=readytoshoot2(player,ball,your_side)
        else:
            res['alpha'] = goforballalpha(player,ball,your_side) #math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
            res['force'] = player['a_max']*player['mass']
            res['shot_request'] = False
            res['shot_power'] = player['shot_power_max']
    else:
        if(ball['x']<416):
            res=readytoshoot2(player,ball,your_side)
        else:
            res['alpha'] = goforballalpha(player,ball,your_side) #math.atan((ball['y']-player['y'])/(ball['x']-player['x']))
            res['force'] = player['a_max']*player['mass']
            res['shot_request'] = False
            res['shot_power'] = player['shot_power_max']               
    return res

def player2field(ball):
        if(ball['y']>0):
            return True
        else:
            return False

def player3field(ball):
        if(ball['y']>0):
            return True
        else:
            return False
                
def decision(our_team, their_team, ball, your_side, half, time_left,our_score,their_score):
    if(our_score-their_score!=Goals.x or half==2):
        Counter.x=0
        F.flag=False
        F4.flag=False
        Counter2.x=0
        Counter2_2.x=0
        Counter3.x=0
        Counter3_2.x=0
        F2.flag=False
        F3.flag=False
        F2_2.flag=False
        F3_2.flag=False
        Counter5.x=0
        F5.flag=False
        F6.flag=False
        if(our_score-their_score<Goals.x):
            Tactic.t+=1
            Tactic.t=Tactic.t%3
        Counterlast.x=0
        Goals.x=our_score-their_score

    if(Tactic.t==0):    
        manager_decision = [dict(), dict(), dict()]
        if(Counterlast.x>=9):
            Counterlast.x=0
            F5.flag=False
            F6.flag=False
        if(your_side=='left'):
#             Player1=our_team[0]
#             manager_decision[0]['alpha'] = Player1['alpha']
#             manager_decision[0]['force'] = 0
#             manager_decision[0]['shot_request'] = True
#             manager_decision[0]['shot_power'] = 500
            manager_decision[0]=goal_keeper1(our_team[0], ball, your_side) 
            Player2=our_team[1]
            Player3=our_team[2]
            if(player2field(ball)):
                if(ball['x']>Player2['x']):
                    if(closer(Player2, Player3, ball)):
                        if(F6.flag==False):
                            F5.flag=True
                            Counter5.x+=1
                            Counterlast.x=0
                            if(Counter5.x==2):
                                Counter5.x=0
                                F5.flag=False
                            manager_decision[1]=forward1(Player2,ball,your_side)
                        else:
                            manager_decision[1]['alpha'] = walknext(Player2, Player3, your_side)
                            manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                            manager_decision[1]['shot_request'] = False
                            manager_decision[1]['shot_power'] = 100
                    else:
                        manager_decision[1]['alpha'] = walknext(Player2, Player3, your_side)
                        manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                        manager_decision[1]['shot_request'] = False
                        manager_decision[1]['shot_power'] = 100
                        Counterlast.x=9
                else:
                    if(Counter.x<5):
                        F.flag=True
                        Counter.x+=1
                        if(Counter.x==5):
                            Counter.x=0
                            F.flag=False
                        manager_decision[1]['alpha'] = defencealpha(Player2,ball,your_side)
                        manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                        manager_decision[1]['shot_request'] = False
                        manager_decision[1]['shot_power'] = 100
                    else:
                        manager_decision[1]['alpha'] = defencealpha(Player2,ball,your_side)
                        manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                        manager_decision[1]['shot_request'] = False
                        manager_decision[1]['shot_power'] = 100
                        Counter.x=0
                        F.flag=False      
            else:
                manager_decision[1]['alpha'] = followball(Player2, ball, your_side)
                manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                manager_decision[1]['shot_request'] = False
                manager_decision[1]['shot_power'] = 100
      
    
    #         if(player3field(ball)):
            if(ball['x']>Player3['x']):
                    if(closer(Player3, Player2, ball)):
                        if(F5.flag==False):
                            F6.flag=True
                            Counter5.x+=1
                            Counterlast.x=0
                            if(Counter5.x==2):
                                Counter5.x=0
                                F6.flag=False
                            manager_decision[2]=forward1(Player3,ball,your_side)
                        else:
                            manager_decision[2]['alpha'] = walknext(Player3, Player2, your_side)
                            manager_decision[2]['force'] = Player3['a_max']*Player3['mass']
                            manager_decision[2]['shot_request'] = False
                            manager_decision[2]['shot_power'] = 100
                    else:
                        manager_decision[2]['alpha'] = walknext(Player3, Player2, your_side)
                        manager_decision[2]['force'] = Player3['a_max']*Player3['mass']
                        manager_decision[2]['shot_request'] = False
                        manager_decision[2]['shot_power'] = 100
                        Counterlast.x=9

            else:
                    if(Counter4.x<5):
                        F4.flag=True
                        Counter4.x+=1
                        if(Counter4.x==5):
                            Counter4.x=0
                            F4.flag=False
                        manager_decision[2]['alpha'] = defencealpha(Player3,ball,your_side)
                        manager_decision[2]['force'] = Player3['a_max']*Player3['mass']
                        manager_decision[2]['shot_request'] = False
                        manager_decision[2]['shot_power'] = Player3['shot_power_max']
                    else:
                        manager_decision[2]['alpha'] = defencealpha(Player3,ball,your_side)
                        manager_decision[2]['force'] = Player3['a_max']*Player3['mass']
                        manager_decision[2]['shot_request'] = False
                        manager_decision[2]['shot_power'] =Player3['shot_power_max']
                        Counter4.x=0
                        F4.flag=False      
    
     ###############################
        else:  
    #         Player1=our_team[0]
    #         manager_decision[0]['alpha'] = Player1['alpha']
    #         manager_decision[0]['force'] = 0
    #         manager_decision[0]['shot_request'] = True
    #         manager_decision[0]['shot_power'] = 500
            manager_decision[0]=goal_keeper1(our_team[0], ball, your_side)
    #         Player2=our_team[1]
    #         manager_decision[1]['alpha'] = Player2['alpha']
    #         manager_decision[1]['force'] = 0
    #         manager_decision[1]['shot_request'] = True
    #         manager_decision[1]['shot_power'] = 500   
            Player2=our_team[1]
            Player3=our_team[2]
            if(player2field(ball)):
                if(ball['x']<Player2['x']):
                    if(closer(Player2, Player3, ball)):
                        if(F6.flag==False):
                            F5.flag=True
                            Counter5.x+=1
                            Counterlast.x=0
                            if(Counter5.x==2):
                                Counter5.x=0
                                F5.flag=False
                            manager_decision[1]=forward1(Player2,ball,your_side)
                        else:
                            manager_decision[1]['alpha'] = walknext(Player2, Player3, your_side)
                            manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                            manager_decision[1]['shot_request'] = False
                            manager_decision[1]['shot_power'] = 100
                    else:
                        manager_decision[1]['alpha'] = walknext(Player2, Player3, your_side)
                        manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                        manager_decision[1]['shot_request'] = False
                        manager_decision[1]['shot_power'] = 100
                        Counterlast.x=9

                else:
                    if(Counter.x<5):
                        F.flag=True
                        Counter.x+=1
                        if(Counter.x==5):
                            Counter.x=0
                            F.flag=False
                        manager_decision[1]['alpha'] = defencealpha(Player2,ball,your_side)
                        manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                        manager_decision[1]['shot_request'] = False
                        manager_decision[1]['shot_power'] = 100
                    else:
                        manager_decision[1]['alpha'] = defencealpha(Player2,ball,your_side)
                        manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                        manager_decision[1]['shot_request'] = False
                        manager_decision[1]['shot_power'] = 100
                        Counter.x=0
                        F.flag=False      
            else:
                manager_decision[1]['alpha'] = followball(Player2, ball, your_side)
                manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                manager_decision[1]['shot_request'] = False
                manager_decision[1]['shot_power'] = 100
      
    
    #         if(player3field(ball)):
            if(ball['x']<Player3['x']):
                    if(closer(Player3, Player2, ball)):
                        if(F5.flag==False):
                            F6.flag=True
                            Counter5.x+=1
                            Counterlast.x=0
                            if(Counter5.x==2):
                                Counter5.x=0
                                F6.flag=False
                            manager_decision[2]=forward1(Player3,ball,your_side)
                        else:
                            manager_decision[2]['alpha'] = walknext(Player3, Player2, your_side)
                            manager_decision[2]['force'] = Player3['a_max']*Player3['mass']
                            manager_decision[2]['shot_request'] = False
                            manager_decision[2]['shot_power'] = 100
                    else:
                        manager_decision[2]['alpha'] = walknext(Player3, Player2, your_side)
                        manager_decision[2]['force'] = Player3['a_max']*Player3['mass']
                        manager_decision[2]['shot_request'] = False
                        manager_decision[2]['shot_power'] = 100
                        Counterlast.x=9

            else:
                    if(Counter4.x<5):
                        F4.flag=True
                        Counter4.x+=1
                        if(Counter4.x==5):
                            Counter4.x=0
                            F4.flag=False
                        manager_decision[2]['alpha'] = defencealpha(Player3,ball,your_side)
                        manager_decision[2]['force'] = Player3['a_max']*Player3['mass']
                        manager_decision[2]['shot_request'] = False
                        manager_decision[2]['shot_power'] = Player3['shot_power_max']
                    else:
                        manager_decision[2]['alpha'] = defencealpha(Player3,ball,your_side)
                        manager_decision[2]['force'] = Player3['a_max']*Player3['mass']
                        manager_decision[2]['shot_request'] = False
                        manager_decision[2]['shot_power'] =Player3['shot_power_max']
                        Counter4.x=0
                        F4.flag=False      
  
        return manager_decision
    #########################################################11111111    
    elif(Tactic.t==2):    
        manager_decision = [dict(), dict(), dict()]
        if(Counterlast.x>=9):
            Counterlast.x=0
            F5.flag=False
            F6.flag=False
        if(your_side=='left'):
            manager_decision[0]=defense_0(our_team[0], our_team[2], ball, your_side)
            Player2=our_team[1]
            manager_decision[2]=defense_2(our_team[2], our_team[0], ball, your_side)
            if(player2field(ball)):
                if(ball['x']>Player2['x']):
                    manager_decision[1]=forward1(Player2,ball,your_side)
                else:
                    if(Counter.x<5):
                        F.flag=True
                        Counter.x+=1
                        if(Counter.x==5):
                            Counter.x=0
                            F.flag=False
                        manager_decision[1]['alpha'] = defencealpha(Player2,ball,your_side)
                        manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                        manager_decision[1]['shot_request'] = False
                        manager_decision[1]['shot_power'] = 100
                    else:
                        manager_decision[1]['alpha'] = defencealpha(Player2,ball,your_side)
                        manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                        manager_decision[1]['shot_request'] = False
                        manager_decision[1]['shot_power'] = 100
                        Counter.x=0
                        F.flag=False      
            else:
                manager_decision[1]['alpha'] = followball(Player2, ball, your_side)
                manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                manager_decision[1]['shot_request'] = False
                manager_decision[1]['shot_power'] = 100
      
    
    #      
     ###############################
        else:  
            manager_decision[0]=defense_0(our_team[0], our_team[2], ball, your_side)
            manager_decision[2]=defense_2(our_team[2], our_team[0], ball, your_side)
            Player2=our_team[1]
            if(player2field(ball)):
                if(ball['x']<Player2['x']):
                    manager_decision[1]=forward1(Player2,ball,your_side)
                else:
                    if(Counter.x<5):
                        F.flag=True
                        Counter.x+=1
                        if(Counter.x==5):
                            Counter.x=0
                            F.flag=False
                        manager_decision[1]['alpha'] = defencealpha(Player2,ball,your_side)
                        manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                        manager_decision[1]['shot_request'] = False
                        manager_decision[1]['shot_power'] = 100
                    else:
                        manager_decision[1]['alpha'] = defencealpha(Player2,ball,your_side)
                        manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                        manager_decision[1]['shot_request'] = False
                        manager_decision[1]['shot_power'] = 100
                        Counter.x=0
                        F.flag=False      
            else:
                manager_decision[1]['alpha'] = followball(Player2, ball, your_side)
                manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                manager_decision[1]['shot_request'] = False
                manager_decision[1]['shot_power'] = 100
        return manager_decision
  
    else:    
        manager_decision = [dict(), dict(), dict()]
        if(Counterlast.x>=9):
            Counterlast.x=0
            F5.flag=False
            F6.flag=False
        if(your_side=='left'):
            manager_decision[0]=goal_keeper1(our_team[0], ball, your_side)
            Player2=our_team[1]
            manager_decision[2]=defender(our_team[2], ball, your_side)
            if(player2field(ball)):
                if(ball['x']>Player2['x']):
                    manager_decision[1]=forward1(Player2,ball,your_side)
                else:
                    if(Counter.x<5):
                        F.flag=True
                        Counter.x+=1
                        if(Counter.x==5):
                            Counter.x=0
                            F.flag=False
                        manager_decision[1]['alpha'] = defencealpha(Player2,ball,your_side)
                        manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                        manager_decision[1]['shot_request'] = False
                        manager_decision[1]['shot_power'] = 100
                    else:
                        manager_decision[1]['alpha'] = defencealpha(Player2,ball,your_side)
                        manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                        manager_decision[1]['shot_request'] = False
                        manager_decision[1]['shot_power'] = 100
                        Counter.x=0
                        F.flag=False      
            else:
                manager_decision[1]['alpha'] = followball(Player2, ball, your_side)
                manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                manager_decision[1]['shot_request'] = False
                manager_decision[1]['shot_power'] = 100
      
    
    #      
     ###############################
        else:  
            manager_decision[0]=goal_keeper1(our_team[0], ball, your_side)
            manager_decision[2]=defender(our_team[2], ball, your_side)
            Player2=our_team[1]
            if(player2field(ball)):
                if(ball['x']<Player2['x']):
                    manager_decision[1]=forward1(Player2,ball,your_side)
                else:
                    if(Counter.x<5):
                        F.flag=True
                        Counter.x+=1
                        if(Counter.x==5):
                            Counter.x=0
                            F.flag=False
                        manager_decision[1]['alpha'] = defencealpha(Player2,ball,your_side)
                        manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                        manager_decision[1]['shot_request'] = False
                        manager_decision[1]['shot_power'] = 100
                    else:
                        manager_decision[1]['alpha'] = defencealpha(Player2,ball,your_side)
                        manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                        manager_decision[1]['shot_request'] = False
                        manager_decision[1]['shot_power'] = 100
                        Counter.x=0
                        F.flag=False      
            else:
                manager_decision[1]['alpha'] = followball(Player2, ball, your_side)
                manager_decision[1]['force'] = Player2['a_max']*Player2['mass']
                manager_decision[1]['shot_request'] = False
                manager_decision[1]['shot_power'] = 100  

  
        return manager_decision