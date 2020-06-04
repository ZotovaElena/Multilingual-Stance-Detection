#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:21:05 2020

@author: elena
"""
import pandas as pd 
import os
import re


punctuation = ['@', '#', '|', '\n']


def removePunctuation(line): 
    for i in punctuation: 
        line = line.replace(i, ' ')
    return line 

def removeURL(text):
	tokens_clean = []
	tokens = text.split()
	for t in tokens:
		t = re.sub(r'http\S+', '', t)
		if not t.startswith(('http')):
			tokens_clean.append(t)
	tokens_text = ' '.join(tokens_clean)
	return tokens_text

def textPreprocessing(line):
	line_new = removePunctuation(line)
	line_new_new = removeURL(line_new)
	return line_new_new


topics = ['abortions', 'atheism','climate', 'clinton', 'feminism']
path = '/home/elena/Desktop/SemEval'

for topic in topics:
	

	df_train = pd.read_csv(os.path.join(path, topic, 'ftft', 'train.csv'), sep='\t')
	df_train['text'] = df_train['text']
	df_train['text'] = df_train['text'].apply(textPreprocessing)
	df_train['Stance'] = '__label__' + df_train['Stance'].astype(str)
	df_train.to_csv(os.path.join(path, topic, 'ftft',  topic+'_train.txt'), sep='\t', index=False, header=None)
	
	# df_train['TWEET_CLEAN'] = df_train['TWEET_CLEAN'].apply(removeURL)
	
	df_test = pd.read_csv(os.path.join(path, topic, 'ftft', 'test.csv'), sep='\t', names=['Stance', 'text'])
	df_test['textN'] = df_test['text'].apply(textPreprocessing)
	df_test['Stance'] = '__label__' + df_test['Stance'].astype(str)
	df_test.to_csv(os.path.join(path, topic, 'ftft',  topic+'_test.txt'), sep='\t', index=False, header=None)
	# # df_test['TWEET_CLEAN'] = df_test['TWEET_CLEAN'].apply(removeURL)
	
	
	df_val = pd.read_csv(os.path.join(path, topic, 'ftft', 'dev.csv'), sep='\t')
	df_val['text'] = df_val['text'].apply(textPreprocessing)
	df_val['Stance'] = '__label__' + df_val['Stance'].astype(str)
	df_val.to_csv(os.path.join(path, topic, 'ftft',  topic+'_val.txt'), sep='\t', index=False, header=None)
	# # df_val['TWEET_CLEAN'] = df_val['TWEET_CLEAN'].apply(removeURL)
	
	
# 	train = df_train[['LABEL', 'TWEET_CLEAN']].rename(columns={"LABEL":"label", "TWEET_CLEAN":"text"})
# 	train['label'] = '__label__' + train['label'].astype(str)
	
	
	
# 	val = df_val[['LABEL', 'TWEET_CLEAN']].rename(columns={"LABEL":"label", "TWEET_CLEAN":"text"})
# 	val['label'] = '__label__' + val['label'].astype(str)
	
	
	# frames = [train1, val]
	
	# train = pd.concat(frames)
# 	train.to_csv('train_user_exp_rand_clean_FT.txt', sep='\t', index=False)
	
	
# 	test['label'] = '__label__' + test['label'].astype(str)
	
