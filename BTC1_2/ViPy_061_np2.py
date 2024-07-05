import numpy as np

# Tạo array từ 0 đến 9 và reshape thành (2, 5)
array1 = np.arange(10).reshape(2, 5)

# Tạo array gồm 2 hàng, mỗi hàng gồm 5 phần tử có giá trị là 1
array2 = np.ones((2, 5), dtype=int)

# Gộp hai array lại với nhau
result = np.vstack((array1, array2))

print(result)
