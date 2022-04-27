# Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; 
#         [2, 3, 5, 6] => [12, 15] 

list = [2, 3, 4, 5, 6, 7]
listMultp = []
i = 0
lenList = len(list) - 1

while i <= (lenList // 2):
    listMultp.append(list[i] * list[lenList-i])
    i += 1

print(list, ' => ', listMultp)
