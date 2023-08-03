import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial as P
from sympy import S 

f = lambda x: np.arctan(x)/x

Nlist = np.round(np.logspace(1,7,200))

rng = np.random.default_rng()
Err = []
G = S.Catalan

for N in Nlist:
    xi = rng.random(int(N))
    est = np.mean(f(xi))
    Err.append(float(abs(est/G -1)))

logx = np.log10(Nlist)
logy = np.log10(Err)
poly = P.fit(logx, logy, 1).convert()
yfit = 10**(poly(logx))

plt.loglog(Nlist, Err, 'b.', 
           Nlist, yfit, 'r')
plt.xlim(10, 1e7)
plt.xlabel(r'$N$ (number of points)')
plt.ylabel('|Fractional error|')
plt.title(f'Gradient = {poly.coef[1]:.3}')
plt.grid('on')
plt.show()
