import numpy as np
import matplotlib.pyplot as plt
import random

Nsims = int(1e3)
Nsteps = 500

Sims = np.arange(Nsims)
Steps= np.arange(Nsteps+1)
SumDist = np.zeros_like(Steps)

fig,(ax1, ax2)=plt.subplots(1,2,figsize=(10,5))
ax1.set_xlim(0, Nsteps)
ax1.set_ylim(-3.5*np.sqrt(Nsteps), 
             3.5*np.sqrt(Nsteps))
ax1.set_xlabel('Number of steps $N$')
ax1.set_ylabel('Displacement from the origin')
ax1.grid('on')
color=plt.cm.prism_r(np.linspace(0, 1, Nsims))

for i in Sims:
    R = [random.randint(0,1) for 
         i in range(1,Nsteps+1)]
    moves = 2*np.array(R)-1
    traj = np.cumsum(moves)
    traj = np.insert(traj, 0, 0)
    ax1.plot(Steps, traj, '-', 
             lw = 0.5, c = color[i])
    SumDist += np.abs(traj)


bound = 3*np.sqrt(Steps)

ax1.plot(Steps, bound, 'k--',
         Steps, -bound, 'k--')

AveDist = SumDist/Nsims    

ax2.plot(Steps, AveDist, 'bo-', ms=1) 
ax2.plot(Steps,np.sqrt(2*Steps/np.pi),'r',lw=1)
ax2.set_xlim(0, Nsteps)
ax2.set_ylim(0, np.ceil(np.max(AveDist)))
ax2.set_xlabel(r'Number of steps $N$')
ax2.set_ylabel('Mean distance from the origin')
ax2.legend(['Simulation', r'$\sqrt{2N/\pi}$'])
ax2.grid('on')

plt.show()
