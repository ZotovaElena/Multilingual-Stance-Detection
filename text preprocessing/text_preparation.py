# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:42:55 2019

@author: EZOTOVA

#as a result we hace a table with the following columns: 
LEMMA - full lemmatized text 
LEMMA_CLEAN - lemmatized text without stopwords and short words, normalized as much as possible, this part used for SVM model for reducing the dimensionality of the matrix
CLEAN - text without stoprwords but with diacritics 
CLEAN_FULL - full cleaned text, used for word embedding models 

"""

import pandas as pd
import re 
import preprocessing as pp

filename = 'stopwords-es.txt'
with open(filename, encoding='utf-8') as f:
    stop = f.readlines()
    
stopwords = []
for line in stop:
    l = line.strip()
    stopwords.append(l)

file_lemma = 'lemmatization-lists-master/lemmatization-es.txt'
lemma_table = pd.read_csv(file_lemma, encoding='utf-8', sep='\t')

filename = 'spanish_val.csv'
df = pd.read_csv(filename, dtype={'id_str': 'str'}, encoding='utf-8', sep='\t')
#df_val = pd.read_csv('DATASET/spanish_val.csv', dtype={'id_str': 'str'}, encoding='utf-8', sep='\t')
#df_test = pd.read_csv('DATASET/spanish_test.csv', dtype={'id_str': 'str'}, encoding='utf-8', sep='\t')


list_of_tweets = list(df.TWEET.values)
list_of_tokens = pp.getTokens(list_of_tweets) #get list of tokens, remove URLs, remove punctuation, lowercase
list_of_tokens_norm = pp.normalizeLine(list_of_tokens) #normalize all words, replace multiple letters with one

list_of_tokens_clean = [] #remove stopwords, usernames and URLs and words shorter than 3 characters
for l in list_of_tokens_norm:
    t_line = []
    for t in l:
        if t not in stopwords and not t.startswith(('@', 'http')) and len(t) > 3: #filter stopwords and user names
            t_line.append(t)
    list_of_tokens_clean.append(t_line)

list_of_tokens_clean_full = [] #remove usernames and URLs, leave all the rest 
for l in list_of_tokens_norm:
    t_line = []
    for t in l:
        if not t.startswith(('@', 'http')): 
            t_line.append(t)
    list_of_tokens_clean_full.append(t_line)
    
list_of_tweets_clean_full = [] #get clean text of full tweets
for line in list_of_tokens_clean_full:
    l = ' '.join(line)
    l_e = pp.remove_emoji(l)
    l_e = re.sub(r'[0-9]', '', l_e) 
    l_s = l_e.strip()
    list_of_tweets_clean_full.append(l_s)
    
    
list_of_tweets_clean =  [] #get clean text of tweets 
for line  in list_of_tokens_clean:
    l = ' '.join(line)
    l_e = pp.remove_emoji(l)
    l_e = re.sub(r'[0-9]', '', l_e) 
    l_s = l_e.strip()
    list_of_tweets_clean.append(l_s)

df['CLEAN'] = list_of_tweets_clean #tweets without usernames, URLs, stopwords and short words
df['CLEAN_FULL'] = list_of_tweets_clean_full #tweets without usernames, URLs

#lemmatization over cleaned tweets
df_preprocessed = pp.lemmatization(df, lemma_table) #replace full word form with lemma, return a new table with new column LEMMA 

list_of_tweets_lemmatized = list(df_preprocessed.LEMMA.values)

list_of_tweets_lema_clean = []
for line in list_of_tweets_lemmatized:
    line_clean = []
    tokens = line.split()
    for t in tokens:
        t = t.translate({ord(k): v for k, v in pp.diacritica.items()}) #remove diacritics
        if len(t) > 3:
            line_clean.append(t)
    
    list_of_tweets_lema_clean.append(' '.join(line_clean))
    
df_preprocessed['LEMMA_CLEAN'] = list_of_tweets_lema_clean #tweets with maximal normalization: lemmatized, normalized, without diacritics

#val_sh = df.drop(['CLEAN', 'CLEAN_FULL', 'LEMMA', 'LEMMA_CLEAN'], axis=1)

to_file = 'val_hSVM_castellano_dataset.csv'
df_preprocessed.to_csv(to_file, sep='\t', encoding='utf-8', index=False)



#test.to_csv('test_hSVM_'+filename, sep='\t', encoding='utf-8', index=False)
#val.to_csv('val_hSVM_'+filename, sep='\t', encoding='utf-8', index=False)
##


#train_sh = train.drop(['CLEAN', 'CLEAN_FULL', 'LEMMA', 'LEMMA_CLEAN'], axis=1)
#test_sh = test.drop(['CLEAN', 'CLEAN_FULL', 'LEMMA', 'LEMMA_CLEAN'], axis=1)
#val_sh = val.drop(['CLEAN', 'CLEAN_FULL', 'LEMMA', 'LEMMA_CLEAN'], axis=1)
#
#train_sh.to_csv('DATASET/spanish_train.csv', sep='\t', encoding='utf-8', index=False)
#test_sh.to_csv('DATASET/spanish_test.csv', sep='\t', encoding='utf-8', index=False)
#val_sh.to_csv('DATASET/spanish_val.csv', sep='\t', encoding='utf-8', index=False)

                              
