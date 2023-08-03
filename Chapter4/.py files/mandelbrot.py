import numpy as np
import matplotlib.pyplot as plt

eps = 3e-3
xmin, xmax = -2, 0.5
ymax = 1.2
X = np.arange(xmin, xmax,eps)
Y = np.arange(0, ymax, eps)
kmax = 100
nx, ny = len(X), len(Y)

kmatrix = np.zeros((ny, nx)) 

modsq= lambda z: z*np.conj(z)

for row in np.arange(ny):
    for col in np.arange(nx):
        c = X[col] + Y[row]*1j
        k = 0
        z = 0
        while (modsq(z)<=4)and(k<=kmax):
            z = z**2 + c
            k=k+1
        kmatrix[row,col]=k-1

kflip = np.flipud(kmatrix)

K = np.concatenate((kflip, kmatrix[1:]))

fig, ax= plt.subplots()
ax.imshow(K, cmap="magma_r", 
          origin='lower',
          extent=[xmin,xmax,-ymax,ymax])
ax.set_xlabel("Re c")
ax.set_ylabel("Im c")
plt.show()
