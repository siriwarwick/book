import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

nmax = 5 
pi = np.pi
x = np.linspace(-2*pi, 2*pi, 1001)

def f(xarray):
    y = np.zeros_like(xarray)
    for ind, x in enumerate(xarray):
        xmod = x%(2*pi)
        if (xmod<pi and xmod>0):
            y[ind] = 1
        if x%pi==0:
            y[ind]= np.nan
    return y

def Fourier(x,nmax):
    S = 0
    for n in np.arange(1,nmax+1,2):
        S += np.sin(n*x)/n
    return 0.5+ 2*S/pi 

fig,ax = plt.subplots()
plt.subplots_adjust(bottom=0.15)

plt.plot(x, f(x),'r',lw=1.5)
Ffunc,= plt.plot(x, Fourier(x,nmax),'b',
        lw=0.5)
plt.xlim([-2*pi, 2*pi])
plt.ylim([-0.2, 1.2])
plt.grid('on')
plt.title(r'Fourier series up to $n$ terms')

axn = plt.axes([0.15, 0.05, 0.7, 0.03])
n_slide = Slider(axn, 'n', 1, 101, 
          valstep = 2, valinit = nmax)

def update(val):
    nmax = n_slide.val
    Ffunc.set_ydata(Fourier(x,nmax))
    fig.canvas.draw_idle()

n_slide.on_changed(update)

plt.show() 
