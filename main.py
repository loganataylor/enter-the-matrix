from vector import Vector
from matrix import Matrix

m1 = Matrix.random(3, 4)

# read in the matrix.txt
# filter the 4x2 and 2x4 matrices into
# different lists

# add any 2 compatible matrices
# multiply any 2 compatible matrices
# scale any matrix
# create a list of 5 3x3 matrices of random values
# and add them together

# multiply a matrix times a vector

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
m2 = Matrix(v1, v2)

print(m1, m2)
