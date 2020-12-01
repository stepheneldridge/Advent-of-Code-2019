# Day 1
INPUT = open('Day 01.txt', 'r')
total1 = 0
total2 = 0
for i in INPUT:
    mass = int(i)
    fuel = mass // 3 - 2
    total1 += fuel
    while fuel > 0:
        total2 += fuel
        fuel = fuel // 3 - 2
INPUT.close()
print("part_1:", total1)
print("part_2:", total2)
