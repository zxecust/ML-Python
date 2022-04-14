import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import scipy.io as sio
import os
from sklearn import svm

# Kernel function
def gaussion_kernel(x1, x2, sigma):
	return np.exp(- np.power(x1 - x2, 2).sum()/(2 * (sigma ** 2)))

x1 = np.array([1.0, 2.0, 1.0])
x2 = np.array([0.0, 4.0, -1.0])
sigma = 2

print(gaussion_kernel(x1, x2, sigma))