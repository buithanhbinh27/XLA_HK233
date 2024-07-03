import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

data = np.genfromtxt(url, delimiter=',', usecols=0)

min_val = data.min()
max_val = data.max()

normalization = (data - min_val) / (max_val - min_val)

print(normalization)