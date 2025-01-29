import os
import string
import numpy as np
import re
import datetime
from scipy.stats import beta
from tqdm import tqdm

# Parameters
punct_set = "["+string.punctuation+"]"
a,b = 4, 0.2
preprocess_length = 13000 # Based on WMT data

def load_data(lang1:str, lang2:str):
    '''
    Loads the parallel NLLB dataset for a language to English from a txt file.

    Args:
        lang: the language code for the non-English language

    Returns:
        list: the dataset in English
        list: the dataset in the given language
    '''
    with open('/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-raw/'+lang1+'-'+lang2+'/NLLB.'+lang1+'-'+lang2+'.'+lang1) as f:
        print('Opening NLLB.'+lang1+'-'+lang2+'.'+lang1+' ...')
        print(datetime.datetime.now())
        lang1_lang2 = f.readlines()
        print('Complete!')
    
    with open('/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-raw/'+lang1+'-'+lang2+'/NLLB.'+lang1+'-'+lang2+'.'+lang2) as f:
        print('Opening NLLB.'+lang1+'-'+lang2+'.'+lang2+' ...')
        print(datetime.datetime.now())
        lang2_lang1 = f.readlines()
        print('Complete!')

    return lang1_lang2, lang2_lang1

def save_to_file(lang1,lang2,lang1_lang2,lang2_lang1):
    
    outpath = r'/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/'+lang1+'-'+lang2+'/'
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    with open(outpath+'NLLB.'+lang1+'-'+lang2+'.'+lang1, 'w') as outfile:
      outfile.write(''.join(str(i) for i in lang1_lang2))
    with open(outpath+'NLLB.'+lang1+'-'+lang2+'.'+lang2, 'w') as outfile:
      outfile.write(''.join(str(i) for i in lang2_lang1))
    
    with open(outpath+'NLLB.'+lang1+'-'+lang2+'.stats', 'w') as outfile:
        outfile.write("Sentences: {}\n".format(len(lang1_lang2)))
        outfile.write("Tokens aligned: {}\n".format(sum([len(line.split(" ")) for line in lang1_lang2])))
        outfile.write("Average sentence length: {:.2f}".format(sum([len(line.split(" ")) for line in lang1_lang2])/len(lang1_lang2)))
        outfile.write('Average character length: {:.2f}'.format(sum([len(line) for line in lang1_lang2])/len(lang1_lang2)))

def preprocess(dir:str):

    lang1, lang2 = dir.split('-')
    
    lang1_lang2, lang2_lang1 = load_data(lang1, lang2)
    
    print("Filtering ...")
    # Filter out strings with n>10 punctuation chars
    lang1_lang2_filt = [lang1_lang2[i] for i in range(len(lang1_lang2)) if len(re.findall(punct_set, lang1_lang2[i]))<10 and len(re.findall(punct_set, lang2_lang1[i]))<10]
    lang2_lang1_filt = [lang2_lang1[i] for i in range(len(lang2_lang1)) if len(re.findall(punct_set, lang1_lang2[i]))<10 and len(re.findall(punct_set, lang2_lang1[i]))<10]
    
    # Sanity check
    assert len(lang1_lang2_filt) == len(lang2_lang1_filt)
    
    print("Filtered out {} sentences".format(len(lang1_lang2) - len(lang1_lang2_filt)))

    if len(lang1_lang2_filt) > preprocess_length:
    
        # Get beta dist
        P = beta.cdf([i/len(lang1_lang2_filt) for i in range(len(lang1_lang2_filt))],a,b)
        sumP = sum(P)
        P_norm = [float(i)/sumP for i in P]
        
        print("Sampling ...")
        # Sample indices using the beta distribution
        lang1_lang2_subset = np.random.choice(a=sorted(lang1_lang2_filt,key=len),
                                              size=preprocess_length,
                                              replace=False,
                                              p=P_norm)
        
        # Get the corresponding sentences in the other language to retain the parallel dataset
        lang2_lang1_subset = [lang2_lang1_filt[lang1_lang2_filt.index(sent)] for sent in tqdm(lang1_lang2_subset)]
        
        save_to_file(lang1,lang2,lang1_lang2_subset,lang2_lang1_subset)

    else:

        save_to_file(lang1,lang2,lang1_lang2_filt,lang2_lang1_filt)

dirs = ['fr-ja','ja-tl','ja-nl','fr-tl','fr-nl','tl-nl', # high -> high
       'ja-ne','fr-ig','tl-cy','nl-li', # high -> low
       'ne-ig','ne-cy','ne-li','ig-cy','ig-li','cy-li'] # low -> low

for dir in dirs:
    preprocess(dir)