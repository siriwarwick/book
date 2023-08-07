import numpy as np
import matplotlib.pyplot as plt
from math import factorial

sims = 500

Ndots = 100
grid = 10
rng = np.random.default_rng()
Tally= []

for sim in range(sims):   
    Count = np.zeros((grid,grid))
    dotx = rng.uniform(0, grid, Ndots)
    doty = rng.uniform(0, grid, Ndots)
    
    for x,y in zip(dotx,doty):
        n, m = int(x), int(y)
        Count[m,n] += 1
    C = Count.flatten()
    Tally = np.concatenate((Tally,C))
    
Max = max(Tally)
xbins = np.arange(Max+2)
bins = xbins-0.5        
prob = plt.hist(Tally, bins=bins, 
               density=True, color='deeppink')

mean = Ndots/(grid**2)
Poisson =[mean**x*np.exp(-mean)/\
     factorial(int(x)) for x in xbins]

plt.title(f'Dot count in a {grid}x{grid} grid' 
          f' with {Ndots} dots')
plt.plot(xbins, Poisson, 'k')
plt.xticks(xbins)
plt.xlim([-0.5, Max+0.5])
plt.grid('on')
plt.show()
