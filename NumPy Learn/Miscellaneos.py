import numpy as np

#Load data from file

data = np.genfromtxt('data.txt', delimiter=',') #load data from file
data = data.astype('int32')
# print(data)

#Boolean Masking & Advanced Indexing
# print(np.all(data>50, axis=0))#check if all elements in each column are greater than 50
# print(data>50)
