from automata_size import automata_size
import numpy as np
from get_last_symbol import get_last_symbol
from findall import findall

def export_to_prism(dffa):

    a_size,valid = automata_size(dffa)
    len_alpha = len(dffa.alphabets)
    arrLabels = np.empty(a_size, dtype=object);
    
    tran_p=dffa.frequency_transition_matrix[1][valid][:]
    g_edge=dffa.frequency_transition_matrix[0][valid][:]
    states=dffa.state_labels[valid]
    
    mask = np.zeros(a_size, dtype = int)
    
    for i in range(0, a_size):
        mask[i] = i
    
    for i in range(0,a_size):
        if valid[i] != mask[i] :
            g_edge[np.where(g_edge == valid[i])] = mask[i]; # careful -> 0 values are same as -1 values!
    
    f = open('output','w');
    
    f.write('dtmc \n \n');
    
    f.write('module test \n');
    ii = mask[np.where(valid == dffa.initial_state)];
    
    f.write('s:[0..%d] init %d;\n' % (a_size-1, ii));
    
    for i in range(0,a_size):
        p = tran_p[i][:];
        edge = g_edge[i][:];
        freq = np.sum(p);
        
        str = states[i];
        index = findall(str, ',')   
        arrLabels[i] = get_last_symbol(str, index);
        
        ind = np.nonzero(p)[0];
    
        if len(ind) == 0:
             f.write('[]s=%d -> %d :(s\'=%d)' % (i,1,i));
             f.write(';\n');
             continue;
    
        f.write('[]s=%d -> %d/%d:(s\'=%d)' % (i,p[ind[0]],freq,edge[ind[0]]));
        
        for k in range(1, len(ind)):
            f.write(' +  %d/%d:(s\'=%d)' % (p[ind[k]],freq,edge[ind[k]]));
    
        f.write(';\n');
    
    f.write('endmodule\n\n');
    
    #label
    alp = dffa.alphabets;
    for i in range(0, len_alpha):
        str = alp[i];
        ind = np.where(arrLabels == str)[0];
    
        if len(ind) == 0:
            continue;

        f.write('label "%s" = s=%d' % (alp[i],ind[0]));
        for j in range (1, len(ind)):
            f.write('|s=%d' % (ind[j]));
            
        f.write(';\n');
    f.write('\n');
    
    f.close();
