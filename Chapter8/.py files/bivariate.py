import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.stats import multivariate_normal

rho = 0.5
S1, S2 = 1, 1

S12 = np.sqrt(S1*S2)

fig = plt.figure(figsize=(10,6))
plt.subplots_adjust(bottom=0.15)

ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)
ax2.set_box_aspect(1)
ax2.set_title('2D projection')
ax2.yaxis.tick_right(); 
ax2.yaxis.set_label_position('right')
ax2.set_xlabel('x'); ax2.set_ylabel('y')

xplot = np.linspace(-2,2)
yplot = np.linspace(-2,2)
X, Y = np.meshgrid(xplot,yplot)

def plots(rho): 
    Cov = [(S1,rho*S12), (rho*S12,S2)]
    rv = multivariate_normal(cov = Cov)
    Z = rv.pdf(np.dstack([X,Y]))
    cmap = 'rainbow'
    plot1 = ax1.plot_surface(X, Y, Z,
                       alpha=0.9, cmap=cmap)
    ax1.set_zlim(0, 0.3)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    
    levels = np.linspace(0,np.max(Z),15)
    plot2 = ax2.contourf(X, Y, Z,
                levels =levels, cmap=cmap)
    return plot1, plot2

axt = plt.axes([0.34, 0.1, 0.4, 0.03])
rho_slide = Slider(axt, r'$\rho$', 
             -1, 1, valstep=0.01, valinit=0)
axt.add_artist(axt.xaxis)
axt.set_xticks([-1,0,1])

plots(0)

def update(val):
    ax1.clear()
    rho = rho_slide.val
    plots(rho)
    
rho_slide.on_changed(update)
plt.show()
