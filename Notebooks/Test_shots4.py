#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:17:20 2019

@author: gabin
"""


import numpy as np
import math as m
import os
import json


Calculated_nb_shots={}
Time_shots={}

def distance(a,b):      #a = (x,y) point de départ ; b = (i,j) point d'arrivée ; v = norme pour l'instant
    return np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def where_attack(moments,j):
    ball=moments[j][5][0][2:5]
    x_mid=94/2
    if (ball[0]-x_mid)<0:
        return(1)
    else :
        return(2)

def player_with_ball(moments,i):
    players=moments[i][5][1:]
    ball=moments[i][5][0][2:5]
    if ball[2]>2.5*3.28:
        return(0)
    else :
        dmin=[m.sqrt((players[0][2]-ball[0])**2+(players[0][3]-ball[1])**2),0]
        for k in range(1,len(players)):
            d=m.sqrt((players[k][2]-ball[0])**2+(players[k][3]-ball[1])**2)
            if d<dmin[0]:
                dmin=[d,k]
        return players[dmin[1]][2:4]
    
def behind_three_point_line(p,where):
    coin=False
    if where==1 :
        basket_pos=[5.25,25]
        if p[0]<15:
            coin=True
    else :
        basket_pos=[94-5.25,25]
        if p[0]>(94-15):
            coin=True
    if coin : 
        if 0<p[1]<3 or 50-3<p[1]<50 : 
            return (True,basket_pos)
        else :
            return (False,basket_pos)
    else :
        if distance(p,basket_pos)>23.75 :  #In fact 23.75 but we take a marge to have all shoots
            return (True,basket_pos)
        else:
            return (False,basket_pos)

def track_event_shots(moments,t_end,w_ball,TIME_SHOTS):
    
    time_shots=TIME_SHOTS
    event_shots=np.array([0,0])
    time=t_end
    
    if len(moments)<=1:
        return([event_shots,time,w_ball,time_shots])
    
    ### begin at the end of the previous moment ###
    i=0
    while [5-moments[i][0],m.ceil(moments[i][2])]>=t_end and (i<(len(moments)-2)):    
        i+=1
    
    time=[5-moments[i][0],moments[i][2]]
    
    if i>=(len(moments)-2) : #no moment
        return([event_shots,time,w_ball,time_shots])
    
    
    who_ball=w_ball
    while i<(len(moments)-2):
        ### looking if the ball goes over 2.5m ###
        if moments[i][5][0][0]==-1: #if the ball is in the moment
            ball0=moments[i][5][0][2:5]
            if ball0[2]>2.5*3.28:
                
                ### looking if the player is in three points zone ###
                who_ball2=player_with_ball(moments,i-1)
                if who_ball2!=0:
                    who_ball=who_ball2
                where=where_attack(moments,i)
                btpl=behind_three_point_line(who_ball,where)
                if btpl[0]:
                    basket_pos=btpl[1]
                    
                    ball1=ball0
                    ### looking if the ball is going above basket ###
                    while i<(len(moments)-2) and ball1[2]>ball0[2] and ball1[2]<10:
                        i+=1
                        if moments[i][5][0][0]==-1:
                            ball1=moments[i][5][0][2:5]
                    
                    ### looking if the ball is going just around the basket ###
                    if ball1[2]>=10:
                        ball2=ball1
                        while i<(len(moments)-2) and ball1[2]>=10 and distance(ball1[:2],basket_pos)>5:
                            ball2=ball1
                            i+=1
                            if moments[i][5][0][0]==-1:
                                ball1=moments[i][5][0][2:5]
                        
                        if ball1[2]>=10 and distance(ball1[:2],basket_pos)<=5:
                            #if [5-moments[i][0],moments[i][2]+5]<time_shots[-1]:
                            event_shots[1]+=1
                            time_shots.append([5-moments[i][0],moments[i][2]])
                        
                            ### waiting for the ball descending under basket ###
                            while i<(len(moments)-2) and ball1[2]>=10:
                                i+=1
                                ball2=ball1
                                if moments[i][5][0][0]==-1:
                                    ball1=moments[i][5][0][2:5]

                            ### looking if the ball passed through the basket ###
                            if ball1[2]<10:
                                a=ball1[0]-ball2[0]
                                b=ball1[1]-ball2[1]
                                c=ball1[2]-ball2[2]
                                t=(10-ball2[2])/c
                                x=ball2[0]+t*a
                                y=ball2[1]+t*b
                                if distance(np.array([x,y]),basket_pos)<0.75:
                                    event_shots[0]+=1
                        
#                            else:
#                                while ball1[2]>=2.5*3.28 and i<(len(moments)-2):
#                                    i+=1
#                                    if moments[i][5][0][0]==-1:
#                                        ball1=moments[i][5][0][2:5]

                        
        i+=1
        
    time=[5-moments[i][0],moments[i][2]]        
    return([event_shots,time,who_ball,time_shots])
                                
                            
    
def track_shots(data):
    with open(data) as json_file:  
        data = json.load(json_file)
        events=data['events']
    event=events[2]
    time_end=[np.inf,np.inf]
    TIME_SHOTS=[[10,100]]
    shots=np.array([0,0])
    who_ball=[50,50]

    for q in range(len(events)):
        event=events[q]
        moments=event['moments']
        print(q)
        res=track_event_shots(moments,time_end,who_ball,TIME_SHOTS)
        shots=shots+res[0]
        time_end=res[1]
        who_ball=res[2]
        TIME_SHOTS=res[3]
    
    return(shots,TIME_SHOTS)

for k in range(638):
    os.chdir('/Volumes/My Passport/GABIN/Documents/CENTRALE_LYON_1A/PaR/Basket/')
    if k<10:
        if ('002150000'+str(k)+'.json') in os.listdir():
            result=track_shots('002150000'+str(k)+'.json')
            print(k,result[0])
            Calculated_nb_shots[str(k)]=result[0]
            Time_shots[str(k)]=result[1]
            
    if 9<k<100:
        if ('00215000'+str(k)+'.json') in os.listdir():
            result=track_shots('00215000'+str(k)+'.json')
            print(k,result[0])
            Calculated_nb_shots[str(k)]=result[0]
            Time_shots[str(k)]=result[1]
            
    if 99<k:
        if ('0021500'+str(k)+'.json') in os.listdir():
            result=track_shots('0021500'+str(k)+'.json')
            print(k,result[0])
            Calculated_nb_shots[str(k)]=result[0]
            Time_shots[str(k)]=result[1]