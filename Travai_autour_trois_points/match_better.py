#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:17:27 2019

@author: gabin
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m
import json
import os 
import pickle
import time
from scipy.spatial import Voronoi, voronoi_plot_2d

#with open("0021500001.json") as json_file:  
#    data = json.load(json_file)
#    events=data['events']
#    event=events[117]
#
#visitor=event['visitor']
#home=event['home']
#moments_test=event['moments']
#
#F=10*3.28     # Force per mass unit 1<F<10m.s-2 ici en feet.s-2
#y_max = 50
#n=50


## in order to have the same representation as in the video
#for mom in moments_test : 
#    l = mom[5]
#    for element in l :
#        element[3] = y_max-element[3]
#
#dt=0.04
#x_mid = 94/2

def distance(a,b):      #a = (x,y) point de départ ; b = (i,j) point d'arrivée ; v = norme pour l'instant
    return m.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def barycentre(moment,i):
    gx,gy = 0,0
    players = moment[5]
    for k in range(1+5*(i-1),11-5*(2-i)):
        gx,gy = gx+ players[k][2],gy+players[k][3]
    return(gx/5,gy/5)
    
def who_attack(moments,i):
    moment=moments[i]
    gx1,gx2 = barycentre(moment,1)[0],barycentre(moment,2)[0]
    x_mid = 94/2
    if abs(gx1-x_mid)<=abs(gx2-x_mid):
        return(1)
    else : 
        return(2)

def where_attack(moments,j):
    ball=players_ball(moments,j)[0]
    x_mid=94/2
    if (ball[0][0]-x_mid)<0:
        return(1)
    else :
        return(2)
  
      
def att_def_ball_pos(moments,j): #index of the moment
    att_pos,def_pos,ball = [], [],[]
    moment1 = moments[j][5]
    moment2 = moments[j+1][5]
    dt=0.04
    m=min(len(moment1),len(moment2))
    index_attack = who_attack(moments,j)
    if index_attack == 2:
        for i in range(m) :
            if i==0:
                ball=[np.array(moment1[i][2:4]),np.array([(moment2[i][2]-moment1[i][2])/dt,(moment2[i][3]-moment1[i][3])/dt]),moment1[i][4]]
            if 6<=i<=11:
                att_pos.append([np.array(moment1[i][2:4]),np.array([(moment2[i][2]-moment1[i][2])/dt,(moment2[i][3]-moment1[i][3])/dt])])
            if 1<=i<=5:
                def_pos.append([np.array(moment1[i][2:4]),np.array([(moment2[i][2]-moment1[i][2])/dt,(moment2[i][3]-moment1[i][3])/dt])])
    else : 
        for i in range(m) :
            if i==0:
                ball=[np.array(moment1[i][2:4]),np.array([(moment2[i][2]-moment1[i][2])/dt,(moment2[i][3]-moment1[i][3])/dt]),moment1[i][4]]
            if 6<=i<=11:
                def_pos.append([np.array(moment1[i][2:4]),np.array([(moment2[i][2]-moment1[i][2])/dt,(moment2[i][3]-moment1[i][3])/dt])])
            if 1<=i<=5:
                att_pos.append([np.array(moment1[i][2:4]),np.array([(moment2[i][2]-moment1[i][2])/dt,(moment2[i][3]-moment1[i][3])/dt])])
    return(att_pos,def_pos,ball)

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

def voronoi(moments,j): #i index of the moment
    moment1=moments[j][5]
    points = np.array([[player[2],player[3]] for player in moment1[1:]])
    vor = Voronoi(points)
    fig = voronoi_plot_2d(vor, show_vertices=False, line_colors='black',line_width=1, line_alpha=0.6, point_size=0)
    plt.xlim(0,94) #force the plt.show to adapt the size
    plt.ylim(0,50)

