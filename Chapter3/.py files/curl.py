import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

r, theta = np.meshgrid(np.linspace(0, 1),
                np.linspace(0, 2*np.pi))

def circulation(a): 
    if (a==0): return 0*r
    else: return  a*r**2*np.cos(2*theta)/\
                  np.sqrt(1+r**2*(a**2-1))
    
fig = plt.figure(figsize=(6,4))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='polar')

def data(a):
    Theta = np.linspace(0,2*np.pi)
    R = np.linspace(0, 1)
    rc, tc = np.meshgrid(R, Theta)
    X = rc*np.cos(tc)
    Y = rc*np.sin(tc)
    Z = a*np.sqrt(1-rc**2)  
    return X, Y, Z

def plotsurf(a):
    ax1.clear()
    ax1.set_title('Surface')
    ax1.set_xlim(-1,1)
    ax1.set_ylim(-1,1)
    ax1.set_zlim(0,2)
    X, Y, Z = data(a)
    P1 = ax1.plot_surface(X,Y,Z, cmap ='bone')
    return P1

def plotcirc(a):
    ax2.clear()
    ax2.set_title('Circulation (projected)')
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    C = circulation(a)
    heat = ax2.pcolormesh(theta, r, C, 
           shading = 'gouraud')
    ctf = ax2.contourf(theta, r, C, 
          levels= 50, cmap ='coolwarm',
          vmin = -1, vmax = 1)
    return heat, ctf

plt.subplots_adjust(bottom=0.15)
axa = plt.axes([0.16, 0.15, 0.7, 0.02])
a_slide = Slider(axa, 'a', 0, 2, 
          valstep = 0.01, valinit = 0)

plotsurf(0); plotcirc(0)

def update(val):
    a = a_slide.val
    plotsurf(a); plotcirc(a)

a_slide.on_changed(update)
plt.show()
