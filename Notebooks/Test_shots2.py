#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 18:46:12 2019

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
               '007':np.array([9,26]),
               '009':np.array([15,41])
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

def first_test(ball0):
    if ball0[2]<2.5*3.28:
        return False
    else : 
        return True
    
def second_test(ball0,where):
    coin=False
    if where==1 :
        basket_pos=[5.25,25]
        if ball0[0]<15:
            coin=True
    else :
        basket_pos=[94-5.25,25]
        if ball0[0]>(94-15):
            coin=True
    if coin : 
        if 0<ball0[1]<3.5 or 50-3.5<ball0[1]<50 : 
            return (True,basket_pos)
        else :
            return (False,basket_pos)
    else :
        if distance(ball0,basket_pos)>23.5 :  #In fact 23.75 but we take a marge to have all shoots
            return (True,basket_pos)
        else:
            return (False,basket_pos)
    
f=0
s=0
t=0
fr=0
def detect_3pt_shot(moments,i):
    global f,s,t,fr
    j=i
    result=[False,False,j]
    ball0=moments[i][5][0][2:5]
    
    if not first_test(ball0):
        return result
    
    f+=1
    
    where=where_attack(moments,i)
    coin=False
    if where==1 :
        basket_pos=[5.25,25]
        if ball0[0]<15:
            coin=True
    else :
        basket_pos=[94-5.25,25]
        if ball0[0]>(94-15):
            coin=True
    
    
    ball=ball0
    while j<(len(moments)-2) and ball[2]<=10 and ball[2]>=ball0[2]:
        j+=1
        ball=moments[j][5][0][2:5]
    
    result[2]=j
    
    if ball[2]<ball0[2] or j>=(len(moments)-2):
        return(result)
    
    t+=1
    
        
    ball2=ball
    ball1=ball2
    while j<(len(moments)-2) and ball2[2]>10:
        ball1=ball2
        j+=1
        while (not test_moment(moments[j])) and (j<(len(moments)-2)):
            j+=1
        ball2=moments[j][5][0][2:5]
    
    result[2]=j
    
    if not ball_in_cercle(ball1,basket_pos):
        return result
    
    s+=1
    
    if not second_test(ball0,where)[0]:
        return result
    
    else :
        basket_pos=second_test(ball0,where)[1]
        
    fr+=1
    
    result[2]=j
    
    print(np.array(ball1)-np.array(basket_pos+[10]))
    
    if not ball_in_cercle(ball1,basket_pos):
        return result
    
    else :
        result[0]=True
    
    if not ball_through_basket(ball1,ball2,basket_pos):
        return result

    else :
        return [True,True,j]

def ball_in_tube2(ball,basket_pos):
    if distance(ball[:2],basket_pos)<5:  
        if 3.05*3.281<ball[2]:
            return True
    return False

def ball_in_cercle(ball,basket_pos): #to know if the ball comes above the basket
    if distance(np.array(ball[:2]),basket_pos)<5:  
        return True
    return False

def ball_through_basket(b1,b2,basket_pos):
    
    a=(b1[2]-b2[2])/(b1[0]-b2[0])
    b=b2[2]-a*b2[0]
    x=(10-b)/a
    a2=(b1[2]-b2[2])/(b1[1]-b2[1])
    b2=b2[2]-a2*b2[1]
    y=(10-b2)/a2
    
    if distance(np.array([x,y]),basket_pos)<0.75:
        return True
    return False

def track_event_shots(moments,t_end):
    event_shots=np.array([0,0])
    time=t_end
    
    if len(moments)<=1:
        return(event_shots,time)
    i=0
    while not test_moment(moments[i]) and (i<(len(moments)-2)):
        i+=1
    while [5-moments[i][0],moments[i][2]]>t_end and (i<(len(moments)-2)):
        i+=1
        
    if i>=(len(moments)-2) : #no moment
        return(event_shots,t_end)

    while i<(len(moments)-2):
        if test_moment(moments[i]):
            result=detect_3pt_shot(moments,i)
            i=result[2]+1
            if result[0]:
                event_shots[1]+=1
                if result[1]:
                    event_shots[0]+=1
        else :
            i+=1
            
    t_end=[5-moments[i][0],moments[i][2]]
    
    return [event_shots,t_end]

def track_shots(data):
    with open(data) as json_file:  
        data = json.load(json_file)
        events=data['events']
    event=events[2]
    time_end=[np.inf,np.inf]
    shots=np.array([0,0])
    
    for q in range(len(events)):
        
        if len(events[q]['moments'])!=len(event['moments']):
            event=events[q]
            moments=event['moments']
            res=track_event_shots(moments,time_end)
            shots=shots+res[0]
            time_end=res[1]
    
    return(shots)

for k in range(638):
    os.chdir('/Volumes/My Passport/GABIN/Documents/CENTRALE_LYON_1A/PaR/Basket/')
    if k<10:
        if ('002150000'+str(k)+'.json') in os.listdir():
            result=track_shots('002150000'+str(k)+'.json')
            print(k,result)
            Calculated_nb_shots[str(k)]=result
            #Time_shots[str(k)]=result[1]
            
    if 9<k<100:
        if ('00215000'+str(k)+'.json') in os.listdir():
            result=track_shots('00215000'+str(k)+'.json')
            print(k,result)
            Calculated_nb_shots[str(k)]=result
            #Time_shots[str(k)]=result[1]
            
    if 99<k:
        if ('0021500'+str(k)+'.json') in os.listdir():
            result=track_shots('0021500'+str(k)+'.json')
            print(k,result)
            Calculated_nb_shots[str(k)]=result
            #Time_shots[str(k)]=result[1]
            
           
