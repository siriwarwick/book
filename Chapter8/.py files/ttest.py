import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

samples =[0.6517,-0.5602,0.8649,1.8570,1.9028] 
N = len(samples)
Smean = np.mean(samples)
Svar = np.var(samples, ddof=1)
scale = np.sqrt(Svar/N)

print(f'mu_Xbar = {Smean:.4}, sigma_Xbar = {scale:.4}')

fig, ax = plt.subplots(1,1, figsize=(6,3))
rv = stats.t(N-1, loc = Smean, scale = scale)
xmin, xmax = -2, 4
x2 = np.linspace(xmin, xmax, 150)
y2 = rv.pdf(x2) 
ax.plot(x2, y2, 'r')
ax.set_xlim((xmin,xmax))
ax.set_ylim((0,0.9))
ax.set_ylabel('Pdf')
ax.set_title('Estimate of the population' 
             ' mean (95% C.I. shaded)')

mu0 = 1.5
print(f'mu_0 = {mu0}')
ax.axvline(mu0, c='k', ls='--', lw=1)
ax.text(mu0, -0.05 , r'$\mu_0$')

res = stats.ttest_1samp(samples, mu0)

t = (Smean-mu0)/scale
print(f't statistic= {t:.4f}')
print(f'SciPy:t statistic= {res.statistic:.4f}')

p = 2*(1-rv.cdf(mu0))
print(f'p value = {p:.4f}')
print(f'SciPy:p value = {res.pvalue:.4f}')
print('')
ax.text(1.1*mu0,0.7, f'p = {p:.4}')

print('95% C.I. for mu')
CL = res.confidence_interval(0.95)
print(f'({CL.low:.4f},{CL.high:.4f})')

Xcl = np.linspace(CL.low, CL.high)
ax.fill_between(Xcl, 0, rv.pdf(Xcl), 
                color='plum', alpha=0.7)
plt.grid('on')
plt.show()
