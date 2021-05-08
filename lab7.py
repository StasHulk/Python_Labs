import math


def exist(a, b, c):
    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        return False
    else:
        return True


def by_length(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s


def by_coords(ax, ay, bx, by, cx, cy):
    a = math.sqrt(math.pow(bx - ax, 2) + math.pow(by - ay, 2))
    b = math.sqrt(math.pow(cx - bx, 2) + math.pow(cy - by, 2))
    c = math.sqrt(math.pow(ax - cx, 2) + math.pow(ay - cy, 2))
    if not exist(a, b, c):
        print("Треугольник не существует!")
        quit()
    s = abs((bx - ax) * (cy - ay) - (cx - ax) * (by - ay)) / 2
    return s


print("Ввведите способ расчета")
print("1 - через длины сторон, 2 - через координаты вершин")
method = int(input())

if (method < 1) or (method > 2) :
    print("Неправильный способ расчёта!!!")
    exit(0)

if method == 1:
    try:
        a = int(input("Введите длину a "))
        b = int(input("Введите длину b "))
        c = int(input("Введите длину c "))
    except:
        print("Некорректный ввод !!!")
        exit(0)
    if not exist(a, b, c) or (a <= 0) or (b <= 0) or (c <= 0):
        print("Треугольник не существует!")
        exit(0)
    print("S = ", by_length(a, b, c))

else:
    try:
        text = input("Введите ax ay ")
        ax = int(text.split(" ")[0])
        ay = int(text.split(" ")[1])
        text = input("Введите bx by ")
        bx = int(text.split(" ")[0])
        by = int(text.split(" ")[1])
        text = input("Введите cx cy ")
        cx = int(text.split(" ")[0])
        cy = int(text.split(" ")[1])
    except:
        print("Некорректный ввод !!!")
        quit()
    if (ax == bx and ay == by) or (bx == cx and by == cy) or (cx == ax and cy == ay):
        print("Координаты точек совпадают!!!")
        exit(0)
    print("S = ", by_coords(ax, ay, bx, by, cx, cy))
