import numpy as np
import matplotlib.pyplot as plt

n=np.arange(1,41)

recp = 1/n
xn = 1-recp
err_xn = recp

yn = np.sin(n)/n
err_yn = abs(yn)

zn = np.log(n)/n
err_zn = abs(zn)

En = (1+recp)**n
err_En = abs(En-np.e)

plt.plot(n, err_xn, 'o-' , ms=3)
plt.plot(n, err_yn, 'o--', ms=3) 
plt.plot(n, err_zn, 'o-.', ms=3)
plt.plot(n, err_En, 'o:' , ms=3)

plt.xlim(0,40)
plt.ylim(0,0.4)
plt.xlabel(r'$n$')
plt.ylabel('|Error|')
plt.legend([r'$|x_n-1|$', r'$|y_n|$', 
            r'$|z_n|$', r'$|E_n-e|$'])
plt.grid('on')
plt.show()