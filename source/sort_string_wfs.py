import numpy as np

def sort_string_wfs(prefixes):
    length_array = np.zeros(len(prefixes))
    for i in range(0, len(prefixes)):
        length_array[i] = prefixes[i].count(',')
    
    length_array_u = np.unique(length_array)
    string_set_new = np.empty(0, dtype=str)
    cursor = 0
    IX = np.empty(0, dtype=int)
    for i in range(0, len(length_array_u)):
        len_s = length_array_u[i]
        indices = np.where(length_array == len_s)
        prefixes_to_sort = prefixes[indices]
        s_temp = np.msort(prefixes_to_sort)
        IXargsort = prefixes_to_sort.argsort()
        for j in range(0, len(s_temp)):
            string_set_new = np.append(string_set_new, s_temp[j])
            IX = np.append(IX, indices[0][IXargsort[j]])
        
        cursor = cursor + len(indices)
    return string_set_new, IX