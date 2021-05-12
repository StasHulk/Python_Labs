a = int(input("Первая переменная: "))
b = int(input("Вторая переменная: "))
tmp = a
a = b
b = tmp

print("Смена с доп переменной")
print("a = ", a, " b = ", b)

a = a + b
b = a - b
a = a - b

print("Смена без доп переменной")
print("a = ", a, " b = ", b)
