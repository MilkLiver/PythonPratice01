import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter 

n = 1024    # data size
X = np.random.normal(0, 1, n) # 每一个点的X值
Y = np.random.normal(0, 1, n) # 每一个点的Y值
T = np.arctan2(Y,X) # for color value

plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlabel('I am x')
plt.ylabel('I am y')

plt.xlim(-1, 1)
plt.ylim(-1, 1)
#plt.xticks(())  # ignore xticks
#plt.yticks(())  # ignore yticks

ax=plt.gca()

#ax.xaxis.set_major_locator( MultipleLocator(0.1))
#ax.xaxis.set_major_formatter(FormatStrFormatter('%2.1f'))

ax.xaxis.set_minor_locator( MultipleLocator(0.01))
ax.xaxis.set_minor_formatter(FormatStrFormatter('%2.2f'))

ax.tick_params(pad=20,labelsize=10)


plt.show()
