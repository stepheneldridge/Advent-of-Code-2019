# Day 10
import math
data = []
asteroids = []
INPUT = open('Day 10.txt', 'r')
for line in INPUT:
    row = []
    line = line.strip()
    for c in line:
        row.append(1 if c == "#" else 0)
    data.append(row)
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 1:
            asteroids.append((j, i))

best = asteroids[0]
best_v = 0
for i in asteroids:
    angles = set()
    for j in asteroids:
        if i != j:
            b = j[0] - i[0]
            a = j[1] - i[1]
            angles.add(math.atan2(b, a))
    if len(angles) > best_v:
        best_v = len(angles)
        best = i
print("part_1:", best_v)

order = {}
for i in asteroids:
    if i != best:
        b = i[0] - best[0]
        a = i[1] - best[1]
        angle = math.atan2(b, -a)
        if angle < 0:
            angle += 2 * math.pi
        entry = (a * a + b * b, i)
        if angle in order:
            order[angle].append(entry)
        else:
            order[angle] = [entry]
for i in order:
    order[i].sort(key=lambda a: a[0])
keys = list(order.keys())
keys.sort()

lasered = 0
index = 0
while lasered < 200:
    lasered += 1
    index %= len(keys)
    angle = keys[index]
    blown_up = order[angle].pop(0)
    if lasered == 200:
        print("part_2:", blown_up[1][0] * 100 + blown_up[1][1])
        break
    if len(order[angle]) == 0:
        del order[angle]
        keys.pop(index)
    else:
        index += 1
