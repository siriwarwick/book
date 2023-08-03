# Version of continuity.ipynb
# Using matplotlib's slider instead of IPywidget
# Credit: Ben Wadsworth (2023)

import numpy as np
from matplotlib.widgets import Slider

x = np.linspace(0, 2)

fig = plt.figure()
ax = plt.axes()

def f(x):
    return np.log(x+1)

def finverse(x):
    return np.exp(x)-1

ax.plot(x, f(x))
eps = 0.2

axt = plt.axes([0.2, 0.025, 0.5, 0.02])
eps_slide = Slider(axt, 'eps', 0.01, 0.4, valstep = 0.01, valinit = 0.2)

def update(val):
    eps = eps_slide.val
    ax.clear()
    ax.plot(x, f(x))
    y = f(x)
    x0 = 1
    y0 = f(x0)
    y0p = y0+eps
    y0m = y0-eps
    x0p = finverse(y0p)
    x0m = finverse(y0m)
    
    vertical = [x0, x0p, x0m]
    horizontal = [y0, y0p, y0m]
    
    ax.plot(x, y, 'r')   
    for Y in horizontal:
        ax.axhline(y = Y, color= 'k', linestyle = ':')    
    for X in vertical:
        ax.axvline(x = X, color= 'c', linestyle = ':')
        
    delta= min(abs(x0-x0p),abs(x0-x0m))
    
    ax.set_title(f'Given \u03B5 = {eps:.2}, found \u03B4 = {delta:.4}')
        
eps_slide.on_changed(update)

update(eps)       
plt.show()