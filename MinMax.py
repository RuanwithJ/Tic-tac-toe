from copy import deepcopy
from Table import _check_game_over, _valid_positions
from math import inf
def evaluate(state, Max):
    if Max:
        if(state==0):
            return 0
        elif(state == 3):
            return inf/2
        elif(state == 1):
            return -inf          
        elif(state == 2):
            return inf
    else:
        if(state==0):
            return 0
        elif(state == 3):
            return -inf/2
        elif(state == 1):
            return -inf           
        elif(state == 2):
            return inf

def min_max(table, Max=True, alpha= -inf, beta=inf, node=9):
    state = _check_game_over(table)
    if(state!=0):
        return evaluate(state, max), (-1, -1)
    if(Max):
        best_val = -inf
        best_position = (7, 7)
        for posi in _valid_positions(table):
            t = deepcopy(table)
            t[posi[0]][posi[1]] = 2
            value, p = min_max(t, False, alpha, beta, node-1)
            if value >= best_val:
                best_val = value
                best_position = posi
            alpha = max(alpha, best_val)
            if(beta<=alpha):
                break   
           
    else:
        best_val = inf
        best_position = (7, 7)
        for posi in _valid_positions(table):
            t = deepcopy(table)
            t[posi[0]][posi[1]] = 1
            value, p = min_max(t, True, alpha, beta, node -1)
            if value <= best_val:
                    best_val = value
                    best_position = posi
            alpha = min(alpha, value)
            if(beta<=alpha):
                break          
    return best_val, best_position
