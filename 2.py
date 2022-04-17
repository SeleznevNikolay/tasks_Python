# Найти максимальное из пяти чисел
arr_number = [2, 9, 5, 7, 1]

def MaxArray(ar):
    max = ar[0]
    for i in ar:
        if i > max:
            max = i
    return max

print('Среди чисел: ', arr_number)
print('Максимальное: ', MaxArray(arr_number))