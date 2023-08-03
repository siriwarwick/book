import numpy as np
import matplotlib.pyplot as plt

R = np.linspace(0, 4, 4000)
rng = np.random.default_rng()
xlist = []
rlist = []

def f(x, r):
    return r*x*(1-x)

for r in R:
    x = rng.random()
    for j in range(500):
        x = f(x, r)
    for k in range(50):
        x = f(x, r)
        xlist.append(x)
        rlist.append(r)
        
plt.plot(rlist, xlist, 'b.', markersize=0.05) 
plt.xlabel('r')
plt.ylabel('x')
plt.xlim([0,4])
plt.ylim([0,1])
plt.grid('on')
plt.show()
