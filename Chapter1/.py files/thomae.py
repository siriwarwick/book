import numpy as np
import matplotlib.pyplot as plt

xlist = []
ylist = []

for q in range(2,200):
    for p in range(1,q):
        if np.gcd(p,q) == 1:
            xlist.append(p/q)
            ylist.append(1/q)

plt.plot(xlist, ylist, 'or', ms=3)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0,1)
plt.grid('on')
plt.show()

lim = 0.1
num = sum(y > lim for y in ylist)
print(f'Found {num} points above y={lim}')
