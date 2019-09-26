#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:11:56 2019

@author: gabin
"""

import json
import pandas as pd
import time

def json_extracter(data): #data should be a string like : 'data.json', the function returns data and events
    with open(data) as json_file:  
        data = json.load(json_file)
        events=data['events']
    return(data,events)

#match_data,events=json_extracter('/Volumes/My Passport/GABIN/Documents/CENTRALE_LYON_1A/PaR/Basket/0021500001.json')

event=events[3]

moments=event['moments']
moment_test=event['moments'][2]
moment_test2=event['moments'][3]

team1=event['home']
team2=event['visitor']

#def mom_infos(mom1,mom2,team1,team2):
 #   df1=2
    
    
    
def players_ball_speed_position(moment1,moment2):
    
    dt=moment1[2]-moment2[2]
    
    mom_infos={}
    mom_infos['ball']={}
    mom_infos['team1']={}
    mom_infos['team2']={}
    for i in range(11) :
        if i==0:
            mom_infos['ball']['xy']=np.array(moment1[5][i][2:4])
            mom_infos['ball']['z']=moment1[5][i][4]
            mom_infos['ball']['v']=np.array([(moment2[5][i][2]-moment1[5][i][2])/dt,(moment2[5][i][3]-moment1[5][i][3])/dt])
        if 6<=i<=11:
            mom_infos['team2'][str(moment1[5][i][1])]={'xy':np.array(moment1[5][i][2:4]),'v':np.array([(moment2[5][i][2]-moment1[5][i][2])/dt,(moment2[5][i][3]-moment1[5][i][3])/dt])}
        if 1<=i<=5:
            mom_infos['team1'][str(moment1[5][i][1])]={'xy':np.array(moment1[5][i][2:4]),'v':np.array([(moment2[5][i][2]-moment1[5][i][2])/dt,(moment2[5][i][3]-moment1[5][i][3])/dt])}
    return(mom_infos)

def vx_calc(row):
    x1=row['x_loc']
    x2=row['x_loc_2']
    t1=row['game_clock']
    t2=row['game_clock_2']
    return((x2-x1)/(t1-t2))

def vy_calc(row):
    y1=row['y_loc']
    y2=row['y_loc_2']
    t1=row['game_clock']
    t2=row['game_clock_2']
    return((y2-y1)/(t1-t2))

def vz_calc(row):
    z1=row['radius']
    z2=row['radius_2']
    t1=row['game_clock']
    t2=row['game_clock_2']
    return((z2-z1)/(t1-t2))

def mom_infos(mom1,mom2):
    
    #headers of the dataframe mom_infos
    headers = ["team_id", "player_id", "x_loc", "y_loc", 
               "radius", "moment", "game_clock", "shot_clock"]
    
    #initialize a new list where we append more information than one inside moment[5]
    mom_df= []
    
    # For each player/ball in the list found within each moment
    for player in mom1[5]:
        p=player.copy()
        # Add additional information to each player/ball
        # This info includes the index of each moment, the game clock
        # and shot clock values for each moment
        p.extend((moments.index(mom1), mom1[2], mom1[3]))
        mom_df.append(p)
        
    #convert to dataframe
    mom_df=pd.DataFrame(mom_df, columns=headers)
    
    #taking the position just after to calculate the speed
    mom_df2= []
    
    # For each player/ball in the list found within each moment
    for player in mom2[5]:
        p=player.copy()
        # Add additional information to each player/ball
        # This info includes the index of each moment, the game clock
        # and shot clock values for each moment
        p.extend((moments.index(mom2), mom2[2], mom2[3]))
        mom_df2.append(p)
        
    #convert to dataframe
    mom_df2=pd.DataFrame(mom_df2, columns=headers)
    
    #join both dataframe
    
    mom_df=mom_df.set_index('player_id').join(mom_df2.set_index('player_id'), rsuffix='_2')
    
    print(mom_df)
        
    #add speed of the ball/player
    mom_df['vx']=mom_df.apply(vx_calc, axis=1)
    mom_df['vy']=mom_df.apply(vy_calc, axis=1)
    mom_df['vz']=mom_df.apply(vz_calc, axis=1)
    
    return(mom_df)

deb1=time.time()
mom=players_ball_speed_position(moment_test,moment_test2)
fin1=time.time()

deb2=time.time()
mom_infos(moment_test,moment_test2)
fin2=time.time()

print('time before:',fin1-deb1)
print('time after:',fin2-deb2)