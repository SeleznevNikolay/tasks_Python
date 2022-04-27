# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

# spisokNumber = input('Введите строку из чисел: ').split()
spisokNumber = ('123 456 25 78 11 345 676').split()
print(spisokNumber)

# for i in range(len(spisokNumber)):
#     spisokNumber[i] = int(spisokNumber[i])

spisokNumber = list(map(int, spisokNumber))
print(spisokNumber)

print(max(spisokNumber))
print(min(spisokNumber))


# def String_Min_and_Max(str):
#     list1 = str.split(' ')
#     # print(list1)
#     min = int(list1[0])
#     max = int(list1[0])
#     for i in range(len(list1)):
#         list1[i] = int(list1[i])
#         if list1[i]<min:
#             min = list1[i]
#         if list1[i]>max:
#             max = list1[i]
#     print(f'Минимум равен {min}, максимум равен {max}')

# a = input('Введите строку, состоящую из наборов чисел. В качестве символа-разделителя используйте пробел ')
# String_Min_and_Max(a)
