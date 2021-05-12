print("Введите время 1 и время 2")
time1 = input()
time2 = input()
try:
    h1, m1 = map(int, time1.split(":"))
    h2, m2 = map(int, time2.split(":"))
except:
    print("Неправильный ввод!!!")
    exit(0)

if h1 > 23 or h1 < 0 or m1 > 59 or m1 < 0 or h2 > 23 or h2 < 0 or m2 > 59 or m2 < 0:
    print("Введено неверное время!!!")
    exit(0)

if abs((h1 * 60 + m1) - (h2 * 60 + m2)) <= 15:
    print("Встреча состоится!!!")
else:
    print("Встреча не состоится!!!")
