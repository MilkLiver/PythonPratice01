# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:04:36 2019

@author: NEIL_YU
"""

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as mp
import numpy as np


n1=np.random.uniform(1,10,100).reshape(-1, 1)
n2=np.random.uniform(3,7,100).reshape(-1, 1)
#print(n1)

degree=10

polynomial_features = PolynomialFeatures(degree=degree,include_bias=False)
linear_regression = LinearRegression(normalize=True)

#pipeline = Pipeline([("polynomial_features", polynomial_features),("linear_regression", linear_regression)])
#pipeline = Pipeline(*polynomial_features),(linear_regression))

model=pipeline.fit(n1,n2)
prex=np.arange(1,10,0.01).reshape(-1, 1)
#print(prex)
prey=model.predict(prex)

#print(np.arange(1,21).reshape(-1, 2))
mp.figure()
mp.plot(prex,prey)
mp.xlim(1, 10)
mp.ylim(1, 10)
mp.scatter(n1, n2, s=75, alpha=.5)

mp.show()