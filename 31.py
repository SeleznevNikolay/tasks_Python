# Составить список простых множителей натурального числа N

numberN = int(input('Введите число N: '))
num = numberN
i = 2
pf = set()

while i <= num:
    if (num % i) == 0:
        pf.add(i)
        num /= i
    else:
        i += 1

if numberN in pf:
    print('число: {} - простое число'.format(numberN))
else:
    pf = list(pf)
    pf.sort()
    print('Список простых множителей:', pf)