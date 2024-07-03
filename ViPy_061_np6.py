import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

data = np.genfromtxt(url, delimiter=',', usecols=range(4))

print(data)
