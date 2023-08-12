import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return np.sqrt(np.abs(x))

h=1e-6
xp= np.linspace(0,1)
xn= np.linspace(-1,-h)
gxp = g(xp)
gxn = g(xn)
dgp = (g(xp+h) - gxp)/h
dgn = (g(xn+h) - gxn)/h

plt.plot(xp, gxp, 'b--', 
         xp, dgp, 'orange', 
         xn, gxn, 'b--',  
         xn, dgn, 'orange')
plt.legend(["y=g(x)" ,"y=g'(x)"])
plt.grid('on')
plt.xlim([-1,1])
plt.ylim([-2,2])
plt.show()