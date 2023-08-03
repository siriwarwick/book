import numpy as np
import matplotlib.pyplot as plt

h = np.logspace(-20, 0, 300)
x = 1 
f = lambda x: x**3   
actual = 3*x**2

fx = f(x)
fxp = f(x+h)
fxm = f(x-h)

est1 = (fxp-fx)/h
est2 = (fxp-fxm)/(2*h)

err1 = abs(actual-est1)
err2 = abs(actual-est2)

plt.loglog(h,err2, 'k', lw=2) 
plt.loglog(h,err1, 'r', lw=1)
plt.legend(['Symmetric difference', 
            'Forward difference'])
plt.xlabel(r'$h$')
plt.ylabel(r'Absolute error $E$')
plt.xlim([1e-20, 1])
plt.grid('on')
plt.show()
