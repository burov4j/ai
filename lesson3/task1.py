def div(a, b):
    return a / b


num1 = float(input("Enter the first number: "))
while True:
    num2 = float(input("Enter the second number: "))
    if num2 == 0:
        print("Unable to divide by zero")
    else:
        print(f"{num1} / {num2} = {div(num1, num2)}")
        break
