listt = list(input("Введите значение: "))

for i in range(0, len(listt) - 1, 2):
    listt[i], listt[i + 1] = listt[i + 1], listt[i]

print(listt)

input("Чтобы закрыть нажмите Enter ")