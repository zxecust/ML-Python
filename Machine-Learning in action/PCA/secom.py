import matplotlib.pyplot as plt
from numpy import *
import os
import pca

# 设置图像保存路径
figure_save_path = "images" 
if not os.path.exists(figure_save_path):
    os.makedirs(figure_save_path) # 如果不存在目录figure_save_path，则创建

dataMat = pca.replaceNanWithMean()
meanVals = mean(dataMat, axis = 0)
meanRemoved = dataMat - meanVals

covMat = cov(meanRemoved, rowvar = 0)
eigVals, eigVects = linalg.eig(mat(covMat))
print(eigVals)