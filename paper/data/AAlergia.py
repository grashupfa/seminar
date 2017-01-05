def AALERGIA(dffa, alpha,dpfa_orig):
    dffa_merged = copy.deepcopy(dffa)
    initial_state = dffa.initial_state  
    dffa_merged.RED = np.append(dffa_merged.RED, initial_state)
        
    initial_blue_states = dffa.frequency_transition_matrix[0][initial_state][:]
    initial_blue_states = initial_blue_states[np.nonzero(initial_blue_states)]
    dffa_merged.BLUE = np.append(dffa_merged.BLUE, initial_blue_states)
        
    while len(dffa_merged.BLUE) > 0:
        dffa_merged.BLUE =  np.msort(dffa_merged.BLUE)
        q_b = dffa_merged.BLUE[0]
        dffa_merged.BLUE = dffa_merged.BLUE[1:len(dffa_merged.BLUE)]
        promote = 1
        labels = dffa.state_labels[dffa_merged.RED]
        state_labels_q_b = dffa_merged.state_labels[q_b]
        label_index = findall(labels, state_labels_q_b)
        
        for i in range(0, len(label_index)):
            q_r = dffa_merged.RED[label_index[i]]    
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
        
        #gets the new blue data (returns data that is not in intersection)
        difference = np.setxor1d(qr_succ, np.append(dffa_merged.RED, dffa_merged.BLUE)) 
        ia = np.empty(0, dtype = int)
        
        for i in range(0, len(qr_succ)):
            for j in range(0, len(difference)):
                if (difference[j] == qr_succ[i]):
                    ia = np.append(ia, qr_succ[i])
        
        dffa_merged.BLUE = np.append(dffa_merged.BLUE, ia)         
    return dffa_merged