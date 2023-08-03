import numpy as np
import matplotlib.pyplot as plt

n = 88
label = True

t = np.linspace(0,2*np.pi)
plt.plot(np.cos(t), np.sin(t), 'b')

A=[a for a in range(1,n+1) if np.gcd(a,n)==1]
B=[pow(a,-1,n) for a in A]

for i, a in enumerate(A):
    tA, tB = 2*np.pi*a/n, 2*np.pi*B[i]/n
    xA, yA = np.cos(tA), np.sin(tA)
    xB, yB = np.cos(tB), np.sin(tB)
    plt.plot([xA, xB], [yA, yB], 'ro-')
    if (label):
        plt.text(x= 1.1*xA, y= 1.1*yA, s = a, 
        fontsize=9, ha='center', va='center')
    
plt.axis('square')
plt.axis('off')
plt.show()
