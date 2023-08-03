import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

x, y = np.meshgrid(np.linspace(-1, 1,20),
                   np.linspace(-1, 1,20))
z=0.5

u = lambda x,y,z: 2*x*z
v = lambda x,y,z: z+2*np.cos(y)
div = lambda x,y,z: 2*z-2*np.sin(y)+ 6*z**2
dmax= 10
dmin= -2

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.15)
ax.axis([x.min(),x.max(),y.min(),y.max()])

def plotdiv(z):
    D = div(x,y,z)
    U = u(x,y,z)
    V = v(x,y,z)
    ax.clear()
    ax.set_title('Divergence heatmap')
    heat = ax.pcolormesh(x, y, D, 
           vmin = dmin, vmax=dmax, 
           shading='gouraud',cmap='RdBu')
    arrow = ax.quiver(x, y, U, V, 
            units='xy', scale=5)
    return arrow, heat

arrow, heat= plotdiv(z)
fig.colorbar(heat, ax=ax)

axz = plt.axes([0.15, 0.05, 0.6, 0.02])
z_slide = Slider(axz, 'z slice', -1, 1, 
          valstep = 0.02, valinit = z)

def update(val):
    z = z_slide.val
    plotdiv(z)

z_slide.on_changed(update)
plt.show()
