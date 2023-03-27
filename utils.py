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



def requestSubscribeStringGenerator(port,):
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


def jsonEncodeAndSend(message,s):
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
    


def validMoves(status,ianame):
    validPositions = []
    player0or1 = 0
    for i in range(2):
        if status['players'][i] == ianame:
            player0or1 = i
    playerPos = status['positions'][player0or1]
    if playerPos>6 and status['board'][playerPos]['N']:
        validPositions.append(playerPos-7)
    if playerPos<42 and status['board'][playerPos]['S']:
        validPositions.append(playerPos+7)
    if (playerPos%7)!=0 and status['board'][playerPos]['W']:
        validPositions.append(playerPos-1)
    if ((playerPos+1)%7)!=0 and status['board'][playerPos]['E']:
        validPositions.append(playerPos+1)
    validPositions.append(playerPos)
    return validPositions
        

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




#############################################################################################################################

"""
EXEMPLE DE STATUS

{'players': ['thomas', 'top'], 'current': 0, 'positions': [0, 48], 'board': [{'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': False, 'E': True, 'S': True, 'W': True, 'item': 0}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 19}, {'N': False, 'E': True, 'S': True, 'W': True, 'item': 1}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': 13}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 23}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': 17}, {'N': True, 'E': True, 'S': True, 'W': False, 'item': 2}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': True, 'W': False, 'item': 3}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': False, 'E': True, 'S': True, 'W': True, 'item': 4}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': 16}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 5}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 22}, {'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 18}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 20}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': 15}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': True, 'W': False, 'item': 6}, {'N': False, 'E': True, 'S': True, 
'W': True, 'item': 21}, {'N': True, 'E': True, 'S': False, 'W': True, 'item': 7}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 8}, {'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 9}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': 
False, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': True, 'item': 10}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': 14}, {'N': True, 'E': True, 'S': False, 'W': True, 'item': 11}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 
'S': False, 'W': True, 'item': None}], 'tile': {'N': True, 'E': False, 'S': False, 'W': True, 'item': 12}, 'target': 10, 'remaining': [4, 4]}  

"""