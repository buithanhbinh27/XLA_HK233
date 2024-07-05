import numpy as np

a = np.array([2, 6, 1, 9, 10, 3, 27])

ans = a[(a >= 5) & (a <= 10)]

ans = ', '.join(map(str, ans))

print('[' + ans + ']')