import numpy as np

output = np.ones((5,5) , dtype = "int32")
output[1:4,1:4] = 0
output[2,2] = 9

print(output)