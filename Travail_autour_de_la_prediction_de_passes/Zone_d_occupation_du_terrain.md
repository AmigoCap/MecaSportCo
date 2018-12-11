# Découpage du terrain 

## Introduction

On s'intéresse à l'occupation du terrain par les défenseurs et les attaquants. On ne prend pas en compte la position du ballon. On va chercher à découper le terrain en zone dans le but de déterminer des zones où les attaquants pourraient faire une passe en ayant une bonne chance de garder la balle sans prendre en compte la position de la balle.

## Diagrammes de Voronoï

La première idée pour découper le terrain consiste à utiliser les diagrammes de Voronoï. Ces diagrammes découpent un plan en cellules à partir d'un ensemble de point appelés germes. Chaque cellule enferme un seul germe, et forme l'ensemble des points du plan plus proches de ce germe que de tous les autres. 

Dans notre cas les germes sont les joueurs. On peut donc découper le terrain en associant à chaque joueur une zone lui appartenant. La figure 1 illustre ce découpage.

<table border="2">
  <tr>
    <td>
      <img src="Images/Voronoi_simple.png" style="width: 50px;">
    </td>
  </tr>
</table>

## Valuation de l'espace

Les diagrammes de Voronoï permettent une première approche simple pour le découpage de l'espace. Cependant au sein d'une zone associée à un joueur celui-ci contrôle plus les points proches de lui que les points loin. On va chercher donc à donner une valeur de contrôle par les joueurs à chaque espace du terrain. Notre démarche est la suivante :
- on découpe le terrain en petites cellules
- pour chaque cellule on calcule temps que chaque joueur met pour rejoindre cette zone avec une vitesse v donnée identique pour tous les joueurs. 
- on cherche l'attaquant et le défenseur qui arrive le plus vite à ce point en conservant leur temps respectif qu'on note t<sub>min def</sub> et t<sub>_min_att</sub>.
- on associe à cette zone la valeur val=t<sub>_min_def</sub>-t<sub>_min_att</sub>

Ainsi plus un attaquant peut arriver vite par rapport aux défenseurs à une cellule, plus il contrôle celle-ci, plus la quantité val est grande. La figure suivante permet d'illustrer la valuation de l'espace en terme de contrôle.

<table border="2">
  <tr>
    <td>
      <img src="Images/Voronoi_value.png" style="width: 20px;">
    </td>
  </tr>
</table>

## Influence de l'inertie sur les espaces de Voronoï

Sur la figure précédente les vecteurs vitesses des joueurs sont représentés par les flèches bleues. De manière intuitive on comprend que le contrôle de l'espace par les joueurs est influencé par cette vitesse. Nous allons donc prendre en compte ceci dans la suite. 

Pour prendre en compte l'influence de l'inertie nous devons changer notre façon de calculer le temps qu'un joueur met pour rejoindre un point. Le principe du calcul repose sur l'idée que les joueurs utilise une force de norme constante et dont la direction dépend de la vitesse initiale pour leur permettre rejoindre un point donné. Le détail du calcul est présenté dans le document [Closest player to a point](https://github.com/AmigoCap/MecaFootCo/blob/master/Travail_autour_de_la_prediction_de_passes/Closest_player_to_a_point.pdf).

On obtient le résultat suivant : 

<table border="2">
  <tr>
    <td>
      <img src="Images/Voronoi_inertie.png" style="width: 20px;">
    </td>
  </tr>
</table>

Tout d'abord si on compare ce résultat avec le résultat précédent on remarque que les zones bleues et rouges ne coïncident plus avec les limites définies par les diagrammes de voronoï. Ceci montre donc le fait que l'inertie a une influence sur l'occupation du terrain par les joueurs.

Pour certaines séquences on a constaté qu'il y avait des problèmes avec le principe de calcul du temps pour les zones proches des joueurs avec de grandes vitesses. En effet, un joueur avec une grande vitesse va avoir besoin d'une force très forte pour compenser. La situtation sur la figure suivante illustre ce problème où le joueur (trajectoire en bleue, vecteur vitesse initiale en vert et force en noir) a dépassé le point visé avant de l'atteindre. Néanmoins il est possible de trouver une explication réelle à ce problème en remarquant le fait qu'un joueur se déplaçant très rapidement ne contrôle pas la zone juste devant lui car à l'instant d'après elle sera derrière lui. Comme nous ne sommes pas encore certains de cette interprétation nous avons pris une force relativement élevée (10m.s-2) et nous avons considéré que les joueurs par leur physique contrôlent naturellement une zone autour d'eux qui sera modélisée par des cercles plus gros pour les représenter.

<table border="2">
  <tr>
    <td>
      <img src="Images/Path.png" style="width: 20px;">
    </td>
  </tr>
</table>

## Animation

On a ensuite animé notre modèle pour une séquence de jeu. 

[Lien vidéo](https://github.com/AmigoCap/MecaFootCo/blob/master/Travail_autour_de_la_prediction_de_passes/Images/video1.mp4)

Nous allons cherché dans la suite à mettre en parallèle à cette séquence la vidéo réelle du match ce qui permettra plus d'interprétation. Nous avons également lancé des animations pour d'autres séquences de jeu puisqu'il se trouve que sur celle-ci il n'y a pas de passes alors que c'est ce qui nous intéresse. 


