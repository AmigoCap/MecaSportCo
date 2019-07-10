#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:07:38 2019

@author: gabin
"""

import json
import space as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

def json_extracter(data): #data should be a string like : 'data.json', the function returns data and events
    with open(data) as json_file:  
        data = json.load(json_file)
        events=data['events']
    return(data,events)

#match_data,events=json_extracter('/Volumes/My Passport/GABIN/Documents/CENTRALE_LYON_1A/PaR/Basket/0021500001.json')

def intercorrel(DELTA_X,DELTA_T,T,N=round(4/0.04)):
    
    RHO=np.zeros(N)
    
    mean_DELTA_X=[[0]*94 for i in range(50)]
    mean_DELTA_T=[[0]*94 for i in range(50)]

    for n in range(50):
        for p in range(94):
            mean_DELTA_X[n][p]=np.mean(DELTA_X[n][p])
            mean_DELTA_T[n][p]=np.mean(DELTA_T[n][p])
    
    print(mean_DELTA_X[0][0],DELTA_X[0][0])
            
    delta_x_RMS=0
    delta_t_RMS=0
    for n in range(50):
        for p in range(94):
            for i in range(len(DELTA_X[n][p])):
                delta_x_RMS+=(DELTA_X[n][p][i]-mean_DELTA_X[n][p])**2
                delta_t_RMS+=(DELTA_T[n][p][i]-mean_DELTA_T[n][p])**2
    delta_x_RMS=np.sqrt(delta_x_RMS/(50*94*T))
    delta_t_RMS=np.sqrt(delta_t_RMS/(50*94*T))
    
    for k in range(N):
        for n in range(50):
            for p in range(94):
                rho=0
                for i in range(len(DELTA_X[n][p])-k):
                    deltax=DELTA_X[n][p][i+k]
                    mean_deltax=mean_DELTA_X[n][p]
                    deltat=DELTA_T[n][p][i]
                    mean_deltat=mean_DELTA_T[n][p]
                    rho+=(deltat-mean_deltat)*(deltax-mean_deltax)
                    
                rho=rho/(T-0.04*k)
                RHO[k]+=rho
        RHO[k]=RHO[k]/(delta_x_RMS*delta_t_RMS)
    
    return(RHO/(94*50))            
    

def event_correlation(event):

    DELTA_X=[[[]]*94 for i in range(50)]
    DELTA_T=[[[]]*94 for i in range(50)]
    moments=event['moments']
    T=moments[0][2]-moments[-1][2]
    print(T)
    
    for k in range(len(moments)-1):
        #if k%10==0:
        deb=time.time()
            #print(k)
        moment1=moments[k]
        moment2=moments[k+1]
        mom_infos=sp.players_ball_speed_position(moment1,moment2)
        for i in range(50):
            for j in range(94):
                
                b=np.array([j,i])
                
                deltax=sp.distance_difference(mom_infos,b)
                deltat=sp.time_difference(mom_infos,b)
    
                DELTA_X[i][j]=DELTA_X[i][j]+[deltax]
                DELTA_T[i][j]=DELTA_T[i][j]+[deltat]
        fin=time.time()
        print(fin-deb)
    
    R=intercorrel(DELTA_X,DELTA_T,T)
    
    plt.plot(R)
    plt.show()
    
    maxi=0
    t=0
    for k in range(len(R)):
        if R[k]>maxi:
            maxi=R[k]
            t=k
    return(maxi,t)

def court_distance_map_player(x,y):
    
    X,Y=np.meshgrid(np.arange(94),np.arange(50))
    court=np.sqrt((X-x)**2+(Y-y)**2)
    return(court)

def court_distance_map_team(team, mom_infos):
    
    distance_map_team=[]
    
    for player in mom_infos[team].keys():
        x=mom_infos[team][player]['xy'][0]
        y=mom_infos[team][player]['xy'][1]
        distance_map_team.append(court_distance_map_player(x,y))
        
    return(np.array(distance_map_team)).min(axis=0)

def court_time_map_player(a,v):
    
    court=np.zeros((50,94))
    
    for i in range(50):
        for j in range(94):
            
            b=np.array([j,i])
            court[i][j]=sp.time_to_point(a,b,v)

    return(court)

def court_time_map_team(team, mom_infos):
    
    time_map_team=[]
    
    for player in mom_infos[team].keys():
        a=mom_infos[team][player]['xy']
        v=mom_infos[team][player]['v']
        time_map_team.append(court_time_map_player(a,v))
        
    return(np.array(time_map_team)).min(axis=0)
    
    
def event_correlation_bis(event):
    
    Maps_distance=[]
    Maps_time=[]
    
    moments=event['moments']
    T=moments[0][2]-moments[-1][2]
    
    for k in range(len(moments)-1):
        #if k%10==0:
        deb=time.time()
            #print(k)
            
        # recuperying moment information we need
        moment1=moments[k]
        moment2=moments[k+1]
        mom_infos=sp.players_ball_speed_position(moment1,moment2)
        
        #calculation of court distance map for both TEAM 
        TEAM1_map_distance=court_distance_map_team('team1', mom_infos)
        TEAM2_map_distance=court_distance_map_team('team2', mom_infos)
        
        Maps_distance.append(TEAM1_map_distance-TEAM2_map_distance)
        
        #calculation of time distance map for both TEAM 
        
        TEAM1_map_time=court_time_map_team('team1', mom_infos)
        TEAM2_map_time=court_time_map_team('team2', mom_infos)
        
        Maps_time.append(TEAM1_map_time-TEAM2_map_time)
        
        fin=time.time()
        print(fin-deb)
        
    R=intercorrel(Maps_distance,Maps_time,T)
    
    plt.plot(R)
    plt.show()
    
    maxi=0
    t=0
    for k in range(len(R)):
        if R[k]>maxi:
            maxi=R[k]
            t=k
    return(maxi,t)
        
        

def match_dataframe(events):
    for event in events:
        print(event)
        
        
def dt_event(i):
    event=events[i]
    moments=event['moments'] 
    T=[] 
    for i in range(len(moments)-1) :
        T.append(moments[i][2]-moments[i+1][2])
    
    T=pd.DataFrame({'time':T})
    print(T['time'].value_counts())


#sp.print_court_teams_occupation_inertia(events,1,300)
#sp.print_court_teams_occupation(events,1,300+18,value=True)