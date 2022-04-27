# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.



spisok = [123, 456, 7, 86, 43, 7, 7]
number = 5
count = 0

for i in spisok:
    if i == number:
        # print('Есть число', number, 'в списке')
        count += 1

if count == 0:
    print('Нет числа', number,'в списке')
else:
    print('Число', number, 'в списке втречается', count, 'раз')

# print(number in spisok)
# print(spisok.index(number))