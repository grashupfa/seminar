from findall import findall

def calculate_likelihood_string(dpfa, string):
    curr_state = dpfa.initial_state[0]
    prob = 1.0
    alphabets = dpfa.alphabets
    index=findall(string, ',')
    
    alphabet_map = {}
    for i in range(0, len(alphabets)):
        alphabet_map[alphabets[i]] = i

    for i in range(1,len(index)):
        ch = string[index[i-1]+1:index[i]]
        alphabet_index = alphabet_map[ch]
        
        next_state = dpfa.probability_transition_matrix[0][curr_state][alphabet_index]
        if (next_state == 0):
            prob = 0.0
            return prob
        else:
            prob = prob * dpfa.probability_transition_matrix[1][curr_state][alphabet_index]
            curr_state = next_state

    prob = prob * dpfa.final_state_probability[curr_state]
    
    return prob