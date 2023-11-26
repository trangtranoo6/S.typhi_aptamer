import numpy as  np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import csv

cluster_file = './static/serve/clusters.csv'

def readClusters(cluster_file):
    with open(cluster_file, 'r') as f:
        ds = csv.reader(f)
        vectors, labels = [], []
        for line in ds:
            labels.append(int(line[1]))
            vectors.append(line[3:])
    vectors = np.array(vectors)
    labels = np.array(labels)
    return vectors, labels

def tsne(vectors):
    return TSNE(n_components = 2, perplexity = 40).fit_transform(vectors)

def visualize(tsne, labels):
    for i in range(np.amax(labels)):
        data = tsne[labels == i]
        plt.scatter(data[:,0], data[:,1])
    plt.savefig('./static/serve/plot.png', bbox='tight')

def generateImage():
    vectors, labels = readClusters(cluster_file)
    tsn = tsne(vectors)
    visualize(tsn, labels)
