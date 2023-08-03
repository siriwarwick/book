import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

f_obs = np.array([12, 33, 36, 16, 3])

C = len(f_obs)
Nsmpl = sum(f_obs)

X = np.arange(C)
f_exp = Nsmpl*stats.binom.pmf(X, C-1, 0.5)

chisq = sum((f_obs - f_exp)**2/f_exp)

res = stats.chisquare(f_obs, f_exp)

print(f'chi2 stat. = {chisq:.4f}')
print(f'SciPy: chi2 stat.={res.statistic:.4f}')
print('')

rv = stats.chi2(df = C-1)
p = 1-rv.cdf(chisq)

print(f'p value = {p:.4f}')
print(f'SciPy:p value = {res.pvalue:.4f}')

fig, ax = plt.subplots(1,1, figsize=(6,4))

width = 0.3
ax.bar(X-width/2, f_obs/Nsmpl, 
       width = width, color = 'skyblue')
ax.bar(X+width/2, f_exp/Nsmpl, 
       width = width, color = 'coral')
ax.set_title('Observed vs expected '
             f'frequencies, p = {p:.4f}') 
ax.set_xlabel('No. of heads')
ax.set_ylabel('Normalised frequency')

plt.legend(['Observed', 'Expected'])
plt.grid()
plt.show()
