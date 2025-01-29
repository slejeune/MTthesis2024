import os
from tqdm import tqdm
import datetime

def load_data(lang:str):
    '''
    Loads the parallel NLLB dataset for a language to English from a txt file.

    Args:
        lang: the language code for the non-English language

    Returns:
        list: the dataset in English
        list: the dataset in the given language
    '''
    with open('/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/English-centric/en-'+lang+'/NLLB.en-'+lang+'.en') as f:
        print('Opening NLLB.en-'+lang+'.en ...')
        print(datetime.datetime.now())
        en_lang = f.readlines()
        print('Complete!')
    
    with open('/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/English-centric/en-'+lang+'/NLLB.en-'+lang+'.'+lang) as f:
        print('NLLB.en-'+lang+'.'+lang+' ...')
        print(datetime.datetime.now())
        lang_en = f.readlines()
        print('Complete!')

    return en_lang, lang_en

def filter_data(en_lang, lang_en, intersection):
    '''
    Filter out any data in the parallel dataset not in the intersection.

    Return:
        list: filtered text in English
        list: filtered text in given language
    '''

    en_lang_i = [i for i in range(len(en_lang)) if en_lang[i] in intersection]
    en_lang_filtered = [en_lang[i] for i in en_lang_i]
    lang_en_filtered = [lang_en[i] for i in en_lang_i]

    return en_lang_filtered, lang_en_filtered

def create_aligned_dataset(trans_dir:str):
    '''
    Create the dataset in the given translation direction.

    Args:
        trans_dir: the translation direction in the format 'lang1-lang2'
    '''
    
    lang1, lang2 = trans_dir.split('-')

    # Load data
    en_lang1, lang1_en = load_data(lang1)
    en_lang2, lang2_en = load_data(lang2)

    # Find the overlay between the English texts
    print('Finding intersection between '+lang1+' and '+lang2+' ...')
    print(datetime.datetime.now())
    intersection = set(en_lang1) & set(en_lang2)
    print('Complete!')

    # Filtering step for reducing computation time
    print('Filtering the data ...')
    print(datetime.datetime.now())
    en_lang1_filtered, lang1_en_filtered = filter_data(en_lang1, lang1_en, intersection)
    en_lang2_filtered, lang2_en_filtered = filter_data(en_lang2, lang2_en, intersection)
    print('Complete!')
    
    print('Getting data for '+lang1+' ...')
    lang1_lang2 = [lang1_en_filtered[en_lang1_filtered.index(sent)] for sent in tqdm(intersection)]
    print('Complete!')
    print('Getting data for '+lang2+' ...')
    lang2_lang1 = [lang2_en_filtered[en_lang2_filtered.index(sent)] for sent in tqdm(intersection)]
    print('Complete!')
    
    # Writing folder & files
    print('Writing '+lang1+'-'+lang2+' to file ...')
    outpath = r'/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-aligned/'+lang1+'-'+lang2+'/'
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    with open(outpath+'NLLB.'+lang1+'-'+lang2+'.'+lang1, 'w') as outfile:
      outfile.write(''.join(str(i) for i in lang1_lang2))
    with open(outpath+'NLLB.'+lang1+'-'+lang2+'.'+lang2, 'w') as outfile:
      outfile.write(''.join(str(i) for i in lang2_lang1))
    
    with open(outpath+'NLLB.'+lang1+'-'+lang2+'.stats', 'w') as outfile:
        outfile.write("Sentences: {}\n".format(len(lang1_lang2)))
        outfile.write("Tokens aligned: {}\n".format(sum([len(line.split(" ")) for line in lang1_lang2])))
        outfile.write("Average sentence length aligned: {:.2f}".format(sum([len(line.split(" ")) for line in lang1_lang2])/len(lang1_lang2)))
    print('Complete!')
    
# Translation pairs
# dirs = ['ja-fr','ja-tl','ja-nl','fr-tl','fr-nl','tl-nl', # high -> high
#        'ja-ne','fr-ig','tl-cy','nl-li', # high -> low
#        'ne-ig','ne-cy','ne-li','ig-cy','ig-li','cy-li'] # low -> low

# Directions not included on https://opus.nlpl.eu/NLLB/
dirs = ['tl-nl','ja-ne','tl-cy','ne-ig','ne-cy','ne-li','ig-cy','ig-li','cy-li']

for dir in dirs:
    create_aligned_dataset(dir)