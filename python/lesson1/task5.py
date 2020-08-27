revenue = float(input("Enter revenue: "))
costs = float(input("Enter costs: "))

if revenue > costs:
    profit = revenue - costs
    print(f"You have a profit. Profitability: {profit / revenue:.2f}")
    employeesCount = int(input("Enter count of employees: "))
    print(f"Profit per employee: {profit / employeesCount:.2f}")
elif revenue < costs:
    print("You have losses")


