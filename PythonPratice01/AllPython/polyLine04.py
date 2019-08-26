import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import interpolate


plt.figure(figsize=(10,6))
xl=50
yl=2
npsize=50


#x=np.array(np.arange(20))
#x=np.array(np.random.randint(0,20,size=20))
x=np.array(sorted(np.random.uniform(0,xl,size=npsize)))
y=np.array(np.random.uniform(-yl,yl,size=npsize))

A=np.vstack([x,np.ones(len(x))]).T


m,c=np.linalg.lstsq(A,y,rcond=None)[0]
#m2,c2=np.linalg.lstsq(A,y,rcond=0.1)[0]

fit_p=np.polyfit(x,y,deg=10)
poly_y=np.polyval(fit_p,x)

maxpeek=np.argmax(poly_y)
minpeek=np.argmin(poly_y)

#----------------------------------------------------------------------------
der_p=np.polyder(fit_p)
roots_p=np.roots(der_p)
reals = roots_p[np.isreal(roots_p)].real
peeks = [[np.min(x), np.polyval(fit_p, np.min(x))]]
#print(peeks)
for real in reals:
    if np.min(x) < real and real < np.max(x):
        peeks.append([real, np.polyval(fit_p, real)])
peeks.append([np.max(x), np.polyval(fit_p, np.max(x))])
peeks.sort()
print(peeks)
peeks = np.array(peeks)
print(peeks)
peeks_x=[]
peeks_y=[]
for peek in peeks:
    peeks_x.append(peek[0])
    peeks_y.append(peek[1])
#----------------------------------------------------------------------------

#der=np.polyder(fit_p)
#tx=np.roots(x)
#ty=np.roots(poly_y)



plt.xlim((0, xl))
plt.ylim((-yl-2, yl+2))

plt.plot(x[maxpeek],poly_y[maxpeek],'o',label='maxpeek line',color='orange',markersize=20)
plt.plot(x[minpeek],poly_y[minpeek],'o',label='minpeek line',color='orange',markersize=20)

plt.plot(peeks_x,peeks_y,'o-',label='peek line',color='purple',markersize=10)

#xnew=np.linspace(x.min(),x.max(),1000)
#func = interpolate.interp1d(x,poly_y,kind='cubic')
#ynew = func(xnew)

N=20
weights=np.hanning(N)
sam=np.convolve(weights/weights.sum(),poly_y)[N-1:-N+1]
print(sam)
t=np.arange(N-1,len(poly_y))
print(t)


plt.plot(t,poly_y[N-1:],'o-',label='Polyfit line',color='red')
#plt.plot(xnew,ynew,'-',label='Polyfit line',color='red',markersize=1)
#plt.plot(x,poly_y,'o-',label='Polyfit line',color='red')

plt.plot(x,y,'o',label='Original data',markersize=10)
plt.plot(x,m*x+c,'-',label='Linalg line',color='green')
#plt.plot(x,m2*x+c2,'r',label='Fitted line rcond=0.1',color='orange')

plt.legend()
plt.show()
