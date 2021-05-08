print("Введите n")
try:
    n = int(input())
except:
    print("Неверный ввод!!!")
    exit(0)

if n < 1 or n > pow(10, 9):
    print("Неверный ввод!!!")
    exit(0)

a = 1
for i in range(1, n + 1):
    a *= i
print(a)
