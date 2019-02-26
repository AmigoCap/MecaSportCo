
# Fonctions

Cette section vise à expliquer le rôle de chaque fonction. 

### distance(a,b)
Renvoie la distance entre deux points A (*a*) et B (*b*).
a et b sont des couples de positions (i,j). 

### barycentre(moment,i)
Renvoie le barycentre de l'équipe *i* pour le moment *moment*.

### who_attack(moments,i)
Renvoie l'indice de l'équipe qui attaque au moment *moments[i]*.

### where_attack(moments,j)
Renvoie le côté duquel l'action a lieu au moment *moments[j]$.

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

### detect_shoot(moments,i,players)

### test_detect_shoot(moments)

### time_to_point(F,a,b,v)

### calcul_aire_un_joueur(moments,j,n,F,player,players)

### three_points(moments,i,who_ball)

### distance_closest_player(moments,i,player,index_player,F,players)

### test_moment(moment)

### track_shoot_event(event)

### track_shoot_match(data,match)
