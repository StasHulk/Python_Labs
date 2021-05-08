print("Введите основание и степень")
try:
    base = int(input())
    exp = int(input())
except:
    print("Неверный ввод!!!")
    exit(0)

if exp == 0:
    print(1)
    exit(0)

acc = base
for i in range(abs(exp) - 1):
    acc *= base

if exp < 0:
    print(1 / acc)
    exit(0)
else:
    print(acc)
