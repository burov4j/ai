import sys

hours = int(sys.argv[1])
rate = int(sys.argv[2])
bonus = int(sys.argv[3])

print(f"Salary: {(hours * rate) + bonus}")
