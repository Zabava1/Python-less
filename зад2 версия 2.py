n = int(input('введите число: '))

a = n // 3600 % 3600
b = n // 60 % 60
c = n % 60

t = str('0')
if a // 10 == 0:
    a = str(a)
    at = str(t + a)
else:
    at = a
if b // 10 == 0:
    b = str(b)
    bt = str(t + b)
else:
    bt = b
if c // 10 == 0:
    c = str(c)
    ct = str(t + c)
else:
    ct = c

print(f"{at}:{bt}:{ct}")