import numpy as np

#                        1D array

# arr = np.array([10, 20, 30, 40, 50])

# # Accesing elements in 1D Array
# print(arr[2])
# print(arr[-1])



#                         2D array :

# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# Accessing elements
#print(arr[0]) #-> [10,20,30]
# print(arr[0][2]) #-> 30
# print(arr[1][1]) #-> 50
# print(arr[2][0]) #-> 70

# To check the dimension of the array
# print(arr.ndim)



#                           3D array
arr = np.array([
                [
                  ['A','B','C'],
                  ['D','E','F']
                ],
                [
                  ['G','H','i'],
                  ['J','K','L']
                ],
                [
                  ['M','N','O'],
                  ['P','Q','R']
                ]
              ])

# Accessing elements in 3D array
# print(arr[2])
# print(arr[1][0][2])
# print(arr[0][1][1])

#Another way to access elements
# print(arr[2,1,2])

word = arr[2,0,0] + arr[0,0,0] + arr[2,0,1]
# print(word)
# Layer,rows,columns (3,2,3)
# print(arr.shape)


array = np.array([[10,20,30], [40,50,60]])

# Converts a multidimensional array into 1D.
# flatten() → always creates a copy
flat = array.flatten()
flat[0] = 100
print(array)

# ravel()   → returns a view when possible
ravel_arr =array.ravel()
ravel_arr[0] = 100
print(array)