def print_court(moments,i):
    att_pos,def_pos,ball = att_def_ball_pos(moments,i)
    voronoi(moments,i)
    court = np.eye(n)
    for i in range(n):
        #print(i)
        for j in range(n):
            b=np.array([i,j]) # point d'arrivée
            #tb = temps_parcours_grav(F,ball[0],b,ball[1])
            
            a=att_pos[0][0]
            v=att_pos[0][1]
            tmin_att=time_to_point(F,a,b,v)
            for player in att_pos[1:] :
                a=player[0]
                v=player[1]
                t=time_to_point(F,a,b,v)
                if t<tmin_att:
                    tmin_att=t
                    
            a=def_pos[0][0]
            v=def_pos[0][1]
            tmin_def=time_to_point(F,a,b,v)
            for player in def_pos[1:] :
                a=player[0]
                v=player[1]
                t=time_to_point(F,a,b,v)
                if t<tmin_def:
                    tmin_def=t
            
            #if tb<tmin_att and tb<tmin_def:
                #court[j,i]=None
            #else :
            court[j,i]=(tmin_def-tmin_att)
    
    for player in att_pos:
        plt.plot(player[0][0],player[0][1],'bo',markersize=15,alpha=0.6)
        plt.arrow(player[0][0],player[0][1],player[1][0],player[1][1],shape='full',lw=1.5,head_width=1)
    
    for player in def_pos:
        plt.plot(player[0][0],player[0][1],'ro',markersize=15,alpha=0.6)
        plt.arrow(player[0][0],player[0][1],player[1][0],player[1][1],shape='full',lw=1.5,head_width=1)
        
    plt.plot(ball[0][0],ball[0][1],'yo')
    field = plt.imread("fullcourt.png")
    im=plt.imshow(court,origin='lower', cmap='RdBu', vmin=-0.5, vmax=0.5)
    plt.colorbar(orientation='vertical')
    plt.imshow(field, extent=[0,94,0,50])
    
    
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

def test_player_with_ball(moments):
    player=[]
    k=len(moments)
    for i in range(k-1):
        player.append(player_with_ball(i))
    num_mom=[j for j in range(k-1)]
    plt.plot(num_mom,player,'o')
    
def basket_direction(player,where_attack):
    if where_attack==1:
        basket_pos1=[1.575*3.28,25-0.9*3.28]
        basket_pos2=[1.575*3.28,25+0.9*3.28]
    else :
        basket_pos1=[94-1.575*3.28,25-0.9*3.28]
        basket_pos2=[94-1.575*3.28,25+0.9*3.28]
    vx1=-player[0]+basket_pos1[0]
    vy1=-player[1]+basket_pos1[1]
    vx2=-player[0]+basket_pos2[0]
    vy2=-player[1]+basket_pos2[1]
    vx=np.sort([vx1,vx2])
    vy=np.sort([vy1,vy2])
    return(vx,vy)
    
def detect_shoot(moments,i,players):
    ball=players[0]
    vball=ball[1]
    if ball[2]<3.05*3.28:
        return(False)
    vx,vy=basket_direction(ball[0],where_attack(moments,i))
    if vx[0]<0:
        if vx[0]<vball[0]<0:        #vx[1]=vx[0]
            if vy[0]<vball[1]<vy[1]:
                return(True)
    else :
        if 0<vball[0]<vx[0]:        #vx[1]=vx[0]
            if vy[0]<vball[1]<vy[1]:
                return(True)
        
def test_detect_shoot(moments):
    shoot=[]
    k=len(moments)
    for i in range(k-1):
       num_mom=[j for j in range(k-1)]
       shoot.append(detect_shoot(i))
    plt.plot(num_mom,shoot,'o') 

def time_to_point(F,a,b,v):   #time to go from a to b with initial speed v
    x0,y0=a
    xf,yf=b
    X=x0-xf
    Y=y0-yf
    k4=1
    k3=0
    k2=4*(v[0]**2+v[1]**2)/F**2
    k1=8*(v[0]*X+v[1]*Y)/F**2
    k0=4*(X**2+Y**2)/F**2
    times=np.roots([k4,k3,-k2,-k1,-k0])
    for i in range(4):                      # Selection of the root real and positive
        if times[i].imag==0:
            if times[i]>0:
                return times[i].real
    print('error')
    return times[0]

