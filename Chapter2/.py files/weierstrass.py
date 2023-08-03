import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

a, b = 0.5, 13
m_max = 25
x = np.linspace(-2,2,2500)

def fn(x,n,a,b):
    return a**n*np.cos(np.pi*x*b**n)

def g(x,a,b):
    S = 0
    for i in np.arange(0,m_max+1):
        S += fn(x,i,a,b)
    return S

fig,ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

Wfunc, = plt.plot(x, g(x,a,b),'k',lw=0.5)
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.grid('on')
plt.title('The Weierstrass Function')

axa = plt.axes([0.15, 0.05, 0.7, 0.02])
a_slide = Slider(axa, 'a', 0, 1, 
                 valstep=0.01, valinit=a)

axb = plt.axes([0.15, 0.1, 0.7, 0.02])
b_slide = Slider(axb, 'b', 1, 25, 
                 valstep=0.01, valinit=b)

def update(val):
    a = a_slide.val
    b = b_slide.val
    Wfunc.set_ydata(g(x,a,b))
    fig.canvas.draw_idle()

a_slide.on_changed(update)
b_slide.on_changed(update)

plt.show() 
