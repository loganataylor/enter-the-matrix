# create a matrix
# any dimension


import random


class Matrix:
    def __init__(self, *vectors):
        self.vectors = vectors

    # create a random mxn matrix
    # with values between 0 and 1
    @staticmethod
    def random(m, n):
        return Matrix(tuple(tuple(random.uniform(0, 1) for i in range(n)) for j in range(m)))

    def __str__(self):
        return "{}".format(self.vectors)

    # add 2 matrices
    def __add__(self, other):
        return Matrix(*[c1 + c2 for c1, c2 in zip(self.vectors, other.vectors)])

    # scale matrix
    def mscale(self, scalar):
        return Matrix(*[n.scale(scalar) for n in self.vectors])

    # multiply 2 matrices
    def matmult(self, other):
        