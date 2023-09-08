import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, beta

Nsample, Nsuccess = 20, 9
Nsim = int(1e5)
Nbins = 20
post = []

a, b = 1, 1

pri = beta.rvs(a, b, size=Nsim)

for p in pri:
    like = binom.rvs(Nsample, p)
    if like == Nsuccess:
        post.append(p)

bins = np.linspace(0, 1, Nbins+1)

pri_b, _ = np.histogram(pri, bins= bins)
pri_prob = pri_b/sum(pri_b)
        
post_b, _ = np.histogram(post, bins= bins)
post_prob = post_b/sum(post_b)

fig,(ax1, ax2)=plt.subplots(1,2,figsize=(11,4))

width = 1/Nbins
X = np.arange(0, 1 ,width) + width/2

ax1.bar(X, pri_prob, width = width, 
        color='coral', edgecolor='k')
ax1.set_title(f'Prior Beta({a},{b})') 
ax1.set_xlabel(r'$\theta$')
ax1.set_ylabel(r'Pr($\theta$)')
ax1.set_xlim(0,1)

ax2.bar(X, post_prob, width = width, 
        color='royalblue', edgecolor='k')
ax2.set_title('Posterior') 
ax2.set_xlabel(r'$\theta$')
ax2.set_ylabel((r'Pr($\theta|$data)'))
ax2.set_xlim(0,1)

plt.show()

post_mean = sum(X*post_b)/sum(post_b)
print(f'Posterior mean = {post_mean:.3}')

post_mode = np.argmax(post_prob)
print(f'Mode at p = {X[post_mode]:.3}')

C = np.cumsum(post_b)/np.sum(post_b)
p05 = np.searchsorted(C, 0.05)
p95 = np.searchsorted(C, 0.95)
print('90% credible interval from '
      f'p = {X[p05]:.3} to {X[p95]:.3}')
