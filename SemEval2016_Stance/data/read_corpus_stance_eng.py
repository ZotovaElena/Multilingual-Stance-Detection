# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 19:00:28 2020

@author: zotov
"""

import pandas as pd 
import os
import text_preprocessing as tp

path = 'data-all-annotations'
file_train = 'trainingdata-all-annotations.txt'
file_del = 'trialdata-all-annotations.txt'
file_test = 'testdata-taskA-all-annotations.txt'

df_tr = pd.read_csv(os.path.join(path, file_train), sep='\t')
df_del = pd.read_csv(os.path.join(path, file_del), sep='\t')
df_test = pd.read_csv(os.path.join(path, file_test), sep='\t')

preprocessing_D = {'punctuation': True,
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


df_tr['text'] = df_tr['Tweet'].apply(tp.textPreprocessing, args=(preprocessing_D, 'en'))
df_tr['text'] = df_tr['text'].str.replace('SemST', '')


df_del['text'] = df_del['Tweet'].apply(tp.textPreprocessing, args=(preprocessing_D, 'en'))
df_del['text'] = df_del['text'].str.replace('SemST', '')



frames = [df_tr, df_del]
df_all = pd.concat(frames)




from sklearn.model_selection import train_test_split

df_train, df_dev = train_test_split(df_all, test_size=0.1)

# df_dev = df_dev[['Stance', 'text']]
# df_train = df_train[['Stance', 'text']]


df_atheism_train = df_train.loc[df_train.Target == 'Atheism']
df_atheism_train = df_atheism_train[['Stance', 'text']]
df_atheism_train.to_csv('atheism/ft/train.csv', sep='\t', index=False)
df_atheism_dev = df_dev.loc[df_dev.Target == 'Atheism']
df_atheism_dev = df_atheism_dev[['Stance', 'text']]
df_atheism_dev.to_csv('atheism/ft/dev.csv', sep='\t', index=False)

df_climate_train = df_train.loc[df_train.Target == 'Climate Change is a Real Concern']
df_climate_train = df_climate_train[['Stance', 'text']]
df_climate_train.to_csv('climate/ft/train.csv', sep='\t', index=False)
df_climate_dev = df_dev.loc[df_dev.Target == 'Climate Change is a Real Concern']
df_climate_dev = df_climate_dev[['Stance', 'text']]
df_climate_dev.to_csv('climate/ft/dev.csv', sep='\t',  index=False)
#
df_feminism_train = df_train.loc[df_train.Target == 'Feminist Movement']
df_feminism_train = df_feminism_train[['Stance', 'text']]
df_feminism_train.to_csv('feminism/ft/train.csv', sep='\t', index=False)
df_feminism_dev = df_dev.loc[df_dev.Target == 'Feminist Movement']
df_feminism_dev = df_feminism_dev[['Stance', 'text']]
df_feminism_dev.to_csv('feminism/ft/dev.csv', sep='\t',  index=False)

df_clinton_train = df_train.loc[df_train.Target == 'Hillary Clinton']
df_clinton_train = df_clinton_train[['Stance', 'text']]
df_clinton_train.to_csv('clinton/ft/train.csv', sep='\t', index=False)
df_clinton_dev = df_dev.loc[df_dev.Target == 'Hillary Clinton']
df_clinton_dev = df_clinton_dev[['Stance', 'text']]
df_clinton_dev.to_csv('clinton/ft/dev.csv', sep='\t', index=False)

df_abortion_train = df_train.loc[df_train.Target == 'Legalization of Abortion']
df_abortion_train = df_abortion_train[['Stance', 'text']]
df_abortion_train.to_csv('abortions/ft/train.csv', sep='\t', index=False)
df_abortion_dev = df_dev.loc[df_dev.Target == 'Legalization of Abortion']
df_abortion_dev = df_abortion_dev[['Stance', 'text']]
df_abortion_dev.to_csv('abortions/ft/dev.csv', sep='\t', index=False)


# df_dev.to_csv('dev_en_full.csv', sep='\t', index=False)
# df_dev = df_dev[['Stance', 'text']]
# df_dev.to_csv('dev.csv', sep='\t', header=None, index=False)

# df_train.to_csv('train_en_full.csv', sep='\t', index=False)
# df_train = df_train[['Stance', 'text']]
# df_train.to_csv('train.csv', sep='\t', header=None, index=False)
# #
# #
#
df_test['text'] = df_test['Tweet'].apply(tp.textPreprocessing, args=(preprocessing_D, 'en'))
df_test['text'] = df_test['text'].str.replace('SemST', '')
df_test.to_csv('test_en_full.csv', sep='\t', index=False)
# #

df_atheism_test = df_test.loc[df_test.Target == 'Atheism']
df_atheism_test = df_atheism_test[['Stance', 'text']]
df_atheism_test.to_csv('atheism/ft/test.csv', sep='\t', header=None, index=False)

df_climate_test = df_test.loc[df_test.Target == 'Climate Change is a Real Concern']
df_climate_test = df_climate_test[['Stance', 'text']]
df_climate_test.to_csv('climate/ft/test.csv', sep='\t', header=None, index=False)
#
df_feminism_test = df_test.loc[df_test.Target == 'Feminist Movement']
df_feminism_test = df_feminism_test[['Stance', 'text']]
df_feminism_test.to_csv('feminism/ft/test.csv', sep='\t', header=None, index=False)

df_clinton_test = df_test.loc[df_test.Target == 'Hillary Clinton']
df_clinton_test = df_clinton_test[['Stance', 'text']]
df_clinton_test.to_csv('clinton/ft/test.csv', sep='\t', header=None, index=False)

df_abortion_test = df_test.loc[df_test.Target == 'Legalization of Abortion']
df_abortion_test = df_abortion_test[['Stance', 'text']]
df_abortion_test.to_csv('abortions/ft/test.csv', sep='\t', header=None, index=False)




#df_test = df_test[['Stance', 'text']]
#df_test.to_csv('test.csv', sep='\t', header=None, index=False)
