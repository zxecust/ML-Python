import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import scipy.io as sio
import os
from sklearn import svm

spam_train = sio.loadmat('data/spamTrain.mat')
spam_test = sio.loadmat('data/spamTest.mat')

# print(spam_train)
# print(spam_test)

X = spam_train['X']
Xtest = spam_test['Xtest']
y = spam_train['y']
ytest = spam_test['ytest'].ravel() # ravel()将数组维度拉成一维数组

# print(X.shape)
# print(Xtest.shape)
# print(y.shape)
# print(ytest.shape)

svc = svm.SVC()
svc.fit(X,y)

print('Training accuracy = {0}%'.format(np.round(svc.score(X,y)*100, 2))) # 2表示保留到小数点后2位

print('Test accuracy = {0}%'.format(np.round(svc.score(Xtest,ytest)*100, 2))) # 2表示保留到小数点后2位