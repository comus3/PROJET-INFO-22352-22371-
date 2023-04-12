import random
from utils import *
import time
import threading
import queue


# ### ---FAIT---    ######CREER CLASSE QUI VA CREER DES OBJETS IA, CHAQUE OBJET IA A UN ATRIBUT Active LES OBJETS SAPPELLLENT IA ET SONT RANGES DANS UNE LISTE
# aussi un attribut socket qui est son socket
# chaque objet ia possede uun attribut modèle qui pinte vers la fonction a utiliser pour calculer le next move
# ecdrire le premier modèle
# negamax qui marche
# MPST
# ### ---A FAIRE--- ######
# debut


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

smollList = []
strategicMessage = 'Perfectly balanced, as all things should be'
offenciveMessage= "you ain't going anywhere son"
defenciveMessage= 'GO GO GO'
start_time = 0

def returnListeIA():
    return listeIA


##########################################################################################################  CLASSE  #####################################################################

class IA:#create ai and assign its model
    def __init__(self,modele,name):
        global listeIA
        self.active = True
        if modele == "manuel":
            self.modele = Manuel([])
        elif modele == "random":
            self.modele = Random([])
        elif modele == "RDFC":
            self.modele = RDFC([])
        elif modele == "negamax":
            self.modele = Negamax([])
        elif modele == "nwpi":
            self.modele = Nwpi([])
        elif modele == "negamaxUlt":
            self.modele = NegamaxUltimate([])
        elif modele == "MPST":
            self.modele = MPST([])
        else:
            self.modele = Random([])
        listeIA.append(self)
        self.name = name
    def __str__(self):
        print("je suis l'ia associée au port" + str(self.port) + "  mon nom est : "+ self.name)

    def think(self,msg):#call its models method for crezaating a new move
        global start_time
        start_time = time.time()
        self.state = msg
        print("message pour "+self.name)
        # print("status:\n"+str(msg))
        ##################print("voici le graphe des moves dispo:     " + transformPath(msg))
        # showState(msg)
        return self.modele.nextMove(self.state,self.name)

    def kill(self):
        self.active = False
        
####################### MODèLES IA  ################################
#all models below are now obselete
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
    def nextMove(self,state,name):#create a valid move and return it
        tile = random_turn_tile(state['tile'])
        while True:
            gateIndex = random.randint(0,11)
            gate = gateList[gateIndex]
            if GATES[gate]['end'] not in state['positions']:
                break
        state['board'],newTile = slideTiles(state['board'],tile,gate)
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
        ValidDirections = validNewPos(state)
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
        time.sleep(2)##############    /!!!!!!\ il faut absolument mettre cette ligne en com pdt le championna sinon on est morts 
        return output
    
#all models below are now obselete
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
        self.depth = 2     # /!\ MODIFIER La PRofondeur ICI /!\ attention elle doit tjs etre paire sionon le code ne fait plus de sens
        self.mode = 'intesive'  
    def nextMove(self,state,name):
        bestMove = None
        bestValue = float('-inf')
        for move in availableMoves(state):
            newState = move['state']
            if move['new_position'] == treasurePos(move['state']):
                bestMove = move
                break
            value = negamax(newState, self.depth - 1)
            if value > bestValue:
                bestValue = value
                bestMove = move
        if bestMove == None:
            newModel = Random(state)
            bestMove = newModel.nextMove(state)
            return output(bestMove)
        print('best value is :  ' + str(bestValue))
        move ={
            "tile": bestMove['tile'],
            "gate": bestMove['gate'],
            "new_position": bestMove['new_position']
        }
        return output(move)


class Nwpi:
    def __init__(self, state, player = 1, timeout=0.2):
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


class NegamaxUltimate:
    #A FAIRE
# alpha encadrement . des qu'un thread se rend compte que ses valeurs sont en dessous de la best val il se stoppe
# vu quon cherche le min parmis les moves possibles apres move enemi et pusi on reprend le max parmis cest mins
#si une valeur d'éval est en dessous du min de ce qu'a return un des threads il se coupe instant pour écvonomiser de la 
# place

