import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

data = np.genfromtxt(url, delimiter=',')

num_rows, num_cols = data.shape
random_rows = np.random.randint(0, num_rows, size=10)
random_cols = np.random.randint(0, num_cols, size=10)

data[random_rows, random_cols] = np.nan

data = np.nan_to_num(data)

print(data)
