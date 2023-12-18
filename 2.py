try:
    with open("flowers.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
except UnicodeDecodeError as e:
    print({e})




flower_names = []
flower_prices = []


for line in lines:
    parts = line.split()
    flower_names.append(parts[0])
    flower_prices.append(int(parts[1]))


expensive_flowers = [name for name, price in zip(flower_names, flower_prices) if price > 5]
print("дороже 5 рублей:", expensive_flowers)


average_price = sum(flower_prices) / len(flower_prices)
print("средняя стоимость :", average_price)


min_price = min(flower_prices)
cheap_flowers = [name for name, price in zip(flower_names, flower_prices) if price == min_price]
print("самые дешевые:", cheap_flowers)
