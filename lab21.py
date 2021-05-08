
def bmi(weight: float, height: float) -> float:
    return weight / pow(height, 2)


def print_bmi(bmi: float) -> float:
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25.0:
        print("Normal")
    elif bmi < 30.0:
        print("Overweight")
    else:
        print("Obesity")


print("Введите вес и рост через пробел")

weight, height = map(int, input().split())
height /= 100
i = bmi(weight, height)
print_bmi(i)