def calcul_aire_un_joueur(moments,j,n,F,player,players): #player is considered as an attackant because he is the one who shoots at the end
    aire=0
    index_player=0
    if player>5:
        att_pos=players[6:]
        def_pos=players[1:6]
        index_player=player-6
    else :
        att_pos=players[1:6]
        def_pos=players[6:]
        index_player=player-1
    where=where_attack(moments,j)
    if where==1:                    #si on attaque à gauche on prend la moitié de terrain gauche (50,50)
        for i in range(n):
            for j in range(n):
                b=np.array([i,j]) # point d'arrivée
                
                a=att_pos[0][0]
                v=att_pos[0][1]
                tmin_att=[time_to_point(F,a,b,v),0]
                for k in range(1,5) :
                    a=att_pos[k][0]
                    v=att_pos[k][1]
                    t=time_to_point(F,a,b,v)
                    if t<tmin_att[0]:
                        tmin_att=[t,k]
                        
                a=def_pos[0][0]
                v=def_pos[0][1]
                tmin_def=time_to_point(F,a,b,v)
                for player in def_pos[1:] :
                    a=player[0]
                    v=player[1]
                    t=time_to_point(F,a,b,v)
                    if t<tmin_def:
                        tmin_def=t
                
                if tmin_att[0]<tmin_def:
                    if tmin_att[1]==index_player:
                        aire+=tmin_def-tmin_att[0]
    else :
        for i in range(45,95):
            for j in range(n):
                b=np.array([i,j]) # point d'arrivée
                
                a=att_pos[0][0]
                v=att_pos[0][1]
                tmin_att=[time_to_point(F,a,b,v),0]
                for k in range(1,5) :
                    a=att_pos[k][0]
                    v=att_pos[k][1]
                    t=time_to_point(F,a,b,v)
                    if t<tmin_att[0]:
                        tmin_att=[t,k]
                        
                a=def_pos[0][0]
                v=def_pos[0][1]
                tmin_def=time_to_point(F,a,b,v)
                for player in def_pos[1:] :
                    a=player[0]
                    v=player[1]
                    t=time_to_point(F,a,b,v)
                    if t<tmin_def:
                        tmin_def=t
                
                if tmin_att[0]<tmin_def:
                    if tmin_att[1]==index_player:
                        aire+=tmin_def-tmin_att[0]
                    
    return aire

def three_points(moments,i,who_ball): #to improve
    where=where_attack(moments,i)
    basket_pos=[]
    player=moments[i][5][who_ball][2:4]
    coin=False
    if where==1 :
        basket_pos=[1.575*3.28,25]
        if player[0]<15:
            coin=True
    else :
        basket_pos=[94-1.575*3.28,25]
        if player[0]>(94-15):
            coin=True
    if coin :  
        if distance(player,basket_pos)>3.28*6.71 :  #Shortest distance close to the coins and considering as a circle so maybe mistakes
            return True
    else :
        if distance(player,basket_pos)>3.28*7.23 :  #Shortest distance close to the coins and considering as a circle so maybe mistakes
            return True
    return False

def distance_closest_player(moments,i,player,index_player,F,players):
    att_pos,def_pos=[],[]
    if index_player>5:
        att_pos=players[6:]
        def_pos=players[1:6]
    else :
        att_pos=players[1:6]
        def_pos=players[6:]
    a=def_pos[0][0]
    v=def_pos[0][1]
    t_min=time_to_point(F,a,player,v)
    for player2 in def_pos[1:]:
        a=player2[0]
        v=player2[1]
        t=time_to_point(F,a,player,v)
        if t<t_min:
            t_min=t
    return(t_min)
        
def test_moment(moment):
    if len(moment[5])!=11:
        return(False)
    for i in range(len(moment[5])):
        if len(moment[5][i])!=5:
            return (False)
    return(True)
            
            
        
# idée : on pourrait tous les tracer sur un même graphique en utilisant mini et maxi
# On pourrait sauvegarder l'image au moment du shoot aussi pour vérifier
        
        
   










