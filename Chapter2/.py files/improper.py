import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

alpha = np.linspace(0.05, 7, 500)
error = []
f = lambda x: np.exp(-x**2)
g = lambda x: np.exp(-1/x**2)/x**2

exact = 0.5*np.sqrt(np.pi)
h = 1e-3

def makeodd(N):
    return N + 1 - (N%2)

for a in alpha:
    N1 = int(a/h)
    N2 = int(1/(a*h))
    x1 = np.linspace(0, a, makeodd(N1))
    x2 = np.linspace(1e-8, 1/a, makeodd(N2))
    
    integ = simpson(f(x1),x1)+simpson(g(x2),x2)
    err = abs(exact-integ)
    error.append(err)

plt.semilogy(alpha,error,'g')
plt.xlim([0,max(alpha)])
plt.xlabel(r'$\alpha$')
plt.ylabel('Absolute error')
plt.grid('on')
plt.show()
