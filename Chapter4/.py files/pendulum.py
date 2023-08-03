import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation

plt.rcParams.update({'font.size': 22})

g = 9.8  
l = 1.0  

def derivs(t, Y):
    dYdt = np.zeros_like(Y) 
    dYdt[0] = Y[1]
    dYdt[1] = -g/l*np.sin(Y[0])
    return dYdt

h = 0.025
Tmax = 10
T = np.arange(0, Tmax+h, h)

Yinit = [np.pi/4, 0]

sol = solve_ivp(derivs, t_span = [0, Tmax], 
                y0= Yinit, t_eval=T)

theta = sol.y[0]
xbob = l*np.sin(theta)
ybob = -l*np.cos(theta)

fig = plt.figure()
ax = fig.add_subplot(111, xlim=(-1.2, 1.2), 
                          ylim=(-1.2, 1.2))
ax.grid('on')
line, = ax.plot([], [], 'ro-', lw=3)
text = 'time = %.1fs'
time = ax.text(-1.1, 0.9, '')
 
def animate_frame(i):
    x_i = [0, xbob[i]]
    y_i = [0, ybob[i]]
    line.set_data(x_i, y_i)
    time.set_text(text % (i*h))
    return line, time

ani = FuncAnimation(fig, animate_frame, 
       frames = len(T), 
       interval = 10)

plt.show()
