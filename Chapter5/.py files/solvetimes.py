import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg as LA
from time import perf_counter as timer

N=np.arange(1,5001,50)
rng = np.random.default_rng()
t1 = []
t2 = []
    
for n in N:
    A = rng.random((n,n))
    b = np.ones((n,1))
    
    tic = timer()
    x1 = LA.solve(A, b)
    toc = timer()
    t1.append(toc-tic)

    tic = timer()
    x2 = LA.inv(A)*b  
    toc = timer()
    t2.append(toc-tic)
    
plt.plot(N,t1, '-ro',N,t2, '-bx') 
plt.xlabel('Matrix dimension')
plt.ylabel('Time (s)')
plt.legend(['linalg.solve(A, b)', 
            'linalg.inv(A)*b'])
plt.grid('on')
plt.show()
