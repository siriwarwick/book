import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

r, theta = np.meshgrid(np.linspace(0, 1),
                np.linspace(0, 2*np.pi))
a = 0.5

def circ(r, theta, a): 
    if (a==0): 
        return 0*r
    else: 
        return  a*r**2*np.cos(2*theta)/\
             np.sqrt(1 + r**2*(a**2-1))

def plotcirc(a):
    C = circ(r,theta,a)
    ax.clear()
    ax.set_title('Circulation heatmap')
    ax.set_yticklabels([])
    heat = ax.pcolormesh(theta, r, C, 
                    shading = 'auto')
    ctf = ax.contourf(theta, r, C, levels=20,
          vmin = -1, vmax = 1)
    return heat,ctf

ax = plt.subplot(projection='polar')
plt.subplots_adjust(bottom=0.15)

heat, ctf = plotcirc(a)
plt.colorbar(ctf)

axa = plt.axes([0.16, 0.05, 0.65, 0.02])
a_slide = Slider(axa, 'a', 0, 2, 
          valstep = 0.01, valinit = a)

def update(val):
    a = a_slide.val
    plotcirc(a)

a_slide.on_changed(update)
plt.show()
