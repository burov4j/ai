import itertools

for i in itertools.count(3):
    print(i)
    if i == 10:
        break

print("***")

summary = 0
for i in itertools.cycle([1, 2, 3]):
    print(i)
    summary += i
    if summary > 20:
        break
