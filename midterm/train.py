#!/usr/bin/env python
# coding: utf-8

import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer


# parameters
output_file = f'model.bin'


# data preparation

data = pd.read_csv('dataset.csv')

data.columns = data.columns.str.lower().str.replace(' ', '_')
string_columns = list(data.dtypes[data.dtypes == 'object'].index)

for col in string_columns:
    data[col] = data[col].str.lower().str.replace(' ', '_')

data.rename(columns = {'nacionality':'nationality', 'age_at_enrollment':'age'}, inplace = True)
data['target'] = data['target'].map({
    'dropout':0,
    'enrolled':1,
    'graduate':2
})

data_copy = data.copy()
data_copy = data_copy.drop(columns=['nationality', 
                                  'mother\'s_qualification', 
                                  'father\'s_qualification', 
                                  'educational_special_needs', 
                                  'international', 
                                  'curricular_units_1st_sem_(without_evaluations)',
                                  'unemployment_rate', 
                                  'inflation_rate'], axis=1)

X = data_copy.drop('target', axis=1)
y = data_copy['target']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)


# training 
def train(X_train, y_train):
    train_dict = X_train.to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(train_dict)

    model = RandomForestClassifier(max_depth=20, random_state=2)
    model.fit(X_train, y_train)
    
    return dv, model


def predict(X,dv, model):
    train_dict = X_train.to_dict(orient='records')

    X = dv.transform(train_dict)
    y_pred = model.predict_proba(X)[0, 1]

    return y_pred

# training the final model

print('output the final model')

dv, model = train(X_train, y_train)
y_pred = predict(X, dv, model)

# Save the model

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'the model is saved to {output_file}')