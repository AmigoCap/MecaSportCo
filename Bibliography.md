# Bibliography

## Data

The data consists of 632 NBA Basketball games. For each match we have the position of the players of each team and the ball in json format. This data is stored in "moments", each of which contains a game phase of the match. It is possible to retrieve the match description and the video feeds associated with each moment at the address [link](https://stats.nba.com/game/0021500061/playbyplay/?GameID=0021500061&GameEventID=303&mtype=pbpmovement&mtitle=West%202%27%20Cutting%20Layup%20Shot%20(10%20PTS)%20(Ginobili%204%20AST)%20during%20San%20Antonio%20Spurs%20@%20Minnesota%20Timberwolves%20-%20WEDNESDAY,%20DECEMBER%2023,%202015#play303~) changing *GameID* in the url to access the match you want.
The two links[1] and[2] explain how the data for each game is organized and how to start using them under python.

[1]	S. Tjortjoglou, « How to Track NBA Player Movements in Python », Savvas Tjortjoglou, 25-août-2015. [En ligne]. Disponible sur: http://savvastjortjoglou.com/nba-play-by-play-movements.html. [Consulté le: 28-oct-2018].

[2]	« Exploring NBA SportVu Movement Data ». [En ligne]. Disponible sur: http://projects.rajivshah.com/sportvu/EDA_NBA_SportVu.html. [Consulté le: 28-oct-2018].

[A list of project based on NBA data](https://github.com/topics/nba-data)

[Python package to scrap NBA data](https://github.com/seemethere/nba_py)

[example of python code to scrap nba data](https://github.com/rd11490/NBA-Play-By-Play-Example/blob/master/scrape_example.py)

[Code for exploring the NBA SportVu motion data in R and link to available data](http://projects.rajivshah.com/sportvu/EDA_NBA_SportVu.html)

[How to get JSON from webpage into Python script](https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script)

[NBA API library](http://nbasense.com/nba-api/Stats/Stats/Game/PlayByPlay#request-code-usage)


## Visualization

### State of the art

The visualization of sports data can take many different forms. Player statistics can be graphically represented to compare their performance on different criteria. This representation only reflects the information provided by the raw data. These data can be presented in a more concrete way by displaying graphs superimposed on the sports field. Finally, it is also possible to view the data directly on the videos of the game phases concerned in order to make a concrete link between the data and the game phase. Article[3] provides a detailed overview of all the work already carried out on the analysis of sports data.

[3] C. Perin, R. Vuillemot, C. D. Stolper, J. T. Stasko, J. Wood, et S. Carpendale, « State of the Art of Sports Data Visualization », Computer Graphics Forum, vol. 37, juin 2018.

### SoccerStories

SoccerStories is an interface to visualize certain phases of a football match. This interface can be very useful by taking into account the fact that data in its pure form speaks little. The interviews with experts confirm this remark since they reveal that in the analysis of football we must not forget the visual side and the selection of game phases that allow us to tell a story. We can draw several inspirations from this interface, in particular the different criteria and cursors presented by adapting them to our own criteria as well as the different approaches presented in the article (interviews with experts, evaluation phase, description of the sport...)

[4] C. Perin, R. Vuillemot, et J.-D. Fekete, « SoccerStories: A Kick-off for Visual Soccer Analysis », IEEE Transactions on Visualization and Computer Graphics, vol. 19, no 12, p. 2506‑2515, déc. 2013.

### BKViz

BKViz[5] is a Basketball data analysis interface that includes a large number of different analysis tools. Thus the contribution of this tool lies in the fact that it allows to navigate between the different available data and the different analysis tools in a simple and efficient way. 

[5] A. G. Losada, R. Therón, et A. Benito Santos, « BKViz: A Basketball Visual Analysis Tool », IEEE Computer Graphics and Applications, vol. 36, p. 58‑68, nov. 2016.

### CourtVision

CourtVision[6] is an analysis tool for the NBA that allows you to visually compare the shots performance of different basketball players. It also highlights the different strategic areas for shoots on a basketball court.

[6] K. Goldsberry, « CourtVision: New Visual and Spatial Analytics for the NBA », p. 7, 2012.

### Combiner vidéo et analyse des données 

Article [7] details the importance of combining data and video while indicating different methods to achieve this. 

[7] M. Stein et al., « Bring It to the Pitch: Combining Video and Movement Data to Enhance Team Sport Analysis », IEEE Transactions on Visualization and Computer Graphics, vol. 24, no 1, p. 13‑22, janv. 2018.

## Modèle d'analyse des données

### Focusing on the ball

- This blog post [8] developp a study of ball's trajectory during a shot. Then it focuses on the influence of the trajecory on freethrows efficiency.

[8] Raymond Cen, Harrison Chase, Carlos Pena-Lobel, et Daniel Silberwasser, « NBA Shot Prediction and Analysis by hwchase17 ». [En ligne]. Disponible sur: https://hwchase17.github.io/sportvu/. [Consulté le: 04-oct-2019]

### About prediction

- Article[9] presents a new metric that allows to characterize a given situation in terms of the possibility of points scored as a result of this action. This quantity is called EPV: Expected Possession Value. The EPV is calculated statistically by taking into account a finite quantity of action possibilities for the player in possession of the ball: dribbles, passes, shots...

[9] D. Cervone, A. D’Amour, L. Bornn, et K. Goldsberry, « Predicting Points and Valuing Decisions in Real Time with NBA Optical Tracking Data », p. 9, 2014.

- The aim of the project [10] is to developp a model to determine the probability of each shot going in and then study the impact of different variables on shot efficiency.

[10] Raymond Cen, Harrison Chase, Carlos Pena-Lobel, et Daniel Silberwasser, « NBA Shot Prediction and Analysis by hwchase17 ». [En ligne]. Disponible sur: https://hwchase17.github.io/sportvu/. [Consulté le: 04-oct-2019].

- Article[11] details the process that led to the development of a visual pass prediction interface (http://projects.yisongyue.com/bballpredict/). This interface allows the user to place the players and the ball on the field himself and from this we observe by means of more or less thick lines the probabilities of passing and shooting of the player in possession of the ball. The principle of the calculation is based on machine learning experimented on the 2012-2013 SportsVu data.

[11] Y. Yue, P. Lucey, P. Carr, A. Bialkowski, et I. Matthews, « Learning Fine-Grained Spatial Models for Dynamic Sports Play Prediction », in 2014 IEEE International Conference on Data Mining, Shenzhen, China, 2014, p. 670‑679.


### Space occupation

- This article [12] presents the state of the art of the various studies of spatio-temporal behaviour in team sports.

[12] J. Gudmundsson et M. Horton, « Spatio-Temporal Analysis of Team Sports », ACM Comput. Surv., vol. 50, no 2, p. 22:1–22:34, avr. 2017.

- The analysis of motion data and space occupation is important as it contributed to the increase of 3-point shots (from few % in 1980 to 33,6% of total shots in 2018) and so the change of basketball strategies [13].

[13](https://www.vice.com/en_au/article/pgj338/numbers-game-how-spatial-analytics-killed-the-mid-range-jump-shot) W. McCagh, « How Spatial Analytics Killed The Mid-Range Jump Shot », Vice, 26-sept-2016.

- The use of space in team sports such as football is essential in the development of strategies by coaches. The main keys to space occupancy are: **interaction between players, player influence zones, pass options, free spaces**. Article[14] studies these different aspects by creating a model to characterize the players' area of influence by taking into account their speed. From this we can determine areas of interaction (intersection of influence zones). The open spaces are all the more so in football as the players, all together, occupy only a small part of the field at a given moment. **The article associates a player with a free space as an area for which he has a greater probability of arriving first** taking into account his direction, speed and distance. The study of the passes is more difficult because it is the result of a complex decision-making process. The article raises several criteria to characterize the risk of a pass: **The speed of the pass, the distance, the pressure exerted on the potential receivers, the direction of the passes and the fact of avoiding the opposing block... All these studies are used by the article[15] which presents a preocédure of analysis of an action in terms of pass. First, it selects the possibility of interesting passes using the previous criteria. Then the procedure consists in looking at whether the pass is made in the opposing side or not. Then if the pass is in the opposing side, it is a question of taking into account the influence of the opposing players. Finally, the last phase consists in analysing what the defenders could have done to prevent the pass. A similar procedure is in place to describe the passes in the open spaces.

[14]	« (PDF) Director’s Cut: Analysis and Annotation of Soccer Matches », ResearchGate. [En ligne]. Disponible sur: https://www.researchgate.net/publication/308756859_Director’s_Cut_Analysis_and_Annotation_of_Soccer_Matches. [Consulté le: 01-nov-2018].

[15] M. Stein et al., « Revealing the Invisible: Visual Analytics and Explanatory Storytelling for Advanced Team Sport Analysis », in 2018 International Symposium on Big Data Visual and Immersive Analytics (BDVA), Konstanz, 2018, p. 1‑9.


- Article[16] carries out a study on the use of space in basketball. It is based on the analogy with market trading. The field is divided up by Voronoi's spaces and within each of these spaces a player's influence is inversely proportional to the distance at which he is located. A basic principle: if a player i gives the ball to a player j it is because the latter occupies a better position. Thus it becomes interesting to associate a value to each space of the field by dividing it into cells. To do this, they use "Bayesian inference" using player position and pass data. He notes that the important areas of the field may vary from one team to another. 

[16] D. Cervone, L. Bornn, et K. Goldsberry, « 1 Intro: the Basketball Court is a Real Estate Market », p. 8, 2016.

- Article[17] carries out a study on the occupation and generation of football spaces. In this sport, players are only in possession of the ball for 3 minutes, hence the importance of playing without a ball. The value of a terrain space can be defined by its position relative to the ball, its proximity to the opponent's goal and the level of belonging of the space. To go further we can look at the player's speed as well. After defining **a player's area of influence**, (using a probability density of a two-variable Gaussian law), the author defines **the state of control of a given area** by a given team by comparing at each location the sum of the influences of the players of one team with that of the other team. Then the searched author gave **the value to an area of the land**. Several criteria considered: position in relation to the ball, the goal and the other players. In order to determine a characteristic function of the value of an area of influence they first study the sum of the influence of the defense of an area as a function of the position of the ball. To do this, they use a neural network feed forward. Once the value of an area is determined from the position of the ball and the defenders, he normalizes it by the value of an area seen in relation to the position of the opposing goal. Finally, they focus on the direction of players' movements with two criteria: SOG (space occupation gain) and SGG (space generation gain). Finally, the author analyses his research with the FC Barcelona game phase.

[17] J. Fernandez, L. Bornn, « Wide Open Spaces: A statistical technique for measuring space creation in professional soccer », p. 19, 2018.

- Many coaches analyze their team's performance after the games. Article[18] provides a visual means of description. It is based on three collective criteria: **the position of the centre of mass, the dispersion of the team (average position of the players in relation to the CDM, speed of dispersion or tightening, distance occupied over a width u of the field) and the synchronization of the team.** The individual criteria are also used but in a secondary way. Two actions are discussed in the article where we can see that a goal action can be explained by one or more of these criteria.

[18] A. Benito Santos, R. Theron, A. Losada, J. E. Sampaio, et C. Lago-Peñas, « Data-Driven Visual Performance Analysis in Soccer: An Exploratory Prototype », Front. Psychol., vol. 9, 2018.

- In[19], the collective behaviour of the players using their trajectory as well as that of the ball. Several criteria are defined: **From these criteria several measures can be calculated as the average area of the players' safe regions, which makes it possible to characterize their ability to stand out.

[19] C. Kang, J. Hwang, et K. Li, « Trajectory Analysis for Soccer Players », in Sixth IEEE International Conference on Data Mining - Workshops (ICDMW’06), Hong Kong, China, 2006, p. 377‑381.

- Article[20] presents in great detail a way of measuring the pressure exerted by defenders on football. Beyond the simple distance between two players, the article seeks to take into account the movements, speed, position of the ball and position in relation to the goal.

[20] G. Andrienko et al., « Visual analysis of pressure in football », Data Mining and Knowledge Discovery, vol. 31, no 6, p. 1793‑1839, nov. 2017.

- The pressure exerced by defensive players on the shooter has an influence on shot efficiency [21,22]. So it is important for teams to try to get *open shots* to improve their efficiency. [22] study which game strategies best lead to open shots for each team.

[21](https://messagerie.ec-lyon.fr/service/home/~/?auth=co&loc=fr&id=10090&part=2) G. Csátaljay, N. James, M. Hughes, et H. Dancs, « Effects of defensive pressure on basketball shooting performance », International Journal of Performance Analysis in Sport, vol. 13, déc. 2013.

[22](http://www.yisongyue.com/publications/ssac2014_open_shot.pdf) P. Lucey, A. Bialkowski, P. Carr, Y. Yue, I. Matthews, et D. Research, « “How to Get an Open Shot”: Analyzing Team Movement in », p. 8.

- Voronoi diagrams can be derived to obtain new metrics characterizing space occupancy. Thus the article [23] details how by superimposing the space occupation of two opposing teams we can quantify their interaction.

[23](https://www.tandfonline.com/doi/abs/10.1080/24748668.2013.11868640) S. Fonseca, J. Milho, B. Travassos, D. Araújo, et A. Lopes, « Measuring spatial interaction behavior in team sports using superimposed Voronoi diagrams », International Journal of Performance Analysis in Sport, vol. 13, no 1, p. 179‑189, avr. 2013.

- The article [24] develops a new metric called "dominant region" that makes it possible to quantify the area of influence of a football player.

[24](https://sci-hub.tw/https://ieeexplore.ieee.org/abstract/document/852338) T. Taki et J. Hasegawa, « Visualization of dominant region in team games and its application to teamwork analysis », Proceedings Computer Graphics International 2000, p. 227‑235, 2000.

###  Correlation between fluid particles and footballers. 

The study of turbulent flows of fluid particles shows that the geometry of the space in which they evolve influences the average change in direction. As it happens, the density function of changes in the direction of football players on a football field reveals a shape common to those of fluid particles confined in 2D. Thus the anisotropic and a priori non-random behaviour of football players has no influence and only the geometry of the limiting domain has an impact on changes in average directions.

[25] Wouter J. T. Bos Benjamin Kadoch and Kai Schneider. Directional change of fluid particles in two-dimensional turbulence and of football players. Physical Review Fluids, June 2017.






