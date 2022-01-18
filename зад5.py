from functools import reduce

mlist = []
[mlist.append(i) for i in range(100, 1001) if i % 2 == 0]

print(mlist)
print(reduce(lambda x, y: x * y, mlist))
