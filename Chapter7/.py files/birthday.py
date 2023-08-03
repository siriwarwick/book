import numpy as np
import matplotlib.pyplot as plt

sims = int(1e5)
grpsize = []
rng = np.random.default_rng()

for i in range(sims):
    BD = []
    sameBD = 0
    while sameBD==0:
        newBD = rng.integers(1, 366)
        BD.append(newBD)
        uniq = set(BD)
        sameBD = len(BD)-len(uniq)
    grpsize.append(len(BD))

Max = max(grpsize)+1

fig,(ax1, ax2) = plt.subplots(2,1)
bins = np.arange(0, Max)-0.5
prob, a1, a2 = ax1.hist(grpsize, bins, 
               density=True, color='purple')
ax1.set_ylabel('Probability distribution')
ax1.set_title('Distribution of group size for'
              ' same birthday to occur')

plt.subplots_adjust(hspace=0.1)
plt.setp(ax1.get_xticklabels(), visible=False)

cprob, b1, b2 = ax2.hist(grpsize, bins, 
                density=True, cumulative=True,
                histtype='step', color = 'b')
ax2.set_ylabel('Cumulative distribution')
ax2.set_yticks(np.arange(0,1.01,0.1))
ax2.set_ylim([0,1])
ax2.set_xlabel('Group size')

ax2.axhline(y=0.5, color='r', linestyle=':')
ans = np.searchsorted(cprob, 0.5)
ax2.text(41, 0.52, 'Pr(>0.5) when group size'
                   r'$\geq$' f'{ans}')
people = np.arange(1,101)

for X in [ax1,ax2]:
    X.set_xticks(range(0,Max,5))
    X.set_xlim(0,Max-2)
    X.grid('on')

plt.show()
