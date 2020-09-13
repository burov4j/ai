with open("task2.txt", "a+") as file_task2:
    print("The new line from python", file=file_task2)
    file_task2.seek(0)
    lines = file_task2.readlines()
    print(f"Lines count: {len(lines)}")
    words = 0
    for line in lines:
        words += len(line.split())
    print(f"Words count: {words}")
