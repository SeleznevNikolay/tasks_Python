# Написать программу преобразования десятичного числа в двоичное
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from cgi import print_arguments


numberN = int(input('Введите число N : '))
tmp = numberN
listStr = []
strBin = ''

while tmp != 0: 
    listStr.insert(0, tmp % 2)
    strBin = str(tmp % 2)+ strBin
    tmp //= 2

print(numberN, ' -> ', listStr)
print(numberN, ' -> ', strBin)
print(numberN, ' -> ', bin(numberN))