rating = []

while True:
    value = float(input("Enter a new value: "))

    # binary search
    left = -1
    right = len(rating)
    while left < right - 1:
        mid = (left + right) // 2
        if rating[mid] > value:
            left = mid
        else:
            right = mid

    rating.insert(right, value)
    print(rating)
