import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

O = np.array([0,0])
A = np.array([1,0])
B = np.array([1,1])
C = np.array([0,1])

fig,ax = plt.subplots()
plt.subplots_adjust(bottom=0.15)
plt.axis('square')

def vecplot(start, end, colour, alpha=1):
    vec = end-start
    ax.quiver(*start, *vec, color=colour, 
              alpha = alpha, angles='xy',
              scale_units='xy', scale=1,
              headaxislength=0, headwidth=0,
              headlength=0)
    return 

def transform(t):
    ax.clear()
    vecplot(O,A,'r',0.4)
    vecplot(A,B,'b',0.4)
    vecplot(B,C,'k',0.4)
    vecplot(C,O,'g',0.4)
    
    s, c = np.sin(t), np.cos(t)
    M = np.array([[c,-s],[s,c]])
    
    At = M@A
    Bt = M@B
    Ct = M@C
    
    vecplot(O,At,'r')
    vecplot(At,Bt,'b')
    vecplot(Bt,Ct,'k')
    vecplot(Ct,O,'g')

    ax.axis([-1.5,1.5,-1.5,1.5])
    ax.grid('on')
    return 

transform(0)
axt = plt.axes([0.23, 0.05, 0.55, 0.02]) 
t_slide = Slider(axt, 't', -2*np.pi, 2*np.pi,
          valstep = 0.02, valinit = 0)

def update(val):
    t = t_slide.val
    transform(t)

t_slide.on_changed(update)

plt.show()
