import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data0 = pd.read_csv('datasetA.csv', 
                    sep=',', header=None)
data1 = pd.read_csv('datasetB.csv', 
                    sep=',', header=None)
X = pd.concat([data0, data1])

kmeans = KMeans(n_clusters=2, random_state=4, 
                n_init='auto').fit(X)
centr  = kmeans.cluster_centers_

fig, ax = plt.subplots(1,1)

ax.scatter(X.values[:,0], X.values[:,1], 
           c=kmeans.labels_, cmap='bwr_r', 
           s=10, alpha=0.5)
ax.scatter(centr[:,0], centr[:,1], c='k', 
           s=80, marker = 'x')
ax.set_title('k-means clustered data')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.grid('on')
plt.show()

print(f'After {kmeans.n_iter_} iterations, ' 
      'the centroids are at')
print(f'{centr[0,:]} and \n{centr[1,:]}')
