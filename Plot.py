

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import re
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
ax = fig.gca(projection="3d")
ax.view_init(azim=30)
xs = []
ys = []
zs = []

groups = []


def ini_Cor():
    with open("coordinates","r") as ins:
        for line in ins:
            # print line
           fline = line.split()

           groups.append(fline[0])
           xs.append(float(fline[1]))
           ys.append(float(fline[2]))
           if(len(fline)>3):
              zs.append(float(fline[3]))
           else:
              zs.append(0)

ini_Cor()
#colors= ("red", "green", "blue")

# print groups
# print xs
# print ys
# print zs
# for  group, x, y, z in zip( groups, xs, ys, zs):
#    # label = '%s (%d, %d, %d)' % (group, x,y,z)
#    label = group
#    ax.scatter(xs, ys, zs)
#    ax.text(x,y,z,label)

# #
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Availability')
ax.set_xlim3d(-130, 110)
ax.set_ylim3d(-130,110)
ax.set_zlim3d(0,18)
#
# ax.scatter(xs,ys,zs)


# for xs, ys, zs, color, group in zip(xs, ys, zs, colors, groups):
#     ax.scatter(xs,ys,zs, alpha=0.8, c = color, edgecolors='none', s=30, label = group)

plt.legend(loc=2)
X = np.array(list(zip(xs,ys,zs)))
# y = zip(groups,xs,ys,zs)

print X
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
# predict the clusters
labels = kmeans.predict(X)
# getting the cluster centers
C = kmeans.cluster_centers_

print(kmeans.labels_)
#
colors = ['r', 'g', 'b']
clusters = np.zeros(len(X))
k =3
for i in range(20):
    color = colors[kmeans.labels_[i]]
    # print 'color'+color
    ax.scatter(X[i, 0], X[i, 1], X[i, 2], s=20, c=color)
    # ax.text(y[i][1], y[i][2], y[i][3], y[i][0])

# ax.scatter(X[:, 0], X[:, 1], X[:, 2])
# ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker ='*',  c='#050505', s=50)
# plt.scatter(X[:,0],X[:,1],X[:,2], c=kmeans.labels_, cmap='rainbow')
#
plt.show()