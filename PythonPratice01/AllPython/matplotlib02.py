import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2*x + 1

plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y,)

plt.plot([-2, 0,2,0,-2],[0, 2,0,-2,0],color='orange')

#plt.plot(0, 2,color='orange',marker='o')
plt.plot([0], [2],color='orange',marker='o')
plt.scatter([0, ], [0, ], s=50, color='r')

ax = plt.gca()

ax.spines['right'].set_color('red')
ax.spines['top'].set_color('green')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2*x0 + 1
plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)
# set dot styles
plt.scatter([x0, ], [y0, ], s=50, color='b')

plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

plt.annotate("Test OwO",xy=(0,0),xytext=(+0.1, +0.2),fontsize=10)

plt.text(-3, 3, r'This is the some text~',
         fontdict={'size': 10, 'color': 'r'})

plt.show()
