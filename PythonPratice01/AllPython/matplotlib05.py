import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
print(Y1)

#plt.bar(X, +Y1)
#plt.bar(X, -Y2)
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='b')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='r')

plt.xlim(-.5, n)
plt.ylim(-1.25, 1.25)

#plt.xticks(())
#plt.yticks(())

for x, y in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x , y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x , -y - 0.05, '%.2f' % y, ha='center', va='top')

plt.show()
