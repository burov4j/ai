count_of_employees = 0
total_salary = 0
print("Employees with low salary: ")
with open("text_3.txt", "r") as file_task3:
    while True:
        line = file_task3.readline().split()
        if not line:
            break
        count_of_employees += 1
        name = line[0]
        salary = float(line[1])
        total_salary += salary
        if salary < 20000:
            print(name)
print(f"Average salary: {total_salary / count_of_employees}")
