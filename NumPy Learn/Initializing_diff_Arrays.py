import numpy as np

a = np.zeros((2,3))#2D array of zeros
# print(a)

b = np.ones((2,3,4), dtype="int32")#3D array of ones of int32 data type
# print(b)

c = np.full((2,2,1,3), 99 , dtype='float32')#2D array of 99s of float32 data type
# print(c)

d = np.full_like(c, 4)#2D array of 4s of int32 data type
# print(d)
# print(d.dtype)

#Random decimal numbers
# print(np.random.rand(4,2))
# print(np.random.random_sample(b.shape))
# print(np.random.randint(7,size=(3,3),dtype='int32'))#Random integers
# print(np.random.rand(4,2))

#repeat an array n times
array = np.array([[1,2,3]])
r1 = np.repeat(array,3, axis=0) #repeat the array 3 times along the row
r2 = np.repeat(array,3, axis=1) #repeat the array 3 times along the column
# print(r1)
# print(r2)

#Be cateful while copying an array

e = np.array([1,2,3])
f = e
# print(f)
# f[0] = 100
# print(f)
# print(e) #e will also change because f is just a reference to e

#instead use copy() method
g = e.copy()
g[1] = 55
# print(g)
# print(e) #e will not change because g is a copy of e
