a = int(input('введите число: '))
b = a % 10

while a > 0:
    a = a // 10
    if a % 10 > b:
        b = a % 10
print(f'Самое большое число: {b}')
