import matplotlib.pyplot as plt
import numpy as np
 
 
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()
 
# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
 
 
def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)
 
 
t1 = np.arange(0, 5, 0.1)
t2 = np.arange(0, 5, 0.02)
 
plt.figure(12)
plt.subplot(221)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'r--')
 
plt.subplot(222)
plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
 
plt.subplot(212)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
 
plt.show()



data = [5, 20, 15, 25, 10]

plt.bar([0.3, 1.7, 4, 6, 7], data, width=0.6, bottom=[10, 0, 5, 0, 5])
plt.bar(1, 2, width=0.6, bottom=3)
plt.show()
