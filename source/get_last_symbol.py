def get_last_symbol(seq, ind):
    label = seq
    if len(ind) > 1:
        label = seq[ind[-2]+1:ind[-1]]
    elif len(ind) == 1:
        label = seq[0:ind[0]]
    
    return label