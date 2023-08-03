import numpy as np
import matplotlib.pyplot as plt

a, b = 1, 2
N = np.round(np.logspace(2,5,300))
actual= 2*np.log(2)-1
Hlist = (b-a)/N
error = []

def simp(y,h):
    return (h/3)*(y[0]+y[-1]+\
    4*sum(y[1:-1:2])+2*sum(y[2:-1:2]))

for n in N:
    n2 = 2*n
    x = np.linspace(a,b,int(n2+1))
    y = np.log(x)
    h = (b-a)/n2
    estim = simp(y,h)
    error.append(actual-estim)
    
plt.loglog(Hlist , np.abs(error))
plt.xlim([1e-5,1e-2])
plt.xlabel('H')
plt.ylabel('E(H)')
plt.grid('on')
plt.show()

k=(np.log(error[0])-np.log(error[50]))/\
  (np.log(Hlist[0])-np.log(Hlist[50]))
print(f'Gradient of line = {k:.5f}.')
