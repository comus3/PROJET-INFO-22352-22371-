import socket
import json
import copy
import random

####    ---FAIT---  ###### quelques fonctions de comm
####    ---A FAIRE--- #### 
# Fonction qui calcule le/les chemins vers trésor avec map comme arg
# fonction random qui prend en param un nombre n(nombre de choix) et rend un chiffre compris entre 0 et n-1

listnames = []
for i in range(500):
    listnames.append('IA'+str(i))
#listnames = ["thomas","top",'nickel','super','ultra','bazarDuGrenier','leLApib','Bat','LEPHOENIX','equateur','tongo','tango','charlie','hebdo','lemecaudessusdemoiestnul','hexadecimal']
index = 0

responseToPing ={
       "response": "pong"
    }


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
##############################################################################################################



def requestSubscribeStringGenerator(port,):#Génère un string et le json.dimps et eoncdoe pr sub une ia
    global index
    matricule2 = str(22371 + index)
    name = listnames[index]
    request_subscribe = {
        "request": "subscribe",
        "port": port,
        "name": name,
        "matricules": ["22352", matricule2]
    }
    index = index+1
    req = json.dumps(request_subscribe)
    req = req.encode()

    return (req,name)


def jsonEncodeAndSend(message,s):#encode json et envoie msg par un socket
    message = jsonEncode(message)
    send =True
    while send:
        try:
            s.send(message)
            send = False
        except Exception as e:
            print("envoi échoué: ", e)
def jsonEncode(message):
    return json.dumps(message).encode()
    


def validMoves(playerPos,board):#return une liste de nouvelles positions valides sur la carte ENTREE: Player position on board and the board
    validPositions = []
    if playerPos>6 and board[playerPos]['N']:
        newPos = playerPos-7
        if (newPos)in range(49):
            if board[newPos]['S']:
                validPositions.append(newPos)
    if playerPos<42 and board[playerPos]['S']:
        newPos = playerPos +7
        if (newPos)in range(49):
            if board[newPos]['N']:
                validPositions.append(newPos)
    if (playerPos%7)!=0 and board[playerPos]['W']:
        newPos = playerPos -1
        if (newPos)in range(49):
            if board[newPos]['E']:
                validPositions.append(newPos)
    if ((playerPos+1)%7)!=0 and board[playerPos]['E']:
        newPos = playerPos +1
        if (newPos)in range(49):
            if board[newPos]['W']:
                validPositions.append(newPos)
    validPositions.append(playerPos)
    return validPositions

def treasurePos(status):#return la position du trésor recherché
    for i in range(49):
        if status['board'][i]['item'] == status['target']:
            return i
        
def returnPos(status):
    return status['positions'][status['current']]

def availableMoves(state):#return les moves possibles pour apres aller itérer dedans
    return 0
def evalState(state):#return le poids de la situation
    return 0
def negamax(board,depth,player):
    return 0
def update(state,move):
    return 0

#ANCIENNE VERSION
"""
def transformPath(status):#Transforme notre labyrinthe en quelque chose de baucoup plus facile a manipuler
    class Nodes:
        def __init__(self,pos,board):
            self.pos = pos
            self.connection = {}
            for i in passages(pos,board):
                longTemp = 1
                (a,b) = recurcif(self.pos,board,i,longTemp)
                self.connection[a] = b
        def returnConnections(self):
            return self.connection
        def returnPosition(self):
            return self.pos
    def passages(pos,board):
        passages = []
        for i in cardinaux:
            if board[pos][i]:
                passages.append(i)
        return passages
    def isInMap(pos):
        for i in newMap:
            if i.pos == pos:
                return True
        return False
    def recurcif(pos,board,direction,longTemp):
        newpos = pos+cardinaux[direction]
        if len(passages(newpos,board)) == 2 and board[newpos][direction]:
            longTemp = longTemp + 1
            recurcif(newpos,board,direction,longTemp)
        elif isInMap(newpos):
            return(newpos,longTemp)
        #elif 
        else:
            newMap.append(Nodes(newpos,board))
            return (newpos,longTemp)
    newMap = []
    cardinaux = {'N':-7,'E':1,'S':7,'W':-1}
    start, end, board = returnPos(status),treasurePos(status),status['board']
    newMap.append(Nodes(start,board))
    return newMap
"""


#########################################UTILS POUR RDCF

