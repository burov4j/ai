class NotNumberError(Exception):
    pass


def check_and_add(p_list, p_num):
    try:
        p_list.append(int(p_num))
    except ValueError:
        raise NotNumberError


result_list = []
while True:
    num = input("Enter a number for list (q - quit): ")
    if num == "q":
        break
    try:
        check_and_add(result_list, num)
    except NotNumberError:
        print("This is not number! Try again...")


print(f"Result: {result_list}")