with open("task1.txt", "w") as file_task1:
    while True:
        user_input = input("Enter a line: ")
        if not user_input:
            break
        print(user_input, file=file_task1)
