import numpy as np
import dffa
import copy
from findall import findall
from calculate_compatible_parameter import calculate_compatible_parameter
from AAlergia_compatible import AAlergia_compatible
from AAlergia_merge import AAlergia_merge

def AALERGIA(dffa, alpha,dpfa_orig):
    dffa_merged = copy.deepcopy(dffa) #be careful with copy!?!
    init_state = dffa.initial_state
    
    dffa_merged.RED = np.append(dffa_merged.RED, init_state)
        
    temp_blue = dffa.frequency_transition_matrix[0][init_state][:]
    temp_blue = temp_blue[np.nonzero(temp_blue)]
    
    dffa_merged.BLUE = np.append(dffa_merged.BLUE, temp_blue)
        
    while len(dffa_merged.BLUE) > 0:
        dffa_merged.BLUE =  np.msort(dffa_merged.BLUE)
        q_b = dffa_merged.BLUE[0]
        dffa_merged.BLUE = dffa_merged.BLUE[1:len(dffa_merged.BLUE)]
        promote = 1
        labels = dffa.state_labels[dffa_merged.RED]
        sb = dffa_merged.state_labels[q_b]
    
        same_label_index = findall(labels, sb) #not sure if this works!!
        
        for i in range(0, len(same_label_index)):
            q_r = dffa_merged.RED[same_label_index[i]]
            
            thresh = calculate_compatible_parameter(dffa, q_r, q_b, alpha)
            
            if (AAlergia_compatible(dffa, dpfa_orig, q_r, q_b, 1, 1, alpha, thresh)):
                dffa_merged = AAlergia_merge(dffa_merged, q_r, q_b)
                promote = 0
                break
            
        if promote == 1:
            dffa_merged.RED = np.append(dffa_merged.RED, q_b)
            
        #build new blue set
        qr_succ = dffa_merged.frequency_transition_matrix[0][dffa_merged.RED][:]
        qr_succ = qr_succ[np.nonzero(qr_succ)]
        
        diff = np.setxor1d(qr_succ, np.append(dffa_merged.RED, dffa_merged.BLUE)) #gets the new blue data (returns data that is not in intersection)
        ia = np.empty(0, dtype = int)
        
        for i in range(0, len(qr_succ)):
            for j in range(0, len(diff)):
                if (diff[j] == qr_succ[i]):
                    ia = np.append(ia, qr_succ[i])
        
        dffa_merged.BLUE = np.append(dffa_merged.BLUE, ia)   
        
    return dffa_merged