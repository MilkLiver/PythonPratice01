import matplotlib.pyplot as plt
import numpy as np



x = np.linspace(-3, 3, 50)

y1 = 2*x + 1
y2 = x**2

plt.figure()

#plt.plot(x, y2,label='linear line')
#plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='square line')
l1=plt.plot(x, y2,label='linear line')
l2=plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='square line')

#plt.legend(loc='upper right')
plt.legend(loc=0)
#plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best') #使用失敗

plt.xlim((-1, 2))
plt.ylim((-2, 3))

plt.xlabel('I am x')
plt.ylabel('I am y')

#plt.yticks([-2, -1.8, -1, 1.22, 3],[r'really bad', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

ax = plt.gca()

ax.spines['right'].set_color('yellow')
ax.spines['top'].set_color('green')
ax.spines['bottom'].set_color('purple')

ax.xaxis.set_ticks_position('top')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.show()
