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

import glob

frames_pred = []

for filename in glob.glob('*predict.txt'):
	colnames = ['label']
	df = pd.read_csv(filename, sep='\t', names= colnames)
	frames_pred.append(df)

df_pred = pd.concat(frames_pred) 
	   
# df_pred['label'] = df_pred.label.replace('__label__', '')

y_pred = df_pred.label.to_list()


frames = []

for filename in glob.glob('*test.txt'):
	df = pd.read_csv(filename, sep='\t', names=['0', '1'])
	frames.append(df)

df_test = pd.concat(frames)

df_test['label'] = df_test.index


# df_test['label'] = df_test.index.replace('__label__', '')

y_true = df_test['label'].to_list()

# y_true = []
# for line in y_list:
# 	l = line.strip()
# # 	l = re.sub('__label__', '', l)
# 	y_true.append(l)
	
cl_report_test = classification_report(y_true, y_pred, digits=4)

report_df_test = pd.read_fwf(io.StringIO(cl_report_test), sep="\s+")

print(cl_report_test)

# df_test['bert_prediction'] = y_pred

# df_test.to_csv('.tsv', index=False, sep='\t')

report_df_test.to_csv('semeval_fasttext_classification_report.csv', index=False, header=None)