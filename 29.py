# Считайте два числа из файла (одно число в одной строке).
# Напишите программу, которая найдёт НОК двух чисел

# Найти наименьшее общее кратное через наибольший общий делитель
# можно по формуле НОК
# ( a , b ) = a ⋅ b : (a, b)=a·b:НОД ( a , b ) (a, b).

# https://pythonstart.ru/list/nahozhdenie-nok-i-nod-v-python-primery
# https://zaochnik.com/spravochnik/matematika/delimost/nahozhdenie-naimenshego-obschego-kratnogo/

# import math
# print(math.lcm(14, 21))


import math
list1=[]
with open(r'E:\GeekEducation\Python\Python Tasks\Task29\Numbrs.txt', 'r') as data:
    for item in data:
        list1.append(item)
    for i in range(len(list1)):
        list1[i] = int(list1[i])
print(math.lcm(list1[0], list1[1]))