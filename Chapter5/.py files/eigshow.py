import numpy as np
from scipy import linalg as LA
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

A = np.array([[1,1],[1.5,0.5]])
lam, w = LA.eig(A)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
ax.set_aspect('equal') 
ax.set_title('Make the vectors parallel!') 
ax.axis([-2,2,-2,2])
ax.grid('on')

Vec1, = ax.plot([0,1], [0,0],'bo-')
Vec2, = ax.plot([0,A[0,0]], [0,A[1,0]],'ro-')
plt.legend(['x', 'Ax'], loc='lower right')

Curve1,=ax.plot(1, 0,'b:')
Curve2,=ax.plot(A[0,0], A[1,0],'r--')
ax.plot([-w[0,0],w[0,0]], 
        [-w[1,0],w[1,0]],'g', lw=0.5)
ax.plot([-w[0,1],w[0,1]], 
        [-w[1,1],w[1,1]],'g', lw=0.5)

axt = plt.axes([0.25, 0.1, 0.5, 0.02]) 
t_slide = Slider(axt, r'$\theta$',
             0, 2*np.pi, valstep=0.001,
             valinit=0)

def update(val):
    t = t_slide.val
    T = np.linspace(0,t,100)
    
    cT = np.cos(T)
    sT = np.sin(T)
    xT = np.array([[cT],[sT]]).reshape(2,len(T))
    AxT= A@xT
    
    Vec1.set_data([0,cT[-1]], [0,sT[-1]])
    Vec2.set_data([0,AxT[0,-1]], [0,AxT[1,-1]])
    Curve1.set_data(cT, sT)
    Curve2.set_data(AxT[0,:], AxT[1,:])
    
    fig.canvas.draw_idle()
    
t_slide.on_changed(update)

plt.show()
