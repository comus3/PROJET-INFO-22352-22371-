import json
import random
from utils import isSameTile,turn_tile,random_turn_tile,showState,validMoves


#### ---FAIT---    ######CREER CLASSE QUI VA CREER DES OBJETS IA, CHAQUE OBJET IA A UN ATRIBUT Active LES OBJETS SAPPELLLENT IA ET SONT RANGES DANS UNE LISTE
#aussi un attribut socket qui est son socket
#chaque objet ia possede uun attribut modèle qui pinte vers la fonction a utiliser pour calculer le next move
#ecdrire le premier modèle
#### ---A FAIRE--- ######
#-Simulateur du jeu
#-modele d'ia
#testing
#ceci est ma brainche

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
        #elif modele == "rdfc":
        #    self.modele = RDFC([])
        else:
            self.modele = Random([])
        listeIA.append(self)
        self.name = name

    def think(self,msg):
        self.state = msg
        print("")
        print("message pour "+self.name)
        return self.modele.nextMove(msg,self.name)

    def kill(self):
        self.active = False
        
        

####################### MODèLES IA  ################################

class Manuel:
    def __init__(self,state):
        self.state = state
        self.history = []
    def nextMove(self,status,name):
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
            return output
        except:
            print('erreur au moment de créer la réponse, veuillez reessayer')
            self.nextMove(status)

            
class Random:
    def __init__(self,state):
        self.state = state
    def nextMove(self,state,name):
        tile = random_turn_tile(state['tile'])
        gateIndex = random.randint(0,11)
        gate = gateList[gateIndex]
        ValidDirections = validMoves(state,name)
        temp = len(ValidDirections)-1
        positionIndex = random.randint(0,temp)
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
    
"""
class RDFC:
    def __init__(self,state):
        self.state = state

    def __str__(self):
        print("je suis l'ia associée au port" + str(self.port) + "  mon nom est : "+ self.name)
    
    def index2coords(index):
        return index // 7, index % 7

    def coords2index(i, j):
        return i * 7 + j
    
    def isCoordsValid(i, j):
        return i >= 0 and i < 7 and j >= 0 and i < 7
    
    def add(A, B):
        return tuple(a + b for a, b in zip(A, B))
    def nextMove(self, start, end, board):   # (self,statue )
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
        
        
    

"""

class NegamaxWithPruningIterativeDeepening:
    def __init__(self, state, player, timeout=0.2):
        self.state = state
        self.player = player
        self.timeout = timeout
        self.cache = defaultdict(lambda: 0)

    def nextMove(self):
        value, move = 0, None
        depth = 1
        start = time.time()
        over = False
        while value > -9 and time.time() - start < self.timeout and not over:
            value, move, over = self.cachedNegamaxWithPruningLimitedDepth(self.state, self.player, depth)
            depth += 1
        return move

    def cachedNegamaxWithPruningLimitedDepth(self, state, player, depth, alpha=float('-inf'), beta=float('inf')):
        over = gameOver(state)
        if over or depth == 0:
            res = -heuristic(state, player), None, over

        else:
            theValue, theMove, theOver = float('-inf'), None, True
            possibilities = [(move, apply(state, move)) for move in moves(state)]
            possibilities.sort(key=lambda poss: self.cache[tuple(poss[1])])
            for move, successor in reversed(possibilities):
                value, _, over = self.cachedNegamaxWithPruningLimitedDepth(successor, player%2+1, depth-1, -beta, -alpha)
                theOver = theOver and over
                if value > theValue:
                    theValue, theMove = value, move
                alpha = max(alpha, theValue)
                if alpha >= beta:
                    break
            res = -theValue, theMove, theOver
        self.cache[tuple(state)] = res[0]
        return res


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
