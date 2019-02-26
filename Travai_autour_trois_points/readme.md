
# Fonctions

Cette section vise à expliquer le rôle de chaque fonction. 

> Sommaire 
- [distance(a,b)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#distanceab)
- [barycentre(moment,i)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#barycentremomenti)
- [who_attack(moments,i)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#who_attackmomentsi)
- [where_attack(moments,j)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#where_attackmomentsj)
- [att_def_ball_pos(moments,j)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#att_def_ball_posmomentsj)
- [players_ball(moments,j)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#players_ballmomentsj)
- [voronoi(moments,j)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#voronoimomentsj)
- [print_court(moments,i)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#print_courtmomentsi)
- [player_with_ball(moments,i)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#print_courtmomentsi)
- [basket_direction(player,where_attack)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#player_with_ballmomentsi)
- [detect_shoot(moments,i,players)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#basket_directionplayerwhere_attack)
- [time_to_point(F,a,b,v)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#detect_shootmomentsiplayers)
- [calcul_aire_un_joueur(moments,j,n,F,player,players)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#distance_closest_playermomentsiplayerindex_playerfplayers)
- [three_points(moments,i,who_ball)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#three_pointsmomentsiwho_ball)
- [distance_closest_player(moments,i,player,index_player,F,players)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#distance_closest_playermomentsiplayerindex_playerfplayers)
- [track_shoot_event(event)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#track_shoot_eventevent)
- [track_shoot_match(data,match)](https://github.com/AmigoCap/MecaFootCo/blob/master/Travai_autour_trois_points/readme.md#track_shoot_matchdatamatch) 

### distance(a,b)
Renvoie la distance entre deux points A (*a*) et B (*b*).
a et b sont des couples de positions (i,j). 

### barycentre(moment,i)
Renvoie le barycentre de l'équipe *i* pour le moment *moment*.

### who_attack(moments,i)
Renvoie l'indice de l'équipe qui attaque au moment *moments[i]*.

### where_attack(moments,j)
Renvoie le côté duquel l'action a lieu au moment *moments[j]*.

### att_def_ball_pos(moments,j)
Renvoie les listes *att_pos*, *def_pos*, *ball* définies au moment *moments[j]*.

### players_ball(moments,j)
Renvoie *players_ball* la liste qui contient la liste de la position, la vitesse et la hauteur du ballon et les listes de la position et de la vitesse pour chaque joueur. 

### voronoi(moments,j)
Trace le diagramme de Voronoï.

### print_court(moments,i)
Trace le terrain ainsi que l'occupation de l'espace selon le modèle utilisant la force *F*.

### player_with_ball(moments,i)
Renvoie qui possède la balle au moment *moments[i]* ou 0 si la balle est en transit.

### basket_direction(player,where_attack)
Renvoie le couple de vecteurs des directions entre *player* (joueur ou ballon) et les extrémités de la planche.

### detect_shoot(moments,i,players)
Renvoie *True* ou *False* selon si le moment *moments[i]* correspond à un tir ou non.

### time_to_point(F,a,b,v)
Renvoie le temps nécessaire pour aller du point A (*a*) au point B (*b*) avec une vitesse initiale *v* en étant attiré par une force de norme *F* dont la direction minimise ce temps.

### calcul_aire_un_joueur(moments,j,n,F,player,players)
Renvoie l'aire d'un joueur 

### three_points(moments,i,who_ball)
Renvoie *True* ou *False* selon que le moment *moments[i]* corresponde à un tir à 3 points.

### distance_closest_player(moments,i,player,index_player,F,players)

### track_shoot_event(event)

### track_shoot_match(data,match)
