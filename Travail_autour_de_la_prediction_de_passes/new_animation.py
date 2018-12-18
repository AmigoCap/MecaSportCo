#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:53:29 2018

@author: nathanriviere
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m
import json
import os 
from scipy.spatial import Voronoi, voronoi_plot_2d

with open("game3.json") as json_file:  
    data = json.load(json_file)
    events=[data['events'][0]]
    events=events[0]
    
visitor=events['visitor']
home=events['home']
moments=events['moments']
moments = moments[300:] #for game3

moment1=moments[25][5]
moment2=moments[26][5]

F=10*3.28     # Force per mass unit 1<F<10m.s-2 ici en feet.s-2
n = 50
dt=0.04
def att_def_ball_pos(i): #index of the moment
    att_pos,def_pos,ball = [], [],[]
    
    moment1 = moments[i][5]
    moment2 = moments[i+1][5]
    for i in range(11) :
        if i==0:
            ball=[np.array(moment1[i][2:4]),np.array([(moment2[i][2]-moment1[i][2])/dt,(moment2[i][3]-moment1[i][3])/dt])]
        if 6<=i<=11:
            att_pos.append([np.array(moment1[i][2:4]),np.array([(moment2[i][2]-moment1[i][2])/dt,(moment2[i][3]-moment1[i][3])/dt])])
        if 1<=i<=5:
            def_pos.append([np.array(moment1[i][2:4]),np.array([(moment2[i][2]-moment1[i][2])/dt,(moment2[i][3]-moment1[i][3])/dt])])
    return(att_pos,def_pos,ball)

def voronoi(j): #i index of the moment
    moment1=moments[j][5]
    points = np.array([[player[2],player[3]] for player in moment1[1:]])
    vor = Voronoi(points)
    fig = voronoi_plot_2d(vor, show_vertices=False, line_colors='black',line_width=1, line_alpha=0.6, point_size=0)
    plt.xlim(0,94) #force the plt.show to adapt the size
    plt.ylim(0,50)

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
    
court = np.eye(n)

            

def print_court(i):
    att_pos,def_pos,ball = att_def_ball_pos(i)
    voronoi(i)
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
    
print_court(110)
#tracer_trajectoire_un_joueur(att_pos[3],16000)
        

#tracer_trajectoire_un_joueur(att_pos[3],16000)