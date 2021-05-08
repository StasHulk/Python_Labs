from itertools import permutations
from itertools import product

print("Введите количество символов в пароле и набор символов")
n = int(input())
symbols = list(input())
if n == len(symbols) or n < len(symbols):
    comb = list(permutations(symbols, n))
    for i in list(comb):
        for j in i:
            print(j, end="")
        print(" ", end="")
else:
    comb = list(product(symbols, repeat=n))
    del comb[0]
    del comb[len(comb) - 1]

    for i in list(comb):
        for j in i:
            print(j, end="")
        print(" ", end="")


