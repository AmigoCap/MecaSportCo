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


#dico=pickle.load(open('../data/Shots_663','rb'))

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
        if SHOT_RESULT[k][0]==1:
            
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



def shooting_efficiency_inferior_one_player(data):
    
    ### getting the data ###
#    D_CLOSEST_PLAYER=data['D_CLOSEST_DEF']
#    T_CLOSEST_PLAYER=data['T_CLOSEST_DEF']
#    TIME=data['TIME_ABSCISSE']
#    TIME_TO_SHOOT=data['TIME_TO_SHOOT']
    
    data1=data.query('player_id==201939')
    D_CLOSEST_PLAYER=data1['D'].tolist()
    T_CLOSEST_PLAYER=data1['T'].tolist()
    TIME=data1['Time'].tolist()
    SHOT_RESULT=data1['Shot result'].tolist()
    
    ### differentiating catch-and-shoot, pull-up shots and success and fails ###
    D_CLOSEST_PLAYER1=[]
    D_CLOSEST_PLAYER2=[]
    T_CLOSEST_PLAYER1=[]
    T_CLOSEST_PLAYER2=[]
    TIME1=[]
    TIME2=[]

    for k in range(len(D_CLOSEST_PLAYER)):
        ## success ##
        if SHOT_RESULT[k]==1:
            
            # all shots #
            D_CLOSEST_PLAYER1.append(D_CLOSEST_PLAYER[k])
            T_CLOSEST_PLAYER1.append(T_CLOSEST_PLAYER[k])
            TIME1.append(np.array(TIME[k]))
                
        ## fails ##
        else :
            
            # all shots #
            D_CLOSEST_PLAYER2.append(D_CLOSEST_PLAYER[k])
            T_CLOSEST_PLAYER2.append(T_CLOSEST_PLAYER[k])
            TIME2.append(np.array(TIME[k]))
            
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
    #plt.xlim(time_abs[0],time_abs[-1])
    #plt.ylim(inferior_values[0],inferior_values[-1]+1)
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
    #plt.xlim(d_abs[0],d_abs[-1])
    #plt.ylim(min(inferior_values),inferior_values[-1]+1)
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



def restructure_data(data):
    
    ### getting the data ###
    D_CLOSEST_PLAYER=data['D_CLOSEST_DEF']
    T_CLOSEST_PLAYER=data['T_CLOSEST_DEF']
    TIME=data['TIME_ABSCISSE']
    TIME_TO_SHOOT=data['TIME_TO_SHOOT']
    
    ### only the second column because the first one contains if it is a succes or a miss ###
    D_CLOSEST_PLAYER_bis=[]
    T_CLOSEST_PLAYER_bis=[]
    TIME_bis=[]
    TIME_TO_SHOOT_bis=[]
    SUCCESS=[]
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
    
    ### put the data into a dataframe ###
    df=pd.DataFrame({'D':D_CLOSEST_PLAYER_bis,'T':T_CLOSEST_PLAYER_bis,'Time':TIME_bis,'Time_to_shoot':TIME_TO_SHOOT_bis,'Shot result':SUCCESS})
    
    ## only evolution between 3.2 seconds before shot and 0.8 second after. (It is because there are some errors in the data) ##
    df=df.query('Time>-3.2 and Time<0.8').copy()
    
    return(df)