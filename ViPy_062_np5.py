import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

data = np.genfromtxt(url, delimiter=',')

colum3_data = data[:, 2]

unique_values, counts = np.unique(colum3_data, return_counts=True)

index_of_max_count = np.argmax(counts)
most_common_value = unique_values[index_of_max_count]
max_count = counts[index_of_max_count]

print(f"{max_count}, {most_common_value:.2f}")
