# Дано число обозначающее день недели.
# Вывести его название и указать является ли он выходным.

weekday = [None, 
           'Понедельник',
           'Вторник',
           'Среда',
           'Четверг',
           'Пятница',
           'Суббота',
           'Воскресенье']

numberWeek = int(input('Введите номер дня недели: '))

if numberWeek in range(1, 6):
    print(weekday[numberWeek], ' - рабочий день')
elif numberWeek == 6 or numberWeek == 7:
    print(weekday[numberWeek], ' - выходной')
else: print('Число', numberWeek, 'не день недели')