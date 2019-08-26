import numpy as np
import matplotlib.pyplot as plt
import random


plt.figure(figsize=(10,6))
xl=50
yl=5
npsize=50


#x=np.array(np.arange(20))
#x=np.array(np.random.randint(0,20,size=20))
x=np.array(np.random.uniform(0,xl,size=npsize))
y=np.array(np.random.uniform(-yl,yl,size=npsize))

A=np.vstack([x,np.ones(len(x))]).T

m,c=np.linalg.lstsq(A,y,rcond=None)[0]
m2,c2=np.linalg.lstsq(A,y,rcond=0.1)[0]

plt.xlim((0, xl))
plt.ylim((-yl-2, yl+2))

plt.plot(x,y,'o',label='Original data',markersize=10)
plt.plot(x,m*x+c,'r',label='Fitted line')
plt.plot(x,m2*x+c2,'r',label='Fitted line rcond=0.1',color='orange')

plt.legend()
plt.show()
