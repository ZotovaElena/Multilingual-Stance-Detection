# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:16:43 2020

@author: zotov
"""

import os 
import pandas as pd
from transformers import MarianMTModel, MarianTokenizer
import progressbar


path_spa = "/home/elena/Desktop/Multilingual-Stance-Detection/CIC_2020_Dataset/data_type_d/spanish"
to_path_spa = "/home/elena/Desktop/Multilingual-Stance-Detection/CIC_2020_Dataset/data_type_d/spanish/translated"

path_cat = "/home/elena/Desktop/Multilingual-Stance-Detection/CIC_2020_Dataset/data_type_d/catalan"
to_path_cat = "/home/elena/Desktop/Multilingual-Stance-Detection/CIC_2020_Dataset/data_type_d/catalan/translated"

file_train_spa = "train.tsv"
file_dev_spa = "dev.tsv"
file_test_spa = 'test.tsv'

col_names = ['labels', 'text']
df_train_spa = pd.read_csv(os.path.join(path_spa, file_train_spa), sep='\t', names=col_names)
train_spa = df_train_spa.text.to_list()

df_dev_spa = pd.read_csv(os.path.join(path_spa, file_dev_spa), sep='\t', names=col_names)
dev_spa = df_dev_spa.text.to_list()

df_test_spa = pd.read_csv(os.path.join(path_spa, file_test_spa), sep='\t', names=col_names)
test_spa = df_test_spa.text.to_list()

file_train_cat = "train.tsv"
file_dev_cat = "dev.tsv"
file_test_cat = 'test.tsv'

df_train_cat = pd.read_csv(os.path.join(path_cat, file_train_cat), sep='\t', names=col_names)
train_cat = df_train_cat.text.to_list()

df_dev_cat = pd.read_csv(os.path.join(path_cat, file_dev_cat), sep='\t', names=col_names)
dev_cat = df_dev_cat.text.to_list()

df_test_cat = pd.read_csv(os.path.join(path_cat, file_test_cat), sep='\t', names=col_names)
test_cat = df_test_cat.text.to_list()

print(test_cat[:5])

def divide_chunks(l, n):    
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
		

model_name = 'Helsinki-NLP/opus-mt-es-ca'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate(text_list, model=None, tokenizer=None): 
  translated = model.generate(**tokenizer.prepare_translation_batch(text_list))
  tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
  return tgt_text

src_text = ['Gipuzkoa recupera el pulso con la vuelta a las clases y la libertad de horarios en la calle ',
            'El 20% de los institutos y «la casi totalidad» de centros de FP vascos abren sin incidencias en su primer día hábil, y bares y centros comerciales empiezan a sumar clientes']

translated = translate(src_text, model=model, tokenizer=tokenizer)
print(translated)

train_spa_lst = list(divide_chunks(train_spa, 4))

train_spa_translated_list = []

for i, chunk in enumerate(train_spa_lst): 
	trans = translate(chunk, model=model, tokenizer=tokenizer)
	train_spa_translated_list.append(trans)
	print('Chunks done: ', i)
	
def flat_list(l):
	flat_list = [item for sublist in l for item in sublist]
	return flat_list

train_spa2cat = flat_list(train_spa_translated_list)



# train_spa2cat = translate(train_spa, model=model, tokenizer=tokenizer)
df_train_spa['spa2cat'] = train_spa2cat
df_train_spa = df_train_spa[['labels', 'spa2cat']]
df_train_spa.to_csv(os.path.join(to_path_spa, file_train_spa), sep='\t', header=None, index=False)


dev_spa_list = list(divide_chunks(dev_spa, 6))
test_spa_list = list(divide_chunks(test_spa, 6))

dev_spa_translated_list = []

for i, chunk in enumerate(dev_spa_list): 
	trans = translate(chunk, model=model, tokenizer=tokenizer)
	dev_spa_translated_list.append(trans)
	print('Chunks done: ', i)

print('DEV done')

test_spa_translated_list = []

for i, chunk in enumerate(test_spa_list): 
	trans = translate(chunk, model=model, tokenizer=tokenizer)
	test_spa_translated_list.append(trans)
	print('Chunks done: ', i)


dev_spa2cat = flat_list(dev_spa_translated_list)
df_dev_spa['spa2cat'] = dev_spa2cat
df_dev_spa = df_dev_spa[['labels', 'spa2cat']]
df_dev_spa.to_csv(os.path.join(to_path_spa, file_dev_spa), sep='\t', header=None, index=False)

test_spa2cat = flat_list(test_spa_translated_list)
df_test_spa['spa2cat'] = test_spa2cat
df_test_spa = df_test_spa[['labels', 'spa2cat']]
df_test_spa.to_csv(os.path.join(to_path_spa, file_test_spa), sep='\t', header=None, index=False)

""""""
#####
""""""
model_name = 'Helsinki-NLP/opus-mt-ca-es'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

