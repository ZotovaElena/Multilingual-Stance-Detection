import pandas as pd 
import numpy as np

df_train = pd.read_csv('train_hSVM_castellano_dataset.csv', dtype={'id_str': 'str'}, encoding='utf-8', sep='\t')
df_train['part'] = 'train'

df_test = pd.read_csv('test_hSVM_castellano_dataset.csv', dtype={'id_str': 'str'}, encoding='utf-8', sep='\t')
df_test['part'] = 'test'

df_val = pd.read_csv('val_hSVM_castellano_dataset.csv', dtype={'id_str': 'str'}, encoding='utf-8', sep='\t')
df_val['part'] = 'val'

df_all = pd.read_csv('tweets_castellano.csv', dtype={'id_str': 'str', 'user_id_str': 'str'}, encoding='utf-8', sep='\t')

df_all['id_str'] = df_all['id_str'].str.replace('.', '')

frames2 = [df_train, df_test, df_val]

data = pd.concat(frames2)

#connect usernames with tweets
data_merged = pd.merge(data, df_all, how='left', on='id_str') 

print(data_merged.columns)
  
data_experiment = data_merged[['id_str', 'TWEET_x', 'LABEL', 'CLEAN', 'CLEAN_FULL', 'LEMMA',
       'LEMMA_CLEAN', 'CLEAN_FULL', 'user_id_str', 'user_screen_name', 'part']]

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

u = data_experiment['user_screen_name'].value_counts() #tweets in the corpus for each user

u_all = pd.DataFrame(u)
u_all['username'] = u_all.index

#randomize the lines in the dataframe
u_all = u_all.sample(frac=1).reset_index(drop=True)

users = list(u_all.username.values)
counts = list(u_all.user_screen_name.values)

#sum of tweets of each users in the dataset
u_all['sum'] = u_all.user_screen_name.cumsum()

#separate the dataset by the sum of the tweets
users_train = u_all[u_all['sum'] <= 6000]
users_val = u_all[(u_all['sum'] > 6000) & (u_all['sum'] < 8050)]
users_test = u_all[(u_all['sum'] >= 8050) & (u_all['sum'] <= 10077)]

users_train_new = users_train['username'].to_list()
users_test_new = users_test['username'].to_list()
users_val_new = users_val['username'].to_list()

train_new = data_experiment[data_experiment['user_screen_name'].isin(users_train_new)]
print(pd.DataFrame(train_new['LABEL'].value_counts()))
train_new.to_csv('train_user_exp_rand.csv', index=False, sep='\t')
    
test_new = data_experiment[data_experiment['user_screen_name'].isin(users_test_new)]
print(pd.DataFrame(test_new['LABEL'].value_counts()))
test_new.to_csv('test_user_exp_rand.csv', index=False, sep='\t')

val_new = data_experiment[data_experiment['user_screen_name'].isin(users_val_new)]
print(pd.DataFrame(val_new['LABEL'].value_counts()))
val_new.to_csv('val_user_exp_rand.csv', index=False, sep='\t')
