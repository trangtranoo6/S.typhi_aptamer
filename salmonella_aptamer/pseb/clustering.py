import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from pseb.pseb import getVectors
from pseb.visualize import generateImage
import csv

def optimal_clustering(X, trials = range(3,50)):
    wcss = []
    for i in trials:
        kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
    plt.plot(trials, wcss)
    plt.title('The Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()


def clustering(vectors, n_clusters):
    kmeans = KMeans(n_clusters = n_clusters, init = 'k-means++', max_iter = 1000, tol = 1e-10)
    return kmeans.fit_predict(vectors), kmeans.cluster_centers_

def dist(source):
    def _dist(dest):
        return np.linalg.norm(source - dest)
    return _dist

def kami(peptides, lamda, n_clusters):
    vectors = getVectors(peptides, lamda)
    vectors = StandardScaler().fit_transform(vectors) #comment for unscaled
    #optimal_clustering(vectors)
    clusters, centers = clustering(vectors, n_clusters = n_clusters)
    outputs = []
    best_center = []
    for i in range(n_clusters):
        idx = clusters == i
        [outputs.append([j,i]+[v for v in vec])
                for m,(j,vec) in enumerate(zip(peptides, vectors))
                if idx[m]]
        clu = vectors[clusters == i]
        distance = dist(centers[i])
        best = np.argmin(list(map(distance, vectors)))
        best_center.append(peptides[best])
    with open('./static/serve/clusters.csv','w') as f:
        writer = csv.writer(f)
        for i in outputs: 
            writer.writerow(i)
    with open('./static/serve/center.txt', 'w') as f:
        f.writelines('\n'.join([f'Cluster {i} : {j}' for i,j in enumerate(best_center)]))
    generateImage()
