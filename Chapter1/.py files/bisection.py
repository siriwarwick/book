import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x)-x

acc = 0.5e-5
a, b = 0, 1

fa, fb = f(a), f(b)                             

if fa*fb>=0:
    raise ValueError('Root is not bracketed.')

n=0                                 
while (b-a)/2 > acc:                    
    x = (a+b)/2                          
    fx = f(x)                          
    if fx == 0:
         break                        
    if fx*fa < 0:                       
        b = x                           
    else:
        a = x                                            
    print(f'Iteration number {n}, x={x}')
    n += 1                          

x=(a+b)/2                       
print(f'Final iteration number {n}, x= {x}')