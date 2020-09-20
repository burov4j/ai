from tabulate import tabulate


class Matrix:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        return tabulate(self.values)

    def __add__(self, other):
        return Matrix([map(sum, zip(*t)) for t in zip(self.values, other.values)])


matrix1 = Matrix([[1, 2, 3], [40, 50, 60], [700, 800, 900]])
matrix2 = Matrix([[5, 6, 7], [50, 60, 70], [500, 600, 700]])
print(matrix1 + matrix2)
