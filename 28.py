# Найти корни квадратного уравнения Ax² + Bx + C = 0
# 1. Математикой
# 2. Используя дополнительные библиотеки*

import math

print("Введите коэффициенты для уравнения")
print("Ax^2 + Bx + C = 0:")
a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = ", discr)

if discr > 0:
    x1 = (-b + discr**0.5) / (2 * a)
    x2 = (-b - discr**0.5) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")