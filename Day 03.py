# Day 3
import math
INPUT = open('Day 03.txt', 'r')
data = []
directions = {
    "D": [0, -1],
    "U": [0, 1],
    "L": [-1, 0],
    "R": [1, 0]
}
for line in INPUT:
    p = line.split(",")
    current = [0, 0]
    path = [(0, 0)]
    for i in range(len(p)):
        d = directions[p[i][0]]
        dist = int(p[i][1:])
        x = current[0] + d[0] * dist
        y = current[1] + d[1] * dist
        current = [x, y]
        path.append((x, y))
    data.append(path)
INPUT.close()


def find_intersect(a1, a2, b1, b2):
    if a1 == b1 or a1 == b2:
        return a1
    if a2 == b1 or a2 == b2:
        return a2
    axis = a1[1] == a2[1]
    if axis != (b1[1] == b2[1]):
        if b1[not axis] <= max(a1[not axis], a2[not axis]) and b1[not axis] >= min(a1[not axis], a2[not axis]):
            if a1[axis] <= max(b1[axis], b2[axis]) and a1[axis] >= min(b1[axis], b2[axis]):
                return (b1[not axis], a1[axis])
    else:
        if a1[axis] == b1[axis]:
            if a1[not axis] <= max(b1[not axis], b2[not axis]) and a1[not axis] >= min(b1[not axis], b2[not axis]):
                return a1
            if a2[not axis] <= max(b1[not axis], b2[not axis]) and a2[not axis] >= min(b1[not axis], b2[not axis]):
                return a2
    return None


def path(p):
    dist = 0
    for i in range(len(p) - 1):
        dist += abs(p[i][0] - p[i + 1][0]) + abs(p[i][1] - p[i + 1][1])
    return dist


best1 = 1 << 32
best2 = 1 << 32
for i in range(len(data[0]) - 1):
    for j in range(len(data[1]) - 1):
        inter = find_intersect(data[0][i], data[0][i + 1], data[1][j], data[1][j + 1])
        if inter:
            cost = path(data[0][:i + 1] + [inter]) + path(data[1][:j + 1] + [inter])
            if cost == 0:
                continue
            best1 = min(abs(inter[0]) + abs(inter[1]), best1)
            best2 = min(cost, best2)
print("part_1:", best1)
print("part_2:", int(best2))
