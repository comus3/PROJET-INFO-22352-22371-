import socket
import json
import copy
import random
from Dijkstra import *

####    ---FAIT---  ###### quelques fonctions de comm
####    ---A FAIRE--- #### 
# Fonction qui calcule le/les chemins vers trésor avec map comme arg
# fonction random qui prend en param un nombre n(nombre de choix) et rend un chiffre compris entre 0 et n-1

listnames = []
for i in range(500):
    listnames.append('IA'+str(i))
#listnames = ["thomas","top",'nickel','super','ultra','bazarDuGrenier','leLApib','Bat','LEPHOENIX','equateur','tongo','tango','charlie','hebdo','lemecaudessusdemoiestnul','hexadecimal']
index = 0

onTrackDict = {0: ['A', 'I', 'L', 'D'], 1: ['A', 'I', 'D', 'L'], 2: ['A', 'I', 'B', 'H', 'D', 'L'], 3: ['B', 'H', 'D', 'L'], 4: ['B', 'H', 'C', 'G', 'D', 'L'], 5: ['C', 'G', 'D', 'L'], 6: ['C', 'G', 'D', 'L'], 7: ['L', 'D', 'A', 'I'], 8: ['L', 'D', 'A', 'I'], 9: ['A', 'I', 'B', 'H', 'L', 'D'], 10: ['B', 'H', 'L', 'D'], 11: ['B', 'H', 'C', 'G', 'L', 'D'], 12: ['C', 'G', 'L', 
'D'], 13: ['C', 'G', 'L', 'D'], 14: ['L', 'D', 'K', 'E', 'A', 'I'], 15: ['L', 'D', 'K', 'E', 'A', 'I'], 16: ['L', 'D', 'K', 'E', 'A', 'I', 'B', 'H'], 17: ['L', 'D', 'E', 'K', 'B', 'H'], 18: ['B', 'H', 'C', 'G', 'L', 'D', 'K', 'E'], 19: ['C', 
'G', 'L', 'D', 'K', 'E'], 20: ['C', 'G', 'D', 'L', 'E', 'K'], 21: ['K', 'E', 'A', 'I'], 22: ['K', 'E', 'A', 'I'], 23: ['A', 'B', 'I', 'H', 'K', 'E'], 24: ['B', 'H', 'K', 'E'], 25: ['K', 'E', 'B', 'H', 'C', 'G'], 26: ['K', 'E', 'C', 'G'], 27: 
['K', 'E', 'C', 'G'], 28: ['K', 'E', 'J', 'F', 'A', 'I'], 29: ['K', 'E', 'J', 'F', 'A', 'I'], 30: ['K', 'E', 'J', 'F', 'A', 'I', 'B', 'H'], 31: ['K', 'E', 'J', 'F', 'B', 'H'], 32: ['K', 'E', 'J', 'F', 'B', 'C', 'G', 'H'], 33: ['K', 'E', 'J', 
'F', 'C', 'G'], 34: ['K', 'E', 'J', 'F', 'C', 'G'], 35: ['J', 'F', 'A', 'I'], 36: ['J', 'F', 'A', 'I'], 37: ['J', 'F', 'A', 'I', 'B', 'H'], 38: ['J', 'F', 'B', 'H'], 39: ['J', 'F', 'B', 'H', 'C', 'G'], 40: ['J', 'F', 'C', 'G'], 41: ['J', 'F', 'C', 'G'], 42: ['J', 'F', 'A', 'I'], 43: ['J', 'F', 'I', 'A'], 44: ['J', 'F', 'I', 'A', 'B', 'H'], 45: ['J', 'F', 'B', 'H'], 46: ['J', 'F', 'B', 'H', 'C', 'H'], 47: ['J', 'F', 'C', 'G'], 48: ['J', 'F', 'C', 'G']}

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
    "N": {"coords": (-1, 0), "inc": -7, "opposite": "S","sides":("E","W")},
    "S": {"coords": (1, 0), "inc": 7, "opposite": "N","sides":("E","W")},
    "W": {"coords": (0, -1), "inc": -1, "opposite": "E","sides":("N","S")},
    "E": {"coords": (0, 1), "inc": 1, "opposite": "W","sides":("N","S")},
    (-1, 0): {"name": "N"},
    (1, 0): {"name": "S"},
    (0, -1): {"name": "W"},
    (0, 1): {"name": "E"},
}

tuileCouloir = {'N':True,'E':False,'S':True,'W':False}

rangeeHaut = [0,1,2,3,4,5,6]
rangeeBas = [42,43,44,45,46,47,48]
rangeeGauche = [0,7,14,21,28,35,42]
rangeeDroite = [6,13,20,27,34,41,48]
stackedExceptionDico={
    'N':rangeeHaut,
    'E':rangeeDroite,
    'S':rangeeBas,
    'W':rangeeGauche
}
##############################################################################################################


