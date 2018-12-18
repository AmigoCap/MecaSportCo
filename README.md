# MecaFootCo

## Introduction du projet

Aujourd’hui la technologie intervient de plus en plus dans le sport. En effet les statistiques des joueurs sont de plus en plus précises et de plus en plus nombreuses. Les clubs emploient des personnes pour acquérir des données et les exploiter. Cependant ces recherches ne sont pas disponibles. C’est dans ce contexte que s’inscrit le Projet d'Application recherche, MécaSportCo, mené à l'**Ecole Centrale de Lyon** par *Gabin Rolland* et *Nathan Rivière*, sous la tutelle de *Wouter Bos* et *Romain Vuillemot*. Son but est d’analyser des données sportives pour trouver un ou plusieurs critères qui pourrait être utiles aux experts.

## Contexte
### Contexte général
L'analyse de données devient essentielle dans le sport et est de plus en plus développée. Le principe est de collecter diverses données et de les analyser afin d'effectuer des prédictions ou d'améliorer les performances à la fois collectives et individuelles des joueurs. De nombreuses startups se créent et proposent leurs services aux professionnels et amateurs. Cette pratique est utilisée par des sportifs de haut niveau comme par exemple l'équipe de football d'Allemagne qui a eu recourt à toutes les données disponibles sur leurs matchs pour se préparer à la coupe du monde de football 2014 qu'elle a par ailleurs remportée. On comprend donc ici l'importance de s'intéresser à cette activité, d'autant plus que la mise à disposition des données étant récente, tout n'a pas été exploré et un large champ de recherche est possible.

De plus l'exploitation de ces données d'un point de vue autre que sportif peut s'avérer pertinent comme c'est le cas dans l'article Directional change of fluid particles in two-dimensional turbulence and of football players, *Physical Review Fluids*, June 2017 de Wouter J. T. Bos Benjamin Kadoch and Kai Schneider, qui illustre l'existence de certaines corrélations entre les mouvements de joueurs de football sur un terrain et des particules sur ce même terrain. C'est dans ce cadre qu'a été créé le PAr MécaSportCo lancé en 2017 afin de caractériser les mouvements de sportifs tout en cherchant à vérifier ces corrélations. Un premier travail a été effectué par Marc Louis Mattis et Alfonso García Hernández. Ce projet est ainsi continué cette année avec pour objectif de progresser dans l'exploration des différentes caractérisations possibles des comportements des sportifs à partir de l'exploitation de différentes données ainsi que dans le développement d'une interface visuelle permettant de communiquer ces données. 

### Recherche de critères pertinents
- Dessin des espaces de Voronoï,
- étude du centre de masse,
- corrélation entre particules fluides et sportifs,
- occupation de l'espace et zones d'influence,
- description et prédiction d'une phase de jeu.

### Source de données disponible
Nous disposons actuellement des données pour 3 sports différents : le Football, le Basket et le Rugby. Pour chacun de ces sports ces données ont des formats différents dont chacun d’eux présente des avantages et des inconvénients :
    - Basket : 632 matchs de NBA. Chaque match est découpé en évènements. Chaque évènement contient la position des joueurs des deux équipes et du ballon.
    - Foot : données pour deux matchs pour les deux équipes. Nous avons également des données pour 3 autres matchs mais seulement avec une équipe.
    - Rugby : tous les matchs et entraînements du LOU depuis 2016.

Au vu de la quantité de données que le Basket peut fournir nous allons concentrer notre étude sur ce sport.

Le jeu de données que nous utilisons est issu des données de l'entreprise ***Stats*** et de la technologie *SportsVU*. Celles-ci sont celles de 600 matchs de basket masculin en NBA. Entre les saisons 2013-2014 et 2016-2017, c'était *SportsVU* qui travaillait avec la NBA. L'année suivante, le championnat américain a fait le choix d'une autre technologie de video-tracking. 
Dans notre cas, ces données sont celles issues des matchs en *play-by-play*, c'est à dire action par action. Chacune est mise sous la forme d'un dictionnaire. Elles sont constituées des clées suivantes : *visitor*, *gamedate*, *events*, *gameid* et *home*. Le point qui nous intéresse est principalement la clé *events* qui se trouve elle aussi être un dictionnaire.
Sur la figure suivante est présentée la structure générale des données : 
