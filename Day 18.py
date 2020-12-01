# Day 18
import math
INPUT = open('Day 18.txt', 'r')
data = []
for i in INPUT:
    data.append(list(i.strip()))


def find(a):
    for i in range(len(data)):
        if a in data[i]:
            return (data[i].index(a), i, 0)


check = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1]
]


def is_tile(s):
    for i in data:
        if s in i:
            return True
    return False


letters = ""
for i in "abcdefghijklmnopqrstuvwxyz":
    if is_tile(i):
        letters += i
upper = letters.upper()


def getbit(a):
    if a == "@":
        return 3  # "@"
    elif a == ".":
        return "."
    elif a == "#":
        return "#"
    a = a.upper()
    return 1 << (ord(a) - 65)


def gettile(a):
    if a[0] >= 0 and a[0] < len(data[0]) and a[1] >= 0 and a[1] < len(data):
        return data[a[1]][a[0]]
    return "#"


def keysfrom(point, keys):
    explored = set()
    reachable = {}
    queue = [point]
    while len(queue) > 0:
        current = queue.pop(0)
        tile = gettile(current)
        explored.add(current[:2])
        if tile in letters and getbit(tile) & keys == 0:
            reachable[getbit(tile)] = current[:3]
            continue
        elif tile in upper:
            if getbit(tile) & keys != getbit(tile):
                continue
        for d in check:
            x = current[0] + d[0]
            y = current[1] + d[1]
            tile = gettile((x, y))
            if tile != "#" and (x, y) not in explored:
                queue.append((x, y, current[2] + 1))
    return reachable


explored = {}


def dfs(point, keys):
    global explored
    if (point, keys) in explored:
        return explored[point, keys]
    reachable = keysfrom(point, keys)
    if len(reachable) == 0:
        explored[point, keys] = 0
        return 0
    best = math.inf
    for i in reachable:
        best = min(best, reachable[i][2] + dfs((*reachable[i][0:2], 0), keys | i))
    explored[point, keys] = best
    return best


print("part_1:", dfs(find("@"), 0))
p = find("@")
starts = []
for i in range(p[0] - 1, p[0] + 2):
    for j in range(p[1] - 1, p[1] + 2):
        if abs(p[0] - i) + abs(p[1] - j) == 2:
            data[j][i] = "@"
            starts.append((i, j, 0, len(starts)))
        else:
            data[j][i] = "#"
starts = tuple(starts)
explored = {}


def dfs4(points, keys):
    global explored
    if (points, keys) in explored:
        return explored[points, keys]
    reachable = {}
    index = 0
    for i in points:
        x = keysfrom(i, keys)
        for j in x:
            reachable[j] = x[j] + (index,)
        index += 1
    if len(reachable) == 0:
        explored[points, keys] = 0
        return 0
    best = math.inf
    for i in reachable:
        ps = []
        for j, p in enumerate(points):
            if j == reachable[i][3]:
                ps.append((*reachable[i][:2], 0, j))
            else:
                ps.append(p)
        best = min(best, reachable[i][2] + dfs4(tuple(ps), keys | i))
    explored[points, keys] = best
    return best


print("part_2:", dfs4(starts, 0))