def track_shoot_event(event):
    moments=event['moments']
    F=5*3.28     # Force per mass unit 1<F<10m.s-2 ici en feet.s-2
    y_max = 50
    n=50
        # in order to have the same representation as in the video
    for mom in moments : 
        l = mom[5]
        for element in l :
            element[3] = y_max-element[3]

    dt=0.04
    x_mid = 94/2
    
    if len(moments)==0:
        return(None)

    i=0
    while (not test_moment(moments[i]) or not test_moment(moments[i+1])) and (i<(len(moments)-2)):
        i+=1
        
    if i>=(len(moments)-2) : #no moment
        return None
    
    players=players_ball(moments,i)
    who_ball=player_with_ball(moments,i)
    when0=i
    when_reception=i
    who_ball2=None
    while (not detect_shoot(moments,i,players)) and i<(len(moments)-2):
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
        return None
    
    else :
        ### Test 3 points ###
        if i>60: #we want to know if we can have enough information
            if three_points(moments,i,who_ball):
                print('shoot3points',i)
                aire=[]
                time=[0]
                closest_player=[0]
                gradient_aire=[0]
                gradient_closest=[0]
                closest_player_reception=0
                aire_reception=0
                
                maxi=min(len(moments)-1,when0+20)
                mini=max(when0-80,0)
                
                max_aire=0
                mom_max_aire=(mini-when0)*0.04
                
                max_distance=0
                mom_max_distance=(mini-when0)*0.04
                
                players=players_ball(moments,mini)
                calcul=calcul_aire_un_joueur(moments,mini,n,F,who_ball,players)
                    
                aire.append(calcul)
                
                for j in range(mini,maxi):   # 3 last seconds for the player and 1 sec after shoot
                    if test_moment(moments[j]) and test_moment(moments[j+1]):
                        
                        players=players_ball(moments,j)
                        
                        calcul=calcul_aire_un_joueur(moments,j,n,F,who_ball,players)
                        
                        aire.append(calcul)
                            
                        time.append((j-when0)*0.04)
                        
                        player=moments[j][5][who_ball][2:4]
                        closest_player.append(distance_closest_player(moments,j,player,who_ball,F,players))
                        if aire[j-mini]>max_aire:
                            if j<=when0:
                                max_aire=aire[j-mini]
                                mom_max_aire=-(j-when0)*0.04
                        gradient_aire.append((aire[j-mini]-aire[j-1-mini])/dt)
                        
                        if closest_player[j-mini]>max_distance:
                            if j<=when0:
                                max_distance=closest_player[j-mini]
                                mom_max_distance=-(j-when0)*0.04
                        gradient_closest.append((closest_player[j-mini]-closest_player[j-1-mini])/dt)
                        
                        if j==when_reception:
                            closest_player_reception=closest_player[-1]
                            aire_reception=calcul
                            
                    else :
                        aire.append(aire[-1])
                        closest_player.append(closest_player[-1])
                        time.append(time[-1])
                        gradient_aire.append(gradient_aire[-1])
                        gradient_closest.append(gradient_closest[-1])
                            
                    
                return[aire[1:],time[1:],closest_player[1:],gradient_aire[1:],gradient_closest[1:],max_aire,max_distance,mom_max_aire,mom_max_distance,(when0-when_reception)*0.04,aire_reception,closest_player_reception]
            else :
                return None
        else :
                return None
  
    
    

