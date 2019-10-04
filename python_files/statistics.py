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

def moyenne_list(l):
    n=len(l)
    return(sum(l)/n)

def moyenne_list_list(l,time_abs,times):
    L=[]
    M=[]
    n=len(l)
    ### creating a dictionnary for each shot which associates time before shoot to the value of pressure at this time ###
    for k in range(n):
        L.append(dict(zip(time_abs[k],l[k])))
    
    ### for each value of time taking the mean of pressure ###
    values=[] # we stock all the values to plot errorbars
    times_values=[] # time associated to values
    for t in times:
        m=0
        number=0
        for k in range(n):
            for t2 in L[k].keys():
                if abs(t-t2)<0.04:
            #if t in L[k].keys():
                    if not np.isinf(L[k][t2]):
                        values.append(L[k][t2])
                        times_values.append(t)
                        m+=L[k][t2]
                        number+=1
                        
        M.append(m/number)
        
    return[M,times,values,times_values]

def arrondi_04(row):
    number=row['Time']
    return(int(number)+(number-int(number))//0.04*0.04)

def shot_type(row):
    if row['Time_to_shoot']>-2:
        return('catch-and-shoot')
    else :
        return('pull-up')
    
def shooting_efficiency_inferior(data,t1):
    
    D_CLOSEST_PLAYER=data['D_CLOSEST_DEF']
    T_CLOSEST_PLAYER=data['T_CLOSEST_DEF']
    TIME=data['TIME_ABSCISSE']
    TIME_TO_SHOOT=data['TIME_TO_SHOOT']
    
    D_CLOSEST_PLAYER1=[]
    D_CLOSEST_PLAYER2=[]
    T_CLOSEST_PLAYER1=[]
    T_CLOSEST_PLAYER2=[]
    TIME1=[]
    TIME2=[]
    
    
    for k in range(len(D_CLOSEST_PLAYER)):
        if (np.array(TIME[k][1]).round(0)!=np.array([0]*len(TIME[k][1]))).all:
            if TIME_TO_SHOOT[k][1]>-2:
                if D_CLOSEST_PLAYER[k][0]==1:
                    D_CLOSEST_PLAYER1.append(D_CLOSEST_PLAYER[k][1])
                    T_CLOSEST_PLAYER1.append(T_CLOSEST_PLAYER[k][1])
                    TIME1.append(np.array(TIME[k][1]))
                else :
                    D_CLOSEST_PLAYER2.append(D_CLOSEST_PLAYER[k][1])
                    T_CLOSEST_PLAYER2.append(T_CLOSEST_PLAYER[k][1])
                    TIME2.append(np.array(TIME[k][1]))
            
            
   # print(len(D_CLOSEST_PLAYER2)+len(D_CLOSEST_PLAYER1))
    closest1=[]
    pos1=[]
    closest2=[]
    pos2=[]
    a=0
    b=0
    c=[]
    for i in range(len(D_CLOSEST_PLAYER1)):
        j=0
        while j<len(TIME1[i])-1 and abs(TIME1[i][j]-t1)>0.03:
            j+=1
        if abs(TIME1[i][j]-t1)<=0.03:
            b+=1
            closest1.append(T_CLOSEST_PLAYER1[i][j])
            pos1.append(D_CLOSEST_PLAYER1[i][j])
        
        else :
            c.append(TIME1[i])
                
    for i in range(len(D_CLOSEST_PLAYER2)):
        j=0
        while j<len(TIME2[i])-1 and abs(TIME2[i][j]-t1)>0.03:
            j+=1
        if abs(TIME2[i][j]-t1)<=0.03:
            b+=1
            closest2.append(T_CLOSEST_PLAYER2[i][j])
            pos2.append(D_CLOSEST_PLAYER2[i][j])
    
    
    print(len(pos1)+len(pos2),a+b,len(closest1)+len(closest2))
    print(len(D_CLOSEST_PLAYER1)+len(D_CLOSEST_PLAYER2))
    print(len(T_CLOSEST_PLAYER1)+len(T_CLOSEST_PLAYER2))
    
    inferior_values=[]
    time_abs=[0.025*i+0.2 for i in range(70)]
    S1=[]
    T1=[]
    for i in range(70):
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
    
    print(success+fails,len(closest1)/(len(closest1)+len(closest2)))
    plt.figure(1)
    plt.plot(time_abs,inferior_values)
    plt.figure(2)
    plt.plot(time_abs,S1)
    plt.plot(time_abs,T1)
        
    d_abs=[0.1*i+0.1 for i in range(200)]
    inferior_values=[]
    S=[]
    T=[]
    for i in range(200):
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
                
        #print('inf to :', i)
        #print(success,fails)
        
        inferior_values.append(success/(fails+success)*100)
        
    plt.figure(3)
    plt.plot(d_abs,inferior_values)
    fig = plt.figure(4)
    plt.plot(S, label='success')
    plt.plot(T, label='fails')
    plt.legend()
    return(c)
    
def shooting_efficiency_inferior_bis(data,t1):
    
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
    D_CLOSEST_PLAYER1_catch=[]
    D_CLOSEST_PLAYER2_catch=[]
    T_CLOSEST_PLAYER1_catch=[]
    T_CLOSEST_PLAYER2_catch=[]
    TIME1_catch=[]
    TIME2_catch=[]
    D_CLOSEST_PLAYER1_pull=[]
    D_CLOSEST_PLAYER2_pull=[]
    T_CLOSEST_PLAYER1_pull=[]
    T_CLOSEST_PLAYER2_pull=[]
    TIME1_pull=[]
    TIME2_pull=[]
    for k in range(len(D_CLOSEST_PLAYER)):
        ## success ##
        if D_CLOSEST_PLAYER[k][0]==1:
            
            # all shots #
            D_CLOSEST_PLAYER1.append(D_CLOSEST_PLAYER[k][1])
            T_CLOSEST_PLAYER1.append(T_CLOSEST_PLAYER[k][1])
            TIME1.append(np.array(TIME[k][1]))
            
            # CnS #
            if TIME_TO_SHOOT[k][1]>-2: 
                D_CLOSEST_PLAYER1_catch.append(D_CLOSEST_PLAYER[k][1])
                T_CLOSEST_PLAYER1_catch.append(T_CLOSEST_PLAYER[k][1])
                TIME1_catch.append(np.array(TIME[k][1]))
                
            # pull-up shots #
            else :
                D_CLOSEST_PLAYER1_pull.append(D_CLOSEST_PLAYER[k][1])
                T_CLOSEST_PLAYER1_pull.append(T_CLOSEST_PLAYER[k][1])
                TIME1_pull.append(np.array(TIME[k][1]))
                
        ## fails ##
        else :
            
            # all shots #
            D_CLOSEST_PLAYER2.append(D_CLOSEST_PLAYER[k][1])
            T_CLOSEST_PLAYER2.append(T_CLOSEST_PLAYER[k][1])
            TIME2.append(np.array(TIME[k][1]))
            
            # CnS #
            if TIME_TO_SHOOT[k][1]>-2: 
                D_CLOSEST_PLAYER2_catch.append(D_CLOSEST_PLAYER[k][1])
                T_CLOSEST_PLAYER2_catch.append(T_CLOSEST_PLAYER[k][1])
                TIME2_catch.append(np.array(TIME[k][1]))
                
            # pull-up shots #
            else :
                D_CLOSEST_PLAYER2_pull.append(D_CLOSEST_PLAYER[k][1])
                T_CLOSEST_PLAYER2_pull.append(T_CLOSEST_PLAYER[k][1])
                TIME2_pull.append(np.array(TIME[k][1]))
            
    print(len(D_CLOSEST_PLAYER1)/(len(D_CLOSEST_PLAYER2)+len(D_CLOSEST_PLAYER1)))
    closest1=[]
    pos1=[]
    closest2=[]
    pos2=[]
    for i in range(len(D_CLOSEST_PLAYER1)):
        min1=0
        min2=0
        for j in range(len(D_CLOSEST_PLAYER1[i])):
            if t1<TIME1[i][j]<0.04:
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
            if t1<TIME2[i][j]<0.04:
                if T_CLOSEST_PLAYER2[i][j]<min1:
                    min1=T_CLOSEST_PLAYER2[i][j]
                if D_CLOSEST_PLAYER2[i][j]<min2:
                    min2=D_CLOSEST_PLAYER2[i][j]
        closest2.append(min1)
        pos2.append(min2)
    
    ### 1 second before ###
#    closest3=[]
#    pos3=[]
#    closest4=[]
#    pos4=[]
#    for i in range(len(D_CLOSEST_PLAYER1)):
#        min1=np.inf
#        min2=np.inf
#        for j in range(len(D_CLOSEST_PLAYER1[i])):
#            if -1.04<TIME1[i][j]<-0.96:
#                if T_CLOSEST_PLAYER1[i][j]<min1:
#                    min1=T_CLOSEST_PLAYER1[i][j]
#                if D_CLOSEST_PLAYER1[i][j]<min2:
#                    min2=D_CLOSEST_PLAYER1[i][j]
#        closest3.append(min1)
#        pos3.append(min2)
#                
#    for i in range(len(D_CLOSEST_PLAYER2)):
#        min1=np.inf
#        min2=np.inf
#        for j in range(len(D_CLOSEST_PLAYER2[i])):
#            if -1.04<TIME2[i][j]<-0.96:
#                if T_CLOSEST_PLAYER2[i][j]<min1:
#                    min1=T_CLOSEST_PLAYER2[i][j]
#                if D_CLOSEST_PLAYER2[i][j]<min2:
#                    min2=D_CLOSEST_PLAYER2[i][j]
#        closest4.append(min1)
#        pos4.append(min2)
#    
#    print(len(pos1)+len(pos2),len(pos3)+len(pos4))
#    print(len(D_CLOSEST_PLAYER1)+len(D_CLOSEST_PLAYER2))
#    print(len(T_CLOSEST_PLAYER1)+len(T_CLOSEST_PLAYER2))
    
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
    
    
    ### 1 second before ###
    
#    inferior_values2=[]
#    time_abs2=[0.02*i+0.2 for i in range(60)]
#    for i in range(60):
#        success=0
#        fails=0
#        for j in range(len(closest3)):
#            if not np.isinf(closest3[j]):
#                if closest3[j]<time_abs2[i]:
#                    success+=1
#        for j in range(len(closest4)):
#            if not np.isinf(closest4[j]):
#                if closest4[j]<time_abs2[i]:
#                    fails+=1
#                
#        #print('inf to :', i)
#        #print(success,fails)
#        
#        inferior_values2.append(success/(fails+success)*100)
#    
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
    
def shooting_efficiency_superior_bis(data,t1):
    
    D_CLOSEST_PLAYER=data['D_CLOSEST_DEF']
    T_CLOSEST_PLAYER=data['T_CLOSEST_DEF']
    TIME=data['TIME_ABSCISSE']
    TIME_TO_SHOOT=data['TIME_TO_SHOOT']
    
    D_CLOSEST_PLAYER1=[]
    D_CLOSEST_PLAYER2=[]
    T_CLOSEST_PLAYER1=[]
    T_CLOSEST_PLAYER2=[]
    TIME1=[]
    TIME2=[]
    
    
    for k in range(len(D_CLOSEST_PLAYER)):
        #if TIME_TO_SHOOT[k][1]>-2:
        if D_CLOSEST_PLAYER[k][0]==1:
            D_CLOSEST_PLAYER1.append(D_CLOSEST_PLAYER[k][1])
            T_CLOSEST_PLAYER1.append(T_CLOSEST_PLAYER[k][1])
            TIME1.append(np.array(TIME[k][1]))
        else :
            D_CLOSEST_PLAYER2.append(D_CLOSEST_PLAYER[k][1])
            T_CLOSEST_PLAYER2.append(T_CLOSEST_PLAYER[k][1])
            TIME2.append(np.array(TIME[k][1]))
            
    print(len(D_CLOSEST_PLAYER1)/(len(D_CLOSEST_PLAYER2)+len(D_CLOSEST_PLAYER1)))
    closest1=[]
    pos1=[]
    closest2=[]
    pos2=[]
    for i in range(len(D_CLOSEST_PLAYER1)):
        max1=np.inf
        max2=np.inf
        for j in range(len(D_CLOSEST_PLAYER1[i])):
            if t1<TIME1[i][j]<0.04:
                if T_CLOSEST_PLAYER1[i][j]<max1:
                    max1=T_CLOSEST_PLAYER1[i][j]
                if D_CLOSEST_PLAYER1[i][j]<max2:
                    max2=D_CLOSEST_PLAYER1[i][j]
        closest1.append(max1)
        pos1.append(max2)
                
    for i in range(len(D_CLOSEST_PLAYER2)):
        max1=np.inf
        max2=np.inf
        for j in range(len(D_CLOSEST_PLAYER2[i])):
            if t1<TIME2[i][j]<0.04:
                if T_CLOSEST_PLAYER2[i][j]<max1:
                    max1=T_CLOSEST_PLAYER2[i][j]
                if D_CLOSEST_PLAYER2[i][j]<max2:
                    max2=D_CLOSEST_PLAYER2[i][j]
        closest2.append(max1)
        pos2.append(max2)
    
    inferior_values=[]
    time_abs=[0.02*i for i in range(60)]
    S1=[]
    T1=[]
    for i in range(60):
        success=0
        fails=0
        for j in range(len(closest1)):
            if not np.isinf(closest1[j]):
                if closest1[j]>time_abs[i]:
                    success+=1
        for j in range(len(closest2)):
            if not np.isinf(closest2[j]):
                if closest2[j]>time_abs[i]:
                    fails+=1
        S1.append(success/len(closest1))
        T1.append(fails/len(closest2))
                
        #print('inf to :', i)
        #print(success,fails)
        
        inferior_values.append(success/(fails+success)*100)
#    
    fig,ax1=plt.subplots()
    plt.plot(time_abs,inferior_values)
    plt.xlabel(r'$\delta_{t}^*(0)$ inferior to [s]')
    plt.ylabel('Three point shooting percentage')
#    plt.vlines(time_abs[15], 19, inferior_values[15], linestyle="dashed",lw=0.5)
#    plt.hlines(inferior_values[15], 0, time_abs[15], linestyle="dashed",lw=0.5)
#    plt.xlim(0.2,time_abs[-1])
#    plt.ylim(19,inferior_values[-1]+1)
#    ax1.tick_params(direction='in')
    plt.show()
#    plt.plot(time_abs2,inferior_values2)
    #plt.figure(2)
    #plt.plot(time_abs,S1)
    #plt.plot(time_abs,T1)
        
    d_abs=[0.1*i for i in range(120)]
    inferior_values=[]
    S=[]
    T=[]
    for i in range(120):
        success=0
        fails=0
        for j in range(len(pos1)):
            if not np.isinf(pos1[j]):
                if pos1[j]>d_abs[i]:
                    success+=1
        for j in range(len(pos2)):
            if not np.isinf(pos2[j]):
                if pos2[j]>d_abs[i]:
                    fails+=1
        S.append(success/len(pos1))
        T.append(fails/len(pos2))
                
        #print('inf to :', i*0.2)
        #print(success,fails)
        #print(round(success/len(pos1),2),round(fails/len(pos2),2),round(success/(fails+success),2)*100)
        
        inferior_values.append(success/(fails+success)*100)
        

    
    fig,ax2=plt.subplots()
    plt.plot(d_abs,inferior_values)
    plt.xlabel(r'$\delta_{d}^*(0)$ inferior to [feet]')
    plt.ylabel('Three point shooting percentage')
#    ax2.tick_params(direction='in')
#    plt.xlim(3,d_abs[-1])
#    plt.ylim(inferior_values[0],inferior_values[-1]+1)
#    plt.vlines(d_abs[10], inferior_values[0], inferior_values[10], linestyle="dashed",lw=0.5)
#    plt.hlines(inferior_values[10], 3, d_abs[10], linestyle="dashed",lw=0.5)
#    plt.vlines(d_abs[50], inferior_values[0], inferior_values[50], linestyle="dashed",lw=0.5)
#    plt.hlines(inferior_values[50], 3, d_abs[50], linestyle="dashed",lw=0.5)
    plt.show()
    
#D_CLOSEST_PLAYER=dico['D_CLOSEST_DEF']
#T_CLOSEST_PLAYER=dico['T_CLOSEST_DEF']
#
#nb_inf_D=0
#nb_inf_T=0
#for i in range(len(D_CLOSEST_PLAYER)):
#    for j in range(len(D_CLOSEST_PLAYER[i])):
#        if np.isinf(D_CLOSEST_PLAYER[i][1][j]):
#            nb_inf_D+=1/len(D_CLOSEST_PLAYER[i])
#        if np.isinf(T_CLOSEST_PLAYER[i][1][j]):
#            nb_inf_T+=1/len(D_CLOSEST_PLAYER[i])
#
#import seaborn as sns
#ax = sns.kdeplot(np.array(dico['TIME_TO_SHOOT'])[:,1])
#ax.set_xlim(-2.5,None)
#plt.show()
#
#D_CLOSEST_PLAYER=dico['D_CLOSEST_DEF']
#T_CLOSEST_PLAYER=dico['T_CLOSEST_DEF']
#TIME=dico['TIME_ABSCISSE']
#TIME_TO_SHOOT=dico['TIME_TO_SHOOT']
#
#maximums1=[]
##maximums2=[]
#a=0
#for k in range(len(D_CLOSEST_PLAYER)):
#    if TIME_TO_SHOOT[k][1]>-1.5:
#        a+=1
#print(a,len(D_CLOSEST_PLAYER))
#    if TIME[k][1][0]==0 and TIME[k][1][-1]==0:
#        a+=1
#    for i in range(len(D_CLOSEST_PLAYER[k][1])):
#    #if max(D_CLOSEST_PLAYER[k][1])>50:
#        #if abs(TIME[k][1][i]-60)<10:
#        plt.plot(TIME[k][1],D_CLOSEST_PLAYER[k][1])
#        plt.show()
#            #if TIME[k][0]==1:
#            #    maximums1.append(D_CLOSEST_PLAYER[k][1][i])
#            #else :
#              #  maximums2.append(D_CLOSEST_PLAYER[k][1][i])
#        #print(TIME_TO_SHOOT[k][1])
#        #plt.plot(TIME[k][1],D_CLOSEST_PLAYER[k][1])
#        #plt.show()
#ax = sns.kdeplot(np.array(maximums1))
#ax = sns.kdeplot(np.array(maximums2))
#plt.show()
#print(np.mean(maximums1),np.std(maximums1),len(maximums1))
#print(np.mean(maximums2),np.std(maximums2),len(maximums2))