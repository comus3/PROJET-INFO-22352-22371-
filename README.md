# Labyrinthe AI
## Auteurs
Ce projet a été réalisé par : 

 - Plantin-Carrenard Côme  (22352)
 - Zekhnini Ayoub  (22371)
## Introduction

Ce projet a pour but de créer une intelligence artificielle pour le jeu du Labyrinthe. L'objectif final est de participer à un championnat organisé entre toutes les IA du laboratoire. Pour cela, chaque IA doit communiquer avec un serveur central dont le code est disponible sur [ce repository](https://github.com/qlurkin/PI2CChampionshipRunner).

## Fonctionnalités

L'IA est capable de :

- Recevoir les informations sur l'état du plateau de jeu
- Analyser les informations reçues et calculer la prochaine action à effectuer
- Envoyer la prochaine action à l'application gérant les parties

## Comment utiliser

Pour utiliser l'IA, vous devez :

1. Cloner le repository :
```bash
git clone https://github.com/comus3/PROJET-INFO-22352-22371-
```
2. Installer les dépendances :
```bash
pip install -r requirements.txt
```
3. Lancer l'IA :
```bash
python communication.py
```
Les commandes disponibles sont:

- /connect (permet de connecter une IA)
- /connect -m (permet de connecter plusieurs IA à la fois)
- /connect -t (permet de tester une IA)
- /kill (termine tous les processus)
- /exit (ferme le programme)

## Spécifications techniques

Notre système d'Intelligence Artificielle (IA) a été implémenté en utilisant le langage de programmation Python 3.0, et nous avons adopté l'algorithme MPST(du moins une variante). Nous avons observé que le fait de créer un arbre de profondeur 2 ou 3, contenant les états actualisés et les nouvelles positions potentielles, consommait des ressources considérables. 

Pour résoudre ce problème, notre IA a été conçue pour créer une liste de tous les mouvements possibles et leurs états associés pour notre joueur. En suite, pour chaque mouvement, un objet "Tree" est créé,, qui contient des attributs "value" et "kids". Ces mouvements sont représentés sous forme d'arbre où le premier niveau contient une tuile, chacune de ces tuiles contenant des "kids" qui sont des "gates", et chacune des "gates" ne ne possédant pas encore de "kids" car il faudrait calculer les nouveaux etats pour connaitres les positions possibles.

Ce processus est exécuté en parallèle, la liste de mouvements étant divisée en un nombre de "cuts" prédéfinies.

Notre IA va ensuite itérer jusqu'à ce que 3 secondes se sont ecoulées parmi les moves disponibles pour notre joueur et dans chaqun de ces moves il va aller evaluer un état au hasard parmi les moves possibles. à ce moment là il va donc calculer l'état correspondant à ce move et trouver les nouvelles positions disponibles et les associer comme kids à la gate en question.

Tous les threads se partangent une valeur best value et une valeur best move et après 3 secondes ils sont tous arêtés et l'ia return bestMove.

Pour ce qui est de la fonction d'évaluation, nous avons développé une stratégie complexe; il y a trois modes:
-stratégique,
-rush,
-offencif,
-défencif.
En fonction de la progression de la partie, l'ia va passer d'une évaluation à l'autre.
1. En mode offencif, le but est de réduire la portée de l'énemi au maximum
2. En mode defencif, le but est de réduire la distance entre notre joueur et le tresor
3. En mode rush, le but est aussi de réduire la distance entre notre joueur et le tresor mais aussi augmenter la portée du tresor
4. En mode stratégique, l'ia essaye de faire un equilibre entre tous les modes ci-dessus

## Bibliothèques Utilisées

Nous avons utilisé plusieurs bibliothèques pour développer notre IA, notamment :
-Socket
-Json
-Copy
-Random
-Dijkstra
-Time
-Threading
-Queue
-Pytest


## Conclusion
En conclusion, ce projet a été une opportunité pour nous de développer une intelligence artificielle efficace pour le jeu du Labyrinthe. Nous avons utilisé les meilleures pratiques de programmation ainsi que les bibliothèques les plus avancées pour créer une IA qui est capable de recevoir les informations sur l'état du plateau de jeu, d'analyser ces informations, de calculer la prochaine action à effectuer et enfin d'envoyer cette action à l'application gérant les parties.

## Informations supplémentaires

Baucoup d'infos sur le développement de l'ia ainsi que le secret du mystère au chocolat sont disponibles sur ce [Git](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley).

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](https://github.com/comus3/PROJET-INFO-22352-22371-/blob/main/LICENCE) pour plus de détails.




