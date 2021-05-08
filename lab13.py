print("Введите n")
try:
    n = int(input())
except:
    print("Неверный ввод!!!")
    exit(0)

if n < 2 or n > pow(10, 9):
    print("Неверный ввод!!!")
    exit(0)

for i in range(2, n):
    if n % i == 0:
        print("Составное")
        exit(0)

print("Простое")
