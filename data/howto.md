# How our data works ?

Nous disposons actuellement des données pour 3 sports différents : le Football, le Basket et le Rugby. Pour chacun de ces sports ces données ont des formats différents dont chacun d’eux présente des avantages et des inconvénients :
- Basket : 632 matchs de NBA. Chaque match est découpé en évènements. Chaque évènement contient la position des joueurs des deux équipes et du ballon.
- Foot : données pour deux matchs pour les deux équipes. Nous avons également des données pour 3 autres matchs mais seulement avec une équipe.
- Rugby : tous les matchs et entraînements du LOU depuis 2016.

Au vu de la quantité de données que le Basket peut fournir nous allons concentrer notre étude sur ce sport.

Le jeu de données que nous utilisons est issu des données de l'entreprise ***Stats*** et de la technologie *SportsVU*. Celles-ci sont celles de 600 matchs de basket masculin en NBA. Entre les saisons 2013-2014 et 2016-2017, c'était *SportsVU* qui travaillait avec la NBA. L'année suivante, le championnat américain a fait le choix d'une autre technologie de video-tracking. 
Dans notre cas, ces données sont celles issues des matchs en *play-by-play*, c'est à dire action par action. Chacune est mise sous la forme d'un dictionnaire. Elles sont constituées des clées suivantes : *visitor*, *gamedate*, *events*, *gameid* et *home*. Le point qui nous intéresse est principalement la clé *events* qui se trouve elle aussi être un dictionnaire.
Sur la figure suivante est présentée la structure générale des données : 
![dataschema](https://github.com/AmigoCap/MecaFootCo/blob/master/Images/data.jpg "data schema")


# Uploaded data

Les données disponibles dans ce répertoire GitHub correspondent aux 4 quarts temps du match San Antonio Spurs vs. Washington Wizards. On peut retrouver ce match à l'adresse : https://stats.nba.com/game/0021500061/playbyplay/?GameID=0021500061.
