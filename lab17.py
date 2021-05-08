black_cells = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_cells = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
s1 = [i for i in range(37)]
rates = {}
maximum = 0
black = 0
red = 0

while True:
    for k in range(12):
        a = int(input())

        if a < 0 or a >= 37:
            exit(0)
        if a in black_cells:
            black += 1
        else:
            red += 1

        if a in rates:
            rates[a] += 1
        else:
            rates[a] = 0
            rates[a] += 1
            pos = s1.index(a)
            del s1[pos]

        maximum = max(rates.values())
        for key in rates.keys():
            if rates[key] == maximum:
                print(key, end=' ')

        print()
        for i in range(len(s1)):
            if s1[i] != -1:
                print(s1[i], end=' ')

        print()
        print(red, black, end=' ')
        print("\n")
