# По двум заданным числам проверить является ли одно квадратом второго 
a = int(input('Введите первое число :'))
b = int(input('Введите второе число :'))

def square(num1, num2):
    if num1 == num2**2:
        return True
    else:
        return False

if square(a, b):
    print('Первое число есть квадрат второго')
elif square(b, a):
    print('Второе число есть квадрат первого')
else:
    print('Числа не являются квадратами')