####Réseau
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
    

####Négamax
def whichGates(positions):
    outPut = []
    for pos in positions:
        for gate in onTrackDict[pos]:
            if gate not in outPut:
                outPut.append(gate)
    return outPut
def validNewPos(playerPos,board,stacked = None):#return une liste de nouvelles positions valides sur la carte ENTREE: Player position on board and the board
    validPositions = []
    #J'ai commencé a réécrire cette fonction car il y a de la place pour l'optimisation
    """
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
    """
    if stacked != None:
        newTile = stacked
    else:
        newTile = stackedTile(playerPos,board)
    for cardinal in tuileCouloir:
        if newTile[cardinal]:
            newPos = playerPos + DIRECTIONS[cardinal]['inc']
            #encore une ancienne version mais maintenant une partie du travail est prémachée par stacked
            """
            if cardinal == 'W' and (playerPos%7)!=0 and newPos in range(49):
                validPositions.append(newPos)
            elif cardinal == 'E' and ((newPos)%7)!=0 and newPos in range(49):
                validPositions.append(newPos)
            else:
                if newPos in range(49):
                    validPositions.append(newPos)
            """
            if newPos in range(49):
                validPositions.append(newPos)
    validPositions.append(playerPos)
    return validPositions
def treasurePos(status):#return la position du trésor recherché
    for i in range(49):
        if status['board'][i]['item'] == status['target']:
            return int(i)
        return(90)   
def returnPos(status):
    return status['positions'][status['current']]
def returnEnemyPos(status):
    return status['positions'][1-status['current']]
def availableMoves(state):#return les moves possibles pour apres aller itérer dedans
    moves = []
    temp = []
    shorTile = {}
    newPos = validNewPos(returnPos(state),state['board'])
    changeGate = whichGates(newPos)
    def iterGates(state,newPos):
        for gate in GATES:
            if GATES[gate]['end'] not in state['positions']:
                move ={
                "tile": state['tile'],
                "gate": gate
                }
                tempState = update(state,move)
                if gate in changeGate:
                    newPos = validNewPos(returnPos(tempState),tempState['board'])
                for i in newPos:
                    move['new_position'] = i
                    move['state'] = tempState
                    res = copy.deepcopy(move)
                    moves.append(res)
    for cardinale in tuileCouloir:#ici j'utilise tuile couloir parceque je veux juste iterer les cardinaux mais on peut faire "plus simple"(je trouve que ca change rien)
        temp.append(state['tile'][cardinale])
        shorTile[cardinale] = state['tile'][cardinale]
    if all(temp) or not any(temp):
        iterGates(state,newPos)
    elif isSameTile(shorTile,tuileCouloir):
        for i in range(2):
            state['tile'] = turn_tile(turn_tile(state['tile']))
            iterGates(state,newPos)
    else:
        for cardinal in tuileCouloir:
            state['tile'] = turn_tile(state['tile'])
            iterGates(state,newPos)
    return moves
def evalState(state,player):#return le poids de la situation
    #ANCIENNE VERSION DU CALCUL DE POIDS MAINTENANT OBSCELETTE
    """
    debut = returnPos(state)
    g = transformPath(state['board'],debut)
    dijkstra(g, g.get_vertex(debut))
    end = g.get_vertex(treasurePos(state))
    if end != None:
        path = [end.get_id()]
        shortest(end, path)
        if type(path) != None:
            printShortestPath(path)
            printGraph(g)
            return 0-(player*len(path))
        else:
            if player == 1:return 1000
            else : return 100
    else:
        if player == 1:return 1000
        else : return 100
    """
    #création du premier graphe
    debutA = returnPos(state)
    gA = transformPath(state['board'],debutA)
    dijkstra(gA, gA.get_vertex(debutA))
    endPos = treasurePos(state)
    end = gA.get_vertex(endPos)
    if end != None:
        weight = end.get_distance()
    else:
        xa,ya = index2coords(debutA)
        xb,yb = index2coords(endPos)
        weight = abs(xb-xa+yb-ya)*2
    """ici, nous pouvons print le graphe obtenu ainsi que calculer le path le plus court vers end avec la methode path(prendre exemple sur l'ancienne version ci dessus)."""
    #création du deuxième graphe
    debutB = returnEnemyPos(state)
    gB = transformPath(state['board'],debutB)
    dijkstra(gB, gB.get_vertex(debutB))
    porteeEnemi = 0
    for i in gB:
        porteeEnemi = porteeEnemi + i.get_distance()
    return player*(1000-(porteeEnemi+(3*weight)))*(1000-weight)
