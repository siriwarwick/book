import numpy as np
import matplotlib.pyplot as plt

def Nth_term(x,N):
    return -(-1)**N*x**N/N
    
x = 0.4
N_max = 15 
Nlist = np.arange(1,N_max+1)
P = 0
PNlist = []
lowlist=[]
hilist=[]

for N in Nlist:
    P = P + Nth_term(x,N)
    PNlist.append(P)
    Np= N+1
    low = (x/(1+x))**Np/Np
    lowlist.append(low)    
    hi = x**Np/Np
    hilist.append(hi)   
    
RN = abs(PNlist-np.log(1+x))
        
plt.semilogy(Nlist, RN, lw=2, 
             color = 'r')
plt.semilogy(Nlist,lowlist,'r:',
             Nlist,hilist, 'r:')
plt.legend([r'$|R_N(x=0.4)|$']) 
plt.xticks(Nlist) 
plt.xlim([1,N_max])
plt.xlabel('Polynomial order N')
plt.ylim([1e-10,0.1])
plt.grid('on')
plt.show()
