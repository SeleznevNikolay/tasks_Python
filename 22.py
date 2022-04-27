# Найти сумму чисел списка стоящих на нечетной позиции

list = [2, 9, 9, 6, 5, 3, 8, 1, 1, 5]
sum = 0

for i in range(len(list)):
    if i%2 != 0:
        sum += list[i]

print(list, end=' => ')
print(sum)