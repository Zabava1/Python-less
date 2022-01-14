mlist = [7, 5, 3, 3, 2]

while True:

    print('Рейтинг: ', mlist)
    n = int(input("Введите новое значение рейтинга: "))
    print('')

    if n <= 0:
        print('Нужно ввести ПОЛОЖИТЕЛЬНОЕ значение!')
        continue

    i = len(mlist)

    while True:
        if n <= mlist[i - 1]:
            mlist.insert(i , n)
            break
        i = i - 1
        if i == 0:
            mlist.insert(0, n)
            break
