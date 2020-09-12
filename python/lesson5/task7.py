import json

profits = {}
total_profit = 0
profitable_firms_count = 0
with open("text_7.txt", "r") as file_task7:
    while True:
        line = file_task7.readline().split()
        if not line:
            break
        name = line[0]
        revenue = float(line[2])
        costs = float(line[3])
        profit = revenue - costs
        profits[name] = profit
        if profit > 0:
            profitable_firms_count += 1
            total_profit += profit
result = [profits, {"average_profit": total_profit / profitable_firms_count}]
with open("text_7_output.json", "w") as file_task8:
    json.dump(result, file_task8, ensure_ascii=False)

