import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])

#Transpose
print (a.T)
print()

#Matrix Addition
print(np.add(a,b))
print()

#Matrix Subtraction
print(np.subtract(a,b))
print()

#Matrix Multiplication
print(np.multiply(a,b))
print()

#Matrix Division
print(np.divide(a,b))
print()

#Matrix Diagonal Values
print(np.diag(a))
print()

#Diagonal horizontal Flip
print(np.fliplr(a).diagonal())
print()

#Diagonal Vertical Flip
print(np.flipud(a).diagonal())
print()

#Matrix Determinant
print(np.linalg.det(a))
print()

#Matrix rank
print(np.linalg.matrix_rank(a))
print()

#Eigen values
print(np.linalg.eig(a))
print()

