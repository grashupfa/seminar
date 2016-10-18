import numpy as np
from calculate_BICscore import calculate_BICscore

def calculate_search_region(dffa,cnt,unique_strs,sample_size,alpha_len,dpfa_Orig):
    old_epsilon = 1
    init_region_left = 0
    init_region_right = 1
    new_epsilon = old_epsilon; 
    
    ES = np.empty(0)
    SS = np.empty(0)
    
    flag_right = 0
    itt2 = 0
    
    ES,SS,new_score=calculate_BICscore(ES,SS,dffa,new_epsilon,cnt,unique_strs,sample_size,alpha_len,dpfa_Orig)
    
    old_score=new_score
    old_epsilon = new_epsilon
    new_epsilon = new_epsilon*0.5
    
    while new_epsilon > 0:
        ES,SS,new_score=calculate_BICscore(ES,SS,dffa,new_epsilon,cnt,unique_strs,sample_size,alpha_len,dpfa_Orig)
        
        if new_score > old_score:
            init_region_right = old_epsilon
            flag_right = 1
            old_epsilon = new_epsilon
            new_epsilon = new_epsilon*0.5
            old_score = new_score
            itt2 = 0
            
        elif new_score == old_score:              
            if itt2 >= 5:
                init_region_left = new_epsilon
                break
            old_epsilon = new_epsilon
            new_epsilon = new_epsilon*0.5
            old_score = new_score
            itt2 = itt2+1
        else:
            init_region_left = new_epsilon;        
            old_score=new_score
            break
        
        
    if not flag_right:
        itt2 = 0
        new_epsilon = init_region_right
        ES,SS,new_score = calculate_BICscore(ES,SS,dffa,new_epsilon,cnt,unique_strs,sample_size,alpha_len,dpfa_Orig)
        old_score=new_score
        old_epsilon = new_epsilon
        new_epsilon = new_epsilon*2.0
    
        while 1:
            ES,SS,new_score = calculate_BICscore(ES,SS,dffa,new_epsilon,cnt,unique_strs,sample_size,alpha_len,dpfa_Orig)
            if (new_score > old_score):
                init_region_left = old_epsilon
                old_epsilon = new_epsilon
                new_epsilon = new_epsilon*2
                old_score = new_score
                itt2 = 0;
            elif new_score == old_score:
                if itt2 >= 5:
                    init_region_right = new_epsilon
                    break
                old_epsilon = new_epsilon
                new_epsilon = new_epsilon*2  
                old_score = new_score
                itt2=itt2+1          
            else:
                init_region_right = new_epsilon
                old_score=new_score
                break

    region = [init_region_left,init_region_right];
    
    return region,ES,SS