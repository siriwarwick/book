import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sympy import zeta

Tmax = 50
T  = np.linspace(0, Tmax, 1000)
Z  = [0.5 + t*1j for t in T]
Dom_r = np.real(Z)
Dom_i = np.imag(Z)
Img_r = []
Img_i = []

for z in Z:
    fz = complex(zeta(z))
    Img_r.append(np.real(fz))
    Img_i.append(np.imag(fz))

fig,(ax1,ax2)=plt.subplots(1,2,figsize=(12,4))
plt.rcParams.update({'font.size': 16})

curve1, = ax1.plot([],[], 'b', markersize=3)
dot1, = ax1.plot([],[],'ro', markersize=6)
text1 = 'z=%.1f +(%.4f)i'
tit1 = ax1.text(0.27, 1.03*Tmax,'') 
ax1.set_ylim(-0.5, 0.5+Tmax) 
ax1.set_xlim(0, 1)
ax1.grid('on')

curve2, = ax2.plot([],[], 'b', markersize=3)
dot2, = ax2.plot([],[],'ro', markersize=6)
text2 = 'zeta(z)=%.4f +(%.4f)i'
tit2 = ax2.text(-1.2, 3.1,'')
ax2.set_ylim(-3, 3) 
ax2.set_xlim(-2, 4)
ax2.grid('on')

def animate_frame(i, Dom_r,Dom_i,Img_r,Img_i):
    curve1.set_data(Dom_r[:i], Dom_i[:i])
    curve2.set_data(Img_r[:i], Img_i[:i])
    dot1.set_data([Dom_r[i]], [Dom_i[i]])
    dot2.set_data([Img_r[i]], [Img_i[i]])
    tit1.set_text(text1 % (Dom_r[i],Dom_i[i]))
    tit2.set_text(text2 % (Img_r[i],Img_i[i]))
    return curve1,curve2, dot1,dot2, tit1,tit2

ani = FuncAnimation(fig, animate_frame,
    fargs=(Dom_r, Dom_i, Img_r, Img_i),
    frames = len(T),
    interval = 20)

plt.show()
