import numpy as np
import matplotlib.pyplot as plt

a, b = 1, 2
N = np.round(np.logspace(2,5))

actual= 2*np.log(2)-1
hlist = (b-a)/N
error = []

def trapz(y,h):
    return h*(sum(y)-(y[0]+y[-1])/2)

for n in N:
    x = np.linspace(a,b,int(n+1))
    y = np.log(x)
    h = (b-a)/n
    estim = trapz(y,h)
    error.append(actual-estim)
    
plt.loglog(hlist, np.abs(error))
plt.xlim([1e-5, 1e-2])
plt.xlabel('h')
plt.ylabel('E(h)')
plt.grid('on')
plt.show()

k=(np.log(error[0])-np.log(error[-1]))/\
  (np.log(hlist[0])-np.log(hlist[-1]))
print(f'Gradient of line = {k:.5f}.')
