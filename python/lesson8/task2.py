class DivisionByZeroError(Exception):
    pass


def div(a, b):
    if b == 0:
        raise DivisionByZeroError
    else:
        return a / b


while True:
    num1 = input("Enter the first number (q - quit): ")
    if num1 == "q":
        break
    num2 = input("Enter the second number (q - quit): ")
    if num2 == "q":
        break
    try:
        print(f"Result of division: {div(int(num1), int(num2))}")
    except DivisionByZeroError:
        print("Division by zero! Try again...")
