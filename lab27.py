

def print_list(list):
    for element in list:
        print(element, end=" ")
    print()


print("Введите n и все сигналы с новой строки через пробел")
n = int(input())
signals = list(map(int, input().split()))
current = []
for i in range(n):
    current.append(signals[i])
    current.sort(reverse=True)
    if i <= 4:
        print_list(current)
    else:
        print_list(current[len(current) - 5: len(current)])


