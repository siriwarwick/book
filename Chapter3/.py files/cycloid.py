import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

theta = np.linspace(0,2*np.pi)

circ_x = lambda t: t+np.cos(theta)
circ_y = 1+np.sin(theta)

cycl_x = lambda t: t - np.sin(t)
cycl_y = lambda t: 1 - np.cos(t)
     
t = 0

fig,ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
plt.ylim(0,3)
plt.xlim(-1,1+4*np.pi)
plt.gca().set_aspect('equal')
plt.grid('on')

Circ,=plt.plot(circ_x(t), circ_y,'k') 
Cycl,=plt.plot(cycl_x(t), cycl_y(t), 
                    'r', markersize=3) 
Pnt,=plt.plot(cycl_x(t), cycl_y(t), 
                    'ro', markersize=5) 
axt = plt.axes([0.18, 0.33, 0.67, 0.02])
t_slide = Slider(axt, 't', 0, 4*np.pi, 
                 valstep=0.001, valinit=t)

def update(val):
    t = t_slide.val
    Circ.set_xdata(circ_x(t))
    T = np.linspace(0,t, int(50*t))
    Cycl.set_data(cycl_x(T),cycl_y(T))  
    Pnt.set_data([cycl_x(t)],[cycl_y(t)]) 
    fig.canvas.draw_idle()

t_slide.on_changed(update)

plt.show()
