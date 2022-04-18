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

# 计算中心点
def compute_centroids(X, idx, k):
	m, n = X.shape
	centroids = np.zeros((k, n)) # 初始化一个k行n列的全零数组

	for i in range(k):
		indices = np.where(idx == i)
		centroids[i,:] = (np.sum(X[indices,:], axis = 1) / len(indices[0])).ravel()

	return centroids

# K-Means 迭代
def run_k_means(X, initial_centroids, max_iters):
	m, n = X.shape
	k = initial_centroids.shape[0]
	idx = np.zeros(m)
	centroids = initial_centroids

	for i in range(max_iters):
		idx = find_closest_centroids(X, centroids)
		centroids = compute_centroids(X, idx, k)

	return idx, centroids

# 创建随机聚类中心
def init_centroids(X, k):
	m, n = X.shape
	centroids = np.zeros((k, n))
	idx = np.random.randint(0, m, k) # 随机生成k个实数，最小值为0，最大值为m

	for i in range(k):
		centroids[i,:] = X[idx[i],:]

	return centroids


# 设置图像保存路径
figure_save_path = "images" 
if not os.path.exists(figure_save_path):
    os.makedirs(figure_save_path) # 如果不存在目录figure_save_path，则创建

data = sio.loadmat('data/ex7data2.mat')
X = data['X']
data2 = pd.DataFrame(data.get('X'), columns = ['X1', 'X2'])
# print(data2.head()) # 显示data2前5行

# 输出 data2 图像
sb.set(context = "notebook", style = "white")
sb.lmplot(x = 'X1', y = 'X2', data = data2, fit_reg = False)
plt.savefig(os.path.join(figure_save_path, 'data2.png'))
plt.show()

initial_centroids = init_centroids(X, 3) # 初始化3个中心点
idx = find_closest_centroids(X, initial_centroids) 

print(compute_centroids(X, idx, 3)) # 输出计算的中心点

# 对K-Means算法进行迭代并输出结果
idx, centroids = run_k_means(X, initial_centroids, 10)
print(idx)
print(centroids) # 输出迭代后计算的中心点

# 对数据进行聚类
cluster1 = X[np.where(idx == 0)[0],:]
cluster2 = X[np.where(idx == 1)[0],:]
cluster3 = X[np.where(idx == 2)[0],:]

# 输出 K-Means 图像
fig, ax = plt.subplots(figsize = (9,6))
ax.scatter(cluster1[:,0], cluster1[:,1], s = 30, color = 'r', label = 'cluster1') # 输出第1组数据点的图像，颜色为红色
ax.scatter(cluster2[:,0], cluster2[:,1], s = 30, color = 'g', label = 'cluster2') # 输出第2组数据点的图像，颜色为绿色
ax.scatter(cluster3[:,0], cluster3[:,1], s = 30, color = 'b', label = 'cluster3') # 输出第3组数据点的图像，颜色为蓝色
ax.legend()
plt.savefig(os.path.join(figure_save_path, 'K-means.png'))
plt.show()