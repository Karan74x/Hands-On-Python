import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# size → total elements
# len  → first dimension


print("ndim:", arr.ndim)
print("shape:", arr.shape)
# size tells you the total number of elements in the array.
print(arr.size)

# len() tells you the size of the first dimension.
print(len(arr))


# dtype tells you the data type of the elements.
print(arr.dtype)
