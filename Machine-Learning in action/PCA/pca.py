from numpy import *
import matplotlib.pyplot as plt
import os

def loadDataSet(fileName, delim='\t'):
	fr = open(fileName)
	stringArr = [line.strip().split(delim) for line in fr.readlines()]
	datArr = [list(map(float,line)) for line in stringArr]
	return mat(datArr)

def pca(dataMat, topNfeat=9999999):
	# 归一化
	meanVals = mean(dataMat, axis=0)
	meanRemoved = dataMat - meanVals
	
	# 求协方差
	covMat = cov(meanRemoved, rowvar = 0)

	# 计算协方差特征值和特征向量
	eigVals, eigVects = linalg.eig(mat(covMat))

    # 对前N个特征值进行排序
	eigValInd = argsort(eigVals)
	eigValInd = eigValInd[:-(topNfeat+1):-1]
	redEigVects = eigVects[:,eigValInd]
	lowDDataMat = meanRemoved * redEigVects
	reconMat = (lowDDataMat * redEigVects.T) +meanVals
	return lowDDataMat, reconMat

# 设置图像保存路径
figure_save_path = "images" 
if not os.path.exists(figure_save_path):
    os.makedirs(figure_save_path) # 如果不存在目录figure_save_path，则创建

dataMat = loadDataSet('C:/Users/zixuan/OneDrive/文档/GitHub/ML-Python/Machine-Learning in action/PCA/data/testSet.txt')
lowDMat, reconMat = pca(dataMat, 1)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dataMat[:,0].flatten().A[0], dataMat[:,1].flatten().A[0], marker = '^', s = 90)
ax.scatter(reconMat[:,0].flatten().A[0], reconMat[:,1].flatten().A[0], marker = 'o', s=50, c='red')
plt.savefig(os.path.join(figure_save_path, "C:/Users/zixuan/OneDrive/文档\GitHub/ML-Python\Machine-Learning in action/PCA/images/pca.png"))
plt.show()