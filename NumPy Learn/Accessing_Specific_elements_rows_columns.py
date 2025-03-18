import numpy as np
b = np.array([[4,5,6,10,11,12],[7,8,9,13,14,15]])

# print(b)
# print(b[1,5]) #Accessing specific element
# print(b[0,:])#Accessing specific row
# print(b[:,1])#Accessing specific column
# print(b[0, 1:5:2])#Accessing specific elements in a row from 1 to before 5 with step 2


a = np.array([[[1,2],[4,5]],
              [[8,9],[10,12]]])#3D array
print(a)

print(a[0,1,1])
print(a[:,1,:])#Accessing specific row
print(a[0,1,:])#Accessing specific column

