# Day 17
INPUT = open('Day 19.txt', 'r')
odata = []
for i in INPUT:
    odata = [int(j) for j in i.split(",")]
odata += [0 for _ in range(2000)]


def run(codes):
    global odata
    data = odata.copy()
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
    return outputs[0]


INPUT.close()
count = 0
for i in range(50):
    for j in range(50):
        x = run([j, i])
        count += x
    #     print(" " if x == 0 else "#", end="")
    # print()
print("part_1:", count)

begin = [0, 100]
while True:
    if run(begin.copy()):
        if run([begin[0] + 99, begin[1] - 99]):
            break
        else:
            begin[1] += 1
    else:
        begin[0] += 1
print("part_2:", begin[0] * 10000 + begin[1] - 99)
