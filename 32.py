# Дана последовательность чисел.
# Получить список неповторяющихся элементов
# исходной последовательности.
# Запишите результат в файл.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

inList = [1, 5, 7, 2, 2, 3, 5, 1, 5, 3, 10]

outList = []
# outList = set()

# for i in inList:
#     outList.add(i)
# outList = list(outList)

for i in inList:
    if i not in outList:
        outList.append(i)

outList.sort()
print(inList, '=>', outList)

f = open('outList.txt', 'w')
# f.write(str(outList))
for i in outList:
    f.write(str(i) + '\n')
f.close()