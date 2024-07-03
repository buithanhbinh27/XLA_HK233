import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

data = np.genfromtxt(url, delimiter=',', usecols=None)

filtered_data = data[(data[:, 2] > 1.5) & (data[:, 0] < 5.0)]

print(filtered_data)
