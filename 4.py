import json
from chardet.universaldetector import UniversalDetector


def calculate_profit(revenue, costs):
    return revenue - costs



file_path = "firms.txt"


detector = UniversalDetector()
with open(file_path, 'rb') as file:
    for line in file:
        detector.feed(line)
        if detector.done:
            break
    detector.close()

file_encoding = detector.result['encoding']


result_list = []


profits_dict = {}


total_profit = 0
count_profitable_firms = 0

with open(file_path, "r", encoding=file_encoding) as file:
    for line in file:

        parts = line.strip().split()


        name, ownership, revenue, costs = parts


        revenue = int(revenue)
        costs = int(costs)


        profit = calculate_profit(revenue, costs)


        profits_dict[name] = profit


        if profit > 0:
            total_profit += profit
            count_profitable_firms += 1


result_list.append(profits_dict)


average_profit = total_profit / count_profitable_firms if count_profitable_firms > 0 else 0


result_list.append({"average": average_profit})


json_file_path = "result.json"


with open(json_file_path, "w") as json_file:
    json.dump(result_list, json_file, indent=2)

print(f"результат в: {json_file_path}")
