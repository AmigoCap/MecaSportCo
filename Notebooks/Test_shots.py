#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:34:48 2019

@author: gabin
"""

import numpy as np
import math as m
import os
import json

True_nb_shots={'001':np.array([20,56]),
               '002':np.array([16,48]),
               '003':np.array([15,48]),
               '004':np.array([12,54]),
               '005':np.array([15,46]),
               '007':np.array([9,31]),
               '009':np.array([15,41]),
               '010':np.array([21,62]),
               '011':np.array([15,45]),
               '012':np.array([18,41]),
               '013':np.array([12,34]),
               '015':np.array([23,65]),
               '016':np.array([17,43]),
               '017':np.array([14,54]),
               '018':np.array([19,46]),
               '019':np.array([16,53]),
               '020':np.array([14,61])
               }
               
Calculated_nb_shots={}
Time_shots={}

def distance(a,b):      #a = (x,y) point de départ ; b = (i,j) point d'arrivée ; v = norme pour l'instant
    return np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def test_moment(moment):
    if len(moment[5])!=11:
        return(False)
    for i in range(len(moment[5])):
        if len(moment[5][i])!=5:
            return (False)
    return(True)

def where_attack(moments,j):
    ball=players_ball(moments,j)[0]
    x_mid=94/2
    if (ball[0][0]-x_mid)<0:
        return(1)
    else :
        return(2)

def players_ball(moments,j):
    dt=0.04
    moment1 = moments[j][5]
    moment2 = moments[j+1][5]
    m=min(len(moment1),len(moment2))
    players_ball=[]
    for i in range(m):
        if i==0:
            players_ball.append([np.array(moment1[i][2:4]),np.array([(moment2[i][2]-moment1[i][2])/dt,(moment2[i][3]-moment1[i][3])/dt]),moment1[i][4]])
        else :
            players_ball.append([np.array(moment1[i][2:4]),np.array([(moment2[i][2]-moment1[i][2])/dt,(moment2[i][3]-moment1[i][3])/dt])])
    return players_ball

def player_with_ball(moments,i):
    players=players_ball(moments,i)
    ball=players[0]
    if ball[2]>2.50*3.28:
        return(0)
    else :
        dmin=[m.sqrt((players[1][0][0]-ball[0][0])**2+(players[1][0][1]-ball[0][1])**2),0]
        for k in range(2,11):
            d=m.sqrt((players[k][0][0]-ball[0][0])**2+(players[k][0][1]-ball[0][1])**2)
            if d<dmin[0]:
                dmin=[d,k]
        if dmin[0]<1*3.28:
            return dmin[1]
        else : 
            return(0)

def detect_shoot(moments,i,players):
    ball=players[0]
    if ball[2]<4*3.28:
        return(False)
    
    where=where_attack(moments,i)
    basket_pos=[]
    if where==1 :
        basket_pos=[5.25,25]
    else :
        basket_pos=[94-5.25,25]
    
    players2=players
        
    j=i
    while j<(len(moments)-2) and ball[2]>3.05*3.28 and not ball_in_tube2(ball,basket_pos):
        j+=1
        while (not test_moment(moments[j]) or not test_moment(moments[j+1])) and (j<(len(moments)-2)):
            j+=1
        players2=players_ball(moments,j)
        ball=players2[0]
        
    return(ball_in_tube2(ball,basket_pos))


def three_points(moments,i,who_ball,players): #to improve
    if not detect_shoot(moments,i,players):
        return False
    where=where_attack(moments,i)
    basket_pos=[]
    player=moments[i][5][who_ball][2:4]
    coin=False
    if where==1 :
        basket_pos=[5.25,25]
        if player[0]<15:
            coin=True
    else :
        basket_pos=[94-5.25,25]
        if player[0]>(94-15):
            coin=True
    if coin : 
        if 0<player[1]<3.5 or 50-3.5<player[1]<50 : 
            return True
    else :
        if distance(player,basket_pos)>23.5 :  #In fact 23.75 but we take a marge to have all shoots
            return True
    return False

def succesfull_three_points(moments,i):
    where=where_attack(moments,i)
    basket_pos=[]
    players=players_ball(moments,i)
    ball=players[0]
    if where==1 :
        basket_pos=[5.25,25]
    else :
        basket_pos=[94-5.25,25]
    j=i
    result=False
    p=[ball[0]]
    while j<(len(moments)-2) and ball[2]>3.05*3.28 and not ball_in_tube3(ball,basket_pos):
        j+=1
        while (not test_moment(moments[j]) or not test_moment(moments[j+1])) and (j<(len(moments)-2)):
            j+=1
        players=players_ball(moments,j)
        ball=players[0]
    
    if not ball_in_tube3(ball,basket_pos):
        return(False)
    
    while j<(len(moments)-2) and ball[2]>2*3.28 and not ball_in_tube(ball,basket_pos):
        j+=1
        while (not test_moment(moments[j]) or not test_moment(moments[j+1])) and (j<(len(moments)-2)):
            j+=1
        players=players_ball(moments,j)
        ball=players[0]
    return(ball_in_tube(ball,basket_pos))

def ball_in_tube(ball,basket_pos):
    if distance(ball[0],basket_pos)<1:  #In fact 0.75 but take a marge
        if 2*3.281<ball[2]<3.00*3.281:
            return True
    return False

def ball_in_tube2(ball,basket_pos):
    if distance(ball[0],basket_pos)<5:  
        if 3.05*3.281<ball[2]:
            return True
    return False

def ball_in_tube3(ball,basket_pos):
    if distance(ball[0],basket_pos)<1.35:  
        if 3.05*3.281<ball[2]:
            return True
    return False

def track_event_shots(moments):
    event_shots=[np.array([0,0]),[]]
    
    if len(moments)<=1:
        return(event_shots)

    i=0
    while (not test_moment(moments[i]) or not test_moment(moments[i+1])) and (i<(len(moments)-2)):
        i+=1
        
    if i>=(len(moments)-2) : #no moment
        return event_shots
    
    players=players_ball(moments,i)
    who_ball=player_with_ball(moments,i)
    when0=i
    when_reception=i
    who_ball2=None

    while (not three_points(moments,i,who_ball,players)) and i<(len(moments)-2):
        if test_moment(moments[i+1]) and test_moment(moments[i+2]):
            who_ball3=who_ball2
            i+=1
            players=players_ball(moments,i)
            who_ball2=player_with_ball(moments,i)
            if who_ball2==0 and who_ball3!=0:
                when0=i
            if who_ball2!=0 and who_ball2!=who_ball3:
                when_reception=i
            if who_ball2!=0 and who_ball2!=who_ball:
                who_ball=who_ball2

        else :
            i+=1
            while (not test_moment(moments[i])) and i<(len(moments)-2):
                i+=1
                
    if i>=(len(moments)-2) :  #no shoot
        return event_shots
    
    event_shots[0][1]=1
    event_shots[1]=[[moments[i][0],moments[i][2]]]

    if succesfull_three_points(moments,i):
        event_shots[0][0]=1
    
    return event_shots

def track_shots(data):
    with open(data) as json_file:  
        data = json.load(json_file)
        events=data['events']
    event=events[2]
    time_shots=[]
    shots=np.array([0,0])
    
    for q in range(len(events)):
        
        if len(events[q]['moments'])!=len(event['moments']):
            event=events[q]
            
            moments=event['moments']
            res=track_event_shots(moments)
            if len(res[1])!=0:
                if res[1][0] not in time_shots:
                    shots=shots+res[0]
                    time_shots=time_shots+res[1]
    
    return(shots,time_shots)

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

#                '001':np.array([20,56]),
#               '002':np.array([16,48]),
#               '003':np.array([15,48]),
#               '004':np.array([12,54]),
#               '005':np.array([15,46]),
#               '007':np.array([9,31]),
#               '009':np.array([15,41])
#               
#1 [20 56]
#2 [20 53]
#3 [20 48]
#4 [12 42]
#5 [ 8 42]
#7 [16 34]
#9 [18 46]