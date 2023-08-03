import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

dist = bernoulli(0.5)

exprmt = int(1e5)
throws = 10 
HHfound, THfound = 0, 0
PHH = []
PTH = []

for i in range(exprmt):
    rolls = dist.rvs(throws)
    seq = ''.join(str(r) for r in rolls)
    posHH = seq.find('11')
    posTH = seq.find('01')
    PHH.append(posHH + 1)
    PTH.append(posTH + 1)
    if posHH !=-1:
        HHfound += 1
    if posTH !=-1:
        THfound += 1

HHprob = HHfound/exprmt
THprob = THfound/exprmt

print(f'Pr(HH seen)= {HHprob}')
print(f'Pr(TH seen)= {THprob}')

fig,(ax1, ax2) = plt.subplots(2,1)
bins = np.arange(0, throws+1) - 0.5
ax1.set_title('Distributions of HH (top) and' 
              ' TH (bottom) occurrences')
HHtally, b1, b2 = ax1.hist(PHH, bins= bins, 
                           color = 'b')
THtally, c1, c2 = ax2.hist(PTH, bins= bins, 
                           color = 'r')
for X in [ax1,ax2]:
    X.set_xticks(range(0,throws))
    X.set_xlim(-0.5, throws-0.5)
    X.set_ylabel('No. of simulations')
    X.grid('on')
ax2.set_xlabel('First-occurrence position')
fig.show()
