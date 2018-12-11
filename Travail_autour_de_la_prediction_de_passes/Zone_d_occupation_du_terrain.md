# Découpage du terrain 

## Introduction

On s'intéresse à l'occupation du terrain par les défenseurs et les attaquants. On ne prend pas en compte la position du ballon. On va chercher à découper le terrain en zone dans le but de déterminer des zones où les attaquants pourraient faire une passe en ayant une bonne chance de garder la balle sans prendre en compte la position de la balle.

## Diagrammes de Voronoï

La première idée pour découper le terrain consiste à utiliser les diagrammes de Voronoï. Ces diagrammes découpent un plan en cellules à partir d'un ensemble de point appelés germes. Chaque cellule enferme un seul germe, et forme l'ensemble des points du plan plus proches de ce germe que de tous les autres. 

Dans notre cas les germes sont les joueurs. On peut donc découper le terrain en associant à chaque joueur une zone lui appartenant. La figure 1 illustre ce découpage.

![Découpage en espace de Voronoï](/Images/Voronoï_simple.png "Découpage")

<table border="2">
  <tr>
    <td>
      <img src="Images/Voronoi_simple.png" style="width: 50px;">
    </td>
  </tr>
</table>

## Valuation de l'espace

## Influence de l'inertie sur les espaces de Voronoï