def update(state,move):
    a,b = slideTiles(state['board'],move['tile'],move['gate'])
    state['board'] = a
    state['tile'] = b
    new_positions = []
    for position in state["positions"]:
        if onTrack(position, move['gate']):
            if position == GATES[move['gate']]["end"]:
                new_positions.append(GATES[move['gate']]["start"])
                continue
            new_positions.append(position + GATES[move['gate']]["inc"])
            continue
        new_positions.append(position)
    state["positions"] = new_positions
    return state
def transformPath(board,debut):
    def recursiveLinks(pos,board,longueur,dir):
        stacked = stackedTile(pos,board)
        if not stacked[dir]:
            return (pos,longueur,DIRECTIONS[dir]['opposite'])
        else:
            if not(stacked[DIRECTIONS[dir]['sides'][0]] and stacked[DIRECTIONS[dir]['sides'][1]]):
                newPos = pos +DIRECTIONS[dir]['inc']
                if newPos in validNewPos(pos,board,stacked):
                    return recursiveLinks(newPos,board,longueur+1,dir)
                else:
                    return (pos,longueur,DIRECTIONS[dir]['opposite'])
            else:
                return (pos,longueur,DIRECTIONS[dir]['opposite'])
    def nodes(pos,board,exception=None):
        stacked = stackedTile(pos,board)
        validNewPositions = validNewPos(pos,board,stacked)
        for card in tuileCouloir:
            if card == exception:
                continue
            if stacked[card]:
                newPos = pos +DIRECTIONS[card]['inc']
                if newPos in validNewPositions:
                    a,b,c = recursiveLinks(newPos,board,1,card)
                    if a not in g.vert_dict:
                        g.add_vertex(a)
                        g.add_edge(pos,a,b)
                        nodes(a,board,c)
                    else:
                        g.add_edge(pos,a,b)
    g = Graph()
    g.add_vertex(debut)
    nodes(debut,board)
    return g
def negamax(state, depth, player):
    if depth == 0:
        return evalState(state,player)
    best_value = float('-inf')
    for move in availableMoves(state):
        newState = move['state']
        value = negamax(newState, depth - 1, -player)
        best_value = max(best_value, value)
    return best_value
def stackedTile(pos,board):
    newTile = {}
    for cardinal in tuileCouloir:
        if pos in stackedExceptionDico[cardinal]:
            newTile[cardinal] = False
        else:
            tilePos = pos+DIRECTIONS[cardinal]['inc']
            liste = [board[pos][cardinal]]
            if tilePos in range(49):
                liste.append(board[tilePos][DIRECTIONS[cardinal]['opposite']])
            newTile[cardinal] = all(liste)
    return newTile


#section print
def printGraph(graph):
    print('Graph data:')
    for v in graph:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print( '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))
def printShortestPath(path):
    print ('The shortest path : %s' %(path[::-1]))


#ANCIENNE VERSION de transform graph(plus utilisée car classe dans Dijkstra meilleure et plus opti)
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
    outPut = (new_board, new_free)
    return outPut
def onTrack(index, gate):
    return index in range(
        GATES[gate]["start"],
        GATES[gate]["end"] + GATES[gate]["inc"],
        GATES[gate]["inc"],
    )

def index2coords(index):
    return index // 7, index % 7
def coords2index(i, j):
    return i * 7 + j
def isCoordsValid(i, j):
    return i >= 0 and i < 7 and j >= 0 and i < 7
def add(A, B):
    return tuple(a + b for a, b in zip(A, B))












#############################################################################################################################

"""
EXEMPLE DE STATUS

{'players': ['thomas', 'top'], 'current': 0, 'positions': [0, 48], 'board': [{'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': False, 'E': True, 'S': True, 'W': True, 'item': 0}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 19}, {'N': False, 'E': True, 'S': True, 'W': True, 'item': 1}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': 13}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 23}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': 17}, {'N': True, 'E': True, 'S': True, 'W': False, 'item': 2}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': True, 'W': False, 'item': 3}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': False, 'E': True, 'S': True, 'W': True, 'item': 4}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': 16}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 5}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 22}, {'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 18}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 20}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': 15}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': True, 'W': False, 'item': 6}, {'N': False, 'E': True, 'S': True, 
'W': True, 'item': 21}, {'N': True, 'E': True, 'S': False, 'W': True, 'item': 7}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 8}, {'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 9}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': 
False, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': True, 'item': 10}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': 14}, {'N': True, 'E': True, 'S': False, 'W': True, 'item': 11}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 
'S': False, 'W': True, 'item': None}], 'tile': {'N': True, 'E': False, 'S': False, 'W': True, 'item': 12}, 'target': 10, 'remaining': [4, 4]}  

"""