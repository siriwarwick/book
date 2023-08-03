import numpy as np
import matplotlib.pyplot as plt
from sympy import sieve
from sympy.ntheory import legendre_symbol

Pmax = 85
L = list(sieve.primerange(3,Pmax))
                
f = lambda i,j: legendre_symbol(L[i], L[j])

array = np.fromfunction(np.vectorize(f),
            (len(L),len(L)), dtype=int)

array = np.vstack((L, array))
u = [2]+ L
array = np.column_stack((u,array))

plt.imshow(array, cmap='terrain',          
        vmin = -1, vmax = 2, origin='lower')

for ind, x in np.ndenumerate(array):
    if x==2:
        plt.text(s='p/q', x = 0, y = 0, 
        va='center', ha='center',fontsize=7)
    else:
        plt.text(s = str(x), 
        x = ind[1], y = ind[0], 
        va='center', ha='center',fontsize=7)
        
plt.title('  Legendre symbols', fontsize=10)
plt.axis('off')
plt.show()
