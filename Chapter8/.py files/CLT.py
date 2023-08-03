import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm
import seaborn as sns

Means = []
Musize = int(1e4)

size = 100

for i in range(Musize):
    samples = uniform.rvs(size=size)
    mu = np.mean(samples)
    Means.append(mu)

fig,(ax1, ax2)=plt.subplots(1,2,figsize=(7,3))
x1 = np.linspace(0,1)
pdf = uniform.pdf(x1)
ax1.plot(x1, pdf)
ax1.set_title(f'Uniform on [0,1]') 
ax1.grid('on')

sns.histplot(Means, bins=25, 
             stat = 'density', ax=ax2)
ax2.set_title(f'Distribution of sample mean') 
x2 = np.linspace(min(Means), max(Means))
ax2.set_ylabel('')
MU = np.mean(Means)
SIG = np.sqrt(np.var(Means, ddof=1))
y2 = norm.pdf(x2, MU, SIG) 
ax2.plot(x2,y2, 'r')
ax2.grid('on')

plt.show()

Mcount = sum(i > 0.55 for i in Means)
Ans = Mcount/Musize
print(f'{Mcount} samples were >0.55. '
      f'P(X>0.55)={Ans}')
