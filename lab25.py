import math
import random


def isSorted(list, ascend):
    if ascend:
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                return False
        return True
    else:
        for i in range(len(list) - 1):
            if list[i] < list[i + 1]:
                return False
        return True


def BozoSort_List(list, ascend=True):
    while not isSorted(list, ascend):
        i1 = random.randint(0, len(list) - 1)
        i2 = random.randint(0, len(list) - 1)

        tmp = list[i1]
        list[i1] = list[i2]
        list[i2] = tmp
    return list


def BozoSort_Matrix(matrix, ascend=True):
    for i in range(len(matrix)):
        matrix[i] = BozoSort_List(matrix[i], ascend)
    return matrix


def BozoSort_Triple(a, b, c, ascend=True):
    return BozoSort_List([a, b, c], ascend)


def printList(list):
    for element in list:
        print(element, end=" ")
    print()


def printMatrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


print("Введите 1 если требуется сортировка одномерного массива, 2 если сортировка двумерного")
if int(input()) == 1:
    print("Введите длину массива, и сам массив с новой строки")
    n = int(input())
    list_in = list(map(int, input().split()))
    if n >= 3:
        printList(BozoSort_Triple(list_in[0], list_in[1], list_in[2]))
        printList(BozoSort_Triple(list_in[0], list_in[1], list_in[2], ascend=False))

    printList(BozoSort_List(list_in))
    printList(BozoSort_List(list_in, ascend=False))

else:
    list_in = []
    print("Введите длину двумерного массива, и каждую строку с новой строки")
    n = int(input())
    for i in range(int(math.sqrt(n))):
        list_in.append(list(map(int, input().split())))
    print()
    printMatrix(BozoSort_Matrix(list_in))
    print()
    printMatrix(BozoSort_Matrix(list_in, ascend=False))
