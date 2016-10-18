from findall import findall
import numpy as np

def AAlergia_merge(dffa, qr, qb):
    #q,i = findall(dffa.frequency_transition_matrix[0],qb)
    #dffa.frequency_transition_matrix[0][q][i] = qr

    indices = np.where(dffa.frequency_transition_matrix[0] == qb)
    dffa.frequency_transition_matrix[0][indices] = qr

    red=[qr]
    blue=[qb]

    while len(blue) > 0:
        qr=int(red[0])
        qb=int(blue[0])
        red=red[1:len(red)]
        blue=blue[1:len(blue)]
        
        dffa.final_state_frequency[qr] = dffa.final_state_frequency[qr] + dffa.final_state_frequency[qb]
        
        tran_r = dffa.frequency_transition_matrix[0][qr][:]
        tran_b = dffa.frequency_transition_matrix[0][qb][:]
        
        freq_r = dffa.frequency_transition_matrix[1][qr][:]
        freq_b = dffa.frequency_transition_matrix[1][qb][:]
        
        tran_r_zero = findall(tran_r, 0)
        
        same_tran = np.intersect1d(np.nonzero(tran_r), np.nonzero(tran_b))
        diff_tran = np.intersect1d(tran_r_zero, np.nonzero(tran_b))
    
        if len(diff_tran) == 0:
            diff_tran = np.empty(0, dtype=int)
            
        if len(same_tran) == 0:
            same_tran = np.empty(0, dtype=int)
    
        dffa.frequency_transition_matrix[1][qr][same_tran] = freq_r[same_tran] + freq_b[same_tran]
        
        red = np.append(red, tran_r[same_tran])
        blue = np.append(blue, tran_b[same_tran])
        
        dffa.frequency_transition_matrix[0][qr][diff_tran] = tran_b[diff_tran]
        dffa.frequency_transition_matrix[1][qr][diff_tran] =  freq_b[diff_tran]
    
    return dffa