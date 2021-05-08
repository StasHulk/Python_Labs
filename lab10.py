
s1 = [0, 1]
s2 = [0, 1]

print("Введите s, l1, r1, l2, r2")
try:
    s, s1[0], s1[1], s2[0], s2[1] = map(int, input().split(" "))
except:
    print("Неверный ввод!!!")
    exit(0)

if s1[0] > s1[1] or s2[0] > s2[1]:
    print("Неверные диапазоны!!!")
    exit(0)

result = [0, 0]
if s1[0] + s2[0] == s or s1[0] + s2[1] == s:
    result = [s1[0], s - s1[0]]

elif s1[1] + s2[0] == s or s1[1] + s2[1] == s:
    result = [s1[1], s - s1[1]]

else:
    print(-1)
    exit(0)

print(result[0], result[1])

