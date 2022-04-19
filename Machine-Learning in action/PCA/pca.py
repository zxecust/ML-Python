from numpy import *

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

    # 对前N个特征值从小到大进行排序
	eigValInd = argsort(eigVals)
	eigValInd = eigValInd[:-(topNfeat+1):-1] # 对eigValInd数据进行切片，剔除不想要的数据
	redEigVects = eigVects[:,eigValInd]
	lowDDataMat = meanRemoved * redEigVects
	reconMat = (lowDDataMat * redEigVects.T) +meanVals
	return lowDDataMat, reconMat