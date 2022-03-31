import numpy as np

A = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
B = np.array([16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1])

print("Before transforming:")
print("A:",A)
print("B:",B)

A = A.reshape(4,4)
B = B.reshape(4,4)
print("\nAfter transforming:")
print("A: \n",A)
print("B: \n",B)

print("\nMultiplication:\n", np.multiply(A,B))

print("\nTranspose of A:\n", np.transpose(A))

print("\nAT X B\n", np.multiply(np.transpose(A),B))

print("\nLast 2 elements of 3rd and 4th row:")
print(B[2:,(2,3)])