def track_shoot_match(data,match):            #argument type : "data.json"
    time1=time.time()
    with open('0021500001.json') as json_file:  
        data = json.load(json_file)
        events=data['events']
    event=events[2]
    AIRES=[]
    CLOSEST_PLAYER=[]
    TIME=[]
    GRADIENT_AIRE=[]
    GRADIENT_CLOSEST=[]
    Max_aires=[]
    Max_distance=[]
    Time_max_aires_to_shoot=[]
    Time_max_distance_to_shoot=[]
    Time_to_shoot=[]
    Aire_reception=[]
    Closest_reception=[]
    Events_shoot=[]
    for q in range(150,250):
        if len(events[q]['moments'])!=len(event['moments']):
            if q%50==0:
                print('event',q)
            event=events[q]
            results=track_shoot_event(event)
            if results!=None:
                if len(results[1])>80:   #because too short events cannot be well interpreted
                   AIRES.append(results[0])
                   TIME.append(results[1])
                   CLOSEST_PLAYER.append(results[2])
                   GRADIENT_AIRE.append(results[3])
                   GRADIENT_CLOSEST.append(results[4])
                   Max_aires.append(results[5])
                   Max_distance.append(results[6])
                   Time_max_aires_to_shoot.append(results[7])
                   Time_max_distance_to_shoot.append(results[8])
                   Time_to_shoot.append(results[9])
                   Aire_reception.append(results[10])
                   Closest_reception.append(results[11])
                   Events_shoot.append(q)
                   
    l=[AIRES,CLOSEST_PLAYER,TIME,GRADIENT_AIRE,GRADIENT_CLOSEST,Max_aires,Max_distance,Time_max_aires_to_shoot,Time_max_distance_to_shoot,Time_to_shoot,Aire_reception,Closest_reception,Events_shoot]
    L=['AIRES','CLOSEST_PLAYER','TIME','GRADIENT_AIRE','GRADIENT_CLOSEST','Max_aires','Max_distance','Time_max_aires_to_shoot','Time_max_distance_to_shoot','Time_to_shoot','Aire_reception','Closest_reception','Events_shoot']
    save=dict(zip(L,l))
    pickle.dump(save, open('0021500001_150_250', 'wb'))
    
    
    for k in range(len(AIRES)):
        plt.plot(TIME[k],AIRES[k],'--')
    plt.xlabel('time')
    plt.ylabel('quantity of occupied espace')
    plt.savefig('Aire.png')
    plt.clf()
    
    for k in range(len(CLOSEST_PLAYER)):
        plt.plot(TIME[k],CLOSEST_PLAYER[k],'--')
    plt.xlabel('time')
    plt.ylabel('time of the closest defender')
    plt.savefig('Distance.png')
    plt.clf()
    
    for k in range(len(GRADIENT_AIRE)):
        plt.plot(TIME[k],GRADIENT_AIRE[k],'--')
    plt.xlabel('time')
    plt.ylabel('gradient of quantity of occupied espace')
    plt.savefig('Gradient_Aire.png')
    plt.clf()
    
    for k in range(len(GRADIENT_CLOSEST)):
        plt.plot(TIME[k],GRADIENT_CLOSEST[k],'--')
    plt.xlabel('time')
    plt.ylabel('gradient of time of the closest defender')
    plt.savefig('Gradient_Time.png')
    plt.clf()
    
    plt.plot(Time_to_shoot,Aire_reception,'o')
    plt.xlabel('time of the reception of the ball')
    plt.ylabel('QOE at the reception of the ball')
    plt.savefig('QOE_time_reception.png')
    plt.clf()
    
    plt.plot(Time_to_shoot,Closest_reception,'o')
    plt.xlabel('time of the reception of the ball')
    plt.ylabel('Time of the closest player at the reception of the ball')
    plt.savefig('Closest_time_reception.png')
    plt.clf()
    
    number=[k for k in range(len(Max_aires))]
    
    plt.plot(number,Max_aires,'-')
    plt.xlabel('shoot n°')
    plt.ylabel('Max of quantity of occupied espace')
    plt.savefig('Max_aires.png')
    plt.clf()
    
    plt.plot(number,Max_distance,'--')
    plt.xlabel('shoot n°')
    plt.ylabel('Max of time of the closest defender')
    plt.savefig('Max_time.png')
    plt.clf()
    
    plt.plot(number,Time_max_aires_to_shoot,'--')
    plt.xlabel('shoot n°')
    plt.ylabel('Time max of QOE to shoot')
    plt.savefig('Time_aire_shoot.png')
    plt.clf()
    
    plt.plot(number,Time_max_distance_to_shoot,'--')
    plt.xlabel('shoot n°')
    plt.ylabel('Time max of time of the closest defender to shoot')
    plt.savefig('Time_distance_shoot.png')
    plt.clf()
    
    
    plt.plot(number,Time_to_shoot,'--')
    plt.xlabel('shoot n°')
    plt.ylabel('Time between recpetion of the ball and shoot')
    plt.savefig('Time_to_shoot.png')
    plt.clf()
    
    print (time.time()-time1)
    
    
# sources d'erreur : moment du tir ballon trop proche du défenseur => on ne regarde pas la bonne évolution + contre attaques problème d'aires à 0 des fois
# idées : normaliser notre métrique autour du temps moyen + ne prendre en compte que 3 ou 4 mètres autour du joueur pour éviter les pbs de 0