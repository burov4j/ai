with open("task5.txt", "w+") as file_task5:
    print("1 2 3 4 5 10 2000", file=file_task5)
    file_task5.seek(0)
    line = file_task5.readline().split()
    summary = 0
    for num in line:
        summary += int(num)
    print(f"Summary: {summary}")
