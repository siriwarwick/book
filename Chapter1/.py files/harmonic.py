import numpy as np
import matplotlib.pyplot as plt

Nmax = 1e5
n = np.arange(1, Nmax+1)
hplot = np.zeros_like(n)
harmo = 0

for N  in np.arange(0, int(Nmax)):
    harmo += 1/n[N]
    hplot[N]=harmo
    
    
fig, (ax1, ax2)=plt.subplots(2, figsize=(5,6))

ax1.semilogx(n, hplot, n, np.log(n) , '--')
ax1.set_xlim([10, Nmax])
ax1.set_ylim([2, 12])
ax1.legend(['Harmonic series', r'$\ln n$'], 
           loc = 'lower right')
ax1.grid('on')

ax2.semilogx(n, hplot-np.log(n), 'r')
ax2.set_xlim([10, Nmax])
ax2.set_ylim([0.57, 0.63])
ax2.set_xlabel(r'$n$')
ax2.legend([r'Harmonic - $\ln n$'])
ax2.grid('on')
plt.show()