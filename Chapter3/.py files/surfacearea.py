import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad

def integrand(u,v):
    return np.sqrt(4-3*(1-u**2)*np.sin(v)**2)

Alist = [0]
hlist = [0]
A, h = 0, 0
dh = 1e-2

while (h<1):
    dA = dblquad(integrand, 
         0, np.pi/2, 
         h, h+dh)
    A += 4*dA[0]
    h += dh
    Alist.append(A)
    hlist.append(h)

Area = Alist[-1]

plt.plot(hlist, Alist, 'r')
plt.plot([0,1],[0, Area], ':b')
plt.xlim(0,1)
plt.xlabel('Height $h$')
plt.xticks(np.arange(0,1.1,0.1))
plt.ylim(0,11)
plt.ylabel('Surface area of ellipsoidal strip')
plt.yticks(np.arange(0,11.1,1))
plt.legend(['Surface area', f'{Area:.4f}$h$'])
plt.grid('on')
plt.show()
