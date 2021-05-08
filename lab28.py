
factors = []


def factorization(n, remainder):
    next = 0
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
            next = int(n / i)
            break

    if next == 0:
        return remainder
    remainder = next
    return factorization(next, remainder)


print("Введите число для разложения")
n = int(input())

remainder = factorization(n, 0)

if len(factors) == 0:
    print("Число простое!!!")
    exit()

factors.append(remainder)

output = []
no_duplicates = list(dict.fromkeys(factors))

for factor in no_duplicates:
    exponent = factors.count(factor)
    if exponent > 1:
        output.append(f"{factor}^{exponent}")
    else:
        output.append(f"{factor}")

print(" * ".join(output))

