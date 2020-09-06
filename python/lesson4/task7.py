def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


for el in fact(4):
    print(el)
