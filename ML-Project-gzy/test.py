# test.py 
# 读取.mat文件

import scipy.io as sio

data = sio.loadmat('data/B0018.mat')

print(data)