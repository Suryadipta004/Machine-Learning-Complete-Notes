import numpy as np

A = np.array([1, 2, 3, 4, 5, 6])
# print("Original Array:\n", A)
B = A.reshape(2, 3)
# print("\nReshaped to 2x3 Matrix:\n", B)
C = A.reshape(3, 2)
# print("\nReshaped to 3x2 Matrix:\n", C)

flattened = B.flatten()
# print("\nFlattened Array:\n", flattened)

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

print("\nVertical Stack:\n", np.vstack([v1, v2]))
print("\nHorizontal Stack:\n", np.hstack([v1, v2]))
print("\nVertical Stack:\n", np.vstack([v1, v2, v1, v2]))
