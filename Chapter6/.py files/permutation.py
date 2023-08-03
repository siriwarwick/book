import numpy as np
import matplotlib.pyplot as plt
from sympy.combinatorics.generators import \
     symmetric

G = list(symmetric(4))
labels = True

f = lambda i,j : G.index(G[j]*G[i]) 

array=np.fromfunction(np.vectorize(f),
           (len(G),len(G)), dtype=int)

plt.imshow(array, cmap='hsv',          
           vmin = 0, vmax = len(G))

if labels:
    for ind, x in np.ndenumerate(array):
        plt.text(s = str(x), 
        x = ind[1], y = ind[0], 
        va='center', ha='center', fontsize=9)
        
plt.title(r'$S_4$',  fontsize=12)
plt.axis('off')
plt.show()
