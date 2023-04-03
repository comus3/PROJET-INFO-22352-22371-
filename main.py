import json
import random
from utils import *


#### ---FAIT---    ######CREER CLASSE QUI VA CREER DES OBJETS IA, CHAQUE OBJET IA A UN ATRIBUT Active LES OBJETS SAPPELLLENT IA ET SONT RANGES DANS UNE LISTE
#aussi un attribut socket qui est son socket
#chaque objet ia possede uun attribut modèle qui pinte vers la fonction a utiliser pour calculer le next move
#ecdrire le premier modèle
#### ---A FAIRE--- ######
#-modele d'ia

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
nonBouges = [0,2,4,6,14,16,18,20,28,30,32,34,32,34,36,38]
listeIA = []
gateList = ["A","B","C","D","E","F","G","H","I","J","K","L"]



def returnListeIA():
    return listeIA


##########################################################################################################  CLASSE  #####################################################################

class IA:
    def __init__(self,modele,name):
        global listeIA
        self.active = True
        if modele == "manuel":
            self.modele = Manuel([])
        elif modele == "random":
            self.modele = Random([])
        elif modele == "RDFC":
            self.modele = RDFC([])
        else:
            self.modele = Random([])
        listeIA.append(self)
        self.name = name
    def __str__(self):
        print("je suis l'ia associée au port" + str(self.port) + "  mon nom est : "+ self.name)

    def think(self,msg):
        self.state = msg
        print("message pour "+self.name)
        return self.modele.nextMove(self.state,self.name)

    def kill(self):
        self.active = False
        
        

####################### MODèLES IA  ################################

class Manuel:
    def __init__(self,state):
        self.state = state
        self.history = []
    def nextMove(self,status,name):
        print("status:\n")
        #print("voici ce que contient le noveayx" + transformPath(status))
        showState(status)
        user_input_orientation = str(input("orientation? (N/E/S/W... 1 et 0)   >>"))
        user_input_gate = input("which gate..?  \n>>")
        user_input_newpos = int(input("and new pos? \n>>"))
        try:
            tile = {
                "N": bool(int(user_input_orientation[0])),
                "E": bool(int(user_input_orientation[1])),
                "S": bool(int(user_input_orientation[2])),
                "W": bool(int(user_input_orientation[3])),
                "item": status['tile']['item']
            }
            move ={
                "tile": tile,
                "gate": user_input_gate,
                "new_position": user_input_newpos
            }
            output = {
                "response": "move",
                "move": move,
                "message": "EMANUEL la menace"
            }
            return output
        except Exception as e:
            print('erreur au moment de créer la réponse, veuillez reessayer     ',e)
            self.nextMove(self,status,name)

            
class Random:
    def __init__(self,state):
        self.state = state
    def nextMove(self,state,name):
        tile = random_turn_tile(state['tile'])
        while True:
            gateIndex = random.randint(0,11)
            gate = gateList[gateIndex]
            if GATES[gate]['end'] not in state['positions']:
                break
        newBoard,newTile = slideTiles(state['board'],tile,gate)
        new_positions = []
        for position in state["positions"]:
            if onTrack(position, gate):
                if position == GATES[gate]["end"]:
                    new_positions.append(GATES[gate]["start"])
                    continue
                new_positions.append(position + GATES[gate]["inc"])
                continue
            new_positions.append(position)
        state["positions"] = new_positions
        ValidDirections = validNewPos(returnPos(state),newBoard)
        positionIndex = random.randint(0,len(ValidDirections)-1)
        newPosition = ValidDirections[positionIndex]
        move ={
            "tile": tile,
            "gate": gate,
            "new_position": newPosition
        }
        output = {
            "response": "move",
            "move": move,
            "message": "I'm random and stupid"
        }
        return output
    

class RDFC:
    def __init__(self,state):
        self.state = state
    def nextMove(self,state,name):   # (self,statue )
        start, end, board = returnPos(state),treasurePos(state),state['board']
        def successors(index):
            res = []
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dir in directions:
                coords = add(index2coords(index), dir)
                dirName = DIRECTIONS[dir]["name"]
                opposite = DIRECTIONS[dirName]["opposite"]
                if isCoordsValid(*coords):
                    if board[index][dirName] and board[coords2index(*coords)][opposite]:
                        res.append(coords2index(*coords))
            return res
    
        
        goals = [end]
        visited = set()
        parent = {}
        parent[start] = None

        def RDFC(node):
            visited.add(node)
            if node in goals:
                return True
            for successor in successors(node):
                if successor not in visited:
                    parent[successor] = node
                    if RDFC(successor):
                        return True
            return False

        RDFC(start)

        res = []
        node = goals[0]
        while node is not None:
            res.append(node)
            node = parent[node]

        return list(reversed(res))
    


class Negamax:
    #for i in moves possibles(ok si je fais un certain move dans les tuiles, quel est la longueur du meilleur pour moi?--> var1 et pour lui --> var2)
    #pour quel move var1-var2 est minimum? --- faire ce move
    def __init__(self,state):
        self.state = state
        self.depth = 1
        self.player = 1
    def nextMove(self,state,name):
        bestMove = None
        bestValue = float('-inf')
        for move in availableMoves(state):
            newState = update(state,move)
            value = -negamax(newState, self.depth - 1,-self.player)
            if value > bestValue:
                bestValue = value
                bestMove = move
        if bestMove == None:
            newModel = Random(state)
            output = newModel.nextMove(state)
        move ={
            "tile": move['tile'],
            "gate": move['gate'],
            "new_position": move['newPos']
        }
        output = {
            "response": "move",
            "move": move,
            "message": "I'm random and stupid"
        }
        return output
        

        
        
        
    





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
