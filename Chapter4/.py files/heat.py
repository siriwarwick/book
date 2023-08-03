import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation


N = 40
x = np.linspace(0,1,N+1)
dx = x[1]-x[0]

def derivs(t, U):
    dUdt = np.zeros_like(U)
    dUdt[1:-1]=(U[2:]-2*U[1:-1]+U[:-2])/dx**2
    return dUdt

h = 5e-4
Tmax = 0.5
T = np.arange(0, Tmax+h, h)
Uinit = np.sin(np.pi*5*x/2)

sol = solve_ivp(derivs, t_span=[0, Tmax],
                y0=Uinit, t_eval=T)

U = np.zeros((len(T),len(x)))

for i in np.arange(1,N):
        U[:,i] = sol.y[i]

U[:,-1] = np.ones(len(T))

fig = plt.figure()
ax = fig.add_subplot(111, xlim=(0, 1),
                          ylim=(-1, 1))
ax.grid('on')
ax.set_xlabel('x') 
ax.set_ylabel('u(x,t)')
line, = ax.plot([], [], 'r', lw=2) 
text = 't = %.3fs'
time = ax.text(0.03, 0.8, '')

def animate_frame(i):
    line.set_data(x, U[i,:])
    time.set_text(text % (i*h))
    return line, time

ani = FuncAnimation(fig, animate_frame,
       frames = len(T),
       interval = 20)

plt.show()
