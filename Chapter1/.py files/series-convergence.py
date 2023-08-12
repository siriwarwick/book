import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,11)

S=np.zeros(len(x))

def afunc(k):
    return 1/k**2

S[0] = afunc(1)

for i in range(1,len(x)):
    S[i] = S[i-1]+afunc(x[i])

plt.plot(x,S, 'o-')
plt.xlim(1,10)
plt.xlabel('Number of terms')
plt.ylabel('Partial sum')
plt.legend(['a'])
plt.grid('on')
plt.show()