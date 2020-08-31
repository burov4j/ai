items = input("Please enter a list: ").split()

index = 1
while index < len(items):
    k = items[index]
    items[index] = items[index - 1]
    items[index - 1] = k
    index = index + 2

print(items)
