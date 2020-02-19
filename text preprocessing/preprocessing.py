#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd 
import numpt as np 
import re

def lemmatization(tweets, lemma_table):
	
	"""Funcition for simple lemmatization. 
	Create lemma dict"""
	
	cols = list(lemma_table.columns)
	
	flex_all = list(lemma_table[cols[1]])
	lemma_all = list(lemma_table[cols[0]])
	dic_lemmas = {}

	for flex,lemma in zip(flex_all, lemma_all):
		dic_lemmas[flex] = lemma
		
	"Create a copy of the table and include a new column"
	
	lemmas = tweets.copy()
	lemmas = lemmas.fillna("")
	lemmas['LEMMA'] = ''
	
	for i, l in enumerate(lemmas['CLEAN_FULL']):
		tweet_lemmas = []
		
		"Get lowercase tweet and split tokens"
		tokens = l.lower().split()
		
		"If the word is in the dictionary include the lemma in the text_lemma"
		for t in tokens:
			if t in dic_lemmas:
				tweet_lemmas.append(dic_lemmas[t])
			else:
				tweet_lemmas.append(t)
		lemmas['LEMMA'][i] = ' '.join(tweet_lemmas)
#		print(i, tweet_lemmas)
#		print(lemmas['text_lemma'][i])
	"Return the new dataframe with new lemma column"
	return lemmas

def removeUsername(tokens):
    for t in tokens:
        if t.startswith('@'):
            tokens.remove(t)
    return tokens

  #regex compiltaions for normalizing the text 
j = re.compile(r"j{2,}") #detects the character the occurs two and more times
jaja = re.compile(r'(ja){2,}')
jeje = re.compile(r'(je){2,}')
haha = re.compile(r'(ha){2,}')
jiji = re.compile(r'(ji){2,}')
a = re.compile(r'a{2,}')
e = re.compile(r'e{3,}')
i = re.compile(r'i{2,}')
o = re.compile(r'o{2,}')
u = re.compile(r'u{2,}')
f = re.compile(r'f{2,}')
h = re.compile(r'h{2,}')
m = re.compile(r'm{2,}')
rt = re.compile(r'RT')
link = re.compile(r'(https?|http)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]')

punctuation = ['!', '"', '$', '%', '&', "'", '€'
               '(', ')', '*', '+', ',', '-', '.', 
               '/', ':', ';', '<', '=', '>', '?', 
               '[', '\\', ']', '^', '_', '`', 
               '{', '|', '}', '~', '–', '—', '"', 
               "¿", "¡", "''", "...", '_', 
               '“', '”', '…', '‘',  '’', "'", "``", 
               '°', '«', '»', '×', '》》', 'ʖ', '(']

## '‘'  '’' "'" "``"

#dictionary with diacritis for normalizing words
diacritica = {
    "á": "a",
    "ó": "o",
    "í": "i",
    "é": "e",
    "ú": "u",
    "ü": "u",
    "ù": "u",
    "à": "a",
    "è": "e",
    "ï": "i",
    "ò": "o"
}

def removePunctuation(line): 
    for i in punctuation: 
        line = line.replace(i, '')
    return line   

#get list of tokens, remove URLs, remove punctuation, lowercase
def getTokens(list_of_strings):	
    list_of_strings_tokenized = []
    for line in list_of_strings:
        line = re.sub(link, '', line)
        line = removePunctuation(line)
        line_tokens = line.split()
        list_of_strings_tokenized.append(line_tokens)
    return list_of_strings_tokenized


def normalizeLine(tokens_list):
    tokens_line_preproc = [] #lines with tokens normalized
    for l in tokens_list: 
        token_line = []
        for t in l: 
            t = re.sub(j, 'j', t)
            t = re.sub(jaja, 'jaja', t)
            t = re.sub(jeje, 'jaja', t)
            t = re.sub(haha, 'jaja', t)
            t = re.sub(jiji, 'jaja', t)
            t = re.sub(a, 'a', t)
            t = re.sub(e, 'e', t)
            t = re.sub(i, 'i', t)
            t = re.sub(o, 'o', t)
            t = re.sub(u, 'u', t)
            t = re.sub(f, 'f', t)
            t = re.sub(h, 'h', t)
            t = re.sub(m, 'm', t)
            t = re.sub(rt, '', t)
	    t = t.lower()
                      
            token_line.append(t)
        tokens_line_preproc.append(token_line)
    return tokens_line_preproc

import emoji

def remove_emoji(text):
    return emoji.get_emoji_regexp().sub(u'', text)
