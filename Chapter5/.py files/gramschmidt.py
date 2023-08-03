import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.Symbol('x')
v = sp.Matrix([[1,x, x**2,x**3, x**4, x**5]])
e = sp.zeros(1,len(v))

def Dot(f,g): 
    return sp.integrate(f*g, (x,-1,1))

def norm(f):
    return sp.sqrt(Dot(f,f))

e[0] = v[0]/norm(v[0])
print(f'e[0] = {e[0]}')

xarray = np.linspace(-1,1,100)
yarray = e[0]*np.ones_like(xarray)
plt.plot(xarray,yarray)

for i in range(1,len(v)):
    vperp = v[i]
    for j in range(1,i+1):
        vperp -= Dot(v[i], e[j-1])*e[j-1]
    e[i] = vperp/norm(vperp)
    print(f'e[{i}] = {e[i]}')
    f= sp.lambdify(x,e[i])
    yarray = f(xarray)
    plt.plot(xarray,yarray)

plt.xlim((-1,1))
plt.ylim((-2,2))
plt.legend([r'$e_0$',r'$e_1$',r'$e_2$',
            r'$e_3$',r'$e_4$',r'$e_5$'],\
          ncol=len(v),loc='lower right')
plt.title(r'Orthonormal basis of $P_5$')
plt.grid('on')
plt.show() 
