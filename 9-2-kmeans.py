# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
X=[]
f=open('city.txt')
for v in f:
    #print(v)
    X.append([float(v.split(',')[2]),float(v.split(',')[3])])
    if (float(v.split(',')[3])>180):
        print float(v.split(',')[3])
    if (float(v.split(',')[2])>50):
        print float(v.split(',')[2])
print(X)
X=np.array(X)
print(X)
n_clusters=3
cls=KMeans(n_clusters).fit(X)
cls.labels_
markers=['^','x','o']
for i in range(n_clusters):
    members = cls.labels_ == i
    plt.scatter(X[members,0],X[members,1],s=60,
                marker=markers[i],c='b',alpha=0.5)
plt.title('')
plt.show()