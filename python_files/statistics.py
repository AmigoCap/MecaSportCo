#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:40:22 2019

@author: gabin
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import time
from scipy.signal import savgol_filter


dico=pickle.load(open('Shots','rb'))

def shot_type(row):
    if row['Time_to_shoot']>-2:
        return('catch-and-shoot')
    else :
        return('pull-up')
    
def shooting_efficiency_inferior(data):
    
    ### getting the data ###
    D_CLOSEST_PLAYER=data['D_CLOSEST_DEF']
    T_CLOSEST_PLAYER=data['T_CLOSEST_DEF']
    TIME=data['TIME_ABSCISSE']
    TIME_TO_SHOOT=data['TIME_TO_SHOOT']
    
    ### differentiating catch-and-shoot, pull-up shots and success and fails ###
    D_CLOSEST_PLAYER1=[]
    D_CLOSEST_PLAYER2=[]
    T_CLOSEST_PLAYER1=[]
    T_CLOSEST_PLAYER2=[]
    TIME1=[]
    TIME2=[]

    for k in range(len(D_CLOSEST_PLAYER)):
        ## success ##
        if D_CLOSEST_PLAYER[k][0]==1:
            
            # all shots #
            D_CLOSEST_PLAYER1.append(D_CLOSEST_PLAYER[k][1])
            T_CLOSEST_PLAYER1.append(T_CLOSEST_PLAYER[k][1])
            TIME1.append(np.array(TIME[k][1]))
                
        ## fails ##
        else :
            
            # all shots #
            D_CLOSEST_PLAYER2.append(D_CLOSEST_PLAYER[k][1])
            T_CLOSEST_PLAYER2.append(T_CLOSEST_PLAYER[k][1])
            TIME2.append(np.array(TIME[k][1]))
            
    print(len(D_CLOSEST_PLAYER1)/(len(D_CLOSEST_PLAYER2)+len(D_CLOSEST_PLAYER1)))
    closest1=[]
    pos1=[]
    closest2=[]
    pos2=[]
    for i in range(len(D_CLOSEST_PLAYER1)):
        min1=0
        min2=0
        for j in range(len(D_CLOSEST_PLAYER1[i])):
            if -0.04<TIME1[i][j]<0.04:
                if T_CLOSEST_PLAYER1[i][j]>min1:
                    min1=T_CLOSEST_PLAYER1[i][j]
                if D_CLOSEST_PLAYER1[i][j]>min2:
                    min2=D_CLOSEST_PLAYER1[i][j]
        closest1.append(min1)
        pos1.append(min2)
                
    for i in range(len(D_CLOSEST_PLAYER2)):
        min1=np.inf
        min2=np.inf
        for j in range(len(D_CLOSEST_PLAYER2[i])):
            if -0.04<TIME2[i][j]<0.04:
                if T_CLOSEST_PLAYER2[i][j]<min1:
                    min1=T_CLOSEST_PLAYER2[i][j]
                if D_CLOSEST_PLAYER2[i][j]<min2:
                    min2=D_CLOSEST_PLAYER2[i][j]
        closest2.append(min1)
        pos2.append(min2)
    
    inferior_values=[]
    time_abs=[0.02*i+0.2 for i in range(60)]
    S1=[]
    T1=[]
    for i in range(60):
        success=0
        fails=0
        for j in range(len(closest1)):
            if not np.isinf(closest1[j]):
                if closest1[j]<time_abs[i]:
                    success+=1
        for j in range(len(closest2)):
            if not np.isinf(closest2[j]):
                if closest2[j]<time_abs[i]:
                    fails+=1
        S1.append(success/len(closest1))
        T1.append(fails/len(closest2))
                
        #print('inf to :', i)
        #print(success,fails)
        
        inferior_values.append(success/(fails+success)*100)
    
    fig,ax1=plt.subplots()
    plt.plot(time_abs,inferior_values)
    plt.xlabel(r'$\delta_{t}^*(0)$ inferior to [s]')
    plt.ylabel('Three point shooting percentage')
    plt.vlines(time_abs[15], inferior_values[0], inferior_values[15], linestyle="dashed",lw=0.5)
    plt.hlines(inferior_values[15], time_abs[0], time_abs[15], linestyle="dashed",lw=0.5)
    plt.xlim(time_abs[0],time_abs[-1])
    plt.ylim(inferior_values[0],inferior_values[-1]+1)
    ax1.tick_params(direction='in')
    plt.show()
#    plt.plot(time_abs2,inferior_values2)
    #plt.figure(2)
    #plt.plot(time_abs,S1)
    #plt.plot(time_abs,T1)
        
    d_abs=[0.1*i+3 for i in range(140)]
    inferior_values=[]
    S=[]
    T=[]
    for i in range(140):
        success=0
        fails=0
        for j in range(len(pos1)):
            if not np.isinf(pos1[j]):
                if pos1[j]<d_abs[i]:
                    success+=1
        for j in range(len(pos2)):
            if not np.isinf(pos2[j]):
                if pos2[j]<d_abs[i]:
                    fails+=1
        S.append(success/len(pos1))
        T.append(fails/len(pos2))
                
        #print('inf to :', i*0.2)
        #print(success,fails)
        #print(round(success/len(pos1),2),round(fails/len(pos2),2),round(success/(fails+success),2)*100)
        
        inferior_values.append(success/(fails+success)*100)
    
    print(inferior_values[10],inferior_values[50])
        
#    d_abs2=[0.2*i+1 for i in range(120)]
#    inferior_values2=[]
#    for i in range(120):
#        success=0
#        fails=0
#        for j in range(len(pos3)):
#            if not np.isinf(pos3[j]):
#                if pos3[j]<d_abs2[i]:
#                    success+=1
#        for j in range(len(pos4)):
#            if not np.isinf(pos4[j]):
#                if pos4[j]<d_abs2[i]:
#                    fails+=1
#        #print('inf to :', i*0.2)
#        #print(success,fails)
#        #print(round(success/len(pos1),2),round(fails/len(pos2),2),round(success/(fails+success),2)*100)
#        
#        inferior_values2.append(success/(fails+success)*100)
    
    fig,ax2=plt.subplots()
    plt.plot(d_abs,inferior_values)
    plt.xlabel(r'$\delta_{d}^*(0)$ inferior to [feet]')
    plt.ylabel('Three point shooting percentage')
    ax2.tick_params(direction='in')
    plt.xlim(d_abs[0],d_abs[-1])
    plt.ylim(min(inferior_values),inferior_values[-1]+1)
    plt.vlines(d_abs[10], inferior_values[0], inferior_values[10], linestyle="dashed",lw=0.5)
    plt.hlines(inferior_values[10], d_abs[0], d_abs[10], linestyle="dashed",lw=0.5)
    plt.vlines(d_abs[50], inferior_values[0], inferior_values[50], linestyle="dashed",lw=0.5)
    plt.hlines(inferior_values[50], d_abs[0], d_abs[50], linestyle="dashed",lw=0.5)
    plt.show()
#    plt.plot(d_abs2,inferior_values2)
    #fig = plt.figure(4)
    #sns.kdeplot(np.array(pos1),bw=0.2)
    #sns.kdeplot(np.array(pos2),bw=0.2)
   # plt.show()
    #plt.plot(S, label='success')
    #plt.plot(T, label='fails')
    #plt.legend()