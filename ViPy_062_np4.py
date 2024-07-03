import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

data = np.genfromtxt(url, delimiter=',')

colum3_data = data[:, 2]

ans = ['small' if x < 3 else 'medium' if 3 <= x < 5 else 'large' for x in colum3_data]

print(ans[:4])
