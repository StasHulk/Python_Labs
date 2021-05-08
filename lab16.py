import re

print("Введите число билетов")
n = int(input())
print("Введите номера билетов через пробел")
nums = input().split(" ")

pattern = "a[a-z][0-9][0-9]55661"
valid = []
for element in nums:
    if re.match(pattern, element):
        valid.append(element)

if len(valid) > 0:
    for element in valid:
        print(element, end=" ")
else:
    print(-1)
