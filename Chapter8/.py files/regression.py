import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial as P
import pandas as pd

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(8,4))

df1 = pd.read_csv('datasetA.csv', sep=',', 
                  header=None)
x1 = df1.values[:,0]
y1 = df1.values[:,1]
ax1.plot(x1,y1,'.r')

df2 = pd.read_csv('datasetB.csv', sep=',', 
                  header=None)
x2 = df2.values[:,0]
y2 = df2.values[:,1]
ax1.plot(x2,y2,'.b')

ax1.legend(['datasetA','datasetB'], 
           loc='lower right')

poly1 = P.fit(x1, y1, 1).convert()
xfit1 = np.linspace(min(x1),max(x1))
yfit1 = poly1(xfit1)
ax1.plot(xfit1, yfit1, 'k')

poly2 = P.fit(x2, y2, 1).convert()
xfit2 = np.linspace(min(x2),max(x2))
yfit2 = poly2(xfit2)
ax1.plot(xfit2, yfit2, 'k')

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid('on')

X = np.concatenate((x1,x2))
Y = np.concatenate((y1,y2))
ax2.plot(X,Y,'.', c='gray')
ax2.legend(['combined'], loc='lower right')

Poly = P.fit(X, Y, 1).convert()
Xfit = np.linspace(min(X),max(X))
Yfit = Poly(Xfit)
ax2.plot(Xfit, Yfit, 'k')

ax2.set_xlabel('x')
ax2.grid('on')

plt.show()
