import numpy as np

n = int(input())

arr = np.arange(n)

arr[arr % 2 == 1] = -1

print(arr)