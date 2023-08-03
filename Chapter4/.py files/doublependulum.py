import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, pi
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation

g = 9.8  
l1, l2, m1, m2 = 1, 1, 1, 1  
mu = 1 + m1/m2
 
def derivs(t, Y):
    dYdt = np.zeros_like(Y) 
    Theta = Y[0]-Y[2]
    F = mu - cos(Theta)**2
    C = cos(Theta)
    S = sin(Theta)
    
    dYdt[0]= Y[1]
    dYdt[1]= (g*(sin(Y[2])*C-mu*sin(Y[0]))
           -(l2*Y[3]**2+l1*Y[1]**2*C)*S)/(l1*F)
    dYdt[2]= Y[3]
    dYdt[3]= (g*mu*(sin(Y[0])*C-sin(Y[2]))
        +(mu*l1*Y[1]**2+l2*Y[3]**2*C)*S)/(l2*F)
    return dYdt

h = 0.02
Tmax = 30
T = np.arange(0, Tmax+h, h)
Yinit = [pi/2, 0, pi/2, 0]

sol = solve_ivp(derivs, t_span = [0, Tmax], 
                y0= Yinit, t_eval=T)
theta1 = sol.y[0]
xbob1 = l1*sin(theta1)
ybob1 = -l1*cos(theta1)

theta2 = sol.y[2]
xbob2 = xbob1+l2*sin(theta2)
ybob2 = ybob1-l2*cos(theta2)

fig = plt.figure()
ax = fig.add_subplot(111, xlim=(-2.2, 2.2), 
                          ylim=(-2.2, 2.2))
ax.grid('on')

line, = ax.plot([], [], 'ro-', lw =3)
trace,= ax.plot([], [], 'b-', lw =1)
text = 'time = %.1fs'
time = ax.text(-2.1, 1.9, '')

def animate_frame(i, xbob2, ybob2, trace):
    x_i = [0, xbob1[i], xbob2[i]]
    y_i = [0, ybob1[i], ybob2[i]]
    line.set_data(x_i, y_i)
    trace.set_data(xbob2[:i], ybob2[:i])
    time.set_text(text % (i*h))
    return line, trace, time

ani = FuncAnimation(fig, animate_frame, 
      fargs=(xbob2, ybob2, trace),
      frames = len(T), 
      interval = 10)

plt.show()
