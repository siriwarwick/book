import numpy as np
import matplotlib.pyplot as plt

Nmax = int(1e6)
d, ell = 0.1, 0.05

Nlist = range(1,Nmax+1)
rng = np.random.default_rng()
Prob =[]
count = 0

for N in Nlist:
    yhead = 10*d*rng.random()
    theta = 2*np.pi*rng.random()
    ytail = yhead + ell*np.sin(theta)

    if yhead//d != ytail//d:
        count += 1
        
    prob = count/N
    Prob.append(prob)

plt.semilogx(Nlist[100:], Prob[100:], 'b')
plt.xlabel('Number of needles')
plt.ylabel('Probability of intersection')
plt.xlim(1e2, Nmax)
plt.title(f'Final probability = {prob:5}')
plt.grid('on')
plt.show()
