from calculate_BICscore import calculate_BICscore

def golden_section_search(ES,SS,dffa,region,sample_size,alphabet,cnt,unique_strs,tp,dpfa_orig):
    
    good_eps = 0
    alpha_len = len(alphabet)

    while len(region) > 0:
    
        a1 = region[0] + 0.382*(region[1]-region[0])
        a2 = region[0] + 0.618*(region[1]-region[0])
        ES,SS,f2 = calculate_BICscore(ES,SS,dffa,a2,cnt,unique_strs,sample_size,alpha_len,dpfa_orig)
        ES,SS,f1 = calculate_BICscore(ES,SS,dffa,a1,cnt,unique_strs,sample_size,alpha_len,dpfa_orig)
        
        if abs(a1-a2) < 0.00001:
            good_eps = (a1+a2)/2
            max_e = 1
            return good_eps, ES,SS,max_e
        
        if f1 < f2:
            region = [a1,region[1]]
            good_eps, ES,SS,max_e = golden_section_search(ES,SS,dffa,region,sample_size,alphabet,cnt,unique_strs,1,dpfa_orig)
            max_e = 1
            return good_eps, ES,SS,max_e
        elif f1 > f2:
            region= [region[0],a2]
            good_eps, ES,SS,max_e = golden_section_search(ES,SS,dffa,region,sample_size,alphabet,cnt,unique_strs,1,dpfa_orig)
            max_e = 1
            return good_eps, ES,SS,max_e
        else :
            if tp == 3:
                max_e = 0 
                return good_eps, ES,SS,max_e
            
            if f1> max(SS):
                region2 = [a1,a2]
                good_eps,ES,SS, max_e = golden_section_search(ES,SS,dffa,region2,sample_size,alphabet,cnt,unique_strs,1,dpfa_orig)
                return good_eps, ES,SS,max_e
            else:
                regionL = [region[0],a1]
                regionR = [a2,region[1]]
                good_eps, ES,SS,max_eL = golden_section_search(ES,SS,dffa,regionL,sample_size,alphabet,cnt,unique_strs,tp+1,dpfa_orig)
                if max_eL:
                    max_e=1
                    return good_eps, ES,SS,max_e
                good_eps, ES,SS,max_eR = golden_section_search(ES,SS,dffa,regionR,sample_size,alphabet,cnt,unique_strs,tp+1,dpfa_orig)
                
                if not max_eL and not max_eR:
                    max_e = 0
                else:
                    max_e=1
                    
                return good_eps, ES,SS,max_e