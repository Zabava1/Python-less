mlist = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 0, 55]

newlist = [mlist[i] for i in range(len(mlist)) if mlist[i] > mlist[i - 1] and i != 0]

print(newlist)