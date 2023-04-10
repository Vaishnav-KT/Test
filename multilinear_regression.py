# -*- coding: utf-8 -*-
"""Multilinear_Regression2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19GEdkjB51-EvFxcCfS8DmGfRUyvihIs3
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from sklearn.feature_selection import RFE

df=pd.read_csv('/content/DPT (1).csv')

df1 =df.drop(['dteday','instant','casual','registered'], axis=1)
df1.head()

outcome ='cnt'
feature= [feat for feat in list(df1)if feat != outcome]
x= df1[feature]
y = df1[outcome]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test= train_test_split(x,y,test_size=0.3,random_state=42)

from sklearn import linear_model
lr_model= linear_model.LinearRegression()
rfe = RFE(lr_model)
fit = rfe.fit(X_train,y_train)
print("Num Features: %d" % fit.n_features_)
print("Selected Features: %s" % fit.support_)
print("Feature Ranking: %s" % fit.ranking_)

list(zip(X_train.columns,fit.support_,fit.ranking_))

x1= df1[['season','yr','holiday','workingday','weathersit']]
y1=df1[outcome]

x_train1,x_test1,y_train1,y_test1=train_test_split(x1,y1,test_size=0.3,random_state=0)

lr_model1= linear_model.LinearRegression()
lr_model1.fit(x_train1,y_train1)

y_pred= lr_model1.predict(x_test1)

import sklearn.metrics as sm
print("Mean absolute error =", round(sm.mean_absolute_error(y_test1, y_pred), 2)) 
print("Mean squared error =", round(sm.mean_squared_error(y_test1,  y_pred), 2)) 
print("Median absolute error =", round(sm.median_absolute_error(y_test1,  y_pred), 2)) 
print("Explain variance score =", round(sm.explained_variance_score(y_test1,  y_pred), 2)) 
print("R2 score =", round(sm.r2_score(y_test1,  y_pred), 2))

