import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

Nx, Ny = 40, 40
x = np.linspace(0,1,Nx+1)
y = np.linspace(0,1,Ny+1)
dx, dy  = x[1]-x[0], y[1]-y[0]
h = 1e-3
Tmax = 3
T = np.arange(0, Tmax+h, h)
Cx2, Cy2 = (h/dx)**2, (h/dy)**2

IC1 = lambda x, y : np.sin(2*np.pi*x)*\
                   np.sin(2*np.pi*y)
IC2 = lambda x, y: 0*x

X, Y = np.meshgrid(x, y)
U = IC1(X, Y)
V = IC2(X, Y)
Unm1 = np.zeros((len(x),len(y)))
Usnap = np.zeros((len(x),len(y),len(T))) 
    
def first_step(U):
    Ustep = np.zeros((len(x),len(y)))
    Uxx=U[:-2, 1:-1]-2*U[1:-1,1:-1]+U[2:,1:-1]
    Uyy=U[1:-1,:-2] -2*U[1:-1,1:-1]+U[1:-1,2:]
    Ustep[1:-1,1:-1]= U[1:-1,1:-1] + \
       h*V[1:-1,1:-1]+ 0.5*(Cx2*Uxx + Cy2*Uyy)
    return Ustep

def next_step(U, Unm1):
    Ustep = np.zeros((len(x),len(y)))
    Uxx=U[:-2, 1:-1]-2*U[1:-1,1:-1]+U[2:,1:-1]
    Uyy=U[1:-1,:-2] -2*U[1:-1,1:-1]+U[1:-1,2:]
    Ustep[1:-1,1:-1]=-Unm1[1:-1, 1:-1]+\
       2*U[1:-1,1:-1]+ Cx2*Uxx + Cy2*Uyy
    return Ustep

Usnap[:,:,0] = U
Usnap[:,:,1] = first_step(U)

for i in np.arange(2, len(T)):
    Usnap[:,:,i] = next_step(Usnap[:,:,i-1], 
                             Usnap[:,:,i-2])
fskip = 10
frames = Usnap[:,:, 0::fskip]

def plot_ith_frame(i):
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    ax.set_zlim([-1,1])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    surf = (ax.plot_surface(X,Y,frames[:,:,i],
        cmap='Spectral', vmax = 1, vmin = -1))
    ax.text(0,0,1.6, f't= {i*fskip*h:.3f} s')
    return surf

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
surf = plot_ith_frame(0)
fig.colorbar(surf,  pad=0.1)              

def animate(i):
    ax.clear()
    surf = plot_ith_frame(i)
    return surf

ani = FuncAnimation(fig, animate, 
      frames =  frames.shape[2])

plt.show()
