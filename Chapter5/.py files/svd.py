import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from PIL import Image
from scipy.linalg import svd

A = Image.open('flowers.jpeg').convert('L')
#import scipy.misc 
#A = scipy.misc.face(gray=True)

U, s, VT = svd(A)

def resize_image(N):
    return U[:,:N] @ np.diag(s[:N]) @ VT[:N,:]

fig,(ax1, ax2) = plt.subplots(1,2,
                 figsize=(10,4))
plt.subplots_adjust(bottom=0.2)
ax1.set_xlim(1,len(s))
ax1.title.set_text('Singular values') 
ax1.grid('on')
ax1.loglog(s,'ro-', markersize=3)

N = 10
image = resize_image(N)
ax2.imshow(image, cmap='gray')

axt = plt.axes([0.125, 0.1, 0.355, 0.05]) 
N_slide = Slider(axt, 'N',
          0, np.log10(len(s)), 
          valstep=0.05, valinit=1)
N_slide.valtext.set_text(N)

def update(val):
    N = round(10**N_slide.val)
    N_slide.valtext.set_text(N)
    image = resize_image(N)
    ax2.imshow(image, cmap='gray')
    fig.canvas.draw_idle()
    
N_slide.on_changed(update)

plt.show()
