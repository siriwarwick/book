import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def rx(t): 
    return np.cos(t)/(1+np.sin(t)**2)
def ry(t):
    return np.sin(t)*np.cos(t)\
           /(1+np.sin(t)**2)
def kappa(t):
    return 3*np.abs(np.cos(t))\
           /(1+np.sin(t)**2)

t = 0

fig,(ax1, ax2) = plt.subplots(1,2, 
                 figsize=(10,6))
plt.subplots_adjust(bottom=0.2)

ax1.set_aspect('equal')
ax1.set_ylim(-0.5,0.5)
ax1.set_xlim(-1.2,1.2)
ax1.title.set_text('Parametric curve')
ax1.grid('on')

r, = ax1.plot(rx(t), ry(t), 
                    'b', markersize=3) 
Pnt1, = ax1.plot(rx(t), ry(t), 
                    'ro', markersize=6) 

ax2.set_aspect('equal')
ax2.set_ylim(-1,4)
ax2.set_xlim(0,4*np.pi)
ax2.title.set_text('Curvature')
ax2.grid('on')

kap, = ax2.plot(t, kappa(t), 
                    'r', markersize=3) 
Pnt2, = ax2.plot(t, kappa(t), 
                    'bo', markersize=6) 

axt = plt.axes([0.25, 0.32, 0.5, 0.02])
t_slide = Slider(axt, 't', 
             0, 4*np.pi, valstep=0.001, 
             valinit=t)

def update(val):
    t = t_slide.val
    T = np.linspace(0,t,200)
    r.set_data(rx(T),ry(T))  
    Pnt1.set_data(rx(t),ry(t)) 
    kap.set_data(T, kappa(T))  
    Pnt2.set_data(t,kappa(t)) 
    fig.canvas.draw_idle()

t_slide.on_changed(update)

plt.show()
