# Day 17
INPUT = open('Day 17.txt', 'r')
odata = []
for i in INPUT:
    odata = [int(j) for j in i.split(",")]

odata += [0 for _ in range(2000)]


def run(codes, manual=False):
    global odata
    data = odata.copy()
    if manual:
        data[0] = 2
    p = 0
    rbase = 0
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
            data[data[p + 1] + (0 if am != 2 else rbase)] = codes.pop(0)
            p += 2
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
            p += 1
            break
        else:
            print(p, "error")
            break
    return outputs


INPUT.close()
scaffold = run([])
# for i in scaffold:
#     print(chr(i), end="")
d = "".join(map(chr, scaffold)).strip().split("\n")
w = len(d[0])
h = len(d)
check = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1]
]
intersect = 0
total = 0
for i in range(h):
    for j in range(w):
        c = 0
        if d[i][j] == '#':
            for k in check:
                x = j + k[0]
                y = i + k[1]
                if x >= 0 and x < w and y >= 0 and y < h:
                    if d[y][x] == '#':
                        c += 1
        if c == 4:
            intersect += 1
            total += i * j
print("part_1:", total)
m = "A,A,B,C,A,C,B,C,A,B\n"
A = "L,4,L,10,L,6\n"
B = "L,6,L,4,R,8,R,8\n"
C = "L,6,R,8,L,10,L,8,L,8\n"
yn = "n\n"
command = list(map(ord, list(m + A + B + C + yn)))
scaffold = run(command, True)
print("part_2:", scaffold[-1])
# for i in scaffold:
#     print(chr(i), end="")
