#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 11:31:40 2019

@author: gabin
"""

#The shots are memorized in python dictionnary called Shots (too big to be on the repository). It is composed of nine keys :
#* D_CLOSEST_DEF : a list of list. Each list corresponds to a shot and has two elements. The first one is 0 or 1 : if it is 1 it means that the shot was a success and if it is 0 the shot was missed. The second element is the evolution of the shooter's *free space* ($\delta_{space}^*$ distance to the closest defender) 3 seconds before the shot. 
#* T_CLOSEST_DEF : It the same but *free space* is calculated as the time (in second) needed by the closest defender to join the position of the shooter ($\delta_{time}^*$). 
#* TIME_TO_SHOOT : a list of list. Each list has two elements : the first one for the result of the shot and the second one corresponds to the time between the reception of the ball and the shot. It is negative : -2 means that the shooter kept the ball 2 seconds before shooting.
#* TIME_ABSCISSE : a list of list. Each list corresponds to a shot and has two elements. The first one is 0 or 1 : if it is 1 it means that the shot was a success and if it is 0 the shot was missed. The second element corresponds to time values linked to pressure evolution.
#* WHO_SHOT : a list which contains shooters' ID.
#* POSITION_SHOT : a list which contains position of the player at the release.
#* BALL_TRAJECTORIES : a list of list which contains for each shots ball's trajectory.
#* TIME_SHOTS : a list of list which contains the release time in the following format : 5-quarter,time in seconds
#* MATCH_ID : a list containing matches ID

import pickle
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json

## load dictionnary ##

dico=pickle.load(open('../data/Shots_663','rb'))

## load players description ##

def players_description(data): #data should be a string like : 'data.json', the function returns data and events
    with open(data) as json_file:  
        data = json.load(json_file)
    firstName=[]
    lastName=[]
    player_id=[]
    team_id=[]
    for d in data:
        if 'firstName' in d.keys():
            firstName.append(d['firstName'])
        else :
            firstName.append(' ')
        lastName.append(d['lastName'])
        player_id.append(d['playerId'])
        team_id.append(d['teamId'])
    
    df=pd.DataFrame({'firstName':firstName,'lastName':lastName,'player_id':player_id,'team_id':team_id},index=player_id)
    return(df)
    
#players=players_description('../data/players.json')


## Structure data to make mean ##

def restructure_data(data):
    
    "This function return a dataframe. Each raw is associated with a shot via shot_id and to a time between -3.2 and 0.8 seconds before and after the release if the ball."
    
    ### getting the data ###
    D_CLOSEST_PLAYER=data['D_CLOSEST_DEF']
    T_CLOSEST_PLAYER=data['T_CLOSEST_DEF']
    TIME=data['TIME_ABSCISSE']
    TIME_TO_SHOOT=data['TIME_TO_SHOOT']
    WHO_SHOT=data['WHO_SHOT']
    POSITION_SHOT=data['POSTION_SHOT']
    BALL_TRAJECTORIES=data['BALL_TRAJECTORIES']
    TIME_SHOTS=data['TIME_SHOTS']
    MATCH_ID=data['MATCH_ID']
    
    ### only the second column because the first one contains if it is a succes or a miss ###
    D_CLOSEST_PLAYER_bis=[]
    T_CLOSEST_PLAYER_bis=[]
    TIME_bis=[]
    TIME_TO_SHOOT_bis=[]
    WHO_SHOT_bis=[]
    X_SHOT=[]
    Y_SHOT=[]
    X_BALL=[]
    Y_BALL=[]
    Z_BALL=[]
    QUARTER=[]
    CLOCK=[]
    MATCH_ID_bis=[]
    SUCCESS=[]
    SHOT_ID=[]
    SHOT_TYPE=[]
    
    nb_catch_and_shoot=0
    nb_pull_up=0
    nb_success=0
    nb_missed=0
    nb_cns_success=0
    nb_cns_missed=0
    nb_pull_up_success=0
    nb_pull_up_missed=0
    for k in range(len(D_CLOSEST_PLAYER)):
        unique,count=np.unique(np.array(TIME[k][1]).round(2), return_counts=True)
        if list(count)==[1]*len(count): # we don't take shots where values of time are repeated, because in the data, sometimes the values of time doesn't change so stay on the same second but we count the evolution on this second
            if D_CLOSEST_PLAYER[k][0]==0:
                nb_missed+=1
                if TIME_TO_SHOOT[k][1]>-2:
                    nb_catch_and_shoot+=1
                    nb_cns_missed+=1
                else :
                    nb_pull_up+=1
                    nb_pull_up_missed+=1
            else :
                nb_success+=1
                if TIME_TO_SHOOT[k][1]>-2:
                    nb_catch_and_shoot+=1
                    nb_cns_success+=1
                else :
                    nb_pull_up+=1
                    nb_pull_up_success+=1
            D_CLOSEST_PLAYER_bis.append(D_CLOSEST_PLAYER[k][1])
            T_CLOSEST_PLAYER_bis.append(T_CLOSEST_PLAYER[k][1])
            TIME_bis.append(np.array(TIME[k][1]).round(2)) # round to 0.01 second
            TIME_TO_SHOOT_bis.append([TIME_TO_SHOOT[k][1]]*len(TIME[k][1]))
            SUCCESS.append([TIME_TO_SHOOT[k][0]]*len(TIME[k][1]))
            WHO_SHOT_bis.append([WHO_SHOT[k]]*len(TIME[k][1]))
            X_SHOT.append([POSITION_SHOT[k][0]]*len(TIME[k][1]))
            Y_SHOT.append([POSITION_SHOT[k][1]]*len(TIME[k][1]))
            X_BALL.append(np.array(BALL_TRAJECTORIES[k][0]))
            Y_BALL.append(np.array(BALL_TRAJECTORIES[k][1]))
            Z_BALL.append(np.array(BALL_TRAJECTORIES[k][2]))
            QUARTER.append([5-TIME_SHOTS[k][0]]*len(TIME[k][1]))
            CLOCK.append([TIME_SHOTS[k][1]]*len(TIME[k][1]))
            MATCH_ID_bis.append([MATCH_ID[k]]*len(TIME[k][1]))
            SHOT_ID.append([k]*len(TIME[k][1]))
            if TIME_TO_SHOOT[k][1]<-2:
                SHOT_TYPE.append(['pull-up 3P']*len(TIME[k][1]))
            else :
                SHOT_TYPE.append(['catch-and-shoot 3P']*len(TIME[k][1]))
    
    print('number of valid shot:',len(D_CLOSEST_PLAYER_bis))
    print('number of success :',nb_success)
    print('number of miss :',nb_missed)
    print('percentage of success:',nb_success/(nb_success+nb_missed)*100)
    print('percentage of catch-and-shoot shots :',nb_catch_and_shoot/(nb_pull_up+nb_catch_and_shoot)*100)
    print('percentage of catch-and-shoot success:',nb_cns_success/(nb_cns_missed+nb_cns_success)*100)
    print('percentage of pull-up success:',nb_pull_up_success/(nb_pull_up_missed+nb_pull_up_success)*100)
    
    ### we concatenate all the data
    TIME_bis=np.concatenate(np.array(TIME_bis)) 
    D_CLOSEST_PLAYER_bis=np.concatenate(np.array(D_CLOSEST_PLAYER_bis))
    T_CLOSEST_PLAYER_bis=np.concatenate(np.array(T_CLOSEST_PLAYER_bis))
    TIME_TO_SHOOT_bis=np.concatenate(np.array(TIME_TO_SHOOT_bis))
    SUCCESS=np.concatenate(np.array(SUCCESS))
    WHO_SHOT_bis=np.concatenate(np.array(WHO_SHOT_bis))
    X_SHOT=np.concatenate(np.array(X_SHOT))
    Y_SHOT=np.concatenate(np.array(Y_SHOT))
    X_BALL=np.concatenate(np.array(X_BALL))
    Y_BALL=np.concatenate(np.array(Y_BALL))
    Z_BALL=np.concatenate(np.array(Z_BALL))
    QUARTER=np.concatenate(np.array(QUARTER))
    CLOCK=np.concatenate(np.array(CLOCK))
    MATCH_ID_bis=np.concatenate(np.array(MATCH_ID_bis))
    SHOT_ID=np.concatenate(np.array(SHOT_ID))
    SHOT_TYPE=np.concatenate(np.array(SHOT_TYPE))
    
    ### put the data into a dataframe ###
    df=pd.DataFrame({'D':D_CLOSEST_PLAYER_bis,'T':T_CLOSEST_PLAYER_bis,'Time':TIME_bis,'Time_to_shoot':TIME_TO_SHOOT_bis,'Shot result':SUCCESS,'player_id':WHO_SHOT_bis,'x_ball':X_BALL,'y_ball':Y_BALL,'z_ball':Z_BALL,'x_shooter':X_SHOT,'y_shooter':Y_SHOT,'quarter':QUARTER,'clock':CLOCK,'Match_id':MATCH_ID_bis,'shot_id':SHOT_ID,'Shot_type':SHOT_TYPE})
    
    ## only evolution between 3.2 seconds before shot and 0.8 second after. (It is because there are some errors in the data) ##
    df=df.query('Time>-3.2 and Time<0.8').copy()
    
    return(df)


## Structure data by shots ##
    
def structure_data_by_shot(data):
    
    "This function return a dataframe.Each raw represents a shot."
    
    ### getting the data ###
    D_CLOSEST_PLAYER=data['D_CLOSEST_DEF']
    T_CLOSEST_PLAYER=data['T_CLOSEST_DEF']
    TIME=data['TIME_ABSCISSE']
    TIME_TO_SHOOT=data['TIME_TO_SHOOT']
    WHO_SHOT=data['WHO_SHOT']
    POSITION_SHOT=data['POSTION_SHOT']
    BALL_TRAJECTORIES=data['BALL_TRAJECTORIES']
    TIME_SHOTS=data['TIME_SHOTS']
    MATCH_ID=data['MATCH_ID']
    
    ### only the second column because the first one contains if it is a succes or a miss ###
    D_CLOSEST_PLAYER_bis=[]
    T_CLOSEST_PLAYER_bis=[]
    TIME_bis=[]
    TIME_TO_SHOOT_bis=[]
    WHO_SHOT_bis=[]
    X_SHOT=[]
    Y_SHOT=[]
    X_BALL=[]
    Y_BALL=[]
    Z_BALL=[]
    QUARTER=[]
    CLOCK=[]
    MATCH_ID_bis=[]
    SUCCESS=[]
    SHOT_ID=[]
    SHOT_TYPE=[]
    
    nb_catch_and_shoot=0
    nb_pull_up=0
    nb_success=0
    nb_missed=0
    nb_cns_success=0
    nb_cns_missed=0
    nb_pull_up_success=0
    nb_pull_up_missed=0
    for k in range(len(D_CLOSEST_PLAYER)):
        unique,count=np.unique(np.array(TIME[k][1]).round(2), return_counts=True)
        if list(count)==[1]*len(count): # we don't take shots where values of time are repeated, because in the data, sometimes the values of time doesn't change so stay on the same second but we count the evolution on this second
            if D_CLOSEST_PLAYER[k][0]==0:
                nb_missed+=1
                if TIME_TO_SHOOT[k][1]>-2:
                    nb_catch_and_shoot+=1
                    nb_cns_missed+=1
                else :
                    nb_pull_up+=1
                    nb_pull_up_missed+=1
            else :
                nb_success+=1
                if TIME_TO_SHOOT[k][1]>-2:
                    nb_catch_and_shoot+=1
                    nb_cns_success+=1
                else :
                    nb_pull_up+=1
                    nb_pull_up_success+=1
            D_CLOSEST_PLAYER_bis.append(D_CLOSEST_PLAYER[k][1])
            T_CLOSEST_PLAYER_bis.append(T_CLOSEST_PLAYER[k][1])
            TIME_bis.append(list(np.array(TIME[k][1]).round(2))) # round to 0.01 second
            TIME_TO_SHOOT_bis.append(TIME_TO_SHOOT[k][1])
            SUCCESS.append(TIME_TO_SHOOT[k][0])
            WHO_SHOT_bis.append(WHO_SHOT[k])
            X_SHOT.append(POSITION_SHOT[k][0])
            Y_SHOT.append(POSITION_SHOT[k][1])
            X_BALL.append(BALL_TRAJECTORIES[k][0])
            Y_BALL.append(BALL_TRAJECTORIES[k][1])
            Z_BALL.append(BALL_TRAJECTORIES[k][2])
            QUARTER.append(5-TIME_SHOTS[k][0])
            CLOCK.append(TIME_SHOTS[k][1])
            MATCH_ID_bis.append(MATCH_ID[k])
            SHOT_ID.append(k)
            if TIME_TO_SHOOT[k][1]<-2:
                SHOT_TYPE.append('pull-up 3P')
            else :
                SHOT_TYPE.append('catch-and-shoot 3P')

    
    print('number of valid shot:',len(D_CLOSEST_PLAYER_bis))
    print('number of success :',nb_success)
    print('number of miss :',nb_missed)
    print('percentage of success:',nb_success/(nb_success+nb_missed)*100)
    print('percentage of catch-and-shoot shots :',nb_catch_and_shoot/(nb_pull_up+nb_catch_and_shoot)*100)
    print('percentage of catch-and-shoot success:',nb_cns_success/(nb_cns_missed+nb_cns_success)*100)
    print('percentage of pull-up success:',nb_pull_up_success/(nb_pull_up_missed+nb_pull_up_success)*100)
    
    ### put the data into a dataframe ###
    df=pd.DataFrame({'D':D_CLOSEST_PLAYER_bis,'T':T_CLOSEST_PLAYER_bis,'Time':TIME_bis,'Time_to_shoot':TIME_TO_SHOOT_bis,'Shot result':SUCCESS,'player_id':WHO_SHOT_bis,'x_ball':X_BALL,'y_ball':Y_BALL,'z_ball':Z_BALL,'x_shooter':X_SHOT,'y_shooter':Y_SHOT,'quarter':QUARTER,'clock':CLOCK,'Match_id':MATCH_ID_bis,'shot_id':SHOT_ID,'Shot_type':SHOT_TYPE})
    
    return(df)
    
## Calculate players stats ##
    
def players_stats(df_shots):
    
    "This function return a dataframe of players statistics."
    
    df1=df_shots[['player_id','Shot result','D','Match_id','Shot_type']].groupby(['player_id','Match_id']).count()
    df2=df_shots[['player_id','Shot result','D','Match_id','Shot_type']].groupby(['player_id','Shot result']).count()
    df3=df_shots[['player_id','Shot result','D','Match_id','Shot_type']].groupby(['player_id','Shot_type','Shot result']).count()
    players_id=df_shots['player_id'].unique()
    
    total=[]
    success=[]
    miss=[]
    percentage=[]
    match_played=[]
    total_cas=[]
    success_cas=[]
    miss_cas=[]
    percentage_cas=[]
    
    for player in players_id:
        match_played.append(len(df1.loc[player]))
        if 1 in df2.loc[player,'D'].index:
            s=df2.loc[(player,1),'D']
        else :
            s=0

        if 0 in df2.loc[player,'D'].index:
            m=df2.loc[(player,0),'D']
        else :
            m=0
                
        
        total.append(m+s)
        success.append(s)
        miss.append(m)
        percentage.append(round(s/(m+s)*100,1))
        
        if "catch-and-shoot 3P" in df3.loc[player,'D'].index[0]:
            if 1 in df3.loc[(player,"catch-and-shoot 3P"),'D'].index: 
                s_cas=df3.loc[(player,"catch-and-shoot 3P",1),'D']
            else :
                m_cas=0
                
            if 0 in df3.loc[(player,"catch-and-shoot 3P"),'D'].index:  
                m_cas=df3.loc[(player,"catch-and-shoot 3P",0),'D']
            else:
                m_cas=0
        else :
            s_cas=0
            m_cas=0
                

        total_cas.append(m_cas+s_cas)
        success_cas.append(s_cas)
        miss_cas.append(m_cas)
        
        if s_cas+m_cas==0:
            percentage_cas.append(0)
        else:
            percentage_cas.append(round(s_cas/(m_cas+s_cas)*100,1))
    
    df_stats=pd.DataFrame({'total':total,'success':success,'miss':miss,'percentage':percentage,'match_played':match_played,'total_cas':total_cas,'success_cas':success_cas,'miss_cas':miss_cas,'percentage_cas':percentage_cas},index=players_id)
    return df_stats

#df_plot_mean=restructure_data(dico)
df_shots=structure_data_by_shot(dico)
#df_stats=players_stats(df_shots)

#df_plot_mean.to_csv('../data/df_plot_mean.csv', sep=',', encoding='utf-8')
#df_shots.to_csv('../data/df_shots.csv', sep=',', encoding='utf-8')
#df_stats.to_csv('../data/df_stats.csv', sep=',', encoding='utf-8')
#players.to_csv('../data/players.csv', sep=',', encoding='utf-8')


def plot_shot(df_shots,i,players):
    fig, (ax1, ax2) = plt.subplots(2, 1,figsize=(5,10))
    Time=df_shots.iloc[i]['Time']
    D=df_shots.iloc[i]['D']
    T=df_shots.iloc[i]['T']
    tts=df_shots.iloc[i]['Time_to_shoot']
    player_id=df_shots.iloc[i]['player_id']
    c=df_shots.iloc[i]['clock']
    print(i,df_shots.iloc[i]['Match_id'],df_shots.iloc[i]['quarter'],str(c//60)+'m '+str(c%60),player_id,players.loc[player_id,'lastName'],df_shots.iloc[i]['Shot_type'],tts,df_shots.iloc[i]['Shot result'])
    ax1.axvline(tts, color='black',linestyle="dashed",lw=1)
    ax2.axvline(tts, color='black',linestyle="dashed",lw=1)
    ax1.plot(Time,D,'r-',alpha=0.8)
    ax2.plot(Time,T,'r-',alpha=0.8)
    
    ax1.set_xlim((-3.2,0.8))
    ax1.set_ylim((0,30))
    ax2.set_xlim((-3.2,0.8))
    ax2.set_ylim((0,2))
    plt.show()