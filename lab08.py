print("Введите операцию в формате 2 + 5")
text = input()

try:
    n1, operator, n2 = text.split()
    n1 = int(n1)
    n2 = int(n2)
except:
    print("Неверно введенные данные!!!")
    exit(0)

result = 0
if operator != '+' and operator != '-' and operator != '*' and operator != '/':
    print("Неподдерживаемый оператор!!!")
    exit(0)
if operator == '+':
    result = n1 + n2
elif operator == '-':
    result = n1 - n2
elif operator == '*':
    result = n1 * n2
elif operator == '/':
    if n2 == 0:
        print("Деление на ноль запрещено!!!")
        exit(0)
    else:
        result = n1 / n2

print(n1, " ", operator, " ", n2, " = ", result)