# ne pas call tous les threads en u,ne fois, call les threads suivants des que un thread est fermé un nouveau est ouvert mais 
# attention un thread n'est pas fermé seulement lorsque il return mais aussi lorsque il se rend compte que ca sert a rien de 
# continuer

# ducps demander au prof prq je vois pas comment faire enft
    def __init__(self,state):
        self.state = state
        self.depth = 2
        self.mode = 'NOTtimed'####      if not necessairy to give outup after 3secs
    def nextMove(self,state,name):
        bestValue = float('-inf')
        result_queue = queue.Queue()

        threads = []
        inputList = availableMoves(state)
        # print(str(len(inputList)))
        for move in inputList:
            if move['new_position'] == treasurePos(move['state']):return output(move)
            moveThread = threading.Thread(target=lambda q,arg1:q.put(negamaxUlt(arg1)),args=(result_queue,move['state']))
            threads.append(moveThread)
            moveThread.start()
        if self.mode == "timed":
            start_time = time.monotonic()
        for thread in threads:
            if self.mode == "timed":
                thread.join(max(0, 3 - (time.monotonic() - start_time)))
            else:
                thread.join()
                resultat = result_queue.get()
                if resultat>bestValue:
                    bestValue = resultat
                    bestMove = inputList[result_queue.qsize()-1]
                # if bestValue == 1000:
                #     return output(inputList[result_queue.qsize()-1])
        return output(bestMove)

