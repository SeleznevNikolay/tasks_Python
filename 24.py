# В заданном списке вещественных чисел 
# найдите разницу между максимальным и минимальным 
# значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.005, 1.2713, 3.11, 523, 1.0002]
max = 0.0
min = 1.0

for i in list:
    if i != int(i):
        fract = i - int(i)
        if fract > max:
            max = fract
        if fract < min:
            min = fract

# print(max, min)
if min == 1.0:
    print('нет вещественных чисел')
else:
    print(list, end=' => ')
    print(round(max-min, 10))
