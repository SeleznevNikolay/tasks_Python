# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

numberN = int(input('Введите число N : '))
list = []
func = 1

for i in range(numberN):
    # print(i, func)
    list.append(func)
    func *= -3

print(list)