#create a 4x5 matrix of even numbers:10,12,14,.. and 
# access rows and columns,extract 3rd column and set fourth row to 1,2,3,4,5
import numpy as np

matrix = np.arange(10, 50, 2).reshape(4, 5)
print("Original Matrix:")
print(matrix)

print("\n3rd Column:")
print(matrix[:, 2])

print("\nAfter setting 4th row to 1,2,3,4,5:")
matrix[3] = [1, 2, 3, 4, 5]
print(matrix)
