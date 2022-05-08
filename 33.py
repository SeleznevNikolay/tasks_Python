# Задана натуральная степень k.
# Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0
#    или x² + 5 = 0
#    или 10*x² = 0

from random import random

k = int(input('Введите число k > 2: '))
coef = []

for i in range(k+1):
    coef.append(int(random() * 10)) # 100 - не информотивно )

# print(coef)
# coef = [5, 1, 7, 0, 1]

polinom = ' = 0'

if coef[0] != 0:
    polinom = ' + ' + str(coef[0]) + polinom

if coef[1] != 0:
    if coef[1] == 1:
        polinom = ' + ' + 'x' + polinom
    else:
        polinom = ' + ' + str(coef[1]) + '*x' + polinom

for i in range(2, len(coef)):
    if coef[i] != 0:
        if coef[i] == 1:
            polinom = ' + ' + 'x^' + str(i) + polinom
        else:
            polinom = ' + ' + str(coef[i]) + '*x^' + str(i) + polinom

polinom = polinom[3::]

print(polinom)

with open('polinom.txt', 'w') as pData:
    pData.write(polinom)