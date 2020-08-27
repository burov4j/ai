totalSeconds = int(input("Enter count of seconds: "))

seconds = totalSeconds % 60
minutes = totalSeconds // 60 % 60
hours = totalSeconds // 3600

print(f"Formatted time: {hours:02d}:{minutes:02d}:{seconds:02d}")
