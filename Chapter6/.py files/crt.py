import numpy as np
import matplotlib.pyplot as plt
from sympy.ntheory.modular import\
     solve_congruence

m0 = 7
m1 = 8

neg = -100

def f(i,j):
    u = solve_congruence((i, m0), (j, m1))
    if u==None:
        return neg
    else:
        return int(u[0])

array=np.fromfunction(np.vectorize(f),
                   (m0,m1), dtype=int)

plt.imshow(array, cmap='magma',          
           vmin = neg, vmax = m0*m1)

for ind, x in np.ndenumerate(array):
    if x!=neg:
        plt.text(s = str(x), 
        x = ind[1], y = ind[0], 
        va='center', ha='center',fontsize=12)
        
plt.title(f'x=(#row-1) (mod {m0}) and ' 
          f'x = (#col-1) (mod {m1})',  
          fontsize=12)
plt.axis('off')
plt.show()
