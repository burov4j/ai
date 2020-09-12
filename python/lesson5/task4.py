translations = {
    1: "Один",
    2: "Два",
    3: "Три",
    4: "Четыре"
}
with open("text_4.txt", "r") as file_task4:
    with open("text_4_output.txt", "w") as file_task4_output:
        while True:
            line = file_task4.readline().split()
            if not line:
                break
            index = int(line[2])
            print(f"{translations[index]} - {index}", file=file_task4_output)
