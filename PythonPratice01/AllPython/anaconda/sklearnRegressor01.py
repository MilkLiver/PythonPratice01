# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:30:58 2019

@author: NEIL_YU
"""

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as mp
import numpy as np


num=100
squ=5   
degree=5


n1=np.random.uniform(1,10,num*squ).reshape(-1, squ)
n2=np.random.uniform(1,10,num).reshape(-1, 1)

prex=np.arange(1,10,0.01).reshape(-1,squ)

mp.figure()

#-----------------------------------------------------------------------------------------------
polynomial_features = PolynomialFeatures(degree=degree,include_bias=False)
linear_regression = LinearRegression(normalize=True)

pipeline = Pipeline([("polynomial_features", polynomial_features),("linear_regression", linear_regression)])
model=pipeline.fit(n1,n2)

prey=model.predict(prex)

mp.plot(prex,prey,color="red")
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
model_regressor=AdaBoostRegressor(DecisionTreeRegressor(max_depth=4),n_estimators=100,random_state=10)
model=model_regressor.fit(n1,n2)

prey2=model.predict(prex)

mp.plot(prex,prey2,color="blue")
#-----------------------------------------------------------------------------------------------

#print(np.arange(1,21).reshape(-1, 2))
mp.xlim(1, 10)
mp.ylim(1, 10)
mp.scatter(n1, n2, s=1, alpha=0.5)

mp.show()