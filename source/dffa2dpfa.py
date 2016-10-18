from dffa import DFFA
from dpfa import DPFA
import numpy as np
from automata_size import automata_size

def dffa2dpfa(dffa):
    len_of_state = len(dffa.finite_set_of_states)
    alpha_len = len(dffa.alphabets)
    fsp = np.zeros(len_of_state)
    prob_trans_matrix = (dffa.frequency_transition_matrix[0],np.zeros((len_of_state, alpha_len)))
    a_size, valid = automata_size(dffa)
    ft = dffa.frequency_transition_matrix[1]

    for i in range(0, a_size):
        node = valid[i]
        terF = dffa.final_state_frequency[node]
        tran = ft[node][:]
        index = np.nonzero(tran)
        sub_tran = tran[index]
        freq_total = np.sum(sub_tran) + terF

        if freq_total > 0:
            prob_trans_matrix[1][node][index] = sub_tran / freq_total
            fsp[node] = terF/freq_total
        else:
            prob_trans_matrix[1][node][:] = np.zeros(alpha_len)
            
    return DPFA(dffa.finite_set_of_states, dffa.state_labels, dffa.alphabets, dffa.initial_state, fsp, prob_trans_matrix)