import pytest
from main import *
from utils import *
from collections import deque



stateOfExample = {'players': ['thomas', 'top'], 'current': 0, 'positions': [0, 48], 'board': [{'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': False, 'E': True, 'S': True, 'W': True, 'item': 0}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 19}, {'N': False, 'E': True, 'S': True, 'W': True, 'item': 1}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': 13}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 23}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': 17}, {'N': True, 'E': True, 'S': True, 'W': False, 'item': 2}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': True, 'W': False, 'item': 3}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': False, 'E': True, 'S': True, 'W': True, 'item': 4}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': 16}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 5}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 22}, {'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 18}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 20}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': 15}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': True, 'W': False, 'item': 6}, {'N': False, 'E': True, 'S': True, 
'W': True, 'item': 21}, {'N': True, 'E': True, 'S': False, 'W': True, 'item': 7}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 8}, {'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 9}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': 
False, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': True, 'item': 10}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': 14}, {'N': True, 'E': True, 'S': False, 'W': True, 'item': 11}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 
'S': False, 'W': True, 'item': None}], 'tile': {'N': True, 'E': False, 'S': False, 'W': True, 'item': 12}, 'target': 10, 'remaining': [4, 4]}



def path(start, end, board):
    def successors(index):
        res = []
        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            coords = add(index2coords(index), dir)
            dirName = DIRECTIONS[dir]["name"]
            opposite = DIRECTIONS[dirName]["opposite"]
            # breakpoint()
            if isCoordsValid(*coords):
                if board[index][dirName] and board[coords2index(*coords)][opposite]:
                    res.append(coords2index(*coords))
        return res
    try:
        res = BFS(start, successors, [end])
        print(res)
        return res
    except IndexError:
        return None
    
def BFS(start, successors, goals):
    q = deque()
    parent = {}
    parent[start] = None
    node = start
    while node not in goals:
        for successor in successors(node):
            if successor not in parent:
                parent[successor] = node
                q.append(successor)
        node = q.popleft()

    res = []
    while node is not None:
        res.append(node)
        node = parent[node]

    return list(reversed(res))


def isValid(move,state,newState):
    if not isSameTile(newState["tile"], move["tile"]):
        return False
    if move["gate"] not in "ABCDEFGHIJKL":
        return False
    if move["new_position"] not in range(49):
        return False
    if (
            path(
                newState["positions"][state["current"]],
                move["new_position"],
                newState["board"],
            )
            is None
        ):
            return False
    return True


def test_IA_valid():
    randome = IA("random","random")
    RDFCc = IA("RDFC","RDFC")
    negamaxx = IA("negamax","negamax")
    nwpi = IA("nwpi","nwpi")
    final = IA('MPST','MPST')
    for ia in listeIA:
        move = ia.think(stateOfExample)
        assert isValid(move,stateOfExample,move['state'])
def test_Utils():
    #pas besoin de tester mes fonctions utils si mes modeles dne font jamais derreurs
    return False
test_IA_valid()