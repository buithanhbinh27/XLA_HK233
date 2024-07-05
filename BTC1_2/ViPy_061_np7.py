import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

data = np.genfromtxt(url, delimiter=',', usecols=0)

mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

print('Mean: ', mean)
print('Median: ', median)
print('Standard Deviation: ', std_dev)
