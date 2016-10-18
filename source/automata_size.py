from dffa import DFFA
from findall import findall
import numpy as np

def automata_size(dffa):
    init = dffa.initial_state
    transition_matrix = dffa.frequency_transition_matrix[0]
    
    queue = np.array(init, dtype=int)
    valid = np.array(init, dtype=int)
    
    while len(queue) != 0:
        state = queue[0]
        tran = transition_matrix[state][:]
        tran = tran[np.nonzero(tran)]
        
        for i in range(0, len(tran)):
            next_tran = tran[i]
            if (len(findall(valid, next_tran)) == 0):
                queue = np.append(queue, next_tran)
                valid = np.append(valid, next_tran)
                
        queue = queue[1:len(queue)]
    size = len(valid)
    return size, valid