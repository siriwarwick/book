import matplotlib.pyplot as plt
import numpy as np

def f(xarray):
    y=np.zeros_like(xarray)
    for i, x in enumerate(xarray):
        if x==0:
            y[i] = 0
        else: 
            y[i] = x*(1+2*x*np.sin(1/x))
    return y

fig, (ax1, ax2) = plt.subplots(1,2,
                  figsize=(10,6))
x1 = np.linspace(-0.4, 0.4, 100)
x2 = np.linspace(-0.04, 0.04, 100)

ax1.plot(x1, f(x1))
ax1.set_ylim(-0.4, 0.4)
ax1.title.set_text('y=f(x)')
ax1.grid('on')

ax2.plot(x2, f(x2))
ax2.set_ylim(-0.04,0.04)
ax2.title.set_text('Zoomed')
ax2.grid('on')

plt.show()