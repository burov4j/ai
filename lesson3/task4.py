def my_func(x, y):
    result = 1
    for _ in range(abs(y)):
        result *= x
    return 1 / result


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"Result: {my_func(num1, num2)}")