def findtreasure(plateau):
    def rdfs(i, j, chemin, visites):   #Méthode qui est utilisé Recursive Depth-first search    
        chemin.append((i, j))
        if plateau[i][j].statue == "trésor":
            positions_tresors.append((i, j))
        visites.add((i, j))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(plateau) and 0 <= nj < len(plateau[0]) and plateau[ni][nj].statue != "board" and (ni, nj) not in visites:
                rdfs(ni, nj, chemin, visites)
        chemin.pop()
        visites.remove((i, j))

    positions_tresors = []  # liste des positions de trésor
    visites = set()  # c'est l'ensemble des cases visitées pour que ça évite les boucles infinies
    for i in range(len(plateau)):
        for j in range(len(plateau[0])):
            if plateau[i][j].statue == "start":
                rdfs(i, j, [], visites)
    return positions_tresors




def index2coords(index):
    return index // 7, index % 7
def coords2index(i, j):
    return i * 7 + j
def isCoordsValid(i, j):
    return i >= 0 and i < 7 and j >= 0 and i < 7
def add(A, B):
    return tuple(a + b for a, b in zip(A, B))



##############################################          ALL CREDITS TO LURK1        ######################################################

def isSameTile(t1, t2):
    for _ in range(4):
        if t1 == t2:
            return True
        t2 = turn_tile(t2)

    return False
def turn_tile(tile):
    res = copy.deepcopy(tile)
    res["N"] = tile["E"]
    res["E"] = tile["S"]
    res["S"] = tile["W"]
    res["W"] = tile["N"]
    return res

def random_turn_tile(tile):
    for _ in range(random.randint(1, 4)):
        tile = turn_tile(tile)
    return tile

def showBoard(board):
    mat = []
    for i in range(28):
        mat.append([])
        for j in range(28):
            mat[i].append(" ")
    for index, value in enumerate(board):
        i = (index // 7) * 4
        j = (index % 7) * 4
        mat[i][j] = "#"
        mat[i][j + 1] = "#" if not value["N"] else " "
        mat[i][j + 2] = "#"
        mat[i][j + 3] = "|"
        mat[i + 1][j] = "#" if not value["W"] else " "
        mat[i + 1][j + 1] = (
            " " if value["item"] is None else chr(ord("A") + value["item"])
        )
        mat[i + 1][j + 2] = "#" if not value["E"] else " "
        mat[i + 1][j + 3] = "|"
        mat[i + 2][j] = "#"
        mat[i + 2][j + 1] = "#" if not value["S"] else " "
        mat[i + 2][j + 2] = "#"
        mat[i + 2][j + 3] = "|"
        mat[i + 3][j] = "-"
        mat[i + 3][j + 1] = "-"
        mat[i + 3][j + 2] = "-"
        mat[i + 3][j + 3] = "-"

    print("\n".join(["".join(line) for line in mat]))
def showState(state):
    print("Player:", state["players"][state["current"]])
    print("Target:", state["target"])
    print("Remaining:", state["remaining"])
    print("Tile:", state["tile"])
    print("Positions:")
    for i, pos in enumerate(state["positions"]):
        print(" - {}: {}".format(state["players"][i], pos))
    showBoard(state["board"])
def slideTiles(board, free, gate):
    start = GATES[gate]["start"]
    end = GATES[gate]["end"]
    inc = GATES[gate]["inc"]
    new_free = board[end]
    new_board = copy.deepcopy(board)
    dest = end
    src = end - inc
    while dest != start:
        new_board[dest] = new_board[src]
        dest = src
        src -= inc
    new_board[start] = free
    return new_board, new_free
def onTrack(index, gate):
    return index in range(
        GATES[gate]["start"],
        GATES[gate]["end"] + GATES[gate]["inc"],
        GATES[gate]["inc"],
    )










#############################################################################################################################

"""
EXEMPLE DE STATUS

{'players': ['thomas', 'top'], 'current': 0, 'positions': [0, 48], 'board': [{'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': False, 'E': True, 'S': True, 'W': True, 'item': 0}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 19}, {'N': False, 'E': True, 'S': True, 'W': True, 'item': 1}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': 13}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 23}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': 17}, {'N': True, 'E': True, 'S': True, 'W': False, 'item': 2}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': True, 'W': False, 'item': 3}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': False, 'E': True, 'S': True, 'W': True, 'item': 4}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': 16}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 5}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 22}, {'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 18}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 20}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': 15}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': True, 'W': False, 'item': 6}, {'N': False, 'E': True, 'S': True, 
'W': True, 'item': 21}, {'N': True, 'E': True, 'S': False, 'W': True, 'item': 7}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 8}, {'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 9}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': 
False, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': True, 'item': 10}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': 14}, {'N': True, 'E': True, 'S': False, 'W': True, 'item': 11}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 
'S': False, 'W': True, 'item': None}], 'tile': {'N': True, 'E': False, 'S': False, 'W': True, 'item': 12}, 'target': 10, 'remaining': [4, 4]}  

"""