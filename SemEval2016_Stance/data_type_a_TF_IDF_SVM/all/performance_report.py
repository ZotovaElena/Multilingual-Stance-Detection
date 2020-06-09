#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:33:49 2020

@author: elena
"""

from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn import preprocessing
from sklearn.metrics import recall_score
import io
import re

import pandas as pd 

# import random

# random.seed(1)

import glob

frames = []

for filename in glob.glob('*.csv'):
	df = pd.read_csv(filename, sep='\t')
	frames.append(df)

df_test = pd.concat(frames) 
	   
# df_test = pd.read_csv(filename, sep='\t', names=colnames, header=None)

y_true = df_test['Stance'].to_list()

# y_true = []
# for line in y_list:
#  	l = line.strip()
# # 	l = re.sub('__label__', '', l)
#  	y_true.append(l)
 	
# df_test['baseline'] = 'FAVOR'

y_pred = df_test['predicted'].to_list()

# y_pred_rand = [random.randrange(3) for i in range(len(df_test))]

# df_test['baseline_random'] = y_pred_rand
# df_test['baseline_random'] = df_test['baseline_random'].replace({0: 'AGAINST', 1: 'FAVOR', 2: 'NONE'})

# y_pred_random = df_test['baseline_random'].to_list()

cl_report_test = classification_report(y_true, y_pred, digits=4)

report_df_test = pd.read_fwf(io.StringIO(cl_report_test), sep="\s+")

print(cl_report_test)


report_df_test.to_csv('asemeval_all_report.csv', index=False, header=None)

# cl_report_test_rand = classification_report(y_true, y_pred, digits=4)
# report_df_test = pd.read_fwf(io.StringIO(cl_report_test_rand), sep="\s+")

# print(cl_report_test_rand)