import numpy as np
from math import sqrt,log

def calculate_compatible_parameter(dffa,qr,qb,epsilon):
   
    n_r=np.sum(dffa.frequency_transition_matrix[1][qr][:])
    n_r= n_r+ dffa.final_state_frequency[qr]
    
    I_r=sqrt(6*epsilon*log(n_r)/n_r)
    
    n_b=np.sum(dffa.frequency_transition_matrix[1][qb][:])
    n_b=n_b+dffa.final_state_frequency[qb]
    I_b=sqrt(6*epsilon*log(n_b)/n_b)
    
    alpha=I_r+I_b
    
    return alpha