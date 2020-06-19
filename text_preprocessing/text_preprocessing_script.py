#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:22:03 2020

@author: elena
"""
import pandas as pd
import re 
import emoji
import preprocess_base
import os
import progressbar

config_dict = {'punctuation': True, #removes punctuation
			   'URLs': True, #removes URLs
			   'numbers': True, #removes digits
			   'stopwords': False,  #removes stopwords fosr selected language 
			   'shortwords': False, #removes words shorter than 3 characters 
			   'diacritics': False, #replaces diacritics with simple letters
			   'usernames': False, #removes Twitter usernames starting with @
			   'normalization': True, #replaces multiple letters with one letter
			   'emojis': True, #removes emojis
			   'lemmatize': False, #replaces a word form with its lemma
			   'lowercase': False, #turns all words to lower case 
			   'hashtags': True, #removes # symbol
			   '@': False, #removes @ symbol
			   'RT': True #removes RT
			   }

preprocessing_A = {'punctuation': True,
			   'URLs': True,
			   'numbers': True,
			   'stopwords': True, 
			   'shortwords': True,
			   'diacritics': True,
			   'usernames': True,
			   'normalization': True,
			   'emojis': True,
			   'lemmatize': True,
			   'lowercase': True, 
			   'hashtags': False,
			   '@': False, 
			   'RT': True
			   }

preprocessing_B = {'punctuation': True,
			   'URLs': True,
			   'numbers': True,
			   'stopwords': False, 
			   'shortwords': False,
			   'diacritics': False,
			   'usernames': True,
			   'normalization': True,
			   'emojis': True,
			   'lemmatize': False,
			   'lowercase': True, 
			   'hashtags': False,
			   '@': False, 
			   'RT': True
			   }

preprocessing_C = {'punctuation': True,
			   'URLs': True,
			   'numbers': False,
			   'stopwords': False, 
			   'shortwords': False,
			   'diacritics': False,
			   'usernames': False,
			   'normalization': False,
			   'emojis': False,
			   'lemmatize': False,
			   'lowercase': False, 
			   'hashtags': True,
			   '@': True, 
			   'RT': False
			   }

preprocessing_D = {'punctuation': False,
			   'URLs': True,
			   'numbers': False,
			   'stopwords': False, 
			   'shortwords': False,
			   'diacritics': False,
			   'usernames': False,
			   'normalization': False,
			   'emojis': False,
			   'lemmatize': False,
			   'lowercase': False, 
			   'hashtags': True,
			   '@': True, 
			   'RT': False
			   }

def removePunctuation(line, punctuation):
	for i in punctuation: 
		line = line.replace(i, '')
	return line  

def removeURL(line):
	tokens = line.split()
	tokens_new = []
	for t in tokens:
		t = re.sub(r'http\S+', '', t)
		if not t.startswith(('http')):
			tokens_new.append(t)
	line_new = ' '.join(tokens_new)
	return line_new


def removeNumbers(line):
	line_new = re.sub(r'[0-9]', '', line) 
	return line_new

def removeStopwords(line, stopwords): 
	tokens = line.split()
	tokens_clean = []
	for t in tokens: 
		if t not in stopwords:
			tokens_clean.append(t)
	line_new = ' '.join(tokens_clean)
	return line_new
	
def removeShortwords(line):
	tokens = line.split()
	tokens_clean = []
	for t in tokens:
		if len(t) > 3:
			tokens_clean.append(t)
	line_new = ' '.join(tokens_clean)
	return line_new
	
def removeDiacritics(line, diacritica):
	tokens = line.split()
	tokens_new = []
	for t in tokens:
		t = t.translate({ord(k): v for k, v in diacritica.items()})
		tokens_new.append(t)
	line_new = ' '.join(tokens_new)
	return line_new

def removeUsernames(line): 
	tokens = line.split()
	tokens_clean = []
	for t in tokens:
		if not t.startswith(('@')):
			tokens_clean.append(t)
	line_new = ' '.join(tokens_clean)
	return line_new
	
def normalizeLine(line, replace_dict):
	tokens = line.split()
	tokens_new = []
	for t in tokens:
		for k in replace_dict:
			for reg in replace_dict[k]:
				t = re.sub(reg, k, t)
					  
		tokens_new.append(t)
	line_new = ' '.join(tokens_new)
	return line_new

def removeEmoji(line):
	line = emoji.get_emoji_regexp().sub(u'', line)
	return line

def lemmatize(line, lemma_table, cols):
	flex_all = list(lemma_table[cols[1]])
	lemma_all = list(lemma_table[cols[0]])
	dic_lemmas = {}

	for flex,lemma in zip(flex_all, lemma_all):
		dic_lemmas[flex] = lemma
	
	tweet_lemmas = []
	tokens = line.lower().split()
	for t in progressbar.progressbar(tokens):
		if t in dic_lemmas:
			tweet_lemmas.append(dic_lemmas[t])
		else:
			tweet_lemmas.append(t)
			
	return ' '.join(tweet_lemmas)

def removeHashtags(line):
	line_new = re.sub('#', '', line)
	return line_new
	
def removeAts(line):
	line_new = re.sub('@', '', line)
	return line_new

def removeRTs(line):
	line_new = re.sub(re.compile(r'RT'), '', line)
	return line_new


def textPreprocessing(line, config_dict, language):
	
	punctuation = preprocess_base.punctuation
	diacritica = preprocess_base.diacritica
	
	if language == 'es':
		stopwords = preprocess_base.stopwords_spa
		lemma_table = preprocess_base.lemma_table_spa
		cols = preprocess_base.cols_spa
		replace_dict = preprocess_base.replace_dict
		
	if language == 'ca':
		stopwords = preprocess_base.stopwords_ca
		lemma_table = preprocess_base.lemma_table_ca
		cols = preprocess_base.cols_ca
		replace_dict = preprocess_base.replace_dict
		
	if language == 'en':
		stopwords = preprocess_base.stopwords_en
		lemma_table = preprocess_base.lemma_table_en
		cols = preprocess_base.cols_en
		replace_dict = preprocess_base.replace_dict
		
		
	if config_dict['URLs'] == True:
		line = removeURL(line)
		
	if config_dict['stopwords'] == True:
		line = removeStopwords(line, stopwords)
	
	if config_dict['punctuation'] == True:
		line = removePunctuation(line, punctuation)

	if config_dict['numbers'] == True:
		line = removeNumbers(line)

	if config_dict['shortwords'] == True:
		line = removeShortwords(line)
		
	if config_dict['diacritics'] == True:
		line = removeDiacritics(line, diacritica)

	if config_dict['usernames'] == True:
		line = removeUsernames(line)
		
	if config_dict['normalization'] == True:
		line = normalizeLine(line, replace_dict)
		
	if config_dict['emojis'] == True:
		line = removeEmoji(line)
		
	if config_dict['RT'] == True:
		line = removeRTs(line)
		
	if config_dict['lowercase'] == True:
		line = line.lower()
		
	if config_dict['hashtags'] == True:
		line = removeHashtags(line)
		
	if config_dict['@'] == True:
		line = removeAts(line)
		
	if config_dict['lemmatize'] == True:
		line = lemmatize(line, lemma_table, cols)

	return line
	

# s = ['RT @JuanGosset: Holaaaaaaaaa El independentismo es el arte de engañar usando la expresión #HASHTAG a punto de . https://t.co/3dHQ9jqtNT', 
#  	 'Antoni Puigverd se queja de que Millo no facilite construir una verdad que incluya la perspectiva independentista (¿puede  construirse  una verdad?). Ahora, sin embargo, sí parecen los... https://t.co/eS2fggfaCk	']

# sent = 'RT @JuanGosset: Holaaaaaaaaa El independentismo es el arte voy de engañar usando la expresión #HASHTAG a puntos de . https://t.co/3dHQ9jqtNT'


path = '/home/elena/Desktop/Independencia/Dataset_Español/DATASET'

lan = 'ca'

df_train = pd.read_csv(os.path.join(path, 'spanish_train.csv'), sep='\t', dtype={'id_str': 'str'})
df_train = df_train[['id_str', 'TWEET', 'LABEL']]
df_train.to_csv('spanish_train.csv', sep='\t', index=False)

df_train['preprocessing_A'] = df_train['TWEET'].apply(textPreprocessing, args=(preprocessing_A, lan))
df_train1 = df_train[['LABEL', 'preprocessing_A']]
df_train1.to_csv('spanish_train_type_A.csv', sep='\t', index=False)

df_train['preprocessing_B'] = df_train['TWEET'].apply(textPreprocessing, args=(preprocessing_B, lan))
df_train2 = df_train[['LABEL', 'preprocessing_B']]
df_train2.to_csv('spanish_train_type_B.csv', sep='\t', index=False)

df_train['preprocessing_C'] = df_train['TWEET'].apply(textPreprocessing, args=(preprocessing_C, lan))
df_train3 = df_train[['LABEL', 'preprocessing_C']]
df_train3.to_csv('spanish_train_type_C.csv', sep='\t', index=False)

df_train['preprocessing_D'] = df_train['TWEET'].apply(textPreprocessing, args=(preprocessing_D, lan))
df_train4 = df_train[['LABEL', 'preprocessing_D']]
df_train4.to_csv('spanish_train_type_D.csv', sep='\t', index=False)


# TEST

df_test = pd.read_csv(os.path.join(path, 'spanish_test.csv'), sep='\t', dtype={'id_str': 'str'})
df_test = df_test[['id_str', 'TWEET', 'LABEL']]
df_test.to_csv('spanish_test.csv', sep='\t', index=False)


df_test['preprocessing_A'] = df_test['TWEET'].apply(textPreprocessing, args=(preprocessing_A, lan))
df_test1 = df_test[['LABEL', 'preprocessing_A']]
df_test1.to_csv('spanish_test_type_A.csv', sep='\t', index=False)

df_test['preprocessing_B'] = df_test['TWEET'].apply(textPreprocessing, args=(preprocessing_B, lan))
df_test2 = df_test[['LABEL', 'preprocessing_B']]
df_test2.to_csv('spanish_test_type_B.csv', sep='\t', index=False)

df_test['preprocessing_C'] = df_test['TWEET'].apply(textPreprocessing, args=(preprocessing_C, lan))
df_test3 = df_test[['LABEL', 'preprocessing_C']]
df_test3.to_csv('spanish_test_type_C.csv', sep='\t', index=False)

df_test['preprocessing_D'] = df_test['TWEET'].apply(textPreprocessing, args=(preprocessing_D, lan))
df_test4 = df_test[['LABEL', 'preprocessing_D']]
df_test4.to_csv('spanish_test_type_D.csv', sep='\t', index=False)

# VAL

df_val = pd.read_csv(os.path.join(path, 'spanish_val.csv'), sep='\t', dtype={'id_str': 'str'})
df_val = df_val[['id_str', 'TWEET', 'LABEL']]
df_val.to_csv('spanish_val.csv', sep='\t', index=False)

df_val['preprocessing_A'] = df_val['TWEET'].apply(textPreprocessing, args=(preprocessing_A, lan))
df_val1 = df_val[['LABEL', 'preprocessing_A']]
df_val1.to_csv('spanish_val_type_A.csv', sep='\t', index=False)


df_val['preprocessing_B'] = df_val['TWEET'].apply(textPreprocessing, args=(preprocessing_B, lan))
df_val2 = df_val[['LABEL', 'preprocessing_B']]
df_val2.to_csv('spanish_val_type_B.csv', sep='\t', index=False)

df_val['preprocessing_C'] = df_val['TWEET'].apply(textPreprocessing, args=(preprocessing_C, lan))
df_val3 = df_val[['LABEL', 'preprocessing_C']]
df_val3.to_csv('spanish_val_type_C.csv', sep='\t', index=False)


df_val['preprocessing_D'] = df_val['TWEET'].apply(textPreprocessing, args=(preprocessing_D, lan))
df_val4 = df_val[['LABEL', 'preprocessing_D']]
df_val4.to_csv('spanish_val_type_D.csv', sep='\t', index=False)


#example with a string
# result = textPreprocessing(sent, preprocessing_D, 'es')
# print('PREPROCESSING D ', result)

#example with dataframe
# df = pd.DataFrame(data = {'text': s})
# df['text_new'] = df['text'].apply(textPreprocessing, args=(config_dict, 'es'))
