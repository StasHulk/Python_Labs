x0 = int(input("Введите x0 "))
v0 = int(input("Введите v0 "))
t = int(input("Введите t "))
g = 9.8
x = x0 + v0 * t - (g * t ** 2) / 2
print("x = ", x)
