# Day 20
from heapq import heappop, heappush
INPUT = open('Day 20.txt', 'r')
data = []
for i in INPUT:
    data.append(list(i))
INPUT.close()

letters = "abcdefghijklmnopqrstuvwxyz".upper()

warps = {}
outer = {}
inner = {}
for i in range(len(data)):
    a = data[i][0]
    b = data[i][1]
    if a in letters and b in letters:
        outer[a + b] = (2, i)

offset = len(data[0]) - 3
for i in range(len(data)):
    a = data[i][offset]
    b = data[i][offset + 1]
    if a in letters and b in letters:
        outer[a + b] = (offset - 1, i)

for i in range(len(data[0])):
    a = data[0][i]
    b = data[1][i]
    if a in letters and b in letters:
        outer[a + b] = (i, 2)

offset = len(data) - 2
for i in range(len(data[0])):
    a = data[offset][i]
    b = data[1 + offset][i]
    if a in letters and b in letters:
        outer[a + b] = (i, offset - 1)

ina = 35
inx = 86
iny = 96

for i in range(len(data[0])):
    a = data[ina][i]
    b = data[ina + 1][i]
    if a in letters and b in letters:
        inner[a + b] = (i, ina - 1)

for i in range(len(data[0])):
    a = data[iny][i]
    b = data[iny + 1][i]
    if a in letters and b in letters:
        inner[a + b] = (i, iny + 2)

for i in range(len(data)):
    a = data[i][ina]
    b = data[i][ina + 1]
    if a in letters and b in letters:
        inner[a + b] = (ina - 1, i)

for i in range(len(data)):
    a = data[i][inx]
    b = data[i][inx + 1]
    if a in letters and b in letters:
        inner[a + b] = (inx + 2, i)

start = "AA"
end = "ZZ"
for i in inner:
    warps[inner[i]] = outer[i]
    warps[outer[i]] = inner[i]

check = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1]
]
goal = outer[end]


def bfs(start):
    queue = [(0, start)]
    explored = {start}
    while len(queue) > 0:
        distance, current = heappop(queue)
        for d in check:
            warped = False
            x = current[0] + d[0]
            y = current[1] + d[1]
            if (x, y) in explored:
                continue
            tile = data[y][x]
            if tile in "#" + letters:
                continue
            if (x, y) in warps:
                x, y = warps[x, y]
                warped = True
            elif (x, y) == goal:
                return distance + 1
            explored.add((x, y))
            heappush(queue, (distance + 1 + warped, (x, y)))


print("part_1:", bfs(outer[start]))
innerwarps = set([inner[i] for i in inner])
goal = (*goal, 0)


def bfs3d(start):
    queue = [(0, start)]
    explored = {start}
    while len(queue) > 0:
        distance, current = heappop(queue)
        for d in check:
            warped = False
            x = current[0] + d[0]
            y = current[1] + d[1]
            z = current[2]
            if (x, y, z) in explored:
                continue
            tile = data[y][x]
            if tile in "#" + letters:
                continue
            if (x, y) in warps:
                if (x, y) in innerwarps:
                    z += 1
                else:
                    z -= 1
                x, y = warps[x, y]
                warped = True
            elif (x, y, z) == goal:
                return distance + 1
            explored.add((x, y, z))
            if z < 0:
                continue
            heappush(queue, (distance + 1 + warped, (x, y, z)))


print("part_2:", bfs3d((*outer[start], 0)))
