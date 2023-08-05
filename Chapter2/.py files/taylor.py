import numpy as np
import matplotlib.pyplot as plt

def nth_term(x,n):
        return -(-1)**n*x**n/n
    
n_max = 40
x = np.linspace(-0.99, 2, 100)
S = np.zeros_like(x)

for n in np.arange(1,n_max+1):
    S = S + nth_term(x,n)
    b=n/n_max
    if (n>=5):
        plt.plot(x,S,label='_nolegend_',
        color = (0,0,b), lw=1)
    
plt.plot(x, np.log(1+x),lw=2,color='k')
plt.legend([r'$y=ln(1+x)$'], loc='upper left')
plt.xlim([-0.99, 2])
plt.ylim([-2,2])
plt.grid('on')
plt.show()
