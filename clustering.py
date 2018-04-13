

import numpy as np
from sklearn.cluster import KMeans

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

# print groups
# print xs
# print ys
# print zs

X = np.column_stack((np.asarray(xs),np.asarray(ys)))
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
# print(groups)
labels = kmeans.labels_



def write_Result():
    result = ""
    for i in range(len(groups)):
        result+= str(groups[i])+","+str(labels[i])+"\n"
        i += 1


    file = open("result","w")
    file.writelines(result)
    file.close

write_Result()