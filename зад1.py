from sys import argv

name, vyrabot, stavka, premia = argv

print("Заработная плата сотруднику = ", int(vyrabot) * int(stavka) + int(premia))
