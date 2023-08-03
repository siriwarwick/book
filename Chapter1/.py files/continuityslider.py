import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def h(xarray):
    y = np.zeros_like(xarray)
    for ind, x in enumerate(xarray):
        if x==0: 
            y[ind] = 1
        else: 
            y[ind] = np.sin(x)/x
    return y

xarray = np.linspace(-2, 2,200)
y = h(xarray)
x0 = 0
y0 = h([x0])
eps = 0.1

harray0 = np.full_like(xarray,y0)
harrayP = np.full_like(xarray,y0+eps)
harrayM = np.full_like(xarray,y0-eps)

fig,ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

plt.ylim(0.5, 1.15)
plt.plot(xarray, h(xarray) , lw=2)

h0 = plt.plot(xarray, harray0, 'b:') 
hP, = plt.plot(xarray, harrayP, 'r:')
hM, = plt.plot(xarray, harrayM, 'r:') 

axeps = plt.axes([0.15, 0.1, 0.7, 0.02])
eps_slide = Slider(axeps, '\u03B5', 
             0, 0.15, valstep=0.001, 
             valinit=eps)

def update(val):
    eps = eps_slide.val
    hP.set_ydata(y0 + eps)
    hM.set_ydata(y0 - eps)
    fig.canvas.draw_idle()

eps_slide.on_changed(update)

plt.show()
