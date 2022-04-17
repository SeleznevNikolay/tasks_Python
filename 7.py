# Проверить истинность утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

resultAB = True
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            resultA = not(x or y or z)
            resultB = not(x) and not(y) and not(z)
            if resultA != resultB: resultAB = False
            print('[', x, y, z, '] |', resultA, '|  |', resultB, '|')
if resultAB == False:
    print('Не для всех значений утверждение верно')
else:
    print('Для всех значений утверждение верно')
