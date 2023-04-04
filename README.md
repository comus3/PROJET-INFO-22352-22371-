# Labyrinthe AI

## Introduction

Ce projet consiste en la réalisation d'une intelligence artificielle pour le jeu Labyrinthe. L'objectif est de participer à un championnat organisé entre toutes les IA du laboratoire.

## Fonctionnalités

L'IA est capable de :

- Recevoir les informations sur l'état du plateau de jeu
- Analyser les informations reçues et calculer la prochaine action à effectuer
- Envoyer la prochaine action à l'application gérant les parties

## Comment utiliser

Pour utiliser l'IA, vous devez :

1. Cloner le repository :
```bash
git clone https://github.com/VOTRE_NOM/Labyrinthe-AI.git
```
```bash
git clone https://github.com/VOTRE_NOM/Labyrinthe-AI.git
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
- /exit (ferme le programme)

## Spécifications techniques

L'IA a été développée en Python 3.
Notre programme utilise l'algorithme negamax pour calculer le prochain mouvement à effectuer. Pour ce faire, il crée un graphe à partir de l'état en entrée et utilise l'algorithme de Dijkstra pour trouver le chemin le plus court entre la position actuelle et le trésor. Cette méthode permet de calculer efficacement le poids de chaque mouvement possible et ainsi déterminer le prochain mouvement optimal.

En cas d'impossibilité de trouver un chemin vers le trésor, que ce soit pour notre programme ou pour son adversaire, notre programme adopte une stratégie différente: Il cherche alors à se rapprocher de son propre trésor dans l'espoir d'augmenter ses chances de victoire. Cette approche permet d'optimiser les chances de gagner, même dans des situations difficiles où trouver le trésor adverse est impossible.


## Auteurs
Les auteurs de ce projet sont:

 - Côme Plantin-Carrenard
 - Ayoub Zekhnini

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](https://github.com/comus3/PROJET-INFO-22352-22371-/blob/main/LICENCE) pour plus de détails.

## Informations supplémentaires

Baucoup d'infos sur le développement de l'ia ainsi que le secret du mystère au chocolat sont disponibles sur ce [Git](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley).


