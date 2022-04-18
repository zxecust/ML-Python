import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import scipy.io as sio
import os

# 找到最近中心点
def find_closest_centroids(X, centroids):
	m = X.shape[0] # 确定数据X的维数
	k = centroids.shape[0] # 确定中心点的维数
	idx = np.zeros(m) # 初始化一个维数为m的全0数组

	for i in range(m):
		min_dist = 1000000 # 初始化最小距离
		for j in range(k):
			dist = np.sum((X[i,:] - centroids[j,:]) ** 2) # X[i,:]是取第1维中下标为j的元素的所有值,下同
			if dist < min_dist:
				min_dist = dist
				idx[i] = j

	return idx

data = sio.loadmat('data/ex7data2.mat')
X = data['X']
initial_centroids = np.array([[3,3],[6,2],[8,5]])

idx = find_closest_centroids(X, initial_centroids)
print(idx[0:3])