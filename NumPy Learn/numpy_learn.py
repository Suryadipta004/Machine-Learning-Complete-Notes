import numpy as np

a = np.array([1, 2, 3] , dtype="int16")#1D array
b = np.array([[3.0,4.0,5.0],[6,7,8]])#2D array
c = np.array([[[1,2,3],[4,5,6]],
              [[7,8,9],[10,11,12]]])#3D array
# print(a)
# print(b)
# print(c)
print(c.ndim) #dimension
print(b.shape) #shape of the array matrix
print(f"Data type: {a.dtype}") #data type
print(f"{b.itemsize} Bytes") #size of each item in bytes
print(c.size) #total number of elements
print(c.nbytes) #total size of the array in bytes (c.itemsize * c.size)