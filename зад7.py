def fact(x):
    y = 1
    for i in range(1, x + 1):
        y *= i
        yield y


n = int(input('Введите значение: '))

a = 0
for el in fact(n):
    a = el
print(f'Факториал числа {n} =', a)