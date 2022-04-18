import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import scipy.io as sio
import os

# PCA 
def pca(X):
	X = (X - X.mean()) / X.std() # 特征归一化
	
	# 计算协方差
	X = np.matrix(X)
	cov = (X.T * X) / X.shape[0]

	# 输出SVD，奇异值分解
	U, S, V = np.linalg.svd(cov)

	return U, S, V
 

# 投影计算
def project_data(X, U, k):
	U_reduced = U[:,:k]
	return np.dot(X, U_reduced)


# 还原数据
def recover_data(Z, U, k):
	U_reduced = U[:,:k]
	return np.dot(Z, U_reduced.T)



# 设置图像保存路径
figure_save_path = "images" 
if not os.path.exists(figure_save_path):
    os.makedirs(figure_save_path) # 如果不存在目录figure_save_path，则创建

data = sio.loadmat('data/ex7data1.mat') # 导入数据
# print(data)

X = data['X']

fig, ax = plt.subplots(figsize = (9, 6))
ax.scatter(X[:, 0], X[:, 1])
plt.savefig(os.path.join(figure_save_path, 'data.png'))
plt.show()

U, S, V = pca(X) # 压缩数据
print("U = ", U,"\n\nS = ", S,"\n\nV = ", V)

# 对数据进行投影
Z = project_data(X, U, 1)
print("\n\nZ = ", Z)

# 反转，恢复数据
X_recovered = recover_data(Z, U, 1)
print("\n\nX_recovered = ",X_recovered)

fig, ax = plt.subplots(figsize = (9, 6))
ax.scatter(list(X_recovered[:,0]), list(X_recovered[:,1]))
plt.savefig(os.path.join(figure_save_path, "reduced_data.png"))
plt.show()