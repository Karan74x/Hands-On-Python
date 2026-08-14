import numpy as np

# 1D array
# arr = np.array([10, 20, 30, 40, 50])

# # Accesing elements in 1D Array
# print(arr[2])
# print(arr[-1])



# 2D array :
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Accessing elements
print(arr[0]) #-> [10,20,30]
print(arr[0][2]) #-> 30
print(arr[1][1]) #-> 50
print(arr[2][0]) #-> 70

# To check the dimension of the array
print(arr.ndim)

