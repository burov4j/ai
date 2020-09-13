import re

result = {}
with open("text_6.txt", "r") as file_task6:
    while True:
        line = file_task6.readline()
        if not line:
            break
        name = re.search("^(.*):", line).group(1)
        lessons = re.findall("\\d+", line)
        summary = 0
        for lesson in lessons:
            summary += int(lesson)
        result[name] = summary
print(result)