#final workjng model is here
class MPST:# Modèle final.
    def __init__(self,state):
        self.state = state 
        self.cuts = 1   #change number of cuts
        self.mode = 'rush'  #here chose first mode
        self.bestValue = 0  #init best value at 0
        self.bestMove = None    #init best move None
        self.running = False    #start off
        self.lastMove = None 
        self.lastValue = 0
        self.lastEvalMode = self.mode
    def nextMove(self,state,name):
        class Tree:# class tree is used to create a tree containing all the possibilities to iterit through using MPST
            def __init__(self,value):
                self.value = value
                self.kids = None
                self.attachedState = None
            def addKids(self,kids):
                self.kids = kids
            def returnKids(self):
                return self.kids
            def addState(self,state):
                self.attachedState = state
            def returnState(self):
                return self.attachedState
            def popKid(self,index):
                self.kids.pop(index)
            def returnValue(self):
                return self.value
        def threadBrains(init):##### target fonction used if mode isnt rush
            def evalRatata(state):#evaluate fonction used if treasure pos in new pos two moves down the road
                porteeEnemi = returnPortee(state)
                return 850-porteeEnemi
            def evalState(state,newPos):#eval function
                def offenciveEval(state,newPos):#objective is to reduce enemy range
                    recherche = treasurePos(state)
                    distance = returnDistanceMin(recherche,newPos)
                    porteeEnemi = returnPortee(state)
                    return 450-porteeEnemi-distance
                def defenciveEval(state,newPos):#objective is to run towards the targe
                    recherche = treasurePos(state)
                    distance = returnDistanceMin(recherche,newPos)
                    return 400-distance
                def strategicEval(state,newPos):#objective is to get closer to target while preventing enemy from moving freely
                    recherche = treasurePos(state)
                    distance = returnDistanceMin(recherche,newPos)
                    porteeEnemi = returnPortee(state)
                    if porteeEnemi>30:
                        return 420-(2*distance)-porteeEnemi
                    else:
                        return 400-(2*distance)
                if self.mode == 'offencive':
                    return offenciveEval(state,newPos)
                elif self.mode == 'defencive':
                    return defenciveEval(state,newPos)
                elif self.mode == 'strategic':
                    return strategicEval(state,newPos)
                else:
                    return strategicEval(state,newPos)
            def iterGates(state):#iterate through possible gates to return list of available gates
                returnList = []
                for gate in GATES:
                    if GATES[gate]['end'] not in state['positions']:
                        returnList.append(Tree(gate))
                return returnList
            possibilityTree = []
            for move in init:#iterate through move list to generate MPST. Create tree ojects for eazch possible tile then give a list of gates as kids to all of them
                state = move['state']
                temp = []
                shorTile = {}
                smollPossibilityTree = []
                for cardinale in tuileCouloir:#ici j'utilise tuile couloir parceque je veux juste iterer les cardinaux mais on peut faire "plus simple"(je trouve que ca change rien)
                    temp.append(state['tile'][cardinale])
                    shorTile[cardinale] = state['tile'][cardinale]
                if all(temp) or not any(temp):#just in case but never called
                    smollPossibilityTree = [Tree(state['tile'])]
                    smollPossibilityTree[0].addKids(iterGates(state))
                elif isSameTile(shorTile,tuileCouloir):#if free tile is a corridor, only two rotations possible
                    smollPossibilityTree.append(Tree(state['tile']))
                    smollPossibilityTree[0].addKids(iterGates(state))
                    state['tile'] = turn_tile(turn_tile(state['tile']))
                    smollPossibilityTree.append(Tree(state['tile']))
                    smollPossibilityTree[1].addKids(iterGates(state))
                else:#iterate trough 4 tiles(4rotations)
                    for cardinal in tuileCouloir:
                        state['tile'] = turn_tile(state['tile'])
                        smollPossibilityTree.append(Tree(state['tile']))
                        smollPossibilityTree[len(smollPossibilityTree)-1].addKids(iterGates(state))
                possibilityTree.append(smollPossibilityTree)

            while self.running:#this is where we are going to iterate through the MPST
                bestMoveIndex = 0
                if possibilityTree == []:
                    self.running = False#just to catch a bug where MPST is empty for some reason
                for move in possibilityTree:#evaluate one of each next move one by one
                    if move == []:#if MPST for this move is empty, just pass over it
                        bestMoveIndex = bestMoveIndex + 1
                        continue
                    tile = random.randint(0,len(move)-1)
                    if move[tile].returnKids() == []:#if we are done iteratign through all pssibilities with this tile, pop it
                        #pop ici les trucs de tile
                        move.pop(tile)
                        bestMoveIndex = bestMoveIndex + 1
                        continue
                    gate = random.randint(0,len(move[tile].returnKids())-1)
                    gateState = move[tile].returnKids()[gate].returnState()
                    if gateState == None:#it we have not calcuated the state for this gate and tile move, calcilate it and associate it to this move
                        newState = update(init[bestMoveIndex]['state'],{'tile':move[tile].returnValue(),'gate':move[tile].returnKids()[gate].returnValue()})
                        move[tile].returnKids()[gate].addState(newState)
                    if move[tile].returnKids()[gate].returnKids() == None:#if we have not calculated the new possible pos in this state, create them
                        move[tile].returnKids()[gate].addKids(validNewPos(move[tile].returnKids()[gate].returnState()))
                        recherche = treasurePos(move[tile].returnKids()[gate].returnState())
                        if recherche in move[tile].returnKids()[gate].returnKids():#if for this move we realise that we can win, evaluate it as a win which is over any other eval
                            evaluated = (evalRatata(move[tile].returnKids()[gate].returnState()),bestMoveIndex)
                            move[tile].popKid(gate)#since we can win, all other newpos are stupid so just remove all of them from MPST
                            lock.acquire()
                            if evaluated[0]>self.bestValue:
                                self.bestValue = evaluated[0]
                                self.bestMove = init[bestMoveIndex]
                            lock.release()
                            bestMoveIndex = bestMoveIndex + 1
                            continue
                    elif move[tile].returnKids()[gate].returnKids() == []:#if we are done iterating through all pssibilities with this gate, pop it
                        move[tile].popKid(gate)
                        bestMoveIndex = bestMoveIndex + 1
                        continue
                    evaluated = (evalState(move[tile].returnKids()[gate].returnState(),move[tile].returnKids()[gate].returnKids()),bestMoveIndex)#tester ici le move gate et pop gate
                    move[tile].popKid(gate)
                    lock.acquire()
                    if evaluated[0]>self.bestValue:
                        self.bestValue = evaluated[0]
                        self.bestMove = init[bestMoveIndex]
                    lock.release()
                    bestMoveIndex = bestMoveIndex + 1
        def threadSmallBrains(init):#activated if we want to unstuck the ai
            while self.running:#objective is to augment the range from treasure pos to maybe create a path towards
                for move in init:
                    newPos = move['new_position']
                    recherche = treasurePos(move['state'])
                    porteeEnemi = returnPortee(state)
                    distance = absoluteDist(newPos,recherche)
                    porteeTresor = returnPorteeTresor(state)
                    if porteeEnemi>30:
                        if recherche == newPos:
                            score = 480-distance+porteeTresor
                        else:
                            score = 100-distance+porteeTresor
                    else:
                        if recherche == newPos:
                            score = 500-distance+porteeTresor
                        else:
                            score = 400-distance+porteeTresor
                    if self.running:
                        lock.acquire()
                        if score>self.bestValue:
                            self.bestMove = move
                            self.bestValue = score
                        lock.release
                    else:break
                self.running = False

        
        lock = threading.Lock()#create a lock so threads dont try to use value at smae time
        evalThreads = []
        self.bestValue = float('-inf')
        self.bestMove = None
        moveList = availableMoves(state)
        if len(moveList) == 1:#if available moves returns only one move its bc its a winning move
            return output(moveList[0],"don't mind if I do")
        inc = len(moveList)//(self.cuts+1)
        ind = 0
        self.running = True#start the thinking proceesss
        for cut in range(self.cuts+1):#divide the move list into cuts+1 parts 
            next = ind+inc
            section = moveList[ind:next]
            ind = next
            if self.mode == 'rush':
                evalThread = threading.Thread(target=threadSmallBrains,args=(section,))#activate smollbrain with its section
            else:
                evalThread = threading.Thread(target=threadBrains,args=(section,))#activztte big btzain wtih its secion
            evalThreads.append(evalThread)
        for thread in evalThreads:#activate al threads
            thread.start()
        elapsedTime = time.time()-start_time
        while elapsedTime<2.9:#wait until 3 seconds passed
            elapsedTime = time.time()-start_time
        self.running = False#cut off all processes
        # for thread in evalThreads:
        #     thread.join(0.01)
        if self.bestMove == None:#catch none error and return random move
            print("quoi? Aucun move trouvé? Vite!! call random")
            newModel = Random(state)
            bestMoveRandom = newModel.nextMove(state,name)
            self.lastEvalMode = "random"
            return (bestMoveRandom)
        #strategies switching module
        if self.lastValue>(self.bestValue-1) and self.mode == 'strategic':
            self.mode = 'rush'
        elif self.lastEvalMode == 'rush':
            self.mode = 'strategic'
        elif self.bestMove['state']['remaining'][1-self.bestMove['state']['current']]-self.bestMove['state']['remaining'][self.bestMove['state']['current']]>1:
            if self.lastEvalMode == 'offencive':self.mode = 'strategic'
            elif self.lastEvalMode == 'strategic':self.mode == 'offencive'
            else:self.mode = 'offencive'
        else: self.mode = 'strategic'
        if self.lastMove==self.bestMove:
            self.mode = 'random'
        self.lastEvalMode = self.mode
        self.lastValue = self.bestValue
        self.lastMove = self.bestMove
        print('processus de calcul terminé en : ' + str(elapsedTime) +'\n avec un score de :     '+str(self.bestValue))
        if self.lastEvalMode == 'offencive':return output(self.bestMove,offenciveMessage)
        elif self.lastEvalMode == 'defencive':return output(self.bestMove,defenciveMessage)
        elif self.lastEvalMode == 'strategic':return output(self.bestMove,strategicMessage)
        elif self.lastEvalMode == 'rush':return output(self.bestMove,"I need to pee so let's end this fast")
        else:
            print('EEERRRREEEEEUURR DE  MOODEEEE WTFFFF.???? (impossible)           ' + str(self.mode))
            return output(self.bestMove)

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
