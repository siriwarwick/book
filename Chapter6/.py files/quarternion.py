import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

v  = np.array((2,0,3))
Ax = np.array((1,1,1))
L= np.sqrt(Ax@Ax)
Axnorm = Ax/L
P = np.append(0,v)

def qmult(q1, q2):
    s1, s2 = q1[0], q2[0]
    v1 = q1[1:]
    v2 = q2[1:]
    S = s1*s2 - v1@v2
    V = s1*v2 + s2*v1 + np.cross(v1,v2)
    return np.append(S,V)

def qrotate(t):
    c, s = np.cos(t/2), np.sin(t/2)
    sI = s*Axnorm
    Q  = np.append(c, sI) 
    Qinv = np.append(c, -sI)
    return qmult(Q, qmult(P, Qinv))[1:]

tstep = 0.001
T = np.arange(0,2*np.pi, tstep)
X, Y, Z = ([] for i in range(3))

for i, t in enumerate(T):
    x,y,z = qrotate(t)
    X.append(x)
    Y.append(y)
    Z.append(z)
    
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d',
     xlabel = 'x', ylabel = 'y', zlabel = 'z',
     xlim = (0,4), ylim = (0,4), zlim= (0,4))
ax.set_box_aspect((1,1,1))

vec  =ax.quiver(0,0,0, *Ax, color = 'k', 
      length=2*L, arrow_length_ratio=0.05)
Cir, =ax.plot(X[0],Y[0],Z[2],'b',markersize=3)
Pnt, =ax.plot(*v, 'ro', markersize=6)
Coord=ax.text(0,1,5,'Initial point at '\
      f'({X[0]:.3f}, {Y[0]:.3f}, {Z[0]:.3f})')

axt = plt.axes([0.26, 0.02, 0.5, 0.02]) 
t_slide = Slider(axt, r'$\theta$', 0, 2*np.pi, 
                 valstep=tstep, valinit=0)
def update(val):
    t = t_slide.val
    i = int(t/tstep)
    x,y,z = qrotate(t)
    Cir.set_data_3d(X[0:i], Y[0:i], Z[0:i])
    Pnt.set_data_3d(x,y,z)
    Coord.set_text('Rotated point at '\
               f'({x:.3f}, {y:.3f}, {z:.3f})')
    fig.canvas.draw_idle()
    
t_slide.on_changed(update)

plt.show()
