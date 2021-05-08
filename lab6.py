import math

try:
    a = int(input("Введите a "))
    b = int(input("Введите b "))
    c = int(input("Введите c "))
except:
    print("Некорректный ввод!!!")
    quit()

if a == 0:
    print("x = -1")
    quit()

D = (b ** 2) - 4 * a * c

if D < 0:
    print("Корней нет")

if D == 0:
    x = -b / (2 * a)
    print("x1 = x2 = ", x)

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("x1 = ", x1)
    print("x2 = ", x2)

