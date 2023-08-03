import numpy as np
import matplotlib.pyplot as plt

n=6

theta = 2*np.pi/n
C, S = np.cos(theta), np.sin(theta)
rot = np.array([[C,-S,0],[S, C,0],[0,0,1]])
ref = np.array([[1, 0,0],[0,-1,0],[0,0,1]])
k = np.array([0,0,1])
V = np.array([1,0,1])
U = V

for i in range(n-1):
    U = rot@U + k
    V= np.vstack((V, U))
    
V = np.vstack((V,np.array([1,0,1]))).T
V = np.linalg.matrix_power(rot,3)@V

poly_x = V[0,:]
poly_y = V[1,:]
poly_z = V[2,:]

plt.plot(poly_x, poly_y, 'ko-')

for i, X in enumerate(poly_x):
    plt.text(x = 1.1*X, y = 1.1*poly_y[i], 
             s=int(poly_z[i]), fontsize=18,
             ha = 'center', va = 'center')

for i in range(n):
    Tx = np.array([0,poly_x[i],poly_x[i+1]])
    Ty = np.array([0,poly_y[i],poly_y[i+1]])
    plt.fill(Tx, Ty)
    
plt.axis('square')
plt.axis('off')
plt.show()
