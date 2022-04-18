import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.io import loadmat
from sklearn import svm
import os

# 设置图像保存路径
figure_save_path = "images" 
if not os.path.exists(figure_save_path):
    os.makedirs(figure_save_path) # 如果不存在目录figure_save_path，则创建

raw_data = loadmat('data/ex6data1.mat')
print(raw_data.keys()) # 输出每列数据的键值

data = pd.DataFrame(raw_data['X'], columns=['X1', 'X2']) # 创建Pandas的DataFrame结构数据
data['y'] = raw_data['y']
print(data.head()) # 输出DataFrame的前5行数据

# 决定每组数据在输出的图表中是 O 还是 X 。
positive = data[data['y'].isin([1])]
negative = data[data['y'].isin([0])]

# fig1
fig, ax = plt.subplots(figsize=(9,6)) # 设置图像大小
ax.scatter(positive['X1'], positive['X2'], s=50, marker='x', label='Positive')
ax.scatter(negative['X1'], negative['X2'], s=50, marker='o', label='Negative')
ax.set_title('Raw Data') # 设置图像标题
ax.set_xlabel('X1') # 设置x轴
ax.set_ylabel('X2') # 设置y轴
ax.legend() # 设置图例
plt.savefig(os.path.join(figure_save_path , 'data1.png')) # 第一个是指存储路径，第二个是图片名字
plt.show() # 显示图像

# SVM 1
svc = svm.LinearSVC(C=1, loss='hinge', max_iter=5000) 
svc.fit(data[['X1', 'X2']],data['y'])
svc.score(data[['X1', 'X2']],data['y'])

data['SVM 1 Confidence'] = svc.decision_function(data[['X1','X2']])

# fig2
fig, ax = plt.subplots(figsize=(9,6)) # 设置图像大小
ax.scatter(data['X1'], data['X2'], s=50, c=data['SVM 1 Confidence'],cmap='seismic')
ax.set_title('SVM(C=1) Decision Confidence') # 设置图像标题
ax.set_xlabel('X1') # 设置x轴
ax.set_ylabel('X2') # 设置y轴
plt.savefig(os.path.join(figure_save_path , 'SVM1.png')) # 第一个是指存储路径，第二个是图片名字
plt.show() # 显示图像

# SVM 100
svc = svm.LinearSVC(C=100, loss='hinge', max_iter=5000) 
svc.fit(data[['X1', 'X2']],data['y'])
svc.score(data[['X1', 'X2']],data['y'])

data['SVM 100 Confidence'] = svc.decision_function(data[['X1','X2']])

# fig3
fig, ax = plt.subplots(figsize=(9,6)) # 设置图像大小
ax.scatter(data['X1'], data['X2'], s=50, c=data['SVM 100 Confidence'],cmap='seismic')
ax.set_title('SVM(C=100) Decision Confidence') # 设置图像标题
ax.set_xlabel('X1') # 设置x轴
ax.set_ylabel('X2') # 设置y轴
plt.savefig(os.path.join(figure_save_path , 'SVM100.png')) # 第一个是指存储路径，第二个是图片名字
plt.show() # 显示图像