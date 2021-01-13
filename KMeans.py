import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import style
style.use("ggplot")

from sklearn.cluster import KMeans

hardCode = 0
if hardCode == 1:
    X = np.array([[1, 2], [5,8], [1.5, 1.8], [8,8], [1, 0.6], [9, 11]])
else:
    df = pd.read_csv("C:/Users/vsuthar1/.NOBACKUP/Data/KMeansEx.csv")
    X = df[['feature 1', 'feature 2']]
    #X = np.ravel(X)

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)
df.insert(0, 'cluster', labels)

colors =["g.", "r.", "c.", "y."]
if hardCode == 1:
    for i in range(len(X)):
        print("Coordindate: ", X[i], "Label:", labels[i])
        plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)
        plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=150, zorder=10)
        plt.show()
else:
    cluster1 = df['cluster']==0
    cluster2 = df['cluster']==1
    print(cluster1, cluster2)
    cluster1.plot(kind='scatter', x='feature 1', y='feature 2', color='black')
    cluster1.plot(kind='scatter', x='feature 1', y='feature 2', color='red')



