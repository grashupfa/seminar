from dffa2dpfa import dffa2dpfa
from math import log
from calculate_likelihood_string import calculate_likelihood_string

def calculate_likelihood(cnt,unique_sample, dffa):
    LL = 0
    dpfa = dffa2dpfa(dffa)

    for i in range(0,len(unique_sample)):
        string=unique_sample[i]
        LL = LL + cnt[i] * log(calculate_likelihood_string(dpfa, string))
   
    return LL