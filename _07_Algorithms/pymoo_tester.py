import numpy as np

#2D array
a = (np.arange(8))
b = (np.arange(8))
# c = np.array([a,b])
c = c = np.concatenate((a, b), axis=1)

#print array
print("The array\n", c)