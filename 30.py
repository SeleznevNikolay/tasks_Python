# Вычислить число ПИ c заданной точностью d
# Пример: при d = 0.001,  ПИ = 3.141. 10-1 <= d <= 10-10

import math

d = int(input('Введите число (степень точности) d (от 1 до 10): '))
if 1 <= d <= 10:
    numPI = int(math.pi * (10**d)) / 10**d
    print(numPI)
else:
    print('Число d - не верно')

