# Даны два файла, в каждом из которых находится запись
# квадратного многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def get_kef(my_str):
    kef_1 = 0
    kef_2 = 0
    kef_3 = 0

    kef_3 = int(my_str.split(' ')[-1])
    if my_str.split(' ')[-2] == '-':
        kef_3 *= -1
    space_raz = my_str.split(' ')

    kef_2 = int(space_raz[2].split('x')[0])
    if my_str.split(' ')[1] == '-':
        kef_2 *= -1

    kef_1 = int(my_str.split('x')[0])
    return kef_1, kef_2, kef_3

data1 = open(r'E:\GeekEducation\Python\Python Tasks\TaskPlus\Numbr1.txt','r')
data2 = open(r'E:\GeekEducation\Python\Python Tasks\TaskPlus\Numbr2.txt','r')

a = get_kef(data1.read())
b = get_kef(data2.read())

data1.close()
data2.close()

summ = []
for i in range(3):
    summ.append(a[i] + b[i])

data3 = open(r'E:\GeekEducation\Python\Python Tasks\TaskPlus\Numbr3.txt','w')

for i in range(1,3):
    if summ[i] > 0:
        summ[i] = '+' + str(summ[i])

data3.writelines(f'{summ[0]}x**2 {summ[1]}x {sum[2]}') 