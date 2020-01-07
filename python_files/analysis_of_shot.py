#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:14:53 2019

@author: gabin
"""

import ast
import pandas as pd
import matplotlib.pyplot as plt
#
#df_shots=pd.read_csv('/Users/gabin/Ordinateur/Documents/CENTRALE_LYON_1A/PaR/MecaFootCo/data/df_shots.csv',index_col=[0],converters={1:ast.literal_eval,2:ast.literal_eval,3:ast.literal_eval,7:ast.literal_eval,8:ast.literal_eval,9:ast.literal_eval,17:ast.literal_eval,18:ast.literal_eval,19:ast.literal_eval,20:ast.literal_eval})

#df_shots_thompson=df_shots.query('player_id==202691')

def plot_shot(df_shots,l,players):
    for j in l:
        #print(df_shots.query('shot_id==@j').index[0])
        #i=df_shots.query('shot_id==@j').index[0]
        i=j
        print(df_shots.iloc[i]['shot_id'])
        Time=df_shots.iloc[i]['Time']
        D=df_shots.iloc[i]['D']
        T=df_shots.iloc[i]['T']
        tts=df_shots.iloc[i]['release_time']
        player_id=df_shots.iloc[i]['player_id']
        c=df_shots.iloc[i]['clock']
        print(i,df_shots.iloc[i]['Match_id'],df_shots.iloc[i]['quarter'],str(c//60)+'m '+str(c%60),player_id,df_shots.iloc[i]['Shot_type'],tts,df_shots.iloc[i]['Shot_result'])
        plt.show()
        
def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / N

def plot_shot_bis(df_shots,j,players):
    fig, ax = plt.subplots(1, 1,figsize=(2,1.5))
    print(df_shots.query('shot_id==@j'))
    print(df_shots.query('shot_id==@j').index[0])
    #df_shots.reset_index(inplace=True)
    i=df_shots.query('shot_id==@j').index[0]
    #print(df_shots.iloc[i])
    Time=df_shots.iloc[i]['Time']
    D=df_shots.iloc[i]['D']
    T=df_shots.iloc[i]['T']
    tts=df_shots.iloc[i]['release_time']
    player_id=df_shots.iloc[i]['player_id']
    c=df_shots.iloc[i]['clock']
    print(c)
    print(i,df_shots.iloc[i]['Match_id'],df_shots.iloc[i]['quarter'],str(c//60)+'m '+str(c%60),player_id,df_shots.iloc[i]['Shot_type'],tts,df_shots.iloc[i]['Shot_result'])
    ax.axvline(tts, color='black',linestyle="dashed",lw=1)
    ax.axvline(0, color='black',linestyle="dashed",lw=1)
    print(Time[T.index(min(T))]-Time[D.index(min(D))])
    #ax2.axvline(tts, color='black',linestyle="dashed",lw=1)
    ax2 = ax.twinx()
    #ax2.hlines(y=T[Time.index(0)], xmin=0, xmax=0.8, color='red',linestyle="dashed",lw=0.5)
    #ax.hlines(y=D[Time.index(0)], xmin=-3, xmax=0, color='blue',linestyle="dashed",lw=0.5)
    ax.plot(Time,D,'b-')
    ax2.plot(Time[:-4],running_mean(T,5),'r-')
    ax.set_xlabel('times [s]',fontsize='large')
    ax.set_ylabel(r'$\delta_{space}^*(t)$ [feets]', color='r',fontsize='large')
    ax2.set_ylabel(r'$\delta_{time}^*(t)$ [s]', color='b',fontsize='large')
    ax.set_xlim((-3,0.8))
    ax.set_ylim((0,11))
    ax2.set_ylim((0,0.9))
    #ax2.set_xlim((-3.2,0.8))
    #ax2.set_ylim((0,2))
    #ax3.plot(list(df_shots.iloc[i]['d_basket']),df_shots.iloc[i]['z_ball'])
    #ind=Time.index(0)
    #ind2=list(np.array(Time).round(2)).index(round(tts,2))
    #ax3.plot(df_shots.iloc[i]['d_basket'][ind],df_shots.iloc[i]['z_ball'][ind],'ro')
    #ax3.plot(df_shots.iloc[i]['d_basket'][ind2],df_shots.iloc[i]['z_ball'][ind2],'ko')
    #print(df_shots.iloc[i]['angle'][ind-1])
    #ax4.plot(Time,df_shots.iloc[i]['nb_def'])
    plt.show()