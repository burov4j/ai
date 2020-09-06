def my_func(a, b, c):
    numbers = [a, b, c]
    min_value = min(numbers)
    numbers.remove(min_value)
    return sum(numbers)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

print(f"Result: {my_func(num1, num2, num3)}")
