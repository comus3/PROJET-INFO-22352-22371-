import pytest
from main import *
from utils import *



stateOfExample = {'players': ['thomas', 'top'], 'current': 0, 'positions': [0, 48], 'board': [{'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': False, 'E': True, 'S': True, 'W': True, 'item': 0}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 19}, {'N': False, 'E': True, 'S': True, 'W': True, 'item': 1}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': 13}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 23}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': 17}, {'N': True, 'E': True, 'S': True, 'W': False, 'item': 2}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': True, 'W': False, 'item': 3}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': False, 'E': True, 'S': True, 'W': True, 'item': 4}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': 16}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 5}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 22}, {'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 18}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 20}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': 15}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': True, 'W': False, 'item': 6}, {'N': False, 'E': True, 'S': True, 
'W': True, 'item': 21}, {'N': True, 'E': True, 'S': False, 'W': True, 'item': 7}, {'N': False, 'E': False, 'S': True, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 8}, {'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': True, 'item': 9}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, {'N': True, 'E': False, 'S': True, 'W': 
False, 'item': None}, {'N': True, 'E': True, 'S': False, 'W': True, 'item': 10}, {'N': True, 'E': False, 'S': False, 'W': True, 'item': 14}, {'N': True, 'E': True, 'S': False, 'W': True, 'item': 11}, {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, {'N': True, 'E': False, 
'S': False, 'W': True, 'item': None}], 'tile': {'N': True, 'E': False, 'S': False, 'W': True, 'item': 12}, 'target': 10, 'remaining': [4, 4]}






def test_IA_valid():
    randome = IA("random","random")
    RDFCc = IA("RDFC","RDFC")
    negamaxx = IA("negamax","negamax")
    nwpi = IA("nwpi","nwpi")
    final = IA('MPST','MPST')
    for ia in listeIA:
        assert ia.think(stateOfExample)
