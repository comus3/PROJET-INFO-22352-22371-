import socket
import json
import copy
import random

####    ---FAIT---  ###### quelques fonctions de comm
####    ---A FAIRE--- #### 
# Fonction qui calcule le/les chemins vers trésor avec map comme arg
# fonction random qui prend en param un nombre n(nombre de choix) et rend un chiffre compris entre 0 et n-1

listnames = ["thomas","top",'nickel','super','ultra','bazarDuGrenier','leLApib','Bat','LEPHOENIX','equateur','tongo','tango','charlie','hebdo','lemecaudessusdemoiestnul','hexadecimal']
index = 0

responseToPing ={
       "response": "pong"
    }



def requestSubscribeStringGenerator(port,):
    global index
    matricule2 = str(22371 + index)
    request_subscribe = {
        "request": "subscribe",
        "port": port,
        "name": listnames[index],
        "matricules": ["22352", matricule2]
    }
    index = index+1
    req = json.dumps(request_subscribe)
    req = req.encode()

    return req


def jsonEncodeAndSend(message,s):
    message = json.dumps(message)
    message = message.encode()
    send =False
    while send:
        try:
            s.send(message)
            send = False
        except Exception as e:
            print("envoi échoué: ", e)

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




#############################################################################################################################