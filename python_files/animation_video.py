#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:38:43 2019

@author: gabin
"""

import cv2
import matplotlib.pyplot as plt
import space as sp
from data_extracter import json_extracter

print('Récupération de la vidéo frame par frame')
# Récupérer la vidéo frame par frame
#vidcap = cv2.VideoCapture('../data/video.mp4')
#fps = vidcap.get(cv2.CAP_PROP_FPS) # getting video framerate
#success,image = vidcap.read()
#count = 0
#success = True
#while success:
#    cv2.imwrite("video_test_frames/frame%d.jpg" % count, image,[int(cv2.IMWRITE_JPEG_QUALITY), 90])     # save frame as JPEG file
#    success,image = vidcap.read()
#    #print ('Read a new frame: ', success)
#    count += 1
    
print('Tracé animation frame par frame')
data,events=json_extracter('../data/game1.json')
moments=events[0]['moments']
# Tracer frame par frame de l'animation
for k in range(len(moments)):
    fig, ax = plt.subplots(1,1,figsize=(15,8)) # rajouter autant d'axes que souhaité et ajuster figsize
    
    sp.animation_print_court_teams_occupation_inertia(fig,ax,events,0,k,voronoi_cut=False,player_info=False,n=50,p=94)

    plt.savefig('../animation_frames/frame%d.jpg' % k)
    plt.clf()
    
print('écriture de la vidéo')
# création vidéo à partir des frames précédentes

## taille des images
img=cv2.imread('animation_frames/frame1.jpg')
height, width, channels = img.shape

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
video = cv2.VideoWriter('../data/video.avi', fourcc, float(fps), (width, height)) # mettre le chemin où on souhaite enregistrer l'animation

for i in range(count):
    frame = cv2.imread('animation_frames/frame%d.jpg' % i)
    video.write(frame)
video.release()