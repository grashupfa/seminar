import numpy as np
from findall import findall
from sort_string_wfs import sort_string_wfs
from get_last_symbol import get_last_symbol
from dffa import DFFA

# build FPTA 
def build_ftpa_data(trainingset_np, alphabets):
    alphabet_map = {}
    for i in range(0, len(alphabets)):
        alphabet_map[alphabets[i]] = i
    
    string_set_u_sorted, m, n = np.unique(trainingset_np, return_index = True,return_inverse = True) #achtung! n hier ist (n+1) in matlab
    string_count, bin_edges = np.histogram(n, len(n)) #achtung, der 0er an stelle 26 ist hier um 1 verschoben
    
    prefixes = np.copy(string_set_u_sorted)
    prefixes = np.append(prefixes, '')
    
    final_stat_freq = np.copy(string_count[np.nonzero(string_count)])
    final_stat_freq = np.append(final_stat_freq, 0)
    
    for i in range (0, len(string_set_u_sorted)):
        seq = string_set_u_sorted[i]                
        ind = findall(seq, ',')
                    
        for j in range(len(ind)-1, -1, -1):
            substr = seq[0:ind[j]+1]
            
            if not substr in prefixes[:]:             
                prefixes = np.append(prefixes, substr)
                    
    #sort string width first
    final_stat_freq = np.append(final_stat_freq, np.zeros(len(prefixes)-len(final_stat_freq)))
    prefixes, IX = sort_string_wfs(prefixes)
    final_stat_freq = final_stat_freq[IX]
    pref_length = len(prefixes)
    alpha_length = len(alphabets)
    labels = np.empty(1, dtype=str)
    labels[0] = ''
    set_of_states = np.zeros(pref_length, dtype = int)
    for i in range(0, len(set_of_states)):
        set_of_states[i] = i
    init_stat_freq = np.zeros(pref_length)
    init_stat_freq[0] = len(trainingset_np)
    freq_trans_matrix = (np.zeros((pref_length, alpha_length), dtype = int),np.zeros((pref_length, alpha_length), dtype = int))
    predecessorLink = np.zeros(pref_length, dtype=int)
    predecessorLink[0] = -1
    
    for i in range (1, pref_length):
        seq = prefixes[i]
        ind = findall(seq, ',')    
        if len(ind) == 1:
            predecessorLink[i] = 0
        else:
            predecessorLink[i] = np.where(prefixes == seq[0:ind[-2]+1])[0][0] #should only be one value!
    
        labels = np.append(labels, get_last_symbol(seq, ind))
            
    for i in range (1, pref_length):
        flowLoad = final_stat_freq[i]
        alpha_index = alphabet_map[labels[i]]
        current = i
        predecessor = predecessorLink[current]
        
        freq_trans_matrix[0][predecessor][alpha_index] = current
        freq_trans_matrix[1][predecessor][alpha_index] = freq_trans_matrix[1][predecessor][alpha_index] + flowLoad
        
        current = predecessor
        predecessor = predecessorLink[current]
        
        while (flowLoad and predecessor != -1):
            index = findall(freq_trans_matrix[0][predecessor][:] ,current)
            if (len(index) == 1):
                freq_trans_matrix[1][predecessor][index] = freq_trans_matrix[1][predecessor][index[0]] + flowLoad
            else:
                break
            current = predecessor
            predecessor = predecessorLink[current]
    
    first = freq_trans_matrix[0][0][:]    
    new_init = first[np.nonzero(first)]
    
    print('finished_FTPA')
    
    return DFFA(set_of_states, labels, alphabets, new_init, init_stat_freq, final_stat_freq, freq_trans_matrix), string_set_u_sorted, n
