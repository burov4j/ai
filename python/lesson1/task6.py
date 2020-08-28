import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))

# bn = b1 * q^(n-1) - geometric progression, where bn = b, b1 = a, q = 1.1
# calculates n from here:
day = math.ceil(math.log(b / a, 1.1) + 1)

print(f"The result day is {day}")
