class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_weight(self, a, b):
        return self._length * self._width * a * b / 1000


road = Road(20, 5000)
print(road.calculate_weight(25, 5))
