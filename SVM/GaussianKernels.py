import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import scipy.io as sio
import os
from sklearn import svm

# 设置图像保存路径
figure_save_path = "images" 
if not os.path.exists(figure_save_path):
    os.makedirs(figure_save_path) # 如果不存在目录figure_save_path，则创建

# Kernel function
def gaussion_kernel(x1, x2, sigma):
	return np.exp(- np.power(x1 - x2, 2).sum()/(2 * (sigma ** 2)))

raw_data = sio.loadmat('data/ex6data2.mat')

data = pd.DataFrame(raw_data['X'], columns=['X1','X2'])
data['y'] = raw_data['y']

positive = data[data['y'].isin([1])]
negative = data[data['y'].isin([0])]

fig, ax = plt.subplots(figsize=(9,6))
ax.scatter(positive['X1'], positive['X2'], s=30, marker='x', label='Positive')
ax.scatter(negative['X1'], negative['X2'], s=30, marker='o', label='Negative')

ax.set_title('Raw Data')
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.legend()
plt.savefig(os.path.join(figure_save_path, 'data2.png'))
plt.show()

svc = svm.SVC(C=100,gamma=10, probability=True)

svc.fit(data[['X1','X2']],data['y'])
svc.score(data[['X1','X2']],data['y'])

data['Probability'] = svc.predict_proba(data[['X1','X2']])[:,0] # 将全部的negative数据显示，如果修改成1，则显示positive数据

fig, ax = plt.subplots(figsize = (9,6))
ax.scatter(data['X1'], data['X2'], s=30, c=data['Probability'], cmap='Reds')
plt.savefig(os.path.join(figure_save_path, 'probability.png'))
plt.show()