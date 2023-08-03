import numpy as np
import matplotlib.pyplot as plt

def odeFE(f, y0, h, a , b):
    N = int(round((b-a)/h))
    y = np.zeros(N+1)
    t = np.linspace(a, b, N+1)
    y[0] = y0
    for i in np.arange(0,N):
        y[i+1]=y[i]+ h*f(y[i],t[i])
    return y, t

def f(y, t):
    return -y

h = 0.001
y0 = 2
a, b = 0, 3
y, t = odeFE(f, y0, h, a, b)
T = np.linspace(a, b)

plt.figure(figsize=(3, 5))
plt.plot(t, y, 'k', 
         T, 2*np.exp(-T), '--')
plt.xlim([0,3])
plt.legend(['Numerical', 'Exact'])
plt.title('Forward-Euler, h=0.001')
plt.grid('on')
plt.show()
