import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def zfunc(r,a):
    return np.sqrt((1-r**2)/a)

def data(a):
    theta = np.linspace(0,2*np.pi)
    if (a==0):
        z = np.linspace(0,5)
        Z, tc = np.meshgrid(z,theta)
        rc = 1
    elif (a>0):
        r = np.linspace(0,1)
        rc, tc = np.meshgrid(r, theta)
        Z = zfunc(rc,a)  
    else:
        r = np.linspace(1,2)
        rc, tc = np.meshgrid(r, theta)
        Z = zfunc(rc,a)  
    X = rc*np.cos(tc)
    Y = rc*np.sin(tc)
    return X, Y, Z

fig = plt.figure()
plt.subplots_adjust(bottom=0.15)                

ax = fig.add_subplot(projection='3d') 
ax.set_box_aspect((1,1,1)) 

def plotfig(a):
    X, Y, Z = data(a)
    ax.clear()
    P1 = ax.plot_surface(X,Y, Z, alpha=0.5)
    P2 = ax.plot_surface(X,Y,-Z, alpha=0.5)
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    ax.set_zlim(-2,2)
    return P1, P2

a = 0

axa = plt.axes([0.3, 0.05, 0.45, 0.02])
a_slide = Slider(axa, 'a', -2, 2,
           valstep = 0.05, valinit = a)

plotfig(a)

def update(val): 
    a = a_slide.val 
    plotfig(a)
    
a_slide.on_changed(update)
plt.show()
