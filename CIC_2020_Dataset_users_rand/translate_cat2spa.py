#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:13:43 2020

@author: elena
"""

import os 
import pandas as pd
from transformers import MarianMTModel, MarianTokenizer

def divide_chunks(l, n):    
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
		
def translate(text_list, model=None, tokenizer=None): 
  translated = model.generate(**tokenizer.prepare_translation_batch(text_list))
  tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
  return tgt_text

def flat_list(l):
	flat_list = [item for sublist in l for item in sublist]
	return flat_list

path_cat = "data_type_d/catalan"
to_path_cat = "data_type_d/catalan/translated"

file_train_cat = "train.tsv"
file_dev_cat = "dev.tsv"
file_test_cat = 'test.tsv'

col_names = ['labels', 'text']

df_train_cat = pd.read_csv(os.path.join(path_cat, file_train_cat), sep='\t', names=col_names)
train_cat = df_train_cat.text.to_list()

df_dev_cat = pd.read_csv(os.path.join(path_cat, file_dev_cat), sep='\t', names=col_names)
dev_cat = df_dev_cat.text.to_list()

df_test_cat = pd.read_csv(os.path.join(path_cat, file_test_cat), sep='\t', names=col_names)
test_cat = df_test_cat.text.to_list()

model_name = 'Helsinki-NLP/opus-mt-ca-es'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)


train_cat_lst = list(divide_chunks(train_cat, 6))
dev_cat_list = list(divide_chunks(dev_cat, 6))
test_cat_list = list(divide_chunks(test_cat, 6))

train_cat_translated_list = []

for i, chunk in enumerate(train_cat_lst): 
	trans = translate(chunk, model=model, tokenizer=tokenizer)
	train_cat_translated_list.append(trans)
	print('Chunks done: ', i)
	
train_cat2spa = flat_list(train_cat_translated_list)

df_train_cat['cat2spa'] = train_cat2spa
df_train_cat = df_train_cat[['labels', 'cat2spa']]
df_train_cat.to_csv(os.path.join(to_path_cat, file_train_cat), sep='\t', header=None, index=False)


dev_cat_translated_list = []

for i, chunk in enumerate(dev_cat_list): 
	trans = translate(chunk, model=model, tokenizer=tokenizer)
	dev_cat_translated_list.append(trans)
	print('Chunks done: ', i)

dev_cat2spa = flat_list(dev_cat_translated_list)

df_dev_cat['cat2spa'] = dev_cat2spa
df_dev_cat = df_dev_cat[['labels', 'cat2spa']]
df_dev_cat.to_csv(os.path.join(to_path_cat, file_dev_cat), sep='\t', header=None, index=False)

print('DEV done')

test_cat_translated_list = []

for i, chunk in enumerate(test_cat_list): 
	trans = translate(chunk, model=model, tokenizer=tokenizer)
	test_cat_translated_list.append(trans)
	print('Chunks done: ', i)

test_cat2spa = flat_list(test_cat_translated_list)

df_test_cat['cat2spa'] = test_cat2spa
df_test_cat = df_test_cat[['labels', 'cat2spa']]
df_test_cat.to_csv(os.path.join(to_path_cat, file_test_cat), sep='\t', header=None, index=False)
