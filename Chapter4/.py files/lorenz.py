import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation

sigma = 10
b = 8/3 
r = 28
 
def derivs(t, X):
    x,y,z = X
    dXdt = np.zeros_like(X)
    dXdt[0] = sigma *(y - x)
    dXdt[1] = x*(r-z) - y
    dXdt[2] = x*y - b*z
    return dXdt
 
h = 0.01 
Tmax = 60
T = np.arange(0, Tmax+h, h)
Xinit = [1, 1, 1] 

sol = solve_ivp(derivs, t_span=[0, Tmax], 
                y0=Xinit, t_eval=T)

x, y, z = sol.y[0], sol.y[1], sol.y[2]
data = np.array([x, y, z]) 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d',
    xlim=(-20,20), ylim=(-30,30), zlim=(0,50))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

traj,= ax.plot([],[],[],'b', lw=0.6)
pnt, = ax.plot([],[],[],'ro', markersize=3)
text = 't = %.1f'
time = ax.text(15,30,60, '')
    
def animate_frame(i, data, traj):
    traj.set_data_3d(data[0:3, :i])
    pnt.set_data_3d(data[0:3, i])
    time.set_text(text % (i*h))
    return traj, pnt, time

ani = FuncAnimation(fig, animate_frame,      
      fargs=(data, traj),
      frames= len(T), 
      interval = 1)

plt.show()
