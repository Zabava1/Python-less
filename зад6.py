from itertools import count, cycle

mlist = []
for i in count(3, 2):
    if i > 14:
        break
    else:
        mlist.append(i)
print(mlist)

t = 0
for i in cycle(mlist):
    if t > 10:
        break
    else:
        print(i)
        t += 1