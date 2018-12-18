# Bibliographie commentée

## Définition du sujet 

- Définition des critères de performance. L'article [1] définit et classe les différents indicateurs qui permettent de caractériser les perfomances au football. Il définit en particulier les variables relatvies aux passes qui sont le sujet de notre recherche (nombre, précision, type de passe, zones de passe, interceptions). On pourra s'inspirer de cette démarche pour définir les variables caractérisant les passees au Basket. 

[1] « Performance analysis », footballscience.net | Soccer, Football, Training, Testing, Recovery, Injury Prevention, Conditioning and other interesting topics. [En ligne]. Disponible sur: http://www.footballscience.net/special-topics/performance-analysis/. [Consulté le: 02-déc-2018].

## Utilisation des données

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

### Combiner vidéo et analyse des données 

L'article 6 détaille l'importance de combiner données et vidéos tout en indiquant différentes méthodes pour réaliser ceci. 

[6] M. Stein et al., « Bring It to the Pitch: Combining Video and Movement Data to Enhance Team Sport Analysis », IEEE Transactions on Visualization and Computer Graphics, vol. 24, no 1, p. 13‑22, janv. 2018.

## Modèle d'analyse des données

### Autour de la prédiction 

- L'article [7] présente une nouvelle métrique qui permet de caractériser une situation donnée en terme de possibilité de points marqués suite à cette action. Cette quantité est appelée EPV : Expected Possession Value. Le calcul de l'EPV se fait de manière statistique en prenant en compte une quantité finie de possibilité d'action pour le joueur en possession de la balle : dribbles, passes, shoots... 

[7] D. Cervone, A. D’Amour, L. Bornn, et K. Goldsberry, « Predicting Points and Valuing Decisions in Real Time with NBA Optical Tracking Data », p. 9, 2014.

### Autour de l'occupation d'espace

- L'utilisation de l'espace dans les sports collectifs comme le football est indispensable dans l'élaboration des stratégies par les entraineurs. Les principales clés de l'occupation d'espace sont : **l'intéraction entre joueurs, les zones d'influences des joueurs, les options de passe, les espaces libres**. L'article [8] étudie ces différents aspects en créant un modèle permettant de caractériser la zone d'influence des joueurs en prenant en compte leur vitesse. Á partir de ceci on peut déterminer des zones d'intéractions (intersection des zones d'influences). Les espaces libres sont d'autant plus autant au foot que les joueurs, tous rassemblés, n'occupent qu'une petite partie du terrain à un instant t. **L'article associe à un joueur un espace libre comme étant une zone pour laquelle il a une plus grande probabilité d'arriver en premier** en prenant en compte sa direction, sa vitesse et la distance. En ce qui concerne l'étude des passes, celle-ci est plus difficile puisqu'elle résulte d'un processus de décision complex. L'article soulève plusieurs critères pour caractériser le risque d'une passe : **la vitesse de la passe, la distance, le pression exercée sur les potentiels receveurs, la direction des passes et le fait d'éviter le bloc adverse.**

[8] [1]	« (PDF) Director’s Cut: Analysis and Annotation of Soccer Matches », ResearchGate. [En ligne]. Disponible sur: https://www.researchgate.net/publication/308756859_Director’s_Cut_Analysis_and_Annotation_of_Soccer_Matches. [Consulté le: 01-nov-2018].


- L'article [9] réalise une étude sur l’occupation de l’espace au basket. Elle repose sur l’analogie avec l’échange sur le marché. Le terrain est découpé grâce aux espaces de Voronoï et au sein de chacun des ces espaces l’influence d’un joueur est inversement proportionnel à la distance à laquelle il se situe. Un principe de base : si un joueur i donne la balle à un joueur j c’est que celui-ci occupe une position mieux placée. Ainsi il devient intéressant d’associer une valeur à chaque espace du terrain en le découpant en cellules. Pour cela ils utilisent “l’inférence bayésienne” à l’aide des données de position des joueurs et de passes. Il remarque que les zones importantes du terrain peuvent varier d’une équipe à une autre. 

[9] D. Cervone, L. Bornn, et K. Goldsberry, « 1 Intro: the Basketball Court is a Real Estate Market », p. 8, 2016.

- L'article [10] réalise une étude sur l’occupation et la génération d’espaces au foot. Dans ce sport, les joueurs ne sont en possession du ballon que 3 minutes, d’où  l’importance du jeu sans ballon. La valeur d’un espace du terrain peut être définie grâce à sa position relativement au ballon, la proximité avec le but adverse et le niveau d’appartenance de l’espace. Pour aller plus loin on peut regarder la vitesse du joueur également. Après avoir défini **la zone d’influence d’un joueur**, (grâce à une densité de probabilité d'une loi gaussienne à deux variables), l’auteur définit **l’état de contrôle d’une zone** par une équipe donnée en comparant à chaque endroit la somme des influences des joueurs d’une équipe avec celle de l’autre équipe. Ensuite l’auteur cherche a donné de **la valeur à une zone du terrain**. Plusieurs critères envisagés : position par rapport à la balle, au but et des autres joueurs. Afin de déterminer une fonction caractéristique de la valeur d’une zone d’influence ils étudient d’abord la somme d’influence de la défense d’une zone en fonction de la position de la balle. Pour cela ils utilisent un feed forward neural network. Une fois la valeur d’une zone déterminée à partir de la position de la balle et des défenseurs il la normalise par la valeur d’une zone vue par rapport à la position du but adverse. Ils se concentrent finalement sur le sens des déplacements des joueurs avec deux critères : SOG (space occupation gain) et SGG (space generation gain). Enfin l’auteur réalise une analyse de ses recherches avec phase de jeu du FC Barcelone.

[10] J. Fernandez, L. Bornn, « Wide Open Spaces: A statistical technique for measuring space creation in professional soccer », p. 19, 2018.

###  Corrélation entre particules fluides et footballers. 

L’étude des écoulements turbulents des particules fluides montre que la géométrie de l’espace dans lequel elles évoluent influe sur le changement de direction moyen. Il se trouve que la fonction de densité des changements de direction des joueurs de football sur un terrain de foot révèle une forme commune à celles de particules fluides confinées en 2D. Ainsi le comportement anisotrope et a priori non aléatoire des joueurs de foot n’a pas d’influence et seule la géométrie du domaine de limitation a un impact sur les changements de directions moyens.

[11] Wouter J. T. Bos Benjamin Kadoch and Kai Schneider. Directional change of fluid particles in two-dimensional turbulence and of football players. Physical Review Fluids, June 2017.





