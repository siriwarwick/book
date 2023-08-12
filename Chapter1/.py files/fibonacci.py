import numpy as np
import matplotlib.pyplot as plt

Nend = 25

F = np.zeros(Nend+1)
R = np.zeros(Nend+1)

F[1] = 1
F[2] = 1

for i in np.arange(3,Nend+1):
    F[i]=F[i-1]+F[i-2]
    R[i]=F[i]/F[i-1]
 
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(11,4))

Nmin = 5
Nplt = range(Nmin, Nend+1)

ax1.semilogy(Nplt, F[Nmin:Nend+1], 'bo-', ms=3)
ax1.set_xlabel(r'$n$')
ax1.set_ylabel(r'$F_n$')
ax1.set_xlim(Nmin, Nend)
ax1.set_xticks(range(Nmin, Nend+1, 5))
ax1.grid('on')

ax2.plot(Nplt, R[Nmin:Nend+1], 'ro-', ms=3)
ax2.set_xlabel(r'$n$')
ax2.set_ylabel(r'$F_{n}/F_{n-1}$')
ax2.set_xlim(Nmin, Nend)
ax2.set_xticks(range(Nmin, Nend+1, 5))
ax2.grid('on')

plt.show()