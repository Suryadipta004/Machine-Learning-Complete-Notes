import numpy as np

a = np.ones((3,3))
# print(a)
b = np.full((3,3), 2)
# print(b)

# print(np.matmul(a,b)) # or a@b
c = np.identity(3)
# print(c)
d = np.array([[1,2,3],[4,1,6],[7,8,9]])

# print(np.linalg.det(d))#Determinant of a matrix
# print(np.linalg.inv(d))#Inverse of a matrix
# print(np.transpose(d))#Transpose of a matrix
# print(np.trace(d))#Trace of a matrix
# print(np.linalg.matrix_rank(d))#Rank of a matrix
# print(np.linalg.matrix_power(d,3))#Matrix power of a matrix

# print(np.linalg.eig(d))#Eigen values and Eigen vectors of a matrix
# print(np.linalg.eigvals(d))#Eigen values of a matrix
# print(np.linalg.eigvalsh(d))#Eigen values of a matrix

# print(np.linalg.svd(d))#Singular value decomposition of a matrix
# print(np.linalg.qr(d))#QR decomposition of a matrix

# np.linalg.cholesky()#Cholesky decomposition of a matrix
# np.linalg.schur()#Schur decomposition of a matrix
# np.linalg.lu()#LU decomposition of a matrix
# np.linalg.hessenberg()#Hessenberg decomposition of a matrix


# print(np.linalg.solve(d, np.array([1,2,3])))#Solve a linear matrix equation, or system of linear scalar equations

# np.linalg.lstsq()#Return the least-squares solution to a linear matrix equation
# np.linalg.tensorinv()#Compute the 'inverse' of an N-dimensional array

