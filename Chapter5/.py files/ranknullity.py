import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as LA
from scipy.spatial.transform import Rotation

A= np.array([[1,-1,-1],[1,1,1],[0,0,1]])

Theta= np.linspace(0,2*np.pi,25)
Phi = np.linspace(0,np.pi,25)
theta, phi = np.meshgrid(Theta, Phi)

X = np.cos(theta)*np.sin(phi)
Y = np.sin(theta)*np.sin(phi)
Z = np.cos(phi)

fig = plt.figure()

### First plot: Domain
ax = fig.add_subplot(131, projection='3d') 

def plot_axes(name):
    ax.set_box_aspect((1,1,1))
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(name)
    ax.plot(0,0,0,'k.')

def plot_3D(X,Y,Z):
    ax.plot_surface(X,Y, Z, alpha=0.2,
         edgecolor='k',cmap='rainbow')
    
plot_axes('Domain')
plot_3D(X,Y,Z)

### Second plot: Image
ax = fig.add_subplot(132, projection='3d') 

def transform(M,x,y,z):
    xyz = np.vstack((np.ravel(x), np.ravel(y), 
                     np.ravel(z)))
    Mxyz = M@xyz
    MX = Mxyz[0,:].reshape(x.shape)
    MY = Mxyz[1,:].reshape(y.shape)
    MZ = Mxyz[2,:].reshape(z.shape)
    return MX, MY, MZ

AX, AY, AZ = transform(A, X,Y,Z)
plot_axes('Image')
plot_3D(AX,AY,AZ)

### Third plot: Kernel
ax = fig.add_subplot(133, projection='3d') 

NS = LA.null_space(A)
nullity = NS.shape[1]

def kernel2D():
    r=np.linspace(0,1,20)
    theta= np.linspace(0,2*np.pi,20)
    R, Theta = np.meshgrid(r,theta)

    xx= R*np.cos(Theta)
    yy= R*np.sin(Theta)
    zz= 0*xx

    normal = A[0,:]
    if normal[0]==0 and normal[1]==0 and\
       normal[2]!=0:
        RX = xx
        RY = yy
        RZ = zz
    else:
        N = normal/LA.norm(normal)
        V = np.cross([0,0,1], N)
        axis = V/LA.norm(V)
        th = np.arccos(N[2])
        cos2, sin2 = np.cos(th/2), np.sin(th/2)
        Isin2 = sin2*axis
        Quat = np.append(Isin2, cos2)
        rot = Rotation.from_quat(Quat)
        RX, RY, RZ = transform(rot.as_matrix(), 
                               xx,yy,zz)
     
    ax.plot([-NS[0,0], NS[0,0]],     
    [-NS[1,0],NS[1,0]],[-NS[2,0],NS[2,0]],'g-')
    ax.plot([-NS[0,1], NS[0,1]],     
    [-NS[1,1],NS[1,1]],[-NS[2,1],NS[2,1]],'g-')
    plot_3D(RX,RY,RZ)
    
if nullity == 1:
    ax.plot([-NS[0,0], NS[0,0]],     
    [-NS[1,0],NS[1,0]],[-NS[2,0],NS[2,0]],'g-')
if nullity == 2:
    kernel2D()    
if nullity == 3:
    plot_3D(X,Y,Z)

plot_axes('Kernel')

plt.tight_layout()
plt.show()
