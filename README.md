# Labyrinthe AI
## Auteurs
Ce projet a été réalisé par : 

 - Plantin-Carrenard Côme  (22352)
 - Zekhnini Ayoub  (22371)
## Introduction

Ce projet a pour but de créer une intelligence artificielle pour le jeu du Labyrinthe. L'objectif final est de participer à un championnat organisé entre toutes les IA du laboratoire. Pour cela, chaque IA doit communiquer avec un serveur central dont le code est disponible sur ce repository [ici](https://github.com/qlurkin/PI2CChampionshipRunner).

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
- /exit (ferme le programme)

## Spécifications techniques

Notre système d'IA a été implémenté en utilisant le langage de programmation Python 3.0. 
Nous avons adopté l'algorithme Negamax, une variante de l'algorithme Minimax, pour déterminer le prochain mouvement optimal.
Pour ce faire, il crée un graphe à partir de l'état en entrée et utilise l'algorithme de Dijkstra pour trouver le chemin le plus court entre la position actuelle et le trésor. 
Cette méthode permet de déterminer de façon efficace le poids de chaque mouvement potentiel, garantissant une décision optimale pour le prochain coup à jouer.

Dans les cas où l'algorithme ne parvient pas à trouver un chemin menant au trésor, que ce soit pour notre programme ou pour son adversaire, notre programme adopte une stratégie différente. Il cherche alors à se rapprocher de son propre trésor dans l'espoir d'augmenter ses chances de victoire. Cette approche permet d'optimiser les chances de gagner, même dans des situations difficiles où la découverte du trésor adverse semble improbable..

## Bibliothèques Utilisées

Nous avons utilisé plusieurs bibliothèques pour développer notre IA, notamment :


## Conclusion
En conclusion, ce projet a été une opportunité pour nous de développer une intelligence artificielle efficace pour le jeu du Labyrinthe. Nous avons utilisé les meilleures pratiques de programmation ainsi que les bibliothèques les plus avancées pour créer une IA qui est capable de recevoir les informations sur l'état du plateau de jeu, d'analyser ces informations, de calculer la prochaine action à effectuer et enfin d'envoyer cette action à l'application gérant les parties.

Pour utiliser notre IA, il vous suffit de cloner notre repository et d'installer les dépendances nécessaires. Nous avons également fourni des commandes pour faciliter son utilisation. Pour plus d'informations sur le développement de notre IA, vous pouvez consulter notre repository.

## Informations supplémentaires

Baucoup d'infos sur le développement de l'ia ainsi que le secret du mystère au chocolat sont disponibles sur ce [Git](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley).

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](https://github.com/comus3/PROJET-INFO-22352-22371-/blob/main/LICENCE) pour plus de détails.




