import numpy as np
import matplotlib.pyplot as plt

creallist = []
cimaglist = []
zreallist = []
crealred = [] 
cimagred = []
zrealred = []
rng = np.random.default_rng()
kmax = 100

eps = 3e-3

for x in np.arange(-2, 0.4, eps):
    ymax = np.sqrt(4-x*x)
    for y in np.arange(0, ymax+eps, eps):
        c = x + y*1j
        z = 4*rng.random() - 2
        test = True
        for k in range(1,kmax+1):
            z = z**2 + c
            modsq = z*np.conj(z)
            test = (modsq<=4)
            if (not test):
                break          
        if (test):
            creallist.append(c.real)
            cimaglist.append(c.imag)
            zreallist.append(z.real)
            if (np.abs(c.imag)<1e-16):
                crealred.append(c.real)
                cimagred.append(c.imag)
                zrealred.append(z.real)

creal =  np.array(creallist)
cimag =  np.array(cimaglist)
zreal =  np.array(zreallist)
crealR =  np.array(crealred)
cimagR =  np.array(cimagred)
zrealR =  np.array(zrealred)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Re c')
ax.set_ylabel('Im c')
ax.set_zlabel('Re z')
ax.set_xlim(-2,0.5)
ax.set_ylim(0,1)
ax.set_zlim(-2,2)

ax.scatter(creal, cimag, zreal, 
           s=0.4, c=zreal, cmap="Blues")
ax.scatter(crealR, cimagR, zrealR, 
           s=1, color='r')
plt.show()
