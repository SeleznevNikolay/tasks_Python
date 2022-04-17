# Вывести на экран числа от -N до N
numberN = int(input('Введите число N :'))
i = - numberN
r = range(-numberN, numberN + 1)
for i in r:
    print(i)