import numpy as np
from scipy import linalg as LA
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

A= np.array([[1,1],[1, 0]])

lam, P = LA.eig(A)
Pinv = LA.inv(P)
D = np.array([[lam[0],0],[0,lam[1]]])

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
ax.set_aspect('equal') 
ax.axis([-2,2,-1.5,1.5])
ax.grid('on')

T = np.linspace(0,2*np.pi,100)
X = np.array([[np.cos(T)],[np.sin(T)]])\
    .reshape(2,len(T))
PinvX= Pinv@X
DPinvX= D@PinvX
PDPinvX= P@DPinvX

Vec1,  = ax.plot([0,X[0,0]], [0,X[1,0]],'bo:')
Curve1,= ax.plot(X[0,:], X[1,:],'b:')
Vec2,  = ax.plot([0,X[0,0]], [0,X[1,0]],'ro-')
Curve2,= ax.plot(X[0,:], X[1,:],'r-')

axt = plt.axes([0.25, 0.1, 0.5, 0.02]) 
t_slide = Slider(axt, '',0, 3, valstep=0.001,
                 valinit=0)
t_slide.valtext.set_visible(False)
axt.add_artist(axt.xaxis)
slider_ticks = [1,2,3]
slider_label = [r'$P^{-1}$', r'$D$', r'$P$']
axt.set_xticks(slider_ticks, slider_label)

def Frame(t):
    if t<1:
        Xt=X
        Ft=t*PinvX+(1-t)*Xt
    elif 1<=t and t<2:
        Xt=PinvX
        Ft=(t-1)*DPinvX+(2-t)*Xt
    else:
        Xt=DPinvX
        Ft=(t-2)*PDPinvX+(3-t)*Xt
    return Xt, Ft

def update(val):
    t = t_slide.val
    Xt, Ft = Frame(t)
    Curve1.set_data(Xt[0,:], Xt[1,:])
    Vec1.set_data([0,Xt[0,-1]], [0,Xt[1,-1]])
    Curve2.set_data(Ft[0,:], Ft[1,:])
    Vec2.set_data([0,Ft[0,-1]], [0,Ft[1,-1]])
    fig.canvas.draw_idle()
    
t_slide.on_changed(update)

plt.show()
