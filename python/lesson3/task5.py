result_sum = 0
while True:
    numbers = input("Enter numbers (press 'q' to quit): ").split()
    should_quit = False
    for num in numbers:
        if num == 'q':
            should_quit = True
            break
        result_sum += float(num)
    print(f"Current sum: {result_sum}")
    if should_quit:
        break
