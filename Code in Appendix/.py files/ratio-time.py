import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter as timer

N = np.around(np.logspace(1,6,1000))
timeL = []
timeA = []

for n in N:
    L = [x for x in range(int(n))]
    A = np.arange(n)
    
    tic = timer()
    [l+1 for l in L]
    toc = timer()
    timeL.append(toc-tic)
    
    tic = timer()
    A+1
    toc = timer()
    timeA.append(toc-tic)

ratio = np.array(timeL)/np.array(timeA)

plt.semilogx(N, ratio, 'r')
plt.xlabel('Length')
plt.ylabel('Ratio of runtimes (List:Array)')
plt.xlim(10, max(N))
plt.grid('on')
plt.show()
