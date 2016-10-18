def AAlergia_compatible(dffa,dpfa, qu, qv, pu,pv,epsilon,thresh):
    
    correct = 1
    if max(pu,pv) <= thresh: 
        return correct
    if (pu == 0 and pv > thresh) or (pv == 0 and pu > thresh):
        correct=0
        return correct
    if pu == 0:
        pf_u = 0
    else:
        pf_u = dpfa.final_state_probability[qu]
        tranP_u = dpfa.probability_transition_matrix[1][qu][:]
        next_u = dpfa.probability_transition_matrix[0][qu][:]

    if (pv == 0):
        pf_v = 0
    else:
        pf_v = dpfa.final_state_probability[qv]
        tranP_v = dpfa.probability_transition_matrix[1][qv][:]
        next_v = dpfa.probability_transition_matrix[0][qv][:]
    
    temp = abs(pu*pf_u-pv*pf_v)

    if (temp > thresh):
        correct = 0
        return correct
 
    for i in range(0, len(next_v)):  
        if next_v[i] != 0 or next_u[i] != 0:
            pu_temp = pu * tranP_u[i]
            pv_temp = pv * tranP_v[i]
            
            if  not AAlergia_compatible(dffa,dpfa,next_u[i], next_v[i], pu_temp,pv_temp,epsilon,thresh):
                correct=0
                return correct
            
    return correct