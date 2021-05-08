print("Введите n")
try:
    n = int(input())
except:
    print("Неверный ввод!!!")
    exit(0)

if n < 0 or n > pow(10, 15):
    print("Неверный ввод!!!")
    exit(0)

acc = 1
k = 0
while(acc <= n):
    acc *= 2
    k += 1
print(k)

