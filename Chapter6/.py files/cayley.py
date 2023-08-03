import numpy as np
import matplotlib.pyplot as plt

N = np.arange(0,10)
Nmod = 10
labels = True

f = lambda i,j : (i+j) % Nmod

array=np.fromfunction(lambda i,j:f(N[i],N[j]),
                   (len(N),len(N)), dtype=int)

plt.imshow(array, cmap='hsv',          
           vmin = N[0], vmax = len(N))

if labels:
    for ind, x in np.ndenumerate(array):
        plt.text(s = str(x), 
        x = ind[1], y = ind[0], 
        va='center', ha='center')
        
plt.title(r'($\mathbb{Z}_{10}, +)$')
plt.axis('off')
plt.show()
