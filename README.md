# MecaSportCo

## Introduction

Today, technology is increasingly used in sport. Indeed, the players' statistics are more and more accurate and more and more numerous. Clubs employ people to acquire data and use it to improve performance. It is in this context that the MecaSportCo Research Application Project, conducted at the **Ecole Centrale de Lyon** by *Gabin Rolland* and *Nathan Rivière*, under the supervision of *Wouter Bos* and *Romain Vuillemot*. 

The aim of this study is to quantify how "free" a basketball player is and how this influences his 3-points shot performance.

## Data

The dataset we use is derived from ***Stats*** company data and *SportsVU* technology. These are the 632 men's basketball games in the NBA between the 2013-2014 and 2016-2017 seasons. For each match we have the movement data for the ball and players taken 25 times per second and stored in the form _JavaScript Object Notation_ (JSON). The following figure shows the general structure of the data:  
![dataschema](https://github.com/AmigoCap/MecaFootCo/blob/master/Images/data.jpg "data schema")

## Work performed

* [1_Introduction_to_space_occupation](https://nbviewer.jupyter.org/github/AmigoCap/MecaFootCo/blob/master/1_Introduction_to_space_occupation.ipynb)
* [2_time_calculation](https://nbviewer.jupyter.org/github/AmigoCap/MecaFootCo/blob/master/2_Time_calculation.ipynb) where we detail a way to model players'trajectories and how to calcul time needed for a player to go from a point a to b with a given initial velocity.
* [3_Comparison_of_ways_to_quantify_free_space](https://nbviewer.jupyter.org/github/AmigoCap/MecaFootCo/blob/master/3_Comparison_of_ways_to_quantify_free_space.ipynb) in which the comparison of occupancy calculations is taken further and in which a new way to quantify how "free" a player is is introduced.
* [4_Free_space_and_3-points_efficiency](https://nbviewer.jupyter.org/github/AmigoCap/MecaFootCo/blob/master/4_Free_space_and_3-points_efficiency.ipynb) in which we focus on 3-points shot and the link between efficiency and free-space.

## Bibliography

