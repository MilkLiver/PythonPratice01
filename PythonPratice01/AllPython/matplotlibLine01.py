import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
x=np.array([0,1,2,3])
y=np.array([-1,0.2,0.9,2.1])
A=np.vstack([x,np.ones(len(x))]).T

m,c=np.linalg.lstsq(A,y,rcond=None)[0]

plt.plot(x,y,'o',label='Original data',markersize=10)
plt.plot(x,m*x+c,'r',label='Fitted line')
plt.legend()
plt.show()
