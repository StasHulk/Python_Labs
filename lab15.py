import random

game = True
while game:
    n = random.randint(0, 100)
    print("Добро пожаловать! Угадайте число!")
    for i in range(5):
        guess = int(input())
        if guess == n:
            print("Поздравляю! Вы угадали!")
            exit(0)
        elif guess > n:
            print("Загаданное число меньше")
        else:
            print("Загаданное число больше")
    print("Вы проиграли. Было загадано", n)
    print("Хотите начать сначала? (1 - ДА)")
    if input() != "1":
        game = False
