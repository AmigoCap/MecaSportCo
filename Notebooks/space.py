#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:39:29 2019

@author: gabin
"""

import numpy as np
import matplotlib.pyplot as plt

def players_ball_speed_position(moment1,moment2):
    team1,team2,ball =[],[],[]
    
    dt=0.04

    for i in range(11) :
        if i==0:
            ball=[np.array(moment1[i][2:4]),np.array([(moment2[i][2]-moment1[i][2])/dt,(moment2[i][3]-moment1[i][3])/dt])]
        if 6<=i<=11:
            team2.append([np.array(moment1[i][2:4]),np.array([(moment2[i][2]-moment1[i][2])/dt,(moment2[i][3]-moment1[i][3])/dt])])
        if 1<=i<=5:
            team1.append([np.array(moment1[i][2:4]),np.array([(moment2[i][2]-moment1[i][2])/dt,(moment2[i][3]-moment1[i][3])/dt])])
    return(team1,team2,ball)

def distance(a,b):      #a = (x,y) departure point ; b = (i,j) arrival point
    return m.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def print_court_teams_occupation(event_id,mom_id,voronoi_cut=False,value=False,n=50,p=94):
    "This function return a visualization of the court for the moment mom_id of the event event_id. If voronoi_cut=True, voronoi cutting is plotted. Then, if value=True, a heat-map giving a value to space occupation is drawn."
    if voronoi_cut:
        voronoi(event_id,mom_id)
    event=events[event_id]
    moment=event['moments'][mom_id][5]
    moment1=moment
    moment2=event['moments'][mom_id+1][5]
    
    # separation of ball, team1 and team2 and calculation of the speed
    playersTeam1,playersTeam2,ball=players_ball_speed_position(event,moment1,moment2)
    
    for player in playersTeam2:
        plt.plot(player[0][0],player[0][1],'bo',markersize=12,alpha=0.6)
        plt.arrow(player[0][0],player[0][1],player[1][0],player[1][1],shape='full',lw=1.5,head_width=1)
    
    for player in playersTeam1:
        plt.plot(player[0][0],player[0][1],'ro',markersize=12,alpha=0.6)
        plt.arrow(player[0][0],player[0][1],player[1][0],player[1][1],shape='full',lw=1.5,head_width=1)
    
    if value:
        court=np.zeros((n,p))
        for i in range(n):
            for j in range(p):
                b=np.array([j,i]) # point d'arrivée
                db=distance(ball[0],b)
            
                a=playersTeam1[0][0]
                dmin_1=distance(a,b)
                for player in playersTeam1[1:]:
                    a=player[0]
                    d=distance(a,b)
                    if d<dmin_1:
                        dmin_1=d
                    
                a=playersTeam2[0][0]
                dmin_2=distance(a,b)
                for player in playersTeam2[1:] :
                    a=player[0]
                    d=distance(a,b)
                    if d<dmin_2:
                        dmin_2=d
                court[i,j]=dmin_1-dmin_2
        im=plt.imshow(court,origin='lower', cmap='RdBu')
        #plt.colorbar(orientation='vertical')
        
    plt.plot(ball[0][0],ball[0][1],'yo')
    plt.xlabel('x in feet')
    plt.ylabel('y in feet')
    field = plt.imread("Images/fullcourt.png")
    plt.imshow(field, extent=[0,94,0,50])
    plt.show()
    
def print_court_teams_occupation_inertia(event_id,mom_id,voronoi_cut=False,n=50,p=94):
    "This function return a visualization of the court for the moment mom_id of the event event_id. If voronoi_cut=True, voronoi cutting is plotted. Then, if value=True, a heat-map giving a value to space occupation is drawn."
    if voronoi_cut:
        voronoi(event_id,mom_id)
    event=events[event_id]
    moment=event['moments'][mom_id][5]
    moment1=moment
    moment2=event['moments'][mom_id+1][5]
    
    # separation of ball, team1 and team2 and calculation of the speed
    playersTeam1,playersTeam2,ball=players_ball_speed_position(event,moment1,moment2)
    
    for player in playersTeam2:
        plt.plot(player[0][0],player[0][1],'bo',markersize=12,alpha=0.6)
        plt.arrow(player[0][0],player[0][1],player[1][0],player[1][1],shape='full',lw=1.5,head_width=1)
    
    for player in playersTeam1:
        plt.plot(player[0][0],player[0][1],'ro',markersize=12,alpha=0.6)
        plt.arrow(player[0][0],player[0][1],player[1][0],player[1][1],shape='full',lw=1.5,head_width=1)

    court=np.zeros((n,p))
    for i in range(n):
         for j in range(p):
            b=np.array([j,i]) # point d'arrivée
        
            a=playersTeam1[0][0]
            v=playersTeam1[0][1]
            tmin_1=time_to_point(a,b,v)
            for player in playersTeam1[1:] :
                a=player[0]
                v=player[1]
                t=time_to_point(a,b,v)
                if t<tmin_1:
                    tmin_1=t
                    
            a=playersTeam2[0][0]
            v=playersTeam2[0][1]
            tmin_2=time_to_point(a,b,v)
            for player in playersTeam2[1:] :
                a=player[0]
                v=player[1]
                t=time_to_point(a,b,v)
                if t<tmin_2:
                    tmin_2=t
            
            court[i,j]=tmin_1-tmin_2
            
    im=plt.imshow(court,origin='lower', cmap='RdBu', vmin=-0.6, vmax=0.6)
    #plt.colorbar(orientation='vertical')
        
    plt.plot(ball[0][0],ball[0][1],'yo')
    plt.xlabel('x in feet')
    plt.ylabel('y in feet')
    field = plt.imread("Images/fullcourt.png")
    plt.imshow(field, extent=[0,94,0,50])
    plt.show()