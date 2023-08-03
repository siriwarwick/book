import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

rx = lambda t: np.sin(t)
ry = lambda t: np.cos(t)
rz = lambda t: t**2/20
tau = lambda t: 10*t/(t**2+101)

t = 0

fig = plt.figure(figsize=(10,6))

ax = fig.add_subplot(121, projection='3d')
r, = ax.plot(rx(t), ry(t), rz(t),
                    'b', markersize=3) 
Pnt1, = ax.plot(rx(t), ry(t), rz(t),
                    'ro', markersize=6) 
ax.set_title('Parametric curve')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(0, 20)

ax = fig.add_subplot(122)
ax.set_aspect(8)
ax.set_title('Torsion')
ax.set_xlim(0,6*np.pi)
ax.set_xlabel('t')
ax.set_ylim(0,0.6)
ax.grid('on')


torsion, = ax.plot(t, tau(t), 
                    'r', markersize=3) 
Pnt2, = ax.plot(t, tau(t), 
                    'bo', markersize=6) 

axt = plt.axes([0.2, 0.1, 0.5, 0.02])
t_slide = Slider(axt, 't', 
             0, 6*np.pi, valstep=0.001, 
             valinit=t)

def update(val):
    t = t_slide.val
    T = np.linspace(0,t,200)
    r.set_data_3d(rx(T),ry(T),rz(T))
    Pnt1.set_data_3d(rx(t),ry(t),rz(t))
    torsion.set_data(T, tau(T))
    Pnt2.set_data(t, tau(t))
    fig.canvas.draw_idle()

t_slide.on_changed(update)

plt.show()
