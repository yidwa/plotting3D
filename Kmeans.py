import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
X = np.array([[5,3],
     [10,15],
     [15,12],
     [24,10],
     [30,45],
     [85,70],
     [71,80],
     [60,78],
     [55,52],
     [80,91],])
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
print(kmeans.labels_)
plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='rainbow')
plt.show()
print "hello"
