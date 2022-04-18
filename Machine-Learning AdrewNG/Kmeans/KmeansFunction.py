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