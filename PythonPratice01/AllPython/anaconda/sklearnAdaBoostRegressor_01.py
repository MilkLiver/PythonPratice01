# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:23:56 2019

@author: NEIL_YU
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:37:39 2019

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

#print(len(n1),len(n2))
#print(n1)


#polynomial_features = PolynomialFeatures(degree=degree,include_bias=False)
#linear_regression = LinearRegression(normalize=True)
#model_regressor=AdaBoostRegressor(linear_regression,n_estimators=10,random_state=10)


model_regressor=AdaBoostRegressor(DecisionTreeRegressor(max_depth=4),n_estimators=100,random_state=10)
model=model_regressor.fit(n1,n2)


prex=np.arange(1,10,0.01).reshape(-1,squ)

prey=model.predict(prex)

#print(np.arange(1,21).reshape(-1, 2))
mp.figure()
mp.plot(prex,prey,color="red")
mp.xlim(1, 10)
mp.ylim(1, 10)
#mp.scatter(n1, n2, s=1, alpha=0.5)

mp.show()