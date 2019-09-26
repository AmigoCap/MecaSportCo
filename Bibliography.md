# Bibliography

## Subject definition

- Définition des critères de performance. L'article [1] définit et classe les différents indicateurs qui permettent de caractériser les perfomances au football. Il définit en particulier les variables relatives aux passes qui sont le sujet de notre recherche (nombre, précision, type de passe, zones de passe, interceptions). On pourra s'inspirer de cette démarche pour définir les variables caractérisant les passes au Basket. 

[1] « Performance analysis », footballscience.net | Soccer, Football, Training, Testing, Recovery, Injury Prevention, Conditioning and other interesting topics. [En ligne]. Disponible sur: http://www.footballscience.net/special-topics/performance-analysis/. [Consulté le: 02-déc-2018].

## Data

Les données sont composées de 632 matchs de Basket de NBA lors de la saison 2015. Pour chaque match nous disposons de la position des joueurs de chaque équipe et du ballon au format json. Ces données sont stockées par "moments" qui contiennent chacun une phase de jeu du match. Il est possible de récupérer le flux vidéo associé à chaque moment à l'adresse https://stats.nba.com/schedule/.
Les deux liens [2] et [3] expliquent comment sont organisées les données de chaque match et comment faire un début d'exploitation de celles-ci sous python.

[2]	S. Tjortjoglou, « How to Track NBA Player Movements in Python », Savvas Tjortjoglou, 25-août-2015. [En ligne]. Disponible sur: http://savvastjortjoglou.com/nba-play-by-play-movements.html. [Consulté le: 28-oct-2018].

[3]	« Exploring NBA SportVu Movement Data ». [En ligne]. Disponible sur: http://projects.rajivshah.com/sportvu/EDA_NBA_SportVu.html. [Consulté le: 28-oct-2018].

## Visualisation des données

### Généralités

La visualisation de données sportives peut prendre de nombreuses formes différentes. On peut représenter sous forme de graphique les statistiques de joueurs pour comparer leur performance sur différents critères. Cette représentation ne fait que restituer les informations qu’apporte les données brutes. On peut présenter ces données de manière plus concrètes en affichant des graphiques superposés au terrain de sport. Enfin il est également possible de visualiser les données directement sur les vidéos des phases de jeu concernées afin de faire un lien concret entre données et phase de jeu. L'article [4] fait un état de l'art détaillé de tous les travaux déjà réalisés autour de l'analyse de données sportives. 

[4] C. Perin, R. Vuillemot, C. D. Stolper, J. T. Stasko, J. Wood, et S. Carpendale, « State of the Art of Sports Data Visualization », Computer Graphics Forum, vol. 37, juin 2018.

### SoccerStories

SoccerStories est une interface permettant de visualiser certaines phases de match de football. Cette interface peut s’avérer très utile en prenant en compte le fait que les données sous leur forme pure parlent peu. L’interviews d’experts confirment cette remarque puisque celles-ci révèlent que dans l’analyse du football il ne faut pas oublier le côté visuel et sélection de phases de jeu qui permettent de raconter une histoire. Nous pouvons tirer plusieurs inspirations de cette interface notamment les différents critères et curseurs présentés en les adaptant à nos propres critères ainsi que les différentes démarchent présentées dans l’article (interview d’experts, phase d’évaluation, description du sport…)

[5] C. Perin, R. Vuillemot, et J.-D. Fekete, « SoccerStories: A Kick-off for Visual Soccer Analysis », IEEE Transactions on Visualization and Computer Graphics, vol. 19, no 12, p. 2506‑2515, déc. 2013.

### BKViz

BKViz [6] est une interface d'analyse de données au Basket qui regroupe un grand nombre d'outils d'analyses différents. Ainsi l'apport de cet outil réside dans le fait qu'il permet de naviguer entre les différentes données disponibles et les différents outils d'analyse d'une manière simple et efficace. 

[6] A. G. Losada, R. Therón, et A. Benito Santos, « BKViz: A Basketball Visual Analysis Tool », IEEE Computer Graphics and Applications, vol. 36, p. 58‑68, nov. 2016.

### CourtVision

CourtVision [7] est un outil d'analyse pour la NBA qui permet de comparer visuellement les perfomances au shoots des différents joueurs de Basket. Il permet également de mettre en évidence les différents zones stratégiques pour les shoots sur un terrain de Basket.

[7] K. Goldsberry, « CourtVision: New Visual and Spatial Analytics for the NBA », p. 7, 2012.

### Combiner vidéo et analyse des données 

L'article 6 détaille l'importance de combiner données et vidéos tout en indiquant différentes méthodes pour réaliser ceci. 

[8] M. Stein et al., « Bring It to the Pitch: Combining Video and Movement Data to Enhance Team Sport Analysis », IEEE Transactions on Visualization and Computer Graphics, vol. 24, no 1, p. 13‑22, janv. 2018.

## Modèle d'analyse des données

### Autour de la prédiction 

- L'article [9] présente une nouvelle métrique qui permet de caractériser une situation donnée en terme de possibilité de points marqués suite à cette action. Cette quantité est appelée EPV : Expected Possession Value. Le calcul de l'EPV se fait de manière statistique en prenant en compte une quantité finie de possibilité d'action pour le joueur en possession de la balle : dribbles, passes, shoots... 

[9] D. Cervone, A. D’Amour, L. Bornn, et K. Goldsberry, « Predicting Points and Valuing Decisions in Real Time with NBA Optical Tracking Data », p. 9, 2014.

- L'article [10] détaille la démarche qui a permis d'obtenir une interface visuelle de prédiction de passe (http://projects.yisongyue.com/bballpredict/). Cette interface permet à l'utilisateur de placer lui-même les joueurs et le ballon sur le terrain et à partir de ceci on observe à l'aide de traits plus ou moins épais les probabilités de passe et de tir du joueur en possession de la balle. Le principe du calcul repose sur du machine learning expérimenté sur les données 2012-2013 de SportsVu.

[10] Y. Yue, P. Lucey, P. Carr, A. Bialkowski, et I. Matthews, « Learning Fine-Grained Spatial Models for Dynamic Sports Play Prediction », in 2014 IEEE International Conference on Data Mining, Shenzhen, China, 2014, p. 670‑679.


### Autour de l'occupation d'espace

- L'utilisation de l'espace dans les sports collectifs comme le football est indispensable dans l'élaboration des stratégies par les entraineurs. Les principales clés de l'occupation d'espace sont : **l'intéraction entre joueurs, les zones d'influences des joueurs, les options de passe, les espaces libres**. L'article [11] étudie ces différents aspects en créant un modèle permettant de caractériser la zone d'influence des joueurs en prenant en compte leur vitesse. Á partir de ceci on peut déterminer des zones d'intéractions (intersection des zones d'influences). Les espaces libres sont d'autant plus autant au foot que les joueurs, tous rassemblés, n'occupent qu'une petite partie du terrain à un instant t. **L'article associe à un joueur un espace libre comme étant une zone pour laquelle il a une plus grande probabilité d'arriver en premier** en prenant en compte sa direction, sa vitesse et la distance. En ce qui concerne l'étude des passes, celle-ci est plus difficile puisqu'elle résulte d'un processus de décision complex. L'article soulève plusieurs critères pour caractériser le risque d'une passe : **la vitesse de la passe, la distance, le pression exercée sur les potentiels receveurs, la direction des passes et le fait d'éviter le bloc adverse.** Toutes ces études sont utilisées par l'article [12] qui présente une préocédure d'analyse d'une action en terme de passe. Dans un premier temps il sélectionne les possibilité de passes ayant un intérêt grâce aux critères précédents. Ensuite la procédure consiste à regarder si la passe se fait dans le camp adverse ou non. Puis si la passe est dans le camp adverse il s'agit de prendre en compte l'influence des joueurs adverses. Enfin la dernière phase consiste à analyser ce que les défenseurs auraient pu faire pour empêcher la passe. Une procédure similaire est mise en place pour décrire les passes dans les espaces libres.

[11]	« (PDF) Director’s Cut: Analysis and Annotation of Soccer Matches », ResearchGate. [En ligne]. Disponible sur: https://www.researchgate.net/publication/308756859_Director’s_Cut_Analysis_and_Annotation_of_Soccer_Matches. [Consulté le: 01-nov-2018].

[12] M. Stein et al., « Revealing the Invisible: Visual Analytics and Explanatory Storytelling for Advanced Team Sport Analysis », in 2018 International Symposium on Big Data Visual and Immersive Analytics (BDVA), Konstanz, 2018, p. 1‑9.


- L'article [13] réalise une étude sur l’occupation de l’espace au basket. Elle repose sur l’analogie avec l’échange sur le marché. Le terrain est découpé grâce aux espaces de Voronoï et au sein de chacun de ces espaces l’influence d’un joueur est inversement proportionnelle à la distance à laquelle il se situe. Un principe de base : si un joueur i donne la balle à un joueur j c’est que celui-ci occupe une position mieux placée. Ainsi il devient intéressant d’associer une valeur à chaque espace du terrain en le découpant en cellules. Pour cela ils utilisent “l’inférence bayésienne” à l’aide des données de position des joueurs et de passes. Il remarque que les zones importantes du terrain peuvent varier d’une équipe à une autre. 

[13] D. Cervone, L. Bornn, et K. Goldsberry, « 1 Intro: the Basketball Court is a Real Estate Market », p. 8, 2016.

- L'article [14] réalise une étude sur l’occupation et la génération d’espaces au foot. Dans ce sport, les joueurs ne sont en possession du ballon que 3 minutes, d’où  l’importance du jeu sans ballon. La valeur d’un espace du terrain peut être définie grâce à sa position relativement au ballon, la proximité avec le but adverse et le niveau d’appartenance de l’espace. Pour aller plus loin on peut regarder la vitesse du joueur également. Après avoir défini **la zone d’influence d’un joueur**, (grâce à une densité de probabilité d'une loi gaussienne à deux variables), l’auteur définit **l’état de contrôle d’une zone** par une équipe donnée en comparant à chaque endroit la somme des influences des joueurs d’une équipe avec celle de l’autre équipe. Ensuite l’auteur cherche a donné de **la valeur à une zone du terrain**. Plusieurs critères envisagés : position par rapport à la balle, au but et des autres joueurs. Afin de déterminer une fonction caractéristique de la valeur d’une zone d’influence ils étudient d’abord la somme d’influence de la défense d’une zone en fonction de la position de la balle. Pour cela ils utilisent un feed forward neural network. Une fois la valeur d’une zone déterminée à partir de la position de la balle et des défenseurs il la normalise par la valeur d’une zone vue par rapport à la position du but adverse. Ils se concentrent finalement sur le sens des déplacements des joueurs avec deux critères : SOG (space occupation gain) et SGG (space generation gain). Enfin l’auteur réalise une analyse de ses recherches avec phase de jeu du FC Barcelone.

[14] J. Fernandez, L. Bornn, « Wide Open Spaces: A statistical technique for measuring space creation in professional soccer », p. 19, 2018.

- Beaucoup d'entraîneurs analysent les performances de leur équipe après les matchs. L'article [15] apporte un moyen visuel de description. Il est basé sur trois critères collectifs : **la position du centre de masse, la dispersion de l'équipe (position moyen des joueurs par rapport au CDM, vitesse de dispersion ou de resserrement, distance occupée sur une largeur u terrain) et la synchronisation de l'équipe.** Les critères individuels sont également utilisés mais de manière secondaire. Deux actions sont traitées dans l'article où on peut voir qu'une action de but peut être expliquée par un ou plusieurs de ces critères.

[15] A. Benito Santos, R. Theron, A. Losada, J. E. Sampaio, et C. Lago-Peñas, « Data-Driven Visual Performance Analysis in Soccer: An Exploratory Prototype », Front. Psychol., vol. 9, 2018.

- Dans [16], le comportement collectif des joueurs à l'aide leur trajectoire ainsi que celle de la balle. Plusieurs critères sont définis : **"possible region" (région qu'un objet peut potentiellement atteindre en un temps donné, à partir d'un temps donné t), "catchable region", "safe region", "competition region".** A partir de ces critères plusieurs mesures peuvent être calculées comme l'aire moyenne des "safe region" des joueurs ce qui permet de caractériser leur capacité à se démarquer.

[16] C. Kang, J. Hwang, et K. Li, « Trajectory Analysis for Soccer Players », in Sixth IEEE International Conference on Data Mining - Workshops (ICDMW’06), Hong Kong, China, 2006, p. 377‑381.

- L'article [17] présente d'une manière très détaillée un moyen de mesurer la pression exercée par les défenseurs au football. Au delà de la simple distance entre deux joueurs l'article cherche à prendre en compte les déplacements, la vitesse, la position de la balle et la position par rapport au but.

[17] G. Andrienko et al., « Visual analysis of pressure in football », Data Mining and Knowledge Discovery, vol. 31, no 6, p. 1793‑1839, nov. 2017.

###  Corrélation entre particules fluides et footballers. 

L’étude des écoulements turbulents des particules fluides montre que la géométrie de l’espace dans lequel elles évoluent influe sur le changement de direction moyen. Il se trouve que la fonction de densité des changements de direction des joueurs de football sur un terrain de foot révèle une forme commune à celles de particules fluides confinées en 2D. Ainsi le comportement anisotrope et a priori non aléatoire des joueurs de foot n’a pas d’influence et seule la géométrie du domaine de limitation a un impact sur les changements de directions moyens.

[18] Wouter J. T. Bos Benjamin Kadoch and Kai Schneider. Directional change of fluid particles in two-dimensional turbulence and of football players. Physical Review Fluids, June 2017.

## To annotate

	https://github.com/topics/nba-data
	https://github.com/ccagrawal/nbaTools
	https://hwchase17.github.io/sportvu/
	https://arxiv.org/ftp/arxiv/papers/1703/1703.07030.pdf
	https://github.com/rajshah4/NBA_SportVu help to treat nba play by play and Sports Vu in R
	http://projects.rajivshah.com/sportvu/EDA_NBA_SportVu.html Merging Sports Vu and play by play
	https://www.inpredictable.com/2015/05/introducing-sharc-shot-arc-analysis.html Shot arc analysis => analysis of the trajectory of the ball
	https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
	https://rpubs.com/jalapic/nbaplaybyplay
	https://github.com/rd11490/NBA-Play-By-Play-Example/blob/master/scrape_example.py
	http://nbasense.com/nba-api/Stats/Stats/Game/PlayByPlay#request-code-usage
	https://www.tandfonline.com/doi/abs/10.1080/24748668.2013.11868640
	https://sci-hub.tw/https://dl.acm.org/citation.cfm?id=3054132
	https://messagerie.ec-lyon.fr/service/home/~/?auth=co&loc=fr&id=10090&part=2
	http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=89086&copyownerid=49896
	https://dtai.cs.kuleuven.be/events/MLSA18/index.php
	https://chyronhego.com/solutions/
	http://www.yisongyue.com/publications/ssac2014_open_shot.pdf
	https://sci-hub.tw/https://ieeexplore.ieee.org/abstract/document/852338





