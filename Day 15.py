# Day 15
import math
INPUT = open('Day 15.txt', 'r')
odata = []
for i in INPUT:
    odata = [int(j) for j in i.split(",")]

odata += [0 for _ in range(2000)]

rbase = 0
p = 0
outputs = []
data = odata.copy()


def run(code):
    global data
    global p
    global rbase
    outputs = []
    while True:
        op = data[p] % 100
        am = (data[p] // 100) % 10
        bm = (data[p] // 1000) % 10
        cm = (data[p] // 10000) % 10

        if op == 1:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            b = data[data[p + 2]] if bm == 0 else data[p + 2] if bm == 1 else data[data[p + 2] + rbase]
            if cm == 2:
                data[data[p + 3] + rbase] = a + b
            else:
                data[data[p + 3]] = a + b
            p += 4
        elif op == 2:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            b = data[data[p + 2]] if bm == 0 else data[p + 2] if bm == 1 else data[data[p + 2] + rbase]
            if cm == 2:
                data[data[p + 3] + rbase] = a * b
            else:
                data[data[p + 3]] = a * b
            p += 4
        elif op == 3:
            if code is not None:
                data[data[p + 1] + (0 if am != 2 else rbase)] = code
                p += 2
                code = None
            else:
                break
        elif op == 4:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            outputs.append(a)
            p += 2
        elif op == 5:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            b = data[data[p + 2]] if bm == 0 else data[p + 2] if bm == 1 else data[data[p + 2] + rbase]
            if a != 0:
                p = b
            else:
                p += 3
        elif op == 6:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            b = data[data[p + 2]] if bm == 0 else data[p + 2] if bm == 1 else data[data[p + 2] + rbase]
            if a == 0:
                p = b
            else:
                p += 3
        elif op == 7:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            b = data[data[p + 2]] if bm == 0 else data[p + 2] if bm == 1 else data[data[p + 2] + rbase]
            data[data[p + 3] + (rbase if cm == 2 else 0)] = int(a < b)
            p += 4
        elif op == 8:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            b = data[data[p + 2]] if bm == 0 else data[p + 2] if bm == 1 else data[data[p + 2] + rbase]
            data[data[p + 3] + (rbase if cm == 2 else 0)] = int(a == b)
            p += 4
        elif op == 9:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            rbase += a
            p += 2
        elif op == 99:
            break
        else:
            print(p, "error")
            break
    return outputs[-1]


INPUT.close()
direction = {
    1: [0, 1],
    2: [0, -1],
    3: [-1, 0],
    4: [1, 0]
}
lowx = 25
lowy = 25
press = 1
current = (0, 0)
goal = (0, 0)
goalv = 0


def printarea(a, p=False):
    global goalv
    for i in range(len(a)):
        for j in range(len(a[i])):
            if i == current[1] + lowy and j == current[0] + lowx:
                if p:
                    print("D", end="")
            else:
                x = " "  # a[i][j] % 10
                if i == lowy and j == lowx:
                    x = "O"
                elif i == goal[1] + lowy and j == goal[0] + lowx:
                    x = "X"
                    goalv = a[i][j]
                elif a[i][j] == -1:
                    x = "#"
                elif a[i][j] == 0:
                    x = "?"
                if p:
                    print(x, end="")
        if p:
            print()


area = [
    [0 for _ in range(50)] for _ in range(50)
]


def getdir():
    lowest = 1
    value = math.inf
    for d in direction:
        cx = current[0] + direction[d][0]
        cy = current[1] + direction[d][1]
        w = area[cy + lowy][cx + lowx]
        if w >= 0 and w < value:
            lowest = d
            value = w
    return lowest


index = 0
dist = 1
while index < 10000:
    index += 1
    status = run(press)
    cx = current[0] + direction[press][0]
    cy = current[1] + direction[press][1]
    if status == 0:
        area[cy + lowy][cx + lowx] = -1
    elif status == 1:
        current = (cx, cy)
        if area[cy + lowy][cx + lowx] > 0:
            dist = min(area[cy + lowy][cx + lowx], dist)
        area[cy + lowy][cx + lowx] = dist
        dist += 1
    elif status == 2:
        goal = (cx, cy)
        current = (cx, cy)
        if area[cy + lowy][cx + lowx] > 0:
            dist = min(area[cy + lowy][cx + lowx], dist)
        area[cy + lowy][cx + lowx] = dist
        dist += 1
    press = getdir()
printarea(area)
print("part_1:", goalv)

for i in range(len(area)):
    for j in range(len(area[i])):
        if area[i][j] >= 0:
            area[i][j] = 0


index = 0
dist = 1
current = goal
while index < 10000:
    index += 1
    cx = current[0] + direction[press][0]
    cy = current[1] + direction[press][1]
    current = (cx, cy)
    if area[cy + lowy][cx + lowx] > 0:
        dist = min(area[cy + lowy][cx + lowx], dist)
    area[cy + lowy][cx + lowx] = dist
    dist += 1
    press = getdir()
best = 0
for i in range(len(area)):
    for j in range(len(area[i])):
        best = max(best, area[i][j])
print("part_2:", best)
