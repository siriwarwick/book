import numpy as np
import matplotlib.pyplot as plt
from sys import getsizeof

N = np.round(np.logspace(1,6,1000))
sizeL = []
sizeA = []

for n in N:
    L = [x for x in range(int(n))]
    A = np.arange(n)
    sizeL.append(getsizeof(L))
    sizeA.append(getsizeof(A))

ratio = np.array(sizeL)/np.array(sizeA)

plt.semilogx(N, ratio, 'b')
plt.xlabel('Length')
plt.ylabel('Ratio of sizes (List:Array)')
plt.xlim(10, max(N))
plt.grid('on')
plt.show()
