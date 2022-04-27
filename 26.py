# Дано число. Составить список чисел Фибоначчи,
# в том числе для отрицательных индексов. 
# Т.е. для k = 8, список будет выглядеть так:
# [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи

numberN = int(input('Введите число N: '))
# listFibonachi = [0, 1]

# def fibonachiRecur(num):
#     if num in (1, 2):
#         return 1
#     return fibonachiRecur(num-1) + fibonachiRecur(num-2)


def fibonachiPos(num):
    lF = [0, 1]
    tmp = 2
    while tmp <= num:
        lF.append(lF[tmp-1] + lF[tmp-2])
        tmp += 1
    return lF

def fibonachiNeg(num):
    lF = [1, 0]
    tmp = 2
    while tmp <= num:
        lF.insert(0, lF[1] - lF[0])
        tmp += 1
    return lF

def fibonachiAll(num):
    lFull = fibonachiNeg(num)
    lFull.pop()
    lFull.extend(fibonachiPos(num))
    return lFull

print(fibonachiPos(numberN))
print(fibonachiNeg(numberN))
print(fibonachiAll(numberN))
# print(fibonachiRecur(numberN))
