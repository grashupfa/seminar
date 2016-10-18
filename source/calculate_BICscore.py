from findall import findall 
import numpy as np
from automata_size import automata_size
from math import log
from calculate_likelihood import calculate_likelihood
from AAlergia import AALERGIA

def calculate_BICscore(ES,SS,dffa,epsilon,cnt,unique_strs,sample_size,alpha_len,dpfa_orig):
    
    dis = abs(ES - epsilon)
    ex = np.where(dis < epsilon*0.001)
         
    if len(dis[ex]) > 0:
        score = SS[ex]
        print('the score corresponding to this alpha exists already! score = ')
        return ES,SS, score
     
    dffa_merged = AALERGIA(dffa, epsilon,dpfa_orig)
    LL = calculate_likelihood(cnt,unique_strs, dffa_merged)
    a_size,valid = automata_size(dffa_merged)
    
    score = LL -0.5*a_size *(alpha_len-1)*log(sample_size)
    
    ES = np.append(ES, epsilon)
    SS = np.append(SS, score)
    
    return ES,SS,score