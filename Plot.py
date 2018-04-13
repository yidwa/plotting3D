

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

print groups
print xs
print ys
print zs
for  group, x, y, z in zip( groups, xs, ys, zs):
   # label = '%s (%d, %d, %d)' % (group, x,y,z)
   label = group
   ax.scatter(xs, ys, zs)
   ax.text(x,y,z,label)

#
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Availability')
# ax.set_xlim3d(0,25)
# ax.set_ylim3d(0,25)
ax.set_zlim3d(0,13)

# ax.scatter(xs,ys,zs)


# for xs, ys, zs, color, group in zip(xs, ys, zs, colors, groups):
#     ax.scatter(xs,ys,zs, alpha=0.8, c = color, edgecolors='none', s=30, label = group)

plt.legend(loc=2)
X = np.column_stack((np.asarray(xs),np.asarray(ys)))
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
print(kmeans.labels_)

#plt.scatter(X[:,0],X[:,1],zs, c=kmeans.labels_, cmap='rainbow')

plt.show()