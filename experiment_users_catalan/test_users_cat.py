# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:19:50 2019

@author: EZOTOVA
"""

import pandas as pd 
import numpy as np

df_train = pd.read_csv('train_hSVM_catalan_dataset.csv', dtype={'id_str': 'str'}, encoding='utf-8', sep='\t')
df_train['part'] = 'train'

df_test = pd.read_csv('test_hSVM_catalan_dataset.csv', dtype={'id_str': 'str'}, encoding='utf-8', sep='\t')
df_test['part'] = 'test'

df_val = pd.read_csv('val_hSVM_catalan_dataset.csv', dtype={'id_str': 'str'}, encoding='utf-8', sep='\t')
df_val['part'] = 'val'

df_pro = pd.read_csv('data_preparation/catalan_pro_sampled_4000.csv', dtype={'id_str': 'str', 'user_id_str': 'str'}, encoding='utf-8', sep='\t')
df_contra = pd.read_csv('data_preparation/catalan_contra_LDA.csv', dtype={'id_str': 'str', 'user_id_str': 'str'}, encoding='utf-8', sep='\t')
df_neutro = pd.read_csv('data_preparation/catalan_neutro_LDA.csv', dtype={'id_str': 'str', 'user_id_str': 'str'}, encoding='utf-8', sep='\t')

frames_classes = [df_pro, df_contra, df_neutro]

df_all = pd.concat(frames_classes)

#df_all = pd.read_csv('tweets_catalan.csv', dtype={'id_str': 'str', 'user_id_str': 'str'}, encoding='utf-8', sep='\t')
#
df_all['id_str'] = df_all['id_str'].str.replace('.', '')
#ids =  list(df_all['id_str'].values)
#
#ids_new = []
#for i in ids: 
#    i  = i[:-3]
##    print(i)
#    ids_new.append(i)
#
#df_all['id_new'] = ids_new 

frames2 = [df_train, df_test, df_val]

data = pd.concat(frames2)
#data['id_str'] = data['id_str'].str.replace('e+18', '')
#data['id_str'] = data['id_str'].astype(str).str[:-3]

#ids_data = list(data['id_str'].values)
#
#
#ids_data_new = []
#for i in ids_data: 
#    i  = i[:-3]
#    ids_data_new.append(i)
#    
#    
#data['id_new'] = ids_data_new


data_merged = pd.merge(data, df_all, how='left', on='id_str') 

data_merged.to_csv('DATASET/catalan_merged.csv', sep='\t', index=False)

print(data_merged.columns)


data_experiment = data_merged[['id_str', 'TWEET_x', 'LABEL_x', 'CLEAN_x', 'CLEAN_FULL', 'LEMMA',
       'LEMMA_CLEAN', 'part', 'user_id_str', 'user_screen_name']]

data_experiment.rename(columns={'LABEL_x':'LABEL', 'TWEET_x': 'TWEET'}, inplace=True)


train = data_experiment.loc[data_experiment['part'] == 'train']
test = data_experiment.loc[data_experiment['part'] == 'test']
val = data_experiment.loc[data_experiment['part'] == 'val']


is_in_train_test = []
train_list = list(train['user_screen_name'])
test_list =  list(test['user_screen_name'])
val_list = list(val['user_screen_name'])

for name in test_list: 
    if name in train_list:
        is_in_train_test.append('true')
    else: 
        is_in_train_test.append('false')

is_in_train_val = []       
for name in val_list: 
    if name in train_list:
        is_in_train_val.append('true')
    else:
        is_in_train_val.append('false')

        
u = data_experiment['user_screen_name'].value_counts() #tweets in the corpus

u_all = pd.DataFrame(u)
u_all['username'] = u_all.index

u_all = u_all.sample(frac=1).reset_index(drop=True)

users = list(u_all.username.values)
counts = list(u_all.user_screen_name.values)

u_all['sum'] = u_all.user_screen_name.cumsum()

users_train = u_all[u_all['sum'] <= 6000]
users_val = u_all[(u_all['sum'] > 6000) & (u_all['sum'] < 8060)]
users_test = u_all[(u_all['sum'] >= 8060) & (u_all['sum'] <= 10049)]

users_train_new = users_train['username'].to_list()
users_test_new = users_test['username'].to_list()
users_val_new = users_val['username'].to_list()

train_new = data_experiment[data_experiment['user_screen_name'].isin(users_train_new)]
print('TRAIN ', len(train_new))
print(pd.DataFrame(train_new['LABEL'].value_counts()))
train_new.to_csv('train_user_exp_rand.csv', index=False, sep='\t')
    
test_new = data_experiment[data_experiment['user_screen_name'].isin(users_test_new)]
print('TEST ', len(test_new))
print(pd.DataFrame(test_new['LABEL'].value_counts()))
test_new.to_csv('test_user_exp_rand.csv', index=False, sep='\t')


val_new = data_experiment[data_experiment['user_screen_name'].isin(users_val_new)]
print('VAL ', len(val_new))
print(pd.DataFrame(val_new['LABEL'].value_counts()))
val_new.to_csv('val_user_exp_rand.csv', index=False, sep='\t')



#
#def numberlist(nums, limit):
#    sum = 0
#    for x in nums:
#        sum += x
#        yield x
#        if sum > limit:
#            return
#
#for i in numberlist(counts, 2001):
#    print(i)


#print('ALL USERS ', users)
#
#print('UNIQUE USERS ', data_experiment['user_screen_name'].nunique())
#
#train, val, test = np.split(data_experiment.sample(frac=1), [int(.6*len(data_experiment)), int(.8*len(data_experiment))])
#
#u_train = pd.DataFrame(train['user_screen_name'].value_counts())
#u_train['username'] = u_train.index
#print('TRAIN USERS ', u_train)
#
#u_test = pd.DataFrame(test['user_screen_name'].value_counts())
#u_test['username'] = u_test.index
#
#print('TEST USERS ', u_test)
#
#u_val = pd.DataFrame(val['user_screen_name'].value_counts())
#print('VAL USERS ', u_val)
#u_val['username'] = u_val.index
#
#
#u_val_train = pd.merge(u_train, u_val, on='username', how='inner')
#
#u_val_train_test =  pd.merge(u_val_train, u_test, on='username', how='inner')

#

#
#df_preprocessed['id_str'] = df_preprocessed['id_str'].str.replace('.', '')
