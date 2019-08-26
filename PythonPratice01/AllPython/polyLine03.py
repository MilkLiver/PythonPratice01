
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

plt.figure(figsize=(10,6))

x = np.array([6, 7, 8, 9, 10, 11, 12])
y = np.array([1.53E+03, 5.92E+02, 2.04E+02, 7.24E+01, 2.72E+01, 1.10E+01, 4.70E+00])
xnew = np.linspace(x.min(),x.max(),300)

func = interpolate.interp1d(x,y,kind='cubic')
ynew = func(xnew)

plt.plot(x, y, "r", linewidth=1)
plt.plot(xnew,ynew)

plt.show()
