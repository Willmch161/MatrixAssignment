import numpy as np

# Define two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix Addition
addition = A + B

# Matrix Subtraction
subtraction = A - B

# Matrix Multiplication
multiplication = np.dot(A, B)  # or A @ B

# Transpose of A
transpose_A = np.transpose(A)

# Determinant of A
det_A = np.linalg.det(A)

# Inverse of A (handling singular matrix error)
try:
    inverse_A = np.linalg.inv(A)
except np.linalg.LinAlgError:
    inverse_A = "Matrix is singular, inverse does not exist."

# Print Results
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("\nAddition:\n", addition)
print("\nSubtraction:\n", subtraction)
print("\nMultiplication:\n", multiplication)
print("\nTranspose of A:\n", transpose_A)
print("\nDeterminant of A:", det_A)
print("\nInverse of A:\n", inverse_A)
