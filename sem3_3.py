# Реализуйте алгоритм задания случайных чисел без
# использования встроенного генератора 
# псевдослучайных чисел.

import time

now = time.clock_settime_ns
print(now)



# import time

# def random_number(minimum,maximum):
#     now = str(time.clock())
#     rnd = float(now[::-1][:3:])/1000
#     return minimum + rnd*(maximum-minimum)