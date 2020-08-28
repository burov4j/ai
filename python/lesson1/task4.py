inputNumber = input("Enter a number: ")

maxNumber = 0

for currentChar in inputNumber:
    currentInt = int(currentChar)
    if currentInt > maxNumber:
        maxNumber = currentInt

print(f"Result is {maxNumber}")
