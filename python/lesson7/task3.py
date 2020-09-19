class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        result = self.count - other.count
        if result > 0:
            return Cell(result)
        else:
            raise ArithmeticError

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(int(self.count / other.count))

    def make_order(self, length):
        result = ""
        count = 0
        while count < self.count:
            result += "*"
            count += 1
            if count % length == 0:
                result += "\n"
        return result


cell1 = Cell(9)
cell2 = Cell(2)

print((cell1 + cell2).make_order(5))
print("---")
print((cell1 - cell2).make_order(2))
print("---")
print((cell1 * cell2).make_order(10))
print("---")
print((cell1 / cell2).make_order(3))
