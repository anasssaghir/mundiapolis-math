#!/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

lib = np.load("pca.npz")
data = lib["data"]
labels = lib["labels"]

data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)

colors = {
    0: '#3800a5',
    1: 'magenta',
    2: '#e8f301'
}

fig = plt.figure()
px = fig.add_subplot(111, projection='3d')

for i, (u1, u2, u3) in enumerate(pca_data):
    px.scatter(u1, u2, u3, c=colors.get(labels[i]), alpha=0.5)

px.set_xlabel('U1')
px.set_ylabel('U2')
px.set_zlabel('U3')
px.set_title('PCA of Iris Dataset')

plt.show()