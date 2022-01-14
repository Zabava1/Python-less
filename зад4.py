mlist = str(input("Введите строку разделенную пробелами: ")).split()

for i in range(len(mlist)):
    if len(mlist[i]) > 10:
        mlist[i] = mlist[i][:10]
    print(f'{i + 1}) {mlist[i]}')

input("Чтобы закрыть нажмите Enter ")
