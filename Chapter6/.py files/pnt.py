import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from sympy import primepi

Nmin=1e1
Nmax=1e8

Nlist = np.logspace(np.log10(Nmin),
                    np.log10(Nmax),300)

P = [primepi(n) for n in Nlist] 

def li(x):
    X, err = quad(lambda t: 1/np.log(t),2,x)
    return X 

Li = np.vectorize(li) 

PNT1 = Nlist/(np.log(Nlist))
PNT2 = Li(Nlist)

err1 = P/PNT1
err2 = P/PNT2

plt.semilogx(Nlist, err1, 
             Nlist, err2,
             Nlist, np.ones_like(Nlist),'k--')
plt.xlim(Nmin,Nmax)
plt.grid('on')
plt.xlabel('x')
plt.legend([r'$\pi(x)/(x/\ln x)$',
            r'$\pi(x)/Li(x)$'])
plt.show()
