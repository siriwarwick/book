import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def F(x, y):
    return x + 2*np.sin(x+y)

x = np.linspace(-2,2)
y = np.linspace(-2,2)
X, Y = np.meshgrid(x, y)
Z = F(X, Y)

N = np.array([-3,-2,1])/np.sqrt(14)

fig = plt.figure()
gs = gridspec.GridSpec(1, 2, 
       width_ratios=[1.5,1])

ax1 = fig.add_subplot(gs[0], 
            projection='3d')
ax1.set_box_aspect((1,1,1))
ax1.plot_surface(X,Y, Z, alpha=0.7,
            rstride=5, cstride=5,
            edgecolor='k',
            cmap='viridis')
ax1.plot(0,0,0, 'or')
ax1.quiver(0,0,0,N[0],N[1],N[2], 
            length=1, color='r')
ax1.set_xlim(-2,2)
ax1.set_ylim(-2,2)
ax1.set_zlim(-2,2)

ax2 = fig.add_subplot(gs[1])
p = ax2.contour(X, Y, Z, 20)
fig.colorbar(p, shrink = 0.4)
ax2.plot(0,0, 'or')
ax2.quiver(0,0, N[0],N[1], color='r',
           scale_units='xy', scale=1)
ax2.set_aspect('equal')
ax2.set_title('Projection onto z=0')

fig.tight_layout()
plt.show()
