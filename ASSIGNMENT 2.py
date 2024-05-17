#dot method
import numpy as np

# Example 1
A = np.array([[21, 32], [31, 42]])
B = np.array([[15, 36], [17, 38]])
result1 = np.dot(A, B)
print("Dot Product 1:\n", result1)

# Example 2
C = np.array([11, 22, 13])
D = np.array([24, 15, 36])
result2 = np.dot(C, D)
print("Dot Product 2:\n", result2)

# Example 3
E = np.array([[31, 12], [31, 14], [25, 16]])
F = np.array([[17, 28], [19, 11]])
result3 = np.dot(E, F)
print("Dot Product 3:\n", result3)



#transpose method
import numpy as np

# Example 1
G = np.array([[11, 21, 23], [41,25, 16]])
result4 = G.transpose()
print("Transpose 1:\n", result4)

# Example 2
H = np.array([[17, 12], [13, 24], [25, 16]])
result5 = np.transpose(H)
print("Transpose 2:\n", result5)

# Example 3
I = np.array([[[12, 22], [31, 14]], [[15, 26], [37, 16]]])
result6 = np.transpose(I, (1, 0, 2))
print("Transpose 3:\n", result6)



#linalg.inv method
import numpy as np

# Example 1
J = np.array([[11, 22], [31, 24]])
result7 = np.linalg.inv(J)
print("Inverse 1:\n", result7)

# Example 2
K = np.array([[24, 17], [12, 26]])
result8 = np.linalg.inv(K)
print("Inverse 2:\n", result8)

# Example 3
L = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
result9 = np.linalg.inv(L)
print("Inverse 3:\n", result9)



#linalg.inv method
import numpy as np

# Example 1
M = np.array([[11, 13], [13, 15]])
result10 = np.linalg.det(M)
print("Determinant 1:\n", result10)

# Example 2
N = np.array([[14, 17], [12, 16]])
result11 = np.linalg.det(N)
print("Determinant 2:\n", result11)

# Example 3
O = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
result12 = np.linalg.det(O)
print("Determinant 3:\n", result12)



#flatten method
import numpy as np

# Example 1
P = np.array([[2, 2], [2, 4]])
result13 = P.flatten()
print("Flatten 1:\n", result13)

# Example 2
Q = np.array([[4, 12, 23], [2, 15, 16], [27, 18, 9]])
result14 = Q.flatten()
print("Flatten 2:\n", result14)

# Example 3
R = np.array([[[11, 12], [14, 24]], [[15, 26], [17, 18]]])
result15 = R.flatten()
print("Flatten 3:\n", result15)

