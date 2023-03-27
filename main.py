import json
import random
from utils import isSameTile,turn_tile,random_turn_tile,showState
#### ---FAIT---    ######CREER CLASSE QUI VA CREER DES OBJETS IA, CHAQUE OBJET IA A UN ATRIBUT Active LES OBJETS SAPPELLLENT IA ET SONT RANGES DANS UNE LISTE
#aussi un attribut socket qui est son socket
#chaque objet ia possede uun attribut modèle qui pinte vers la fonction a utiliser pour calculer le next move
#ecdrire le premier modèle
#### ---A FAIRE--- ######
#-Simulateur du jeu
#-modele d'ia


listeIA = []

def returnListeIA():
    return listeIA

class IA:
    def __init__(self,modele):
        global listeIA
        self.active = True
        if modele == "manuel":
            self.modele = Manuel([])
        else:
            self.modele = Manuel([])
        listeIA.append(self)
        self.name = "IA" + str(len(listeIA))
    def __str__(self):
        print("je suis l'ia associée au port" + self.port)
    def think(self,msg):
        print("message pour "+self.name)
        return self.modele.nextMove(msg)
    def kill(self):
        self.active = False
        
        

####################### MODèLES IA  ################################

class Manuel:
    def __init__(self,state):
        self.state = state
        self.history = []
    def nextMove(self,status):
        cardinaux = [False,False,False,False]
        print("status:\n")
        showState(status)
        user_input_orientation = str(input("orientation? (N/E/S/W... 1 et 0)   >>"))
        user_input_gate = input("which gate..?  \n>>")
        user_input_newpos = input("and new pos? \n>>")
        try:
            j = 0
            for i in user_input_orientation:
                cardinaux[j] = bool(i)
                j= j+1
            tile ={
                "N": cardinaux[0],
                "E": cardinaux[1],
                "S": cardinaux[2],
                "W": cardinaux[3],
                "item": 1
            }
            move ={
                "tile": tile,
                "gate": user_input_gate,
                "new_position": user_input_newpos
            }
            output = {
                "response": "move",
                "move": move,
                "message": "Y o Y"
            }
            return json.dumps(output).encode()
        except:
            print('erreur au moment de créer la réponse, veuillez reessayer')
            self.nextMove(status)
class Random:
    def __init__(self,state):
        self.state = state
    def think(self):
        return 0





####################### EMULATEURS JEU  ################################

#       A     B     C
#    0  1  2  3  4  5  6
# L  7  8  9 10 11 12 13 D
#   14 15 16 17 18 19 20
# K 21 22 23 24 25 26 27 E
#   28 29 30 31 32 33 34
# J 35 36 37 38 39 40 41 F
#   42 43 44 45 46 47 48
#       I     H     G

GATES = {
    "A": {"start": 1, "end": 43, "inc": 7},
    "B": {"start": 3, "end": 45, "inc": 7},
    "C": {"start": 5, "end": 47, "inc": 7},
    "D": {"start": 13, "end": 7, "inc": -1},
    "E": {"start": 27, "end": 21, "inc": -1},
    "F": {"start": 41, "end": 35, "inc": -1},
    "G": {"start": 47, "end": 5, "inc": -7},
    "H": {"start": 45, "end": 3, "inc": -7},
    "I": {"start": 43, "end": 1, "inc": -7},
    "J": {"start": 35, "end": 41, "inc": 1},
    "K": {"start": 21, "end": 27, "inc": 1},
    "L": {"start": 7, "end": 13, "inc": 1},
}
DIRECTIONS = {
    "N": {"coords": (-1, 0), "inc": -7, "opposite": "S"},
    "S": {"coords": (1, 0), "inc": 7, "opposite": "N"},
    "W": {"coords": (0, -1), "inc": -1, "opposite": "E"},
    "E": {"coords": (0, 1), "inc": 1, "opposite": "W"},
    (-1, 0): {"name": "N"},
    (1, 0): {"name": "S"},
    (0, -1): {"name": "W"},
    (0, 1): {"name": "E"},
}
class Emulateur:
    def __init__(self):
        self.state = 0