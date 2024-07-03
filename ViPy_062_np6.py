import numpy as np

np.random.seed(101) 
arr = np.random.randint(1,4, size=6)

arr = arr - 1

identity = np.eye(3)

one_hot = identity[arr]

print(one_hot)
