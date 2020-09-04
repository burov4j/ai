string = input("Enter a string: ").split()

index = 0
while index < len(string):
    print(f"{index}. {string[index][:10]}")
    index = index + 1
