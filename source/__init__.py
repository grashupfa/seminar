from csvimporter import load_data
from build_ftpa_data import build_ftpa_data
from findall import findall
from dffa2dpfa import dffa2dpfa
from calculate_search_region import calculate_search_region
from numpy import array,nonzero,histogram,sum
from automata_size import automata_size
from calculate_likelihood import calculate_likelihood
from math import log
from golden_section_search import golden_section_search
from AAlergia import AALERGIA
from export_to_prism import export_to_prism

#those are the variables that need to be changed
FOLDERNAME = 'channel_analysis_be_max_change_300'
MODELNAME = 'channel_analysis_be_max_change_300_344'
DELIMITER = ':'
SYMBOL_COUNT = 640
FLAG_TOKEN = 1
FLAG_OUTPUT = 1

#import data from file
alphabets, trainingset = load_data(FOLDERNAME, MODELNAME, DELIMITER)
        
#Model learning
trainingset_np = array(trainingset)
sample_size = 0

for i in range(0,len(trainingset)):
    count_seq = findall(trainingset[i],',')
    sample_size += len(count_seq)

dffa,unique_strs, n = build_ftpa_data(trainingset_np, alphabets)
dpfa_orig = dffa2dpfa(dffa)

alpha_len=len(alphabets);
cnt, bin_edges = histogram(n, len(n))
cnt = cnt[nonzero(cnt)]

#Golden search
region,ES,SS = calculate_search_region(dffa,cnt,unique_strs,sample_size,alpha_len,dpfa_orig)

good_eps, ES,SS,max_e = golden_section_search(ES,SS,dffa,region,sample_size,alphabets,cnt,unique_strs,1,dpfa_orig)

max_si = (SS == max(SS))
good_e = max(ES[max_si])
final_dffa = AALERGIA(dffa, good_e,dpfa_orig)
LL = calculate_likelihood(cnt,unique_strs, final_dffa)
a_size,valid = automata_size(final_dffa)
score= LL -0.5 * a_size *(alpha_len - 1) * log(sample_size)

export_to_prism(final_dffa)

print('finished')