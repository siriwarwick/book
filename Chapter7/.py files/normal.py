import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

Nballs = 25000
Nrows = 50 

Ber = bernoulli(0.5)
dx = 1
X = []

for i in range(Nballs):
    D = Ber.rvs(Nrows)
    rights = sum(D)
    x = (2*rights - Nrows)*dx
    X.append(x)
    
Max = max(X) + 4*dx
Min = min(X) - 4*dx

xN = np.linspace(Min, Max,100)
sig2 = Nrows*dx**2
yN = np.exp(-0.5*xN**2/sig2)/\
     np.sqrt(2*np.pi*sig2)

fig, ax = plt.subplots(1,1)
bins = np.arange(Min, Max, 2*dx)-dx
ax.hist(X, bins, density=True, color='teal') 
ax.set_xlabel('x')
ax.set_ylabel('Probability distribution')
ax.set_title(
    f'{Nballs} balls, {Nrows} rows of pegs')
ax.set_xlim([-round(Max),round(Max)])
ax.plot(xN, yN, 'r', linewidth=2)
plt.grid('on')
plt.show()
