n = int(input('введите число: '))
i = 0
a = n
while a > 0:
    a = a // 10
    i += 1
b = (n * 3) + ((10 ** i) * 2 * n) + (100 ** i) * n

print(b)

input("закрыть: ")