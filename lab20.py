
def isEnough(budget, prices: list):
    if all(price > budget for price in prices):
        return False
    else:
        return True


def find_best(budget, prices, volumes):
    result = {"max_index": 0, "max_volume": 0, "count": 0, "remainder": 0}
    for i in range(len(prices)):
        if prices[i] <= budget:
            count = budget // prices[i]
            volume = count * volumes[i]
            if volume > result["max_volume"]:
                result["count"] = count
                result["max_volume"] = volume
                result["max_index"] = i
                result["remainder"] = budget - prices[i] * count
    return result


print("Введите количество денег")
budget = int(input())
print('Введите количество напитков')
drinks_amount = int(input())
print('Введите название, цену и объем каждого напитка')

names = [0] * drinks_amount
prices = [0] * drinks_amount
volumes = [0] * drinks_amount

for i in range(drinks_amount):
    names[i], prices[i], volumes[i] = input().split()
    prices[i] = int(prices[i])
    volumes[i] = int(volumes[i])
print()

if not isEnough(budget, prices):
    print(-1)
    exit(0)

remains = budget

while isEnough(remains, prices):
    best = find_best(remains, prices, volumes)
    remains = best["remainder"]
    i = best["max_index"]
    print(f"{names[i]} {best['count']}")
    print(f"Объём {best['max_volume']}")
    print(f"Остаток {best['remainder']}")
    print()