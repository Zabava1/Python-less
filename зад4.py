mylist = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

coplist = mylist.copy()
newlist = mylist.copy()

[coplist.remove(i) for i in set(mylist)]
[newlist.remove(i) for i in mylist if i in coplist]

print('Исходный список: ', mylist)
print('Результат: ', newlist)