# Day 11
import matplotlib.pyplot as plot
INPUT = open('Day 11.txt', 'r')
odata = []
for i in INPUT:
    odata = [int(j) for j in i.split(",")]
INPUT.close()
odata += [0 for _ in range(2000)]
p = 0
rbase = 0
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
                code = None
                p += 2
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
    return outputs


tiles = {}


def paint(start):
    global p
    global rbase
    global data
    global odata
    global tiles
    p = 0
    rbase = 0
    data = odata.copy()
    tiles = {(0, 0): start}
    direction = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]
    d = 1
    current = [0, 0]
    params = run(start)
    while len(params) == 2:
        tiles[(current[0], current[1])] = params[0]
        d += 1 if params[1] == 0 else -1
        d %= 4
        current[0] += direction[d][0]
        current[1] += direction[d][1]
        tile = 0
        if (current[0], current[1]) in tiles:
            tile = tiles[(current[0], current[1])]
        params = run(tile)


paint(0)
print("part_1:", len(tiles))

paint(1)
xs = []
ys = []
for i in tiles:
    if tiles[i] == 1:
        xs.append(i[0])
        ys.append(i[1])
plot.figure("part_2:", figsize=(5, 1))
plot.scatter(xs, ys)
plot.show()
