from functools import reduce

input_list = [num for num in range(100, 1001) if num % 2 == 0]
print(reduce(lambda a, b: a * b, input_list))
