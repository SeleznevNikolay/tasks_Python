# Даны два файла, в каждом из которых находится запись
# квадратного многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def get_koefPolinom(strPolinom):    # "достаем" коэффициенты
    # print(strPolinom)
    splStr = strPolinom.split()
    # print(splStr)
    # обработка отсутсвия коеффициента x, x^2 и т.д.
    for i in splStr:
        if i.isdigit():
            if int(i) != 0:
                if splStr[splStr.index(i) - 1] == '-':
                    koefX0 = - int(i)
                else:
                    koefX0 = int(i)
    # print(koefX0)

    for i in splStr:
        if i.find('x') != -1:
            # print(i)
            if i.find('x') == len(i) -1:                # x крайний?
                if splStr[splStr.index(i) - 1] == '-':  # какой знак?
                    koefX1 = - int(i.split('*')[0])
                else:
                    koefX1 = int(i.split('*')[0])
            else:
                # print(i.split('^')[1]))                  # степень x?
                if splStr.index(i) != 0:
                    if splStr[splStr.index(i) - 1] == '-':  # какой знак?
                        koefX2 = - int(i.split('*')[0])
                else:
                    koefX2 = int(i.split('*')[0])

    # print(koefX1)
    # print(koefX2)
    # в общем случае для многочлена степени k
    # на выходе функции надо выдавать список k коэффицинтов
    return [koefX0, koefX1, koefX2]

f = open('polinom1.txt')
str1 = f.read()
f.close()

f = open('polinom2.txt')
str2 = f.read()
f.close()

print(get_koefPolinom(str1))
print(get_koefPolinom(str2))

def sum_coefPolinom(koefPol1, koefPol2):    # складываем
    koefX = []
    for i in range(3):
        koefX.append(koefPol1[i] + koefPol2[i])
    return koefX

sum = sum_coefPolinom(get_koefPolinom(str1), get_koefPolinom(str2))
print(sum)

def out_polinom(koefPol):   # из коэффициентов делаем строку
    strPol = ' = 0'
    for i in range(3):  # (3) - для квадратного многочлена
                        # для многочлена степени k - надо (k)
        if i == 0:
            if koefPol[0] > 0:
                strPol = ' + ' + str(koefPol[0]) + strPol
            elif koefPol[0] < 0:
                strPol = ' - ' + str(-koefPol[0]) + strPol
        elif i == 1:
            if koefPol[1] > 0:
                if koefPol[1] == 1:
                    strPol = ' + x' + strPol
                else:
                    strPol = ' + ' + str(koefPol[1]) + '*x' + strPol
            elif koefPol[1] < 0:
                if koefPol[1] == -1:
                    strPol = ' - x' + strPol
                else:
                    strPol = ' - ' + str(-koefPol[1]) + '*x' + strPol
        else:
            if koefPol[i] > 0:
                if koefPol[i] == 1:
                    strPol = 'x^' + str(i) + strPol
                    # если решать для k многочлена
                    # надо поработать с "крайним" плюсом
                    # strPol = ' + x^' + str(i) + strPol
                else:
                    strPol = str(koefPol[i]) + '*x^' + str(i) + strPol
                    # тоже надо поработать с плюсом
                    # strPol = ' + ' + str(koefPol[i]) + '*x^' + str(i) + strPol
            elif koefPol[i] < 0:
                if koefPol[i] == -1:
                    strPol = ' - x^' + str(i) + strPol
                else:
                    strPol = ' - ' + str(-koefPol[i]) + '*x^' + str(i) + strPol
        print(strPol)
    return strPol

print(out_polinom(sum))

with open('sum_polinom.txt', 'w') as fSum:
    fSum.write(out_polinom(sum))