#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 23:55:21 2020

@author: elena
"""

import re
import pandas as pd

filename_stop_spa = 'stopwords/stopwords-es.txt'
with open(filename_stop_spa, encoding='utf-8') as f:
	stop_spa = f.readlines()
	
stopwords_spa = []
for line in stop_spa:
	l = line.strip()
	stopwords_spa.append(l)
	
filename_stop_ca = 'stopwords/stopwords-cat.txt'
with open(filename_stop_ca, encoding='utf-8') as f:
	stop_ca = f.readlines()
	
stopwords_ca = []
for line in stop_ca:
	l = line.strip()
	stopwords_ca.append(l)
	
filename_stop_en = 'stopwords/stopwords-en.txt'
with open(filename_stop_en, encoding='utf-8') as f:
	stop_en = f.readlines()
	
stopwords_en = []
for line in stop_en:
	l = line.strip()
	stopwords_en.append(l)
	

file_lemma_spa = 'lemmatization-lists-master/lemmatization-es.txt'
lemma_table_spa = pd.read_csv(file_lemma_spa, encoding='utf-8', sep='\t') 
cols_spa = list(lemma_table_spa.columns)

file_lemma_ca = 'lemmatization-lists-master/lemmatization-ca.txt'
lemma_table_ca = pd.read_csv(file_lemma_ca, encoding='utf-8', sep='\t') 
cols_ca = list(lemma_table_ca.columns)

file_lemma_en = 'lemmatization-lists-master/llemmatization-en.txt'
lemma_table_en = pd.read_csv(file_lemma_ca, encoding='utf-8', sep='\t') 
cols_en = list(lemma_table_en.columns)


# Regex for normalization 

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

replace_dict = {'j': [j],
				'jaja': [jaja, jeje, haha, jiji],
				'a': [a], 
				'e': [e],
				'i': [i], 
				'o': [o],
				'u': [u],
				'f': [f],
				'h': [h],
				'm': [m],
				'': [rt]
				}

punctuation = ['!', '"', '$', '%', '&', "'", '€'
			   '(', ')', '*', '+', ',', '-', '.', 
			   '/', ':', ';', '<', '=', '>', '?', 
			   '[', '\\', ']', '^', '_', '`', 
			   '{', '|', '}', '~', '–', '—', '"', 
			   "¿", "¡", "''", "...", '_', 
			   '“', '”', '…', '‘',  '’', "'", "``", 
			   '°', '«', '»', '×', '》》', 'ʖ', '(']

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
